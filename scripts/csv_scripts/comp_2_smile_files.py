# Copyright 2014-2020 Sebastian Raschka
#
# Compares SMILE strings between 2 input CSV files, where each
# file consists of rows with 2 columns ZINC_ID,SMILE_string to #
# identify duplicate SMILE string across both files.
# Generates a new CSV file with ZINC IDs of identified
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
#     file_origin,zinc_id,smile_str,duplicates
#     my_file1.csv,ZINC00029323,COc1cccc(c1)NC(=O)c2cccnc2,1,ZINC00029323,
#     my_file1.csv,ZINC83310457,Cc1cccc(c1n2c(cc(c2C)/C=N\NC(=O)C(=O)Nc3ccc(cc3)[N+](=O)[O-])C)C,0,
#     my_file1.csv,ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,0,
#     my_file2.csv,ZINC00029323,COc1cccc(c1)NC(=O)c2cccnc2,1,ZINC00029323,
#     my_file2.csv,ZINC83310457,Cc1cccc(c1n2c(cc(c2C)/C=N\NC(=O)C(=O)Nc3ccc(cc3)[N+](=O)[O-])C)C,0,
#     my_file2.csv,ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,0,
#
#
#
#     Where
#     1st column: name of the origin file
#     2nd column: ZINC ID
#     3rd column: SMILE string
#     4th-nth column: ZINC IDs of duplicates
#
# Usage:
# [shell]>> python3 comp_2_smile_files.py in1.csv in2.csv out.csv [simplify]
#
# Example 1:
# [shell]>> python3 comp_2_smile_files.py \
# ../examples/zid_smiles2.csv \
# ../examples/zid_smiles3.csv \
# ../examples/comp_2_files.csv
#
# Example 2:
# [shell]>> python3 comp_2_smile_files.py \
# ../examples/zid_smiles2.csv \
# ../examples/zid_smiles3.csv \
# ../examples/comp_2_files.csv simplify


import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 comp_2_smile_files.py'
          ' in1.csv in2.csv out.csv [simplify]')
    print('\nEXAMPLE 1: python3 comp_2_smile_files.py'
          ' ../examples/zid_smiles2.csv ../examples/zid_smiles3.csv'
          ' ../examples/comp_2_files.csv\n')
    print('\nEXAMPLE 2: python3 comp_2_smile_files.py'
          ' ../examples/zid_smiles2.csv ../examples/zid_smiles3.csv'
          ' ../examples/comp_2_files.csv simplify\n')


try:
    in_csv1 = sys.argv[1]
    in_csv2 = sys.argv[2]
    out_csv = sys.argv[3]
    simplify = False

    if len(sys.argv) > 4:
        simplify = True

    smilite.comp_two_csvfiles(in_csv1, in_csv2,
                              out_csv, compare_simplified_smiles=simplify)

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()

except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()
