# Copyright 2014 Sebastian Raschka
#
# Generates a ZINC_ID,SMILE_STR csv file from a input file of
# ZINC IDs. The input file should consist of 1 columns with 1 ZINC ID per row.
#
# Input example file format:
#      ZINC0000123456
#      ZINC0000234567
#      ...
#
# Output example file format:
#      ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC
#      ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
#      ...
#
# Usage: 
# [shell]>> python3 gen_zincid_smile_csv.py in.csv out.csv
#
# Example:
# [shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv


import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 gen_zincid_smile_csv.py in.csv out.csv')
    print('\nEXAMPLE: python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv\n')

try:
    in_csv = sys.argv[1]
    out_csv = sys.argv[2]

    smilite.generate_zincid_smile_csv(in_csv, out_csv, print_progress_bar=True)

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()

