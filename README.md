# smilite

smilite is a Python module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System) of chemical compounds from ZINC (a free database of commercially-available compounds for virtual screening, [http://zinc.docking.org](http://zinc.docking.org)).  
Now supports both Python 3.x and Python 2.x.

![](https://raw.github.com/rasbt/smilite/master/images/smilite_overview.png)  

#### Sections

• [Installation](#installation)  
• [Simple command line online query scripts](#simple_cmd_scripts)  
      - [lookup_zincid.py](#lookup_zincid)  
      - [lookup_smile_str.py](#lookup_smile_str)  
• [CSV file command line scripts](#csv_scripts)  
      - [gen_zincid_smile_csv.py (downloading SMILES)](#gen_zincid)  
      - [comp_smile_strings.py (checking for duplicates within 1 file)](#comp_smile)  
      - [comp_2_smile_files.py (checking for duplicates across 2 files)](#comp_2_smile)  
• [SQLite file command line scripts](#sqlite_scripts)  
      - [lookup_single_id.py](#lookup1id)  
      - [lookup_smile.py](#lookupsmile)  
      - [add_to_sqlite.py](#add_to_sqlite)  
      - [sqlite_to_csv.py](#sqlite_to_csv)  
• [Documentation](#documentation)  
      - [General functions](#general_func)  
      - [CSV file functions](#csvfile_func)  
      - [SQLite functions](#sqlite_func)  

• [Contact](#contact)  
• [Changelog](#changelog)  

<a name="installation"></a>

# Installation

You can use the following command to install smilite:  
`pip install smilite`  
or  
`easy_install smilite`

Alternatively, you can download the package manually from the Python Package Index [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite), unzip it, navigate into the package, and use the command:

`python3 setup.py install`

<a name="simple_cmd_scripts"></a>

# Simple command line online query scripts

If you downloaded the smilite package from [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite) or [https://github.com/rasbt/smilite](https://github.com/rasbt/smilite), you can use the command line scripts I provide in the `scripts/cmd_line_online_query_scripts` dir.

<a name="lookup_zincid"></a>

### lookup_zincid.py

Retrieves the SMILE string and simplified SMILE string for a given ZINC ID  
from the online Zinc. It uses [ZINC12](http://zinc.docking.org) as the default backend, and via an additional commandline argument `zinc15`, the [ZINC15](http://zinc15.docking.org) database will be used instead.

**Usage:**  
`[shell]>> python3 lookup_zincid.py ZINC_ID [zinc12/zinc15]`  

**Example (retrieve data from ZINC):**  
`[shell]>> python3 lookup_zincid.py ZINC01234567 zinc15`  

**Output example:**

<pre>ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>

Where  
- 1st row: ZINC ID  
- 2nd row: SMILE string  
- 3rd row: simplified SMILE string

<a name="lookup_smile_str"></a>

### lookup_smile_str.py

Retrieves the corresponding ZINC_IDs for a given SMILE string  
from the online ZINC database. 

**Usage:**  
`[shell]>> python3 lookup_smile_str.py SMILE_str`  

**Example (retrieve data from ZINC):**  
`[shell]>> python3 lookup_smile_str.py "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"`  

**Output example:**

<pre>ZINC01234567
ZINC01234568
ZINC01242053
ZINC01242055</pre>

<a name="csv_scripts"></a>

# CSV file command line scripts

If you downloaded the smilite package from [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite) or [https://github.com/rasbt/smilite](https://github.com/rasbt/smilite), you can use the command line scripts I provide in the `scripts/csv_scripts` dir.

<a name="gen_zincid"></a>

### gen_zincid_smile_csv.py (downloading SMILES)

Generates a ZINC_ID,SMILE_STR csv file from a input file of ZINC IDs. The input file should consist of 1 columns with 1 ZINC ID per row. [ZINC12](http://zinc.docking.org) is used as the default backend, and via an additional commandline argument `zinc15`, the [ZINC15](http://zinc15.docking.org) database can be used instead.

**Usage:**  
`[shell]>> python3 gen_zincid_smile_csv.py in.csv out.csv [zinc12/zinc15]`

**Example:**  
`[shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv zinc15`

**Screen Output:**

<pre>Downloading SMILES
0%                          100%
[##########                    ] | ETA[sec]: 106.525 </pre>

**Input example file format:**  
![](https://raw.github.com/rasbt/smilite/master/images/zinc_ids.png)  
[zinc_ids.csv](https://raw.github.com/rasbt/smilite/master/examples/zinc_ids.csv)

**Output example file format:**  
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png)  
[zid_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv)

<a name="comp_smile"></a>

### comp_smile_strings.py (checking for duplicates within 1 file)

Compares SMILE strings within a 2 column CSV file (ZINC_ID,SMILE_string) to identify duplicates. Generates a new CSV file with ZINC IDs of identified duplicates listed in a 3rd-nth column(s).

**Usage:**  
`[shell]>> python3 comp_smile_strings.py in.csv out.csv [simplify]`

**Example 1:**  
`[shell]>> python3 comp_smile_strings.py ../examples/zinc_smiles.csv ../examples/comp_smiles.csv`

**Input example file format:**  
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png)  
[zid_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv)

**Output example file format 1:**  
![](https://raw.github.com/rasbt/smilite/master/images/comp_smiles.png)  
[comp_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_smiles.csv)

Where  
- 1st column: ZINC ID  
- 2nd column: SMILE string  
- 3rd column: number of duplicates  
- 4th-nth column: ZINC IDs of duplicates

**Example 2:**  
`[shell]>> python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify`

**Output example file format 2:** ![](https://raw.github.com/rasbt/smilite/master/images/comp_simple_smiles.png)  
[comp_simple_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_simple_smiles.csv)

<a name="comp_2_smile"></a>

### comp_2_smile_files.py (checking for duplicates across 2 files)

Compares SMILE strings between 2 input CSV files, where each file consists of rows with 2 columns ZINC_ID,SMILE_string to identify duplicate SMILE string across both files.  
Generates a new CSV file with ZINC IDs of identified duplicates listed in a 3rd-nth column(s).

**Usage:**  
`[shell]>> python3 comp_2_smile_files.py in1.csv in2.csv out.csv [simplify]`

**Example:**  
`[shell]>> python3 comp_2_smile_files.py ../examples/zid_smiles2.csv ../examples/zid_smiles3.csv ../examples/comp_2_files.csv`

**Input example file 1:**  
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles2.png)  
[zid_smiles2.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles2.csv)

**Input example file 2:**  
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles3.png)  
[zid_smiles3.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles3.csv)

**Output example file format:**  
![](https://raw.github.com/rasbt/smilite/master/images/comp_2_files.png)  
[comp_2_files.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_2_files.csv)

Where:  
- 1st column: name of the origin file  
- 2nd column: ZINC ID  
- 3rd column: SMILE string  
- 4th-nth column: ZINC IDs of duplicates

<a name="sqlite_scripts"></a>

# SQLite file command line scripts

If you downloaded the smilite package from [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite) or [https://github.com/rasbt/smilite](https://github.com/rasbt/smilite), you can use the command line scripts I provide in the `scripts/sqlite_scripts` dir.

<a name="lookup1id"></a>

### lookup_single_id.py

Retrieves the SMILE string and simplified SMILE string for a given ZINC ID  
from a previously built smilite SQLite database or from the online ZINC database.

**Usage:**  
`[shell]>> python3 lookup_single_id.py ZINC_ID [sqlite_file]`  

**Example1 (retrieve data from a smilite SQLite database):**  
`[shell]>> python3 lookup_single_id.py ZINC01234567 ~/Desktop/smilite_db.sqlite`  

**Example2 (retrieve data from the ZINC online database):**  
`[shell]>> python3 lookup_single_id.py ZINC01234567`  

**Output example:**

<pre>ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>

Where  
- 1st row: ZINC ID  
- 2nd row: SMILE string  
- 3rd row: simplified SMILE string

<a name="lookupsmile"></a>

### lookup_smile.py

Retrieves the ZINC ID(s) for a given SMILE sting or simplified SMILE string from a previously built smilite SQLite database.

**Usage:**  
`[shell]>> python3 lookup_smile.py sqlite_file SMILE_STRING [simplify]`  

**Example1 (search for SMILE string):**  
`[shell]>> python3 lookup_smile.py ~/Desktop/smilite.sqlite "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"`  

**Example2 (search for simplified SMILE string):**  
`[shell]>> python3 lookup_smile.py ~/Desktop/smilite.sqlite "CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O" simple`  

**Output example:**

<pre>ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>

Where  
- 1st row: ZINC ID  
- 2nd row: SMILE string  
- 3rd row: simplified SMILE string

<a name="add_to_sqlite"></a>

### add_to_sqlite.py

Reads ZINC IDs from a CSV file and looks up SMILE strings and simplified SMILE strings from the ZINC online database. Writes those SMILE strings to a smilite SQLite database. A new database will be created if it doesn't exist, yet.

**Usage:**  
`[shell]>> python3 add_to_sqlite.py sqlite_file csv_file`  

**Example:**  
`[shell]>> python3 add_to_sqlite.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_ids.csv`  

**Input CSV file example format:**

<pre>ZINC01234567
ZINC01234568
...
</pre>

An example of the smilite SQLite database contents after successful insertion is shown in the image below. ![https://raw.github.com/rasbt/smilite/master/images/add_to_sqlite_1.png](https://raw.github.com/rasbt/smilite/master/images/add_to_sqlite_1.png)

<a name="sqlite_to_csv"></a>

### sqlite_to_csv.py

Writes contents of an SQLite smilite database to a CSV file.

**Usage:**  
`[shell]>> python3 sqlite_to_csv.py sqlite_file csv_file`  

**Example:**  
`[shell]>> python3 sqlite_to_csv.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_smiles.csv`  

**Input CSV file example format:**

<pre>ZINC_ID,SMILE,SIMPLE_SMILE
ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>

An example of the CSV file contents opened in an spreadsheet program is shown in the image below. ![https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_2.png](https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_2.png)

<a name="documentation"></a>

# Documentation

After you installed the smilite module, you can import it in Python via `import smilite`. The current functions include:

<a name="general_func"></a>

### General functions

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_zinc_smile</span>(zinc_id):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Gets the corresponding SMILE string for a ZINC ID query from</span>
 <span style="color: #DD4422">the ZINC online database. Requires an internet connection.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">zinc_id (str): A valid ZINC ID, e.g. 'ZINC00029323'</span>

 <span style="color: #DD4422">Returns the SMILE string for the corresponding ZINC ID.</span>
 <span style="color: #DD4422">E.g., 'COc1cccc(c1)NC(=O)c2cccnc2'</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_zincid_from_smile</span>(smile_str):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Gets the corresponding ZINC ID(s) for a SMILE string query from</span>
 <span style="color: #DD4422">the ZINC online database. Requires an internet connection.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">smile_str (str): A valid SMILE string, e.g. 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O'</span> 

 <span style="color: #DD4422">Returns the SMILE string for the corresponding ZINC ID(s) in a list.</span>
 <span style="color: #DD4422">E.g., ['ZINC01234567', 'ZINC01234568', 'ZINC01242053', 'ZINC01242055']</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">simplify_smile</span>(smile_str):
    <span style="color: #DD4422">"""</span> 
 <span style="color: #DD4422">Simplifies a SMILE string by removing hydrogen atoms (H),</span> 
 <span style="color: #DD4422">chiral specifications ('@'), charges (+ / -), '#'-characters,</span>
 <span style="color: #DD4422">and square brackets ('[', ']').</span>

 <span style="color: #DD4422">Keyword Arguments:</span>
 <span style="color: #DD4422">smile_str (str): A smile string, e.g., C[C@H](CCC(=O)NCCS(=O)(=O)[O-])</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Returns a simplified SMILE string, e.g., CC(CCC(=O)NCCS(=O)(=O)O)</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<a name="csvfile_func"></a>

### CSV file functions

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">generate_zincid_smile_csv</span>(zincid_list, out_file, print_progress_bar<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Generates a CSV file of ZINC_ID,SMILE_string entries by querying the ZINC online</span>
 <span style="color: #DD4422">database.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">zincid_list (str): Path to a UTF-8 or ASCII formatted file</span> 
 <span style="color: #DD4422">that contains 1 ZINC_ID per row. E.g.,</span> 
 <span style="color: #DD4422">ZINC0000123456</span>
 <span style="color: #DD4422">ZINC0000234567</span>
 <span style="color: #DD4422">[...]</span>
 <span style="color: #DD4422">out_file (str): Path to a new output CSV file that will be written.</span>
 <span style="color: #DD4422">print_prgress_bar (bool): Prints a progress bar to the screen if True.</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">check_duplicate_smiles</span>(zincid_list, out_file, compare_simplified_smiles<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Scans a ZINC_ID,SMILE_string CSV file for duplicate SMILE strings.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">zincid_list (str): Path to a UTF-8 or ASCII formatted file that</span> 
 <span style="color: #DD4422">contains 1 ZINC_ID + 1 SMILE String per row.</span>
 <span style="color: #DD4422">E.g.,</span> 
 <span style="color: #DD4422">ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC</span>
 <span style="color: #DD4422">ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O</span>
 <span style="color: #DD4422">[...]</span>
 <span style="color: #DD4422">out_file (str): Path to a new output CSV file that will be written.</span>
 <span style="color: #DD4422">compare_simplified_smiles (bool): If true, SMILE strings will be simplified</span>
 <span style="color: #DD4422">for the comparison.</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">comp_two_csvfiles</span>(zincid_list1, zincid_list2, out_file, compare_simplified_smiles<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Compares SMILE strings across two ZINC_ID CSV files for duplicates</span> 
 <span style="color: #DD4422">(does not check for duplicates within each file).</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">zincid_list1 (str): Path to a UTF-8 or ASCII formatted file that</span> 
 <span style="color: #DD4422">contains 1 ZINC_ID + 1 SMILE String per row.</span>
 <span style="color: #DD4422">E.g.,</span> 
 <span style="color: #DD4422">ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC</span>
 <span style="color: #DD4422">ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O</span>
 <span style="color: #DD4422">[...]</span>
 <span style="color: #DD4422">zincid_list2 (str): Second ZINC_ID list file, similarly</span> 
 <span style="color: #DD4422">out_file (str): Path to a new output CSV file that will be written.</span>
 <span style="color: #DD4422">compare_simplified_smiles (bool): If true, SMILE strings will be simplified</span>
 <span style="color: #DD4422">for the comparison.</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">"""</span>
</pre>

</div>

<a name="sqlite_func"></a>

### SQLite functions

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">create_sqlite</span>(sqlite_file):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Creates a new SQLite database file if it doesn't exist yet.</span>
 <span style="color: #DD4422">The database created will consists of 3 columns:</span> 
 <span style="color: #DD4422">1) 'zinc_id' (ZINC ID as Primary Key)</span>
 <span style="color: #DD4422">2) 'smile' (SMILE string obtained from the ZINC online db)</span>
 <span style="color: #DD4422">3) 'simple_smile' (simplified SMILE string, see smilite.simplify_smile())</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to the new SQLite database file.</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">insert_id_sqlite</span>(sqlite_file, zinc_id):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Inserts a new ZINC ID into an existing SQLite database if the ZINC ID</span>
 <span style="color: #DD4422">isn't contained in the database, yet. Obtains the SMILE string from the</span>
 <span style="color: #DD4422">ZINC online database and adds it to the new ZINC ID database entry together</span>
 <span style="color: #DD4422">with an simplified SMILE string.</span>

 <span style="color: #DD4422">Example database entry:</span>
 <span style="color: #DD4422">zinc_id,smile,simple_smile</span>
 <span style="color: #DD4422">"ZINC01234567","C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O","CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O"</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to an existing SQLite database file</span>
 <span style="color: #DD4422">zinc_id (str): A valid ZINC ID</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

An example database entry is shown in the image below. ![https://raw.github.com/rasbt/smilite/master/images/insert_id_sqlite_1.png](https://raw.github.com/rasbt/smilite/master/images/insert_id_sqlite_1.png)

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lookup_smile_sqlite</span>(sqlite_file, smile_str, simple_smile<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">False</span>):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Looks up an ZINC ID for a given SMILE string in an existing</span> 
 <span style="color: #DD4422">SQLite database file.</span> 
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to an existing SQLite database file</span>
 <span style="color: #DD4422">smile_str (str): A SMILE string to query the database</span>
 <span style="color: #DD4422">simple_smile (bool): Queries simplified smile strings in the</span>
 <span style="color: #DD4422">database if true</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Returns a list with the ZINC ID, SMILE string, and simplified SMILE</span> 
 <span style="color: #DD4422">string or an empty list if SMILE string could not be found.</span>
 <span style="color: #DD4422">Example returned list:</span>
 <span style="color: #DD4422">['ZINC01234567', 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',</span>
 <span style="color: #DD4422">'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']</span>
 <span style="color: #DD4422">If multiple ZINC IDs match the query SMILE string, a list of sublists</span>
 <span style="color: #DD4422">is returned.</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lookup_smile_sqlite</span>(sqlite_file, smile_str, simple_smile<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">False</span>):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Looks up an ZINC ID for a given SMILE string in an existing</span> 
 <span style="color: #DD4422">SQLite database file.</span> 
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to an existing SQLite database file</span>
 <span style="color: #DD4422">smile_str (str): A SMILE string to query the database</span>
 <span style="color: #DD4422">simple_smile (bool): Queries simplified smile strings in the</span>
 <span style="color: #DD4422">database if true</span>
 <span style="color: #DD4422"></span> 
 <span style="color: #DD4422">Returns a list with the ZINC ID, SMILE string, and simplified SMILE</span> 
 <span style="color: #DD4422">string or an empty list if SMILE string could not be found.</span>
 <span style="color: #DD4422">Example returned list:</span>
 <span style="color: #DD4422">['ZINC01234567', 'C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',</span>
 <span style="color: #DD4422">'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">sqlite_to_dict</span>(sqlite_file):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Returns contents of an SQLite smilite database as Python dictionary object.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to an existing SQLite database file</span>

 <span style="color: #DD4422">Returns an SQLite smilite database as Python dictionary object with</span>
 <span style="color: #DD4422">ZINC IDs as keys and corresponding</span> 
 <span style="color: #DD4422">[SMILE_string, Simple_SMILE_string] lists as values.</span>

 <span style="color: #DD4422">Example returned dictionary:</span>
 <span style="color: #DD4422">{</span>
 <span style="color: #DD4422">'ZINC01234568': ['C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',</span> 
 <span style="color: #DD4422">'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O'],</span> 
 <span style="color: #DD4422">'ZINC01234567': ['C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O',</span> 
 <span style="color: #DD4422">'CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O']</span>
 <span style="color: #DD4422">}</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">

<pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">sqlite_to_csv</span>(sqlite_file, csv_file):
    <span style="color: #DD4422">"""</span>
 <span style="color: #DD4422">Writes contents of an SQLite smilite database to a CSV file.</span>

 <span style="color: #DD4422">Keyword arguments:</span>
 <span style="color: #DD4422">sqlite_file (str): Path to an existing SQLite database file</span>
 <span style="color: #DD4422">csv_file (str): Path to the output CSV file</span>

 <span style="color: #DD4422">Example output CSV file contents:</span>

 <span style="color: #DD4422">ZINC_ID,SMILE,SIMPLE_SMILE</span>
 <span style="color: #DD4422">ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O</span>
 <span style="color: #DD4422">ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O</span>
 <span style="color: #DD4422">...</span>

 <span style="color: #DD4422">"""</span>
</pre>

</div>

An example output CSV file from an SQLite smilite database is shown in the image below. ![https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_1.png](https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_1.png)

<a name="contact"></a>

# Contact

If you have any questions or comments about smilite, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)

<a name="changelog"></a>

# Changelog

**VERSION 2.1.0**

*   Functions and scripts to fetch ZINC IDs corresponding to a SMILE string query

**VERSION 2.0.1**

*   Progress bar for add_to_sqlite.py

**VERSION 2.0.0**

*   added SQLite features

**VERSION 1.3.0**

*   added script and module function to compare SMILE strings across 2 files.

**VERSION 1.2.0**

*   added Python 2.x support

**VERSION 1.1.1**

*   PyPrind dependency fix

**VERSION 1.1.0**

*   added a progress bar (PyPrind) to `generate_zincid_smile_csv()` function