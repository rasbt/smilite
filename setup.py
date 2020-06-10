from setuptools import setup

setup(name='smilite',
      version='2.3.0',
      description='smilite is a Python module to download'
                  ' and analyze SMILE strings',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/smilite',
      packages=['smilite'],
      package_data={'': ['LICENSE.txt',
                         'README.md',
                         'CHANGELOG.txt']},
      install_requires=['PyPrind>=2.3.1'],
      license='GPLv3',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
      ],
      long_description="""

smilite is a Python module to download and analyze SMILE strings
(Simplified Molecular-Input Line-entry System)
of chemical compounds from ZINC
(a free database of commercially-available compounds for virtual screening,
http://zinc.docking.org).

Source repository: https://github.com/rasbt/smilite

""")
