# Copyright 2014 Sebastian Raschka
#
# Retrieves the ZINC ID(s) for a given SMILE sting or simplified SMILE string
# from a previously built smilite SQLite database.
#
#
# Usage: 
# [shell]>> python3 lookup_smile.py sqlite_file SMILE_STRING [simplify]
#
# Example1 (search for SMILE string):
# [shell]>> python3 lookup_smile.py ~/Desktop/smilite.sqlite "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"
#
# Example2 (search for simplified SMILE string):
# [shell]>> python3 lookup_smile.py ~/Desktop/smilite.sqlite "CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O" simple
#
#
#
# Output example:
#  ZINC01234567
#  C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
#  CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
#
#     Where
#     1st row: ZINC ID
#     2nd row: SMILE string
#     3rd row: simplified SMILE string
#



import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 lookup_smile.py sqlite_file SMILE_STRING [simplify]')
    print('\n\nEXAMPLE1 (search for SMILE string):\n'\
          'python3 lookup_smile.py ~/Desktop/smilite.sqlite "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"')
    print('\n\nEXAMPLE2 (search for simplified SMILE string):\n'\
          'python3 lookup_smile.py ~/Desktop/smilite.sqlite "CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O simple\n"')

zinc_id = ''
simple_smile = False

try:
    sqlite_file = sys.argv[1]
    smile = sys.argv[2]
    if len(sys.argv) > 3:
        simple_smile = True
                
    result = smilite.lookup_smile_sqlite(sqlite_file, smile, simple_smile)
    for i in result:
        if isinstance(i, list):
            for j in i:
                print(j)
        else:
            print(i)

    
except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()

