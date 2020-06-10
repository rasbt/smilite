# Copyright 2014 Sebastian Raschka
#
# Retrieves the corresponding ZINC_IDs for a given SMILE string
# from the online ZINC database.
#
#
# Usage:
# [shell]>> python3 lookup_smile_str.py SMILE_str
#
# Example (retrieve data from the ZINC online database):
# [shell]>> python3 lookup_smile_str.py \
#           'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O'
#
#
# Output example:
# ZINC01234567
# ZINC01234568
# ZINC01242053
# ZINC01242055
#

import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 lookup_smile_str.py SMILE_str Backend')
    print('\n\nUses zinc15 as backend by default'
          '\n\nEXAMPLE 1 (retrieve data from ZINC12):\n'
          'python3 lookup_smile_str.py'
          ' C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"'
          '\n\nEXAMPLE 2 (retrieve data from ZINC12):\n'
          'python3 lookup_smile_str.py'
          ' CCOc1ccc(cc1)N([C@@H](C)C(=O)Nc2ccc(cc2C)Cl)S(=O)(=O)C" zinc12')


zinc_id = [None]

try:
    smile_str = sys.argv[1]

    if len(sys.argv) >= 3:
        backend = sys.argv[2]
    else:
        backend = 'zinc15'

    zinc_ids = smilite.get_zincid_from_smile(smile_str, backend=backend)
    for zid in zinc_ids:
        print(zid)

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()

except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()
