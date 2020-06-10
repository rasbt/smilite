# Copyright 2014-2020 Sebastian Raschka
#
# A small module to retrieve SMILE strings 
# (Simplified molecular-input line-entry system) from the ZINC online
# database (http://zinc.docking.org)

from .smilite import get_zinc_smile
from .smilite import generate_zincid_smile_csv
from .smilite import simplify_smile
from .smilite import check_duplicate_smiles
from .smilite import comp_two_csvfiles
from .smilite import create_id_smile_list
from .smilite import create_sqlite
from .smilite import insert_id_sqlite
from .smilite import lookup_id_sqlite
from .smilite import lookup_smile_sqlite
from .smilite import sqlite_to_dict
from .smilite import sqlite_to_csv
from .smilite import get_zincid_from_smile

__version__ = '2.3.0'

