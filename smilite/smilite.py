# Copyright 2014 Sebastian Raschka
# 
# Functions to retrieve SMILE strings from the ZINC online database
# (http://zinc.docking.org)

import urllib.request
import urllib.parse

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
        response = urllib.request.urlopen('http://zinc.docking.org/substance/{}'.format(stripped_id))
    except urllib.error.HTTPError:
        print('Invalid ZINC ID {}'.format(zinc_id))
        response = []
    for line in response:
        line = line.decode(encoding='UTF-8').strip()
        if line.startswith('<a href="//zinc.docking.org/search/structure?smiles='):
            line = line.split('<a href="//zinc.docking.org/search/structure?smiles=')[-1].split('">Draw</a>')[0]
            smile_str = urllib.parse.unquote(line)
            break
    return smile_str    


def generate_zincid_smile_csv(zincid_list, out_file):
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

    """
    id_smile_pairs = []
    with open(zincid_list, 'r') as infile:
        for line in infile:
             line = line.strip()
             id_smile_pairs.append((line, get_zinc_smile(line)))
    with open(out_file, 'w') as out:
        for p in id_smile_pairs:
            out.write('{},{}\n'.format(p[0], p[1]))


def check_duplicate_smiles(zincid_list, out_file, compare_simplified_smiles=False):
    """
    Scans a ZINC_ID,SMILE_string CSV file for duplicate SMILE strings.

    Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file that 
               contains 1 ZINC_ID per row.
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
        for line in infile:
             zinc_id,smile_str = line.strip().split(',')
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

