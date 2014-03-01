# Sebastian Raschka, 2014

import urllib.request
import urllib.parse

def get_zinc_smile(zinc_id):
    """
    Gets the corresponding SMILE string for a ZINC ID query from
    the ZINC online database. Requires an internet connection.

    Keyword arguments:
        zinc_id (str): A valid ZINC ID, e.g. 'ZINC00029323'

    Returns the SMILE string for the corresponding ZINC ID.
        E.g., 'COc1cccc(c1)NC(=O)c2cccnc2'

    """
    stripped_id = zinc_id.strip('ZINC')
    smile_str = None
    response = urllib.request.urlopen('http://zinc.docking.org/substance/{}'.format(stripped_id))
    for line in response:
        line = line.decode(encoding='UTF-8').strip()
        if line.startswith('<a href="//zinc.docking.org/search/structure?smiles='):
            line = line.split('<a href="//zinc.docking.org/search/structure?smiles=')[-1].split('">Draw</a>')[0]
            smile_str = urllib.parse.unquote(line)
            break
    return smile_str    


def generate_zincid_smile_csv(zincid_list, out_file):
    """ 
    Generates a CSV file of ZINC_ID,SMILE_string entries by querying the ZINC online
    database.

    Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file that contains 1 ZINC_ID
        per row.
        E.g., 
        ZINC0000123456
        ZINC0000234567

    """
    id_smile_pairs = []
    with open(zincid_list, 'r') as infile:
        for line in infile:
             line = line.strip()
             id_smile_pairs.append((line, get_zinc_smile(line)))
    with open(out_file, 'w') as out:
        for p in id_smile_pairs:
            out.write('{},{}\n'.format(p[0], p[1]))
