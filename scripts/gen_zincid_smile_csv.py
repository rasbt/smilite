# Sebastian Raschka, 2014
#
# Generates a ZINC_ID,SMILE_STR csv file from a input file of
# ZINC IDs

import smilite

smilite.query_zinc.generate_zincid_smile_csv('/Users/sebastian/Desktop/zinc_ids.csv', '/Users/sebastian/Desktop/zinc_smile.csv')
