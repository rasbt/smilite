# Sebastian Raschka, 02/2014

import smilite

def test_simplify_smile():
    out = smilite.simplify_smile('C[C@H](CCC(=O)NCCS(=O)(=O)[O-])')
    assert out == 'CC(CCC(=O)NCCS(=O)(=O)O)'

