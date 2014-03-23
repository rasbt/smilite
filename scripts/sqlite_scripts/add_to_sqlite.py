# Copyright 2014 Sebastian Raschka
#
# Reads ZINC IDs from a CSV file and looks up SMILE strings and simplified SMILE strings
# from the ZINC online database. Writes those SMILE strings to a smilite SQLite database.
# A new database will be created if it doesn't exist, yet.
#
# Usage: 
# [shell]>> python3 add_to_sqlite.py sqlite_file csv_file
#
# Example:
# [shell]>> python3 add_to_sqlite.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_ids.csv
#
#
# Input CSV file example format:
# ZINC01234567
# ZINC01234568
# ...
#
#
#



import smilite
import sys
import os

def print_usage():
    print('\nUSAGE: python3 add_to_sqlite.py sqlite_file csv_file')
    print('\nEXAMPLE:\n'\
          'python3 add_to_sqlite.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_ids.csv')

try:
    sqlite_file = sys.argv[1]
    csv_file = sys.argv[2]
    if not os.path.exists(sqlite_file):
        smilite.create_sqlite(sqlite_file)
    with open(csv_file, 'r') as in_csv:
        for line in in_csv:
            line = line.strip()
            if line:
                zinc_id = line.split(',')[0]
                smilite.insert_id_sqlite(sqlite_file, zinc_id)
    
except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()
    
except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()

