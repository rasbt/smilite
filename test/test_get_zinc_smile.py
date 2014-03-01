# Sebastian Raschka, 02/2014

import smilite

def test_get_zinc_smile():
    out = smilite.get_zinc_smile('ZINC00029323')
    assert out == 'COc1cccc(c1)NC(=O)c2cccnc2'

