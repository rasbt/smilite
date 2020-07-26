# Copyright 2014-2020 Sebastian Raschka
#
# Writes contents of an SQLite smilite database to a CSV file.
#
# Usage: 
# [shell]>> python3 sqlite_to_csv.py sqlite_file csv_file
#
# Example:
# [shell]>> python3 sqlite_to_csv.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_smiles.csv
#
# Output CSV file example:
# ZINC_ID,SMILE,SIMPLE_SMILE
# ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
# ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
#

import smilite
import sys
import os

def print_usage():
    print('\nUSAGE: python3 sqlite_to_csv.py sqlite_file csv_file')
    print('\nEXAMPLE:\n'\
          'python3 sqlite_to_csv.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_smiles.csv')

try:
    sqlite_file = sys.argv[1]
    csv_file = sys.argv[2]
    smilite.sqlite_to_csv(sqlite_file, csv_file)
    
except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()

