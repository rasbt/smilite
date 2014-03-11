# Copyright 2014 Sebastian Raschka
# 
# Functions to retrieve SMILE strings from the ZINC online database
# (http://zinc.docking.org)

import sys
import pyprind


# Load Python version specific modules
if sys.version_info[0] == 3:
    import urllib.request
    import urllib.parse
else:
    import urllib


def get_zinc_smile(zinc_id):
    """
    Gets the corresponding SMILE string for a ZINC ID query from
    the ZINC online database. Requires an internet connection.

    Keyword arguments:
        zinc_id (str): A valid ZINC ID, e.g. 'ZINC00029323'

    Returns the SMILE string for the corresponding ZINC ID.
        E.g., 'COc1cccc(c1)NC(=O)c2cccnc2'

    """
    stripped_id = zinc_id.strip('ZINC')
    smile_str = None
    try:
        if sys.version_info[0] == 3: 
            response = urllib.request.urlopen('http://zinc.docking.org/substance/{}'\
                                             .format(stripped_id))
        else:
            response = urllib.urlopen('http://zinc.docking.org/substance/{}'\
                                             .format(stripped_id))
    except urllib.error.HTTPError:
        print('Invalid ZINC ID {}'.format(zinc_id))
        response = []
    for line in response:
        line = line.decode(encoding='UTF-8').strip()
        if line.startswith('<a href="//zinc.docking.org/search/structure?smiles='):
            line = line.split('<a href="//zinc.docking.org/search/structure?smiles=')[-1].split('">Draw</a>')[0]
            if sys.version_info[0] == 3:
                smile_str = urllib.parse.unquote(line)
            else:
                smile_str = urllib.unquote(line)
            break
    return smile_str    


def generate_zincid_smile_csv(zincid_list, out_file, print_progress_bar=False):
    """
    Generates a CSV file of ZINC_ID,SMILE_string entries by querying the ZINC online
    database.

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
            id_smile_pairs.append((line, get_zinc_smile(line)))
            if print_progress_bar:
                pbar.update()
    with open(out_file, 'w') as out:
        for p in id_smile_pairs:
            out.write('{},{}\n'.format(p[0], p[1]))


def check_duplicate_smiles(zincid_list, out_file, compare_simplified_smiles=False):
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
        compare_simplified_smiles (bool): If true, SMILE strings will be simplified
               for the comparison.
       
    """
    smile_dict = dict()
    with open(zincid_list, 'r') as infile:
        all_lines = infile.readlines()
        for line in all_lines:
             line = line.strip().split(',')
             if len(line) == 2:
                 zinc_id,smile_str = line
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
                 zinc_id,smile_str = line
             if simplify_smiles:
                 smile_str = simplify_smile(smile_str)
             smile_list.append([zinc_id,smile_str])
    return smile_list


def comp_two_files(zincid_list1, zincid_list2, out_file, compare_simplified_smiles=False):
    """
    Compares SMILE strings across two ZINC_ID files for duplicates 
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
        compare_simplified_smiles (bool): If true, SMILE strings will be simplified
               for the comparison.
       
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

