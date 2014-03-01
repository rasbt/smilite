Copyright 2014 Sebastian Raschka <br><br>

smilite
=======

smilite is a Python 3 module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System) of chemical compounds from ZINC (a free database of commercially-available compounds for virtual screening, [http://zinc.docking.org](http://zinc.docking.org))

####Sections
<p><a href="#installation">Installation</a><br>
<p><a href="#documentation">Documentation</a><br>
<p><a href="#examples">Command Line Scripts Examples</a><br>
<p><a href="#contact">Contact</a><br>
<p><a href="#changelog">Changelog</a><br>


<br>
<br>


<p><a name="installation"></a></p>

Installation
=============
You can use the following command to install PyPrind:  
`pip install smilite`  
 or    
`easy_install smilite`  

Alternatively, you download the package manually from the Python Package Index [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite), unzip it, navigate into the package, and use the command:

`python3 setup.py install`  

<br>
<br>

<p><a name="documentation"></a></p>

Documentation
=============

After you installed the smilite module, you can import it in Python via `import smilite`. 
The current functions include:

<pre>def get_zinc_smile(zinc_id):
    Gets the corresponding SMILE string for a ZINC ID query from
    the ZINC online database. Requires an internet connection.
    Keyword arguments:
        zinc_id (str): A valid ZINC ID, e.g. 'ZINC00029323'
    Returns the SMILE string for the corresponding ZINC ID.
        E.g., 'COc1cccc(c1)NC(=O)c2cccnc2'</pre>
        
<pre>def generate_zincid_smile_csv(zincid_list, out_file):
   Generates a CSV file of ZINC_ID,SMILE_string entries by querying the ZINC online
   database.
   Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file 
             that contains 1 ZINC_ID per row. E.g., 
             ZINC0000123456
             ZINC0000234567
             [...]
        out_file (str): Path to a new output CSV file that will be written.</pre>

<pre>def check_duplicate_smiles(zincid_list, out_file, compare_simplified_smiles=False):
   Scans a ZINC_ID,SMILE_string CSV file for duplicate SMILE strings.
   Keyword arguments:
        zincid_list (str): Path to a UTF-8 or ASCII formatted file that 
               contains 1 ZINC_ID per row.
               E.g., 
               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC
               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
               [...]
        out_file (str): Path to a new output CSV file that will be written.
        compare_simplified_smiles (bool): If true, SMILE strings will be simplified
               for the comparison.</pre>
               
<pre>def simplify_smile(smile_str):
        Simplifies a SMILE string by removing hydrogen atoms (H), 
        chiral specifications ('@'), charges (+ / -), '#'-characters,
        and square brackets ('[', ']').
    Keyword Arguments:
        smile_str (str): A smile string, e.g., C[C@H](CCC(=O)NCCS(=O)(=O)[O-])
    Returns a simplified SMILE string, e.g., CC(CCC(=O)NCCS(=O)(=O)O)</pre>


<br>
<br>

<p><a name="examples"></a></p>

Command Line Scripts Examples
=============

If you downloaded the smilite package from [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite) or [https://github.com/rasbt/smilite](https://github.com/rasbt/smilite), you can use the command line scripts I provide in the `scripts/` dir.


<br>
<br>

###gen_zincid_smile_csv.py

Generates a ZINC_ID,SMILE_STR csv file from a input file of
ZINC IDs. The input file should consist of 1 columns with 1 ZINC ID per row.

**Usage:**    
`[shell]>> python3 gen_zincid_smile_csv.py in.csv out.csv`

**Example:**    
`[shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv`


**Input example file format:**   
![](https://github.com/rasbt/smilite/blob/master/images/zinc_ids.png)  
(zinc_ids.csv)

**Output example file format:**   
![](https://github.com/rasbt/smilite/blob/master/images/zid_smiles.png)  
(zid_smiles.csv)

<br>
<br>

###comp_smile_strings.py

Compares SMILE strings in a 2 column CSV file (ZINC_ID,SMILE_string) to identify duplicates. Generates a new CSV file with ZINC IDs of identified
duplicates listed in a 3rd-nth column(s).

**Usage:**  
`[shell]>> python3 comp_smile_strings.py in.csv out.csv [simplify]`

**Example 1:**  
`[shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv`



**Input example file format:**   
![](https://github.com/rasbt/smilite/blob/master/images/zid_smiles.png)  
(zid_smiles.csv)



**Output example file format 1:**    
![](https://github.com/rasbt/smilite/blob/master/images/comp_smiles.png)  
(comp_smiles.csv)


Where  
- 1st column: ZINC ID  
- 2nd column: SMILE string  
- 3rd column: number of duplicates  
- 4th-nth column: ZINC IDs of duplicates  

**Example 2:**  
`[shell]>> python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify`  

**Output example file format 2:**
![](https://github.com/rasbt/smilite/blob/master/images/comp_simple_smiles.png)  
(comp_simple_smiles.csv)

<br>
<br>

<p><a name="contact"></a></p>

 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)


<br>
<br>

<p><a name="changelog"></a></p>

Changelog
==========



