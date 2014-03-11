# Copyright 2014 Sebastian Raschka
#
# A small module to retrieve SMILE strings 
# (Simplified molecular-input line-entry system) from the ZINC online
# database (http://zinc.docking.org)

from .smilite import get_zinc_smile
from .smilite import generate_zincid_smile_csv
from .smilite import simplify_smile
from .smilite import check_duplicate_smiles
from .smilite import comp_two_files
from .smilite import create_id_smile_list

__version__ = '1.3.0'


