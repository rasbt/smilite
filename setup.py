from distutils.core import setup

setup(name='smilite',
      version='2.1.0',
      description='smilite is a Python module to download and analyze SMILE strings',
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
                    ('examples', ['examples/comp_2_files.csv']),
                    ('examples', ['examples/README.md']),
                    ('examples', ['examples/zid_smiles.csv']),
                    ('examples', ['examples/zid_smiles2.csv']),
                    ('examples', ['examples/zid_smiles3.csv']),
                    ('examples', ['examples/zinc_ids.csv']),
                    ('scripts', ['scripts/csv_scripts/comp_smile_strings.py']),
                    ('scripts', ['scripts/csv_scripts/gen_zincid_smile_csv.py']),
                    ('scripts', ['scripts/csv_scripts/comp_2_smile_files.py']),
                    ('scripts', ['scripts/sqlite_scripts/lookup_single_id.py']),
                    ('scripts', ['scripts/sqlite_scripts/lookup_smile.py']),
                    ('scripts', ['scripts/sqlite_scripts/add_to_sqlite.py']),
                    ('scripts', ['scripts/sqlite_scripts/sqlite_to_csv.py']),
                    ('scripts', ['scripts/cmd_line_online_query_scripts/lookup_zincid.py']),
                    ('scripts', ['scripts/cmd_line_online_query_scripts/lookup_smile_str.py']),
                   ],
      install_requires=['PyPrind>=2.3.1'],
      license='GPLv3',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2.7',
          'Environment :: Console',
      ],
      long_description="""

smilite is a Python module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System)
of chemical compounds from ZINC 
(a free database of commercially-available compounds for virtual screening, http://zinc.docking.org).
Now supports both Python 3.x and Python 2.x.


 Contact
=============

If you have any questions or comments about smilite, please feel free to contact me via
eMail: se.raschka@gmail.com
or Twitter: https://twitter.com/rasbt

""",
    )
