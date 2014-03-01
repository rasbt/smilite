# Copyright 2014 Sebastian Raschka
#
# Compares SMILE strings in a 2 column CSV file (ZINC_ID,SMILE_string) to
# identify duplicates. Generates a new CSV file with ZINC IDs of identified
# duplicates listed in a 3rd-nth column(s).
#
#
# Input example file format:
#     ZINC00029323,COc1cccc(c1)NC(=O)c2cccnc2
#     ZINC00029323,COc1cccc(c1)NC(=O)c2cccnc2
#     ZINC83310457,Cc1cccc(c1n2c(cc(c2C)/C=N\NC(=O)C(=O)Nc3ccc(cc3)[N+](=O)[O-])C)C
#     ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
#
# Output example file format:
#     zinc_id,smile_str,duplicates
#     ZINC00029323,COc1cccc(c1)NC(=O)c2cccnc2,1,ZINC00029323,
#     ZINC83310457,Cc1cccc(c1n2c(cc(c2C)/C=N\NC(=O)C(=O)Nc3ccc(cc3)[N+](=O)[O-])C)C,0,
#     ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,0,
#
#     Where
#     1st column: ZINC ID
#     2nd column: SMILE string
#     3rd column: number of duplicates
#     4th-nth column: ZINC IDs of duplicates
#
# Usage: 
# [shell]>> python3 comp_smile_strings.py in.csv out.csv [simplify]
#
# Example1:
# [shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv
#
# Example2:
# [shell]>> python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify


import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 comp_smile_strings.py in.csv out.csv [simplify]')
    print('\nEXAMPLE1: python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_smiles.csv\n')
    print('\nEXAMPLE2: python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify\n')


try:
    in_csv = sys.argv[1]
    out_csv = sys.argv[2]
    simplify = False
    
    if len(sys.argv) > 3:
        simplify = True
    
    smilite.check_duplicate_smiles(in_csv, out_csv, compare_simplified_smiles=simplify)

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()


