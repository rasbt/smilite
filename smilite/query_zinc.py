# Sebastian Raschka, 2014

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

if __name__ == '__main__':
    print(get_zinc_smile('ZINC00029323'))
