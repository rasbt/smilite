from distutils.core import setup

setup(name='smilite',
      version='1.1.0',
      description='smilite is a Python 3 module to download and analyze SMILE strings',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/smilite',
      packages=['smilite'],
      data_files = [('', ['LICENSE.txt']),
                    ('', ['README.html']),
                    ('', ['README.md']),
                    ('', ['CHANGELOG.txt']),
                    ('test', ['test/test_get_zinc_smile.py']),
                    ('test', ['test/test_simplify_smile.py']),
                    ('examples', ['examples/comp_simple_smiles.csv']),
                    ('examples', ['examples/comp_smiles.csv']),
                    ('examples', ['examples/README.md']),
                    ('examples', ['examples/zid_smiles.csv']),
                    ('examples', ['examples/zinc_ids.csv']),
                    ('scripts', ['scripts/comp_smile_strings.py']),
                    ('scripts', ['scripts/gen_zincid_smile_csv.py']),
                   ],
      install_requires=['pyprind>=2.3.1'],
      license='GPLv3',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
      ],
      long_description="""

smilite is a Python 3 module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System)
of chemical compounds from ZINC 
(a free database of commercially-available compounds for virtual screening, http://zinc.docking.org)


 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via
eMail: se.raschka@gmail.com
or Twitter: https://twitter.com/rasbt

""",
    )
