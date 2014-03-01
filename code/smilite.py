# Sebastian Raschka, 2014
#
# A Python tool to build a SQLite database with Molecule SMILE Strings for quick molecule comparisons.
#
#

import sqlite3

def print_menu():
    """ 
    Prints the menu that prompts the user to select an operation. 
    """
    pass

def parse_user_option():
    """
    Prompts user for an option an executes the appropriate function.
    """ 
    pass

def connect_2_db():
    """ 
    Asks user to provide a SQLite database location or creates a
    new SQLite database. 
    Returns an open connection to the database file.
    """
    pass

def create_new_db(file_dir):
    """
    Creates a new SQLite database with the following specifications:
    table name: smilite_db
    primary key column (TEXT): molecule_id (TEXT)
    2nd column (TEXT): smile_str
    3rd column (INT): duplicates (counts the number of duplicate SMILE strings in the database)

    Keyword arguments:
        file_dir (str): Name of the new SQLite file.

    """
    pass

def close_conn(conn):
    """
    Closes connection to an open SQLite database file object.

    Keyword arguments:
        conn (obj): open connection to a SQLite database file object.

    """
    conn.close()


def sqlite_2_csv(conn):
    """
    Write the complete SQLite database to a csv file.

    Keyword arguments:
        conn (obj): open connection to a SQLite database file object.

    """
    pass

def write_to_db(conn):
    """
    Adds new entries to the database based on an input csv file
    or a single ID-SMILE entry combination on the command line.

    Keyword arguments:
        conn (obj): open connection to a SQLite database file object.

    """
    pass

def query_db(conn):
    """
    Queries the database based on an input csv file or a single
    ID-SMILE entry combination on the command line.

    Keyword arguments:
        conn (obj): open connection to a SQLite database file object.

    """
    pass


def simplify_smile(smile_str):
    """ Simplifies a SMILE string by removing hydrogen atoms (H), 
    chiral specifications ('@'), charges (+ / -), and square brackets ('[', ']') 

    Keyword Arguments:
        smile_str (str): A smile string, e.g., C[C@H](CCC(=O)NCCS(=O)(=O)[O-])
    
    Returns a simplified SMILE string, e.g., C[C](CCC(=O)NCCS(=O)(=OO)

    """
    remove_chars = ['@', '-', '+', 'H', '[', ']' ]
    stripped_smile = []
    for sym in smile_str:
        if sym.isalpha():
            sym = sym.upper()
        if sym not in remove_chars:
            stripped_smile.append(sym)
    return "".join(stripped_smile)
    

if __name__ == '__main__':
    pass
