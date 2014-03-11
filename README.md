Copyright 2014 Sebastian Raschka <br><br>

smilite
=======

smilite is a Python module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System) of chemical compounds from ZINC (a free database of commercially-available compounds for virtual screening, [http://zinc.docking.org](http://zinc.docking.org)).    
Now supports both Python 3.x and Python 2.x.

####Sections
&#8226; <a href="#installation">Installation</a><br>
&#8226; <a href="#documentation">Documentation</a><br>
&#8226; <a href="#examples">Command Line Scripts Examples</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#gen_zincid">gen_zincid_smile_csv.py (downloading SMILES)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#comp_smile">comp_smile_strings.py (checking for duplicates within 1 file)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#comp_2_smile">comp_2_smile_files.py (checking for duplicates across 2 files)</a><br>
&#8226; <a href="#contact">Contact</a><br>
&#8226; <a href="#changelog">Changelog</a><br>


<br>
<br>


<p><a name="installation"></a></p>

Installation
=============
You can use the following command to install smilite:  
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

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_zinc_smile</span>(zinc_id):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Gets the corresponding SMILE string for a ZINC ID query from</span>
<span style="color: #DD4422">    the ZINC online database. Requires an internet connection.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        zinc_id (str): A valid ZINC ID, e.g. &#39;ZINC00029323&#39;</span>

<span style="color: #DD4422">    Returns the SMILE string for the corresponding ZINC ID.</span>
<span style="color: #DD4422">        E.g., &#39;COc1cccc(c1)NC(=O)c2cccnc2&#39;</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">simplify_smile</span>(smile_str):
    <span style="color: #DD4422">&quot;&quot;&quot; </span>
<span style="color: #DD4422">    Simplifies a SMILE string by removing hydrogen atoms (H), </span>
<span style="color: #DD4422">    chiral specifications (&#39;@&#39;), charges (+ / -), &#39;#&#39;-characters,</span>
<span style="color: #DD4422">    and square brackets (&#39;[&#39;, &#39;]&#39;).</span>

<span style="color: #DD4422">    Keyword Arguments:</span>
<span style="color: #DD4422">        smile_str (str): A smile string, e.g., C[C@H](CCC(=O)NCCS(=O)(=O)[O-])</span>
<span style="color: #DD4422">    </span>
<span style="color: #DD4422">    Returns a simplified SMILE string, e.g., CC(CCC(=O)NCCS(=O)(=O)O)</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


        
<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">generate_zincid_smile_csv</span>(zincid_list, out_file, print_progress_bar<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Generates a CSV file of ZINC_ID,SMILE_string entries by querying the ZINC online</span>
<span style="color: #DD4422">    database.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        zincid_list (str): Path to a UTF-8 or ASCII formatted file </span>
<span style="color: #DD4422">             that contains 1 ZINC_ID per row. E.g., </span>
<span style="color: #DD4422">             ZINC0000123456</span>
<span style="color: #DD4422">             ZINC0000234567</span>
<span style="color: #DD4422">             [...]</span>
<span style="color: #DD4422">        out_file (str): Path to a new output CSV file that will be written.</span>
<span style="color: #DD4422">        print_prgress_bar (bool): Prints a progress bar to the screen if True.</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">check_duplicate_smiles</span>(zincid_list, out_file, compare_simplified_smiles<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Scans a ZINC_ID,SMILE_string CSV file for duplicate SMILE strings.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        zincid_list (str): Path to a UTF-8 or ASCII formatted file that </span>
<span style="color: #DD4422">               contains 1 ZINC_ID + 1 SMILE String per row.</span>
<span style="color: #DD4422">               E.g., </span>
<span style="color: #DD4422">               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC</span>
<span style="color: #DD4422">               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O</span>
<span style="color: #DD4422">               [...]</span>
<span style="color: #DD4422">        out_file (str): Path to a new output CSV file that will be written.</span>
<span style="color: #DD4422">        compare_simplified_smiles (bool): If true, SMILE strings will be simplified</span>
<span style="color: #DD4422">               for the comparison.</span>
<span style="color: #DD4422">       </span>
<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">comp_two_files</span>(zincid_list1, zincid_list2, out_file, compare_simplified_smiles<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Compares SMILE strings across two ZINC_ID files for duplicates </span>
<span style="color: #DD4422">    (does not check for duplicates within each file).</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        zincid_list1 (str): Path to a UTF-8 or ASCII formatted file that </span>
<span style="color: #DD4422">               contains 1 ZINC_ID + 1 SMILE String per row.</span>
<span style="color: #DD4422">               E.g., </span>
<span style="color: #DD4422">               ZINC12345678,Cc1ccc(cc1C)OCCOc2c(cc(cc2I)/C=N/n3cnnc3)OC</span>
<span style="color: #DD4422">               ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O</span>
<span style="color: #DD4422">               [...]</span>
<span style="color: #DD4422">        zincid_list2 (str): Second ZINC_ID list file, similarly </span>
<span style="color: #DD4422">        out_file (str): Path to a new output CSV file that will be written.</span>
<span style="color: #DD4422">        compare_simplified_smiles (bool): If true, SMILE strings will be simplified</span>
<span style="color: #DD4422">               for the comparison.</span>
<span style="color: #DD4422">       </span>
<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>
               


<br>
<br>

<p><a name="examples"></a></p>

Command Line Scripts Examples
=============

If you downloaded the smilite package from [https://pypi.python.org/pypi/smilite](https://pypi.python.org/pypi/smilite) or [https://github.com/rasbt/smilite](https://github.com/rasbt/smilite), you can use the command line scripts I provide in the `scripts/` dir.


<br>
<br>

<p><a name="gen_zincid"></a></p>

###gen_zincid_smile_csv.py (downloading SMILES)

Generates a ZINC_ID,SMILE_STR csv file from a input file of
ZINC IDs. The input file should consist of 1 columns with 1 ZINC ID per row.

**Usage:**    
`[shell]>> python3 gen_zincid_smile_csv.py in.csv out.csv`

**Example:**    
`[shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv`

**Screen Output:**  
<pre>
Downloading SMILES
0%                          100%
[##########                    ] | ETA[sec]: 106.525 </pre>

<br>
**Input example file format:**   
![](https://raw.github.com/rasbt/smilite/master/images/zinc_ids.png)  
[zinc_ids.csv](https://raw.github.com/rasbt/smilite/master/examples/zinc_ids.csv)

<br>

**Output example file format:**   
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png)  
[zid_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv)

<br>
<br>
<p><a name="comp_smile"></a></p>

###comp_smile_strings.py (checking for duplicates within 1 file)

Compares SMILE strings within a 2 column CSV file (ZINC_ID,SMILE_string) to identify duplicates. Generates a new CSV file with ZINC IDs of identified
duplicates listed in a 3rd-nth column(s).

**Usage:**  
`[shell]>> python3 comp_smile_strings.py in.csv out.csv [simplify]`

**Example 1:**  
`[shell]>> python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv`


<br>

**Input example file format:**   
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png)  
[zid_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv)

<br>

**Output example file format 1:**    
![](https://raw.github.com/rasbt/smilite/master/images/comp_smiles.png)  
[comp_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_smiles.csv)

<br>

Where  
- 1st column: ZINC ID  
- 2nd column: SMILE string  
- 3rd column: number of duplicates  
- 4th-nth column: ZINC IDs of duplicates  

<br>

**Example 2:**  
`[shell]>> python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify`  

<br>

**Output example file format 2:**
![](https://raw.github.com/rasbt/smilite/master/images/comp_simple_smiles.png)  
[comp_simple_smiles.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_simple_smiles.csv)

<br>
<br>
<p><a name="comp_2_smile"></a></p>

###comp_2_smile_files.py (checking for duplicates across 2 files)

Compares SMILE strings between 2 input CSV files, where each file consists of rows with 2 columns ZINC_ID,SMILE_string to identify duplicate SMILE string across both files.  
Generates a new CSV file with ZINC IDs of identified duplicates listed in a 3rd-nth column(s).


**Usage:**  
`[shell]>> python3 comp_2_smile_files.py in1.csv in2.csv out.csv [simplify]`

**Example:**  
`[shell]>> python3 comp_2_smile_files.py ../examples/zid_smiles2.csv ../examples/zid_smiles3.csv ../examples/comp_2_files.csv`


<br>

**Input example file 1:**   
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles2.png)  
[zid_smiles2.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles2.csv)

<br>

**Input example file 2:**   
![](https://raw.github.com/rasbt/smilite/master/images/zid_smiles3.png)  
[zid_smiles3.csv](https://raw.github.com/rasbt/smilite/master/examples/zid_smiles3.csv)

<br>

**Output example file format:**    
![](https://raw.github.com/rasbt/smilite/master/images/comp_2_files.png)  
[comp_2_files.csv](https://raw.github.com/rasbt/smilite/master/examples/comp_2_files.csv)

<br>

Where:  
     - 1st column: name of the origin file  
     - 2nd column: ZINC ID  
     - 3rd column: SMILE string  
     - 4th-nth column: ZINC IDs of duplicates  








<br>
<br>

<p><a name="contact"></a></p>

 Contact
=============

If you have any questions or comments about smilite, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)


<br>
<br>

<p><a name="changelog"></a></p>

Changelog
==========

**VERSION 1.3.0**

- added script and module function to compare SMILE strings across 2 files.


**VERSION 1.2.0**

- added Python 2.x support


**VERSION 1.1.1**

- PyPrind dependency fix


**VERSION 1.1.0**  

- added a progress bar (PyPrind) to `generate_zincid_smile_csv()` function




