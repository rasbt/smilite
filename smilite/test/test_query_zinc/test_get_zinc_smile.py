# Sebastian Raschka, 02/2014

import smilite.query_zinc

def test_query_zinc():
    out = smilite.query_zinc.get_zinc_smile('ZINC00029323')
    assert out == 'COc1cccc(c1)NC(=O)c2cccnc2'

