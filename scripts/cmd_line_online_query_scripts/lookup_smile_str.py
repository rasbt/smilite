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
# [shell]>> python3 lookup_smile_str.py 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O'
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
    print('\nUSAGE: python3 ookup_smile_str.py SMILE_str')
    print('\n\nEXAMPLE (retrieve data from ZINC):\n'\
          'python3 lookup_smile_str.py "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"')

zinc_id = [None]

try:
    smile_str = sys.argv[1]
    zinc_ids = smilite.get_zincid_from_smile(smile_str)
    for zid in zinc_ids:
        print(zid)    

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()


