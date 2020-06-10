# Copyright 2014-2020 Sebastian Raschka
#
# smilite is a Python module to download and analyze SMILE strings
# (Simplified Molecular-Input Line-entry System) of chemical compounds
# from ZINC (a free database of commercially-available compounds
# for virtual screening:
# http://zinc.docking.org
# Now supports both Python 3.x and Python 2.x.

import sys
import sqlite3
import os
import pyprind

# Load Python version specific modules
if sys.version_info[0] == 3:
    import urllib.request
    import urllib.parse
else:
    import urllib


def get_zinc_smile(zinc_id, backend='zinc12'):
    """
    Gets the corresponding SMILE string for a ZINC ID query from
    the ZINC online database. Requires an internet connection.

    Keyword arguments:
        zinc_id (str): A valid ZINC ID, e.g. 'ZINC00029323'
        backend (str): zinc12 or zinc15

    Returns the SMILE string for the corresponding ZINC ID.
        E.g., 'COc1cccc(c1)NC(=O)c2cccnc2'

    """
    if backend not in {'zinc12', 'zinc15'}:
        raise ValueError("backend must be 'zinc12' or 'zinc15'")

    stripped_id = zinc_id.strip('ZINC')

    if backend == 'zinc12':
        min_len = 8
        base_path = 'http://zinc.docking.org/substance/'
        line_lookup = ('<a href="//zinc.docking.org'
                       '/search/structure?smiles=')
        first_linesplit = line_lookup
        second_linesplit = '">Draw</a>'

    else:
        min_len = 12
        base_path = 'http://zinc15.docking.org/substances/'
        line_lookup = 'id="substance-smiles-field" readonly value="'
        first_linesplit = line_lookup
        second_linesplit = '">'

    while len(stripped_id) < min_len:
        stripped_id = '0' + stripped_id

    smile_str = None

    try:
        if sys.version_info[0] == 3:
            response = urllib.request.urlopen(
                '{}{}'
                .format(base_path, stripped_id))
        else:
            response = urllib.urlopen('{}{}'
                                      .format(base_path, stripped_id))
    except urllib.error.HTTPError:
        print('Invalid ZINC ID {}'.format(zinc_id))
        response = []
    for line in response:
        line = line.decode(encoding='UTF-8').strip()
        if line_lookup in line:
            line = (line.split(first_linesplit)[-1]
                    .split(second_linesplit)[0])
            if sys.version_info[0] == 3:
                smile_str = urllib.parse.unquote(line)
            else:
                smile_str = urllib.unquote(line)
            break
    return smile_str


def get_zincid_from_smile(smile_str, backend='zinc15'):
    """
    Gets the corresponding ZINC ID(s) for a SMILE string query from
    the ZINC online database. Requires an internet connection.

    Keyword arguments:
        smile_str (str): A valid SMILE string, e.g.,
            C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O'
        backend (str): Specifies the database backend, "zinc12" or "zinc15"

    Returns the SMILE string for the corresponding ZINC ID(s) in a list.
        E.g., ['ZINC01234567', 'ZINC01234568', 'ZINC01242053', 'ZINC01242055']

    """

    if backend not in {'zinc12', 'zinc15'}:
        raise ValueError("backend must be 'zinc12' or 'zinc15'")

    stripped_smile = smile_str.strip()
    encoded_smile = urllib.parse.quote(stripped_smile)

    if backend == 'zinc12':
        url_part1 = 'http://zinc12.docking.org/results?structure.smiles='
        url_part3 = '&structure.similarity=1.0'
    elif backend == 'zinc15':
        url_part1 = 'http://zinc.docking.org/substances/search/?q='
        url_part3 = ''
    else:
        raise ValueError("Backend must be 'zinc12' or 'zinc15'. "
                         "Got %s" % (backend))

    zinc_ids = []

    try:
        if sys.version_info[0] == 3:
            #smile_url = urllib.request.pathname2url(encoded_smile)
            response = urllib.request.urlopen('{}{}{}'
                                              .format(url_part1,
                                                      encoded_smile,
                                                      url_part3))
        else:
            #smile_url = urllib.pathname2url(encoded_smile)
            response = urllib.urlopen('{}{}{}'
                                      .format(url_part1,
                                              encoded_smile,
                                              url_part3))
    except urllib.error.HTTPError:
        print('Invalid SMILE string {}'.format(smile_str))
        response = []
    for line in response:
        line = line.decode(encoding='UTF-8').strip()

        if backend == 'zinc15':
            if line.startswith('<a href="/substances/ZINC'):
                line = line.split('/')[-2]
                if sys.version_info[0] == 3:
                    zinc_id = urllib.parse.unquote(line)
                else:
                    zinc_id = urllib.unquote(line)
                zinc_ids.append(str(zinc_id))
        else:
            if line.startswith('<a href="//zinc.docking.org/substance/'):
                line = line.split('</a>')[-2].split('>')[-1]
                if sys.version_info[0] == 3:
                    zinc_id = urllib.parse.unquote(line)
                else:
                    zinc_id = urllib.unquote(line)
                zinc_id = 'ZINC' + (8-len(zinc_id)) * '0' + zinc_id
                zinc_ids.append(str(zinc_id))
    return zinc_ids


def generate_zincid_smile_csv(zincid_list, out_file,
                              print_progress_bar=True, backend='zinc12'):
    """
    Generates a CSV file of ZINC_ID,SMILE_string entries
    by querying the ZINC online database.

    Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file
             that contains 1 ZINC_ID per row. E.g.,
             ZINC0000123456
             ZINC0000234567
             [...]
        out_file (str): Path to a new output CSV file that will be written.
        print_prgress_bar (bool): Prints a progress bar to the screen if True.

    """
    id_smile_pairs = []
    with open(zincid_list, 'r') as infile:
        all_lines = infile.readlines()
        if print_progress_bar:
            pbar = pyprind.ProgBar(len(all_lines), title='Downloading SMILES')
        for line in all_lines:
            line = line.strip()
            id_smile_pairs.append((line, get_zinc_smile(line,
                                                        backend=backend)))
            if print_progress_bar:
                pbar.update()
    with open(out_file, 'w') as out:
        for p in id_smile_pairs:
            out.write('{},{}\n'.format(p[0], p[1]))


def check_duplicate_smiles(zincid_list, out_file,
                           compare_simplified_smiles=False):
    """
    Scans a ZINC_ID,SMILE_string CSV file for duplicate SMILE strings.

    Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file that
               contains 1 ZINC_ID + 1 SMILE String per row.
               E.g.,
               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC
               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
               [...]
        out_file (str): Path to a new output CSV file that will be written.
        compare_simplified_smiles (bool): If true, S
               SMILE strings will be simplified for the comparison.

    """
    smile_dict = dict()
    with open(zincid_list, 'r') as infile:
        all_lines = infile.readlines()
        for line in all_lines:
            line = line.strip().split(',')
            if len(line) == 2:
                zinc_id, smile_str = line
            if compare_simplified_smiles:
                smile_str = simplify_smile(smile_str)
            if smile_str not in smile_dict:
                smile_dict[smile_str] = [zinc_id]
            else:
                smile_dict[smile_str].append(zinc_id)

    with open(out_file, 'w') as out:
        out.write('zinc_id,smile_str,duplicates')
        for entry in smile_dict:
            out.write('\n{},{},{},'.format(
                    smile_dict[entry][0], entry, len(smile_dict[entry]) - 1))
            for duplicate in smile_dict[entry][1:]:
                out.write(duplicate + ',')
    print('\nResults written to', out_file)


def create_id_smile_list(id_smile_csv, simplify_smiles=False):
    """
    Reads in a CSV file and returns a list of [ZINC_ID,SMILE_STR] sublists.

    Keyword arguments:
        id_smile_csv (str): Path to a UTF-8 or ASCII formatted file that
               contains 1 ZINC_ID + 1 SMILE String per row.
               E.g.,
               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC
               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
               [...]
        simplify_smiles (bool): If true, SMILE strings will be simplified.

    """
    smile_list = []
    with open(id_smile_csv, 'r') as infile:
        all_lines = infile.readlines()
        for line in all_lines:
            line = line.strip().split(',')
            if len(line) == 2:
                zinc_id, smile_str = line
            if simplify_smiles:
                smile_str = simplify_smile(smile_str)
            smile_list.append([zinc_id, smile_str])
    return smile_list


def comp_two_csvfiles(zincid_list1, zincid_list2, out_file,
                      compare_simplified_smiles=False):
    """
    Compares SMILE strings across two ZINC_ID CSV files for duplicates
    (does not check for duplicates within each file).

    Keyword arguments:
        zincid_list1 (str): Path to a UTF-8 or ASCII formatted file that
               contains 1 ZINC_ID + 1 SMILE String per row.
               E.g.,
               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC
               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
               [...]
        zincid_list2 (str): Second ZINC_ID list file, similarly
        out_file (str): Path to a new output CSV file that will be written.
        compare_simplified_smiles (bool): If true,
               SMILE strings will be simplified for the comparison.

    """
    smile_list1 = create_id_smile_list(zincid_list1, compare_simplified_smiles)
    smile_list2 = create_id_smile_list(zincid_list2, compare_simplified_smiles)

    with open(out_file, 'w') as out:
        out.write('file_origin,zinc_id,smile_str,duplicates')
        for entry in smile_list1:
            out.write('\n{},{},{},'.format(
                zincid_list1, entry[0], entry[1]))
            for comp in smile_list2:
                if comp[1] == entry[1]:  # if SMILES are similar
                    out.write(comp[0] + ',')
        for entry in smile_list2:
            out.write('\n{},{},{},'.format(
                zincid_list2, entry[0], entry[1]))
            for comp in smile_list1:
                if comp[1] == entry[1]:  # if SMILES are similar
                    out.write(comp[0] + ',')
    print('\nResults written to', out_file)


def simplify_smile(smile_str):
    """
    Simplifies a SMILE string by removing hydrogen atoms (H),
    chiral specifications ('@'), charges (+ / -), '#'-characters,
    and square brackets ('[', ']').

    Keyword Arguments:
        smile_str (str): A smile string, e.g., C[C@H](CCC(=O)NCCS(=O)(=O)[O-])

    Returns a simplified SMILE string, e.g., CC(CCC(=O)NCCS(=O)(=O)O)

    """
    remove_chars = ['@', '-', '+', 'H', '[', ']', '#']
    stripped_smile = []
    for sym in smile_str:
        if sym.isalpha():
            sym = sym.upper()
        if sym not in remove_chars:
            stripped_smile.append(sym)
    return "".join(stripped_smile)


def create_sqlite(sqlite_file):
    """
    Creates a new SQLite database file if it doesn't exist yet.
    The database created will consists of 3 columns:
        1) 'zinc_id' (ZINC ID as Primary Key)
        2) 'smile' (SMILE string obtained from the ZINC online db)
        3) 'simple_smile' (simplified SMILE string,
            see smilite.simplify_smile())

    Keyword arguments:
        sqlite_file (str): Path to the new SQLite database file.

    """
    if not os.path.exists(sqlite_file):
        # open connection to a sqlite file object
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # creating a new SQLite table with 3 columns
        c.execute('CREATE TABLE smilite (zinc_id TEXT PRIMARY KEY,'
                  ' smile TEXT, simple_smile TEXT)')

        # commit changes and close the connection to the sqlite file object.
        conn.commit()
        conn.close()


def insert_id_sqlite(sqlite_file, zinc_id, backend='zinc12'):
    """
    Inserts a new ZINC ID into an existing SQLite database if the ZINC ID
    isn't contained in the database, yet. Obtains the SMILE string from the
    ZINC online database and adds it to the new ZINC ID database entry together
    with an simplified SMILE string.

    Example database entry:
    zinc_id,smile,simple_smile
    "ZINC01234567","C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O","CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O"

    Keyword arguments:
        sqlite_file (str): Path to an existing SQLite database file
        zinc_id (str): A valid ZINC ID

    Returns True if insertion was successful, else returns False.

    """
    success = False
    if os.path.exists(sqlite_file):
        # open connection to a sqlite file object
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # get smile string and simplified smile string
        smile_str = get_zinc_smile(zinc_id, backend=backend)
        if smile_str:
            simple_smile = simplify_smile(smile_str)

        # insert data into database
        if smile_str and simple_smile:
            c.execute('INSERT OR IGNORE INTO smilite (zinc_id, smile,'
                      ' simple_smile) VALUES (?, ?, ?)',
                      (zinc_id, smile_str, simple_smile))
            success = True

        # commit changes and close the connection to the sqlite file object.
        conn.commit()
        conn.close()
        return success

    else:
        return success


def lookup_id_sqlite(sqlite_file, zinc_id):
    """
    Looks up an ZINC ID in an existing SQLite database file.

    Keyword arguments:
        sqlite_file (str): Path to an existing SQLite database file
        zinc_id (str): A valid ZINC ID

    Returns a list with the ZINC ID, SMILE string, and simplified SMILE
        string or an empty list if ZINC ID could not be found.
        Example returned list:
        ['ZINC01234567', 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',
         'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']

    """
    result = []
    if os.path.exists(sqlite_file):

        # open connection to a sqlite file object
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        c.execute('SELECT * FROM smilite WHERE zinc_id=?', (zinc_id,))
        all_rows = c.fetchall()
        try:
            result = [i for i in all_rows[0]]
        except IndexError:
            pass

        # close the connection to the sqlite file object.
        conn.close()

    return result


def lookup_smile_sqlite(sqlite_file, smile_str, simple_smile=False):
    """
    Looks up an ZINC ID for a given SMILE string in an existing
    SQLite database file.

    Keyword arguments:
        sqlite_file (str): Path to an existing SQLite database file
        smile_str (str): A SMILE string to query the database
        simple_smile (bool): Queries simplified smile strings in the
            database if true

    Returns a list with the ZINC ID, SMILE string, and simplified SMILE
        string or an empty list if SMILE string could not be found.
        Example returned list:
        ['ZINC01234567', 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',
         'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']
        If multiple ZINC IDs match the query SMILE string, a list of sublists
        is returned.

    """
    result = []
    if os.path.exists(sqlite_file):

        # open connection to a sqlite file object
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        if simple_smile:
            c.execute('SELECT * FROM smilite WHERE simple_smile=?',
                      (smile_str,))
        else:
            c.execute('SELECT * FROM smilite WHERE smile=?', (smile_str,))
        all_rows = c.fetchall()
        try:
            for i in all_rows:
                result.append([j for j in i])
        except IndexError:
            pass

        # close the connection to the sqlite file object.
        conn.close()

    return result


def sqlite_to_dict(sqlite_file):
    """
    Returns contents of an SQLite smilite database as Python dictionary object.

    Keyword arguments:
        sqlite_file (str): Path to an existing SQLite database file

    Returns an SQLite smilite database as Python dictionary object with
        ZINC IDs as keys and corresponding
        [SMILE_string, Simple_SMILE_string] lists as values.

    Example returned dictionary:
    {
        'ZINC01234568': ['C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',
                        'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O'],
        'ZINC01234567': ['C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',
                        'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']
    }

    """
    result = {}
    if os.path.exists(sqlite_file):

        # open connection to a sqlite file object
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        c.execute('SELECT * FROM smilite')
        all_rows = c.fetchall()
        try:
            result = {i[0]: [i[1], i[2]] for i in all_rows}
        except IndexError:
            pass

        # close the connection to the sqlite file object.
        conn.close()

    return result


def sqlite_to_csv(sqlite_file, csv_file):
    """
    Writes contents of an SQLite smilite database to a CSV file.

    Keyword arguments:
        sqlite_file (str): Path to an existing SQLite database file
        csv_file (str): Path to the output CSV file

    Example output CSV file contents:

    ZINC_ID,SMILE,SIMPLE_SMILE
    ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
    ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
    ...

    """
    zinc_dict = sqlite_to_dict(sqlite_file)
    with open(csv_file, 'a') as out_csv:
        out_csv.write('ZINC_ID,SMILE,SIMPLE_SMILE\n')
        for k in zinc_dict.keys():
            line = '{},{}\n'.format(k, ",".join(zinc_dict[k]))
            out_csv.write(line)
