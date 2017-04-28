# Copyright 2014 Sebastian Raschka
#
# Retrieves the SMILE string and simplified SMILE string for a given ZINC ID
# from the online ZINC database.
#
#
# Usage:
# [shell]>> python3 lookup_zincid.py ZINC_ID
#
# Example (retrieve data from the ZINC online database):
# [shell]>> python3 lookup_zincid.py ZINC01234567
#
#
#
# Output example:
# ZINC01234567
# C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
# CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
#
#     Where
#     1st row: ZINC ID
#     2nd row: SMILE string
#     3rd row: simplified SMILE string
#

import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 lookup_zincid.py ZINC_ID [zinc12 (default)/zinc15]')
    print('\n\nEXAMPLES (retrieve data from ZINC):\n'
          '1) python3 lookup_zincid.py ZINC01234567 zinc12\n'
          '2) python3 lookup_zincid.py ZINC01234567 zinc15')


smile_str = ''
simple_smile_str = ''

try:
    zinc_id = sys.argv[1]

    if len(sys.argv) >= 3:
        backend = sys.argv[2]
    else:
        backend = 'zinc12'

    smile_str = smilite.get_zinc_smile(zinc_id, backend=backend)
    if smile_str:
        simple_smile_str = smilite.simplify_smile(smile_str)
    print('{}\n{}\n{}'.format(zinc_id, smile_str, simple_smile_str))

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()

except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()
