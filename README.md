<p>Copyright 2014 Sebastian Raschka <br><br></p>

<h1>smilite</h1>

<p>smilite is a Python module to download and analyze SMILE strings (Simplified Molecular-Input Line-entry System) of chemical compounds from ZINC (a free database of commercially-available compounds for virtual screening, <a href="http://zinc.docking.org">http://zinc.docking.org</a>).  <br/>
Now supports both Python 3.x and Python 2.x.</p>
<br><br>
<img src="https://raw.github.com/rasbt/smilite/master/images/smilite_overview.png" alt="" /><br/>
<br><br>

<h4>Sections</h4>

<p>&#8226; <a href="#installation">Installation</a><br>
&#8226; <a href="#simple_cmd_scripts">Simple command line online query scripts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#lookup_zincid">lookup_zincid.py</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#lookup_smile_str">lookup_smile_str.py</a><br>
&#8226; <a href="#csv_scripts">CSV file command line scripts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#gen_zincid">gen_zincid_smile_csv.py (downloading SMILES)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#comp_smile">comp_smile_strings.py (checking for duplicates within 1 file)</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#comp_2_smile">comp_2_smile_files.py (checking for duplicates across 2 files)</a><br>
&#8226; <a href="#sqlite_scripts">SQLite file command line scripts</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#lookup1id">lookup_single_id.py</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#lookupsmile">lookup_smile.py</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#add_to_sqlite">add_to_sqlite.py</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#sqlite_to_csv">sqlite_to_csv.py</a><br>
&#8226; <a href="#documentation">Documentation</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#general_func">General functions</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#csvfile_func">CSV file functions</a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#45; <a href="#sqlite_func">SQLite functions</a><br></p>

<p>&#8226; <a href="#contact">Contact</a><br>
&#8226; <a href="#changelog">Changelog</a><br></p>

<p><br>
<br></p>

<p><a name="installation"></a></p>


<h1>Installation</h1>

<p>You can use the following command to install smilite:<br/>
<code>pip install smilite</code><br/>
 or  <br/>
<code>easy_install smilite</code></p>

<p>Alternatively, you download the package manually from the Python Package Index <a href="https://pypi.python.org/pypi/smilite">https://pypi.python.org/pypi/smilite</a>, unzip it, navigate into the package, and use the command:</p>

<p><code>python3 setup.py install</code></p>

<p><br>
<br></p>



<p><a name="simple_cmd_scripts"></a></p>


<h1>Simple command line online query scripts</h1>

<p>If you downloaded the smilite package from <a href="https://pypi.python.org/pypi/smilite">https://pypi.python.org/pypi/smilite</a> or <a href="https://github.com/rasbt/smilite">https://github.com/rasbt/smilite</a>, you can use the command line scripts I provide in the <code>scripts/cmd_line_online_query_scripts</code> dir.</p>

<p><br>
<br></p>

<p><a name="lookup_zincid"></a></p>


<h3>lookup_zincid.py</h3>

<p>Retrieves the SMILE string and simplified SMILE string for a given ZINC ID<br>
from the online ZINC database.
</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_zincid.py ZINC_ID</code>
<br><br></p>

<p><strong>Example (retrieve data from ZINC):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_zincid.py ZINC01234567</code>
<br><br></p>

<p><strong>Output example:</strong></p>

<pre>
ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>

<p>Where<br/>
- 1st row: ZINC ID <br/>
- 2nd row: SMILE string <br/>
- 3rd row: simplified SMILE string</p>

<p><br>
<br></p>


<p><a name="lookup_smile_str"></a></p>


<h3>lookup_smile_str.py</h3>

<p>Retrieves the corresponding ZINC_IDs for a given SMILE string<br>
from the online ZINC database.
</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_smile_str.py SMILE_str</code>
<br><br></p>

<p><strong>Example (retrieve data from ZINC):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_smile_str.py "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"</code>
<br><br></p>

<p><strong>Output example:</strong></p>

<pre>
ZINC01234567
ZINC01234568
ZINC01242053
ZINC01242055</pre>


<p><br>
<br></p>






<p><a name="csv_scripts"></a></p>


<h1>CSV file command line scripts</h1>

<p>If you downloaded the smilite package from <a href="https://pypi.python.org/pypi/smilite">https://pypi.python.org/pypi/smilite</a> or <a href="https://github.com/rasbt/smilite">https://github.com/rasbt/smilite</a>, you can use the command line scripts I provide in the <code>scripts/csv_scripts</code> dir.</p>

<p><br>
<br></p>

<p><a name="gen_zincid"></a></p>


<h3>gen_zincid_smile_csv.py (downloading SMILES)</h3>

<p>Generates a ZINC_ID,SMILE_STR csv file from a input file of
ZINC IDs. The input file should consist of 1 columns with 1 ZINC ID per row.</p>

<p><strong>Usage:</strong>  <br/>
<code>[shell]&gt;&gt; python3 gen_zincid_smile_csv.py in.csv out.csv</code></p>

<p><strong>Example:</strong>  <br/>
<code>[shell]&gt;&gt; python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv</code></p>

<p><strong>Screen Output:</strong></p>

<pre>
Downloading SMILES
0%                          100%
[##########                    ] | ETA[sec]: 106.525 </pre>


<p><br>
<strong>Input example file format:</strong> <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/zinc_ids.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/zinc_ids.csv">zinc_ids.csv</a></p>

<p><br></p>

<p><strong>Output example file format:</strong> <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv">zid_smiles.csv</a></p>

<p><br>
<br></p>

<p><a name="comp_smile"></a></p>


<h3>comp_smile_strings.py (checking for duplicates within 1 file)</h3>

<p>Compares SMILE strings within a 2 column CSV file (ZINC_ID,SMILE_string) to identify duplicates. Generates a new CSV file with ZINC IDs of identified
duplicates listed in a 3rd-nth column(s).</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 comp_smile_strings.py in.csv out.csv [simplify]</code></p>

<p><strong>Example 1:</strong><br/>
<code>[shell]&gt;&gt; python3 gen_zincid_smile_csv.py ../examples/zinc_ids.csv ../examples/zid_smiles.csv</code></p>

<p><br></p>

<p><strong>Input example file format:</strong> <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/zid_smiles.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/zid_smiles.csv">zid_smiles.csv</a></p>

<p><br></p>

<p><strong>Output example file format 1:</strong>  <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/comp_smiles.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/comp_smiles.csv">comp_smiles.csv</a></p>

<p><br></p>

<p>Where<br/>
- 1st column: ZINC ID<br/>
- 2nd column: SMILE string<br/>
- 3rd column: number of duplicates<br/>
- 4th-nth column: ZINC IDs of duplicates</p>

<p><br></p>

<p><strong>Example 2:</strong><br/>
<code>[shell]&gt;&gt; python3 comp_smile_strings.py ../examples/zid_smiles.csv ../examples/comp_simple_smiles.csv simplify</code></p>

<p><br></p>

<p><strong>Output example file format 2:</strong>
<img src="https://raw.github.com/rasbt/smilite/master/images/comp_simple_smiles.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/comp_simple_smiles.csv">comp_simple_smiles.csv</a></p>

<p><br>
<br></p>

<p><a name="comp_2_smile"></a></p>


<h3>comp_2_smile_files.py (checking for duplicates across 2 files)</h3>

<p>Compares SMILE strings between 2 input CSV files, where each file consists of rows with 2 columns ZINC_ID,SMILE_string to identify duplicate SMILE string across both files.<br/>
Generates a new CSV file with ZINC IDs of identified duplicates listed in a 3rd-nth column(s).</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 comp_2_smile_files.py in1.csv in2.csv out.csv [simplify]</code></p>

<p><strong>Example:</strong><br/>
<code>[shell]&gt;&gt; python3 comp_2_smile_files.py ../examples/zid_smiles2.csv ../examples/zid_smiles3.csv ../examples/comp_2_files.csv</code></p>

<p><br></p>

<p><strong>Input example file 1:</strong> <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/zid_smiles2.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/zid_smiles2.csv">zid_smiles2.csv</a></p>

<p><br></p>

<p><strong>Input example file 2:</strong> <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/zid_smiles3.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/zid_smiles3.csv">zid_smiles3.csv</a></p>

<p><br></p>

<p><strong>Output example file format:</strong>  <br/>
<img src="https://raw.github.com/rasbt/smilite/master/images/comp_2_files.png" alt="" /><br/>
<a href="https://raw.github.com/rasbt/smilite/master/examples/comp_2_files.csv">comp_2_files.csv</a></p>

<p><br></p>

<p>Where:<br/>
     - 1st column: name of the origin file<br/>
     - 2nd column: ZINC ID<br/>
     - 3rd column: SMILE string<br/>
     - 4th-nth column: ZINC IDs of duplicates</p>

<p><br>
<br></p>

<p><a name="sqlite_scripts"></a></p>


<h1>SQLite file command line scripts</h1>

<p>If you downloaded the smilite package from <a href="https://pypi.python.org/pypi/smilite">https://pypi.python.org/pypi/smilite</a> or <a href="https://github.com/rasbt/smilite">https://github.com/rasbt/smilite</a>, you can use the command line scripts I provide in the <code>scripts/sqlite_scripts</code> dir.</p>

<p><br>
<br></p>

<p><a name="lookup1id"></a></p>


<h3>lookup_single_id.py</h3>

<p>Retrieves the SMILE string and simplified SMILE string for a given ZINC ID<br/>
from a previously built smilite SQLite database or from the online ZINC database.</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_single_id.py ZINC_ID [sqlite_file]</code>
<br><br></p>

<p><strong>Example1 (retrieve data from a smilite SQLite database):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_single_id.py ZINC01234567 ~/Desktop/smilite_db.sqlite</code>
<br><br></p>

<p><strong>Example2 (retrieve data from the ZINC online database):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_single_id.py ZINC01234567</code>
<br><br></p>

<p><strong>Output example:</strong></p>

<pre>
ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>


<p>Where<br/>
- 1st row: ZINC ID <br/>
- 2nd row: SMILE string <br/>
- 3rd row: simplified SMILE string</p>

<p><br>
<br></p>

<p><a name="lookupsmile"></a></p>


<h3>lookup_smile.py</h3>

<p>Retrieves the ZINC ID(s) for a given SMILE sting or simplified SMILE string
from a previously built smilite SQLite database.</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_smile.py sqlite_file SMILE_STRING [simplify]</code>
<br><br></p>

<p><strong>Example1 (search for SMILE string):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_smile.py ~/Desktop/smilite.sqlite "C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O"</code>
<br><br></p>

<p><strong>Example2 (search for simplified SMILE string):</strong><br/>
<code>[shell]&gt;&gt; python3 lookup_smile.py ~/Desktop/smilite.sqlite "CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O" simple</code>
<br><br></p>

<p><strong>Output example:</strong></p>

<pre>
ZINC01234567
C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>


<p>Where<br/>
- 1st row: ZINC ID <br/>
- 2nd row: SMILE string <br/>
- 3rd row: simplified SMILE string</p>

<p><br>
<br></p>

<p><a name="add_to_sqlite"></a></p>


<h3>add_to_sqlite.py</h3>

<p>Reads ZINC IDs from a CSV file and looks up SMILE strings and simplified SMILE strings
from the ZINC online database. Writes those SMILE strings to a smilite SQLite database.
A new database will be created if it doesn't exist, yet.</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 add_to_sqlite.py sqlite_file csv_file</code>
<br><br></p>

<p><strong>Example:</strong><br/>
<code>[shell]&gt;&gt; python3 add_to_sqlite.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_ids.csv</code>
<br><br></p>

<p><strong>Input CSV file example format:</strong></p>

<pre>
ZINC01234567
ZINC01234568
...
</pre>


<p><br><br>
An example of the smilite SQLite database contents after successful insertion is shown in the image below.
<img src="https://raw.github.com/rasbt/smilite/master/images/add_to_sqlite_1.png" alt="https://raw.github.com/rasbt/smilite/master/images/add_to_sqlite_1.png" /></p>

<p><br>
<br></p>

<p><a name="sqlite_to_csv"></a></p>


<h3>sqlite_to_csv.py</h3>

<p>Writes contents of an SQLite smilite database to a CSV file.</p>

<p><strong>Usage:</strong><br/>
<code>[shell]&gt;&gt; python3 sqlite_to_csv.py sqlite_file csv_file</code>
<br><br></p>

<p><strong>Example:</strong><br/>
<code>[shell]&gt;&gt; python3 sqlite_to_csv.py ~/Desktop/smilite.sqlite ~/Desktop/zinc_smiles.csv</code>
<br><br></p>

<p><strong>Input CSV file example format:</strong></p>

<pre>
ZINC_ID,SMILE,SIMPLE_SMILE
ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
</pre>


<p><br><br>
An example of the CSV file contents opened in an spreadsheet program is shown in the image below.
<img src="https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_2.png" alt="https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_2.png" /></p>

<p><br>
<br></p>

<p><a name="documentation"></a></p>


<h1>Documentation</h1>

<p>After you installed the smilite module, you can import it in Python via <code>import smilite</code>.
The current functions include:</p>

<p><br>
<br></p>

<p><a name="general_func"></a></p>


<h3>General functions</h3>

<p><br></p>

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


<p><br></p>

<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">get_zincid_from_smile</span>(smile_str):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Gets the corresponding ZINC ID(s) for a SMILE string query from</span>
<span style="color: #DD4422">    the ZINC online database. Requires an internet connection.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        smile_str (str): A valid SMILE string, e.g. &#39;C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&#39; </span>

<span style="color: #DD4422">    Returns the SMILE string for the corresponding ZINC ID(s) in a list.</span>
<span style="color: #DD4422">        E.g., [&#39;ZINC01234567&#39;, &#39;ZINC01234568&#39;, &#39;ZINC01242053&#39;, &#39;ZINC01242055&#39;]</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>

<p><br></p>


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

<p><br>
<br></p>





<p><a name="csvfile_func"></a></p>


<h3>CSV file functions</h3>

<p><br></p>

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


<p><br></p>

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


<p><br></p>

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">comp_two_csvfiles</span>(zincid_list1, zincid_list2, out_file, compare_simplified_smiles<span style="color: #333333">=</span><span style="color: #007020">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Compares SMILE strings across two ZINC_ID CSV files for duplicates </span>
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


<p><br>
<br></p>

<p><a name="sqlite_func"></a></p>


<h3>SQLite functions</h3>

<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">create_sqlite</span>(sqlite_file):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Creates a new SQLite database file if it doesn&#39;t exist yet.</span>
<span style="color: #DD4422">    The database created will consists of 3 columns: </span>
<span style="color: #DD4422">        1) &#39;zinc_id&#39; (ZINC ID as Primary Key)</span>
<span style="color: #DD4422">        2) &#39;smile&#39; (SMILE string obtained from the ZINC online db)</span>
<span style="color: #DD4422">        3) &#39;simple_smile&#39; (simplified SMILE string, see smilite.simplify_smile())</span>
<span style="color: #DD4422">    </span>
<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to the new SQLite database file.</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">insert_id_sqlite</span>(sqlite_file, zinc_id):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Inserts a new ZINC ID into an existing SQLite database if the ZINC ID</span>
<span style="color: #DD4422">    isn&#39;t contained in the database, yet. Obtains the SMILE string from the</span>
<span style="color: #DD4422">    ZINC online database and adds it to the new ZINC ID database entry together</span>
<span style="color: #DD4422">    with an simplified SMILE string.</span>

<span style="color: #DD4422">    Example database entry:</span>
<span style="color: #DD4422">    zinc_id,smile,simple_smile</span>
<span style="color: #DD4422">    &quot;ZINC01234567&quot;,&quot;C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&quot;,&quot;CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O&quot;</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to an existing SQLite database file</span>
<span style="color: #DD4422">        zinc_id (str): A valid ZINC ID</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br><br>
An example database entry is shown in the image below.
<img src="https://raw.github.com/rasbt/smilite/master/images/insert_id_sqlite_1.png" alt="https://raw.github.com/rasbt/smilite/master/images/insert_id_sqlite_1.png" /></p>

<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lookup_smile_sqlite</span>(sqlite_file, smile_str, simple_smile<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Looks up an ZINC ID for a given SMILE string in an existing </span>
<span style="color: #DD4422">    SQLite database file.    </span>
<span style="color: #DD4422">    </span>
<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to an existing SQLite database file</span>
<span style="color: #DD4422">        smile_str (str): A SMILE string to query the database</span>
<span style="color: #DD4422">        simple_smile (bool): Queries simplified smile strings in the</span>
<span style="color: #DD4422">            database if true</span>
<span style="color: #DD4422">        </span>
<span style="color: #DD4422">    Returns a list with the ZINC ID, SMILE string, and simplified SMILE </span>
<span style="color: #DD4422">        string or an empty list if SMILE string could not be found.</span>
<span style="color: #DD4422">        Example returned list:</span>
<span style="color: #DD4422">        [&#39;ZINC01234567&#39;, &#39;C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&#39;,</span>
<span style="color: #DD4422">         &#39;CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O&#39;]</span>
<span style="color: #DD4422">        If multiple ZINC IDs match the query SMILE string, a list of sublists</span>
<span style="color: #DD4422">        is returned.</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">lookup_smile_sqlite</span>(sqlite_file, smile_str, simple_smile<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">False</span>):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Looks up an ZINC ID for a given SMILE string in an existing </span>
<span style="color: #DD4422">    SQLite database file.    </span>
<span style="color: #DD4422">    </span>
<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to an existing SQLite database file</span>
<span style="color: #DD4422">        smile_str (str): A SMILE string to query the database</span>
<span style="color: #DD4422">        simple_smile (bool): Queries simplified smile strings in the</span>
<span style="color: #DD4422">            database if true</span>
<span style="color: #DD4422">        </span>
<span style="color: #DD4422">    Returns a list with the ZINC ID, SMILE string, and simplified SMILE </span>
<span style="color: #DD4422">        string or an empty list if SMILE string could not be found.</span>
<span style="color: #DD4422">        Example returned list:</span>
<span style="color: #DD4422">        [&#39;ZINC01234567&#39;, &#39;C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&#39;,</span>
<span style="color: #DD4422">         &#39;CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O&#39;]</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">sqlite_to_dict</span>(sqlite_file):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Returns contents of an SQLite smilite database as Python dictionary object.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to an existing SQLite database file</span>

<span style="color: #DD4422">    Returns an SQLite smilite database as Python dictionary object with</span>
<span style="color: #DD4422">        ZINC IDs as keys and corresponding </span>
<span style="color: #DD4422">        [SMILE_string, Simple_SMILE_string] lists as values.</span>

<span style="color: #DD4422">    Example returned dictionary:</span>
<span style="color: #DD4422">    {</span>
<span style="color: #DD4422">        &#39;ZINC01234568&#39;: [&#39;C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&#39;, </span>
<span style="color: #DD4422">                        &#39;CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O&#39;], </span>
<span style="color: #DD4422">        &#39;ZINC01234567&#39;: [&#39;C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O&#39;, </span>
<span style="color: #DD4422">                        &#39;CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O&#39;]</span>
<span style="color: #DD4422">    }</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br></p>

<!-- HTML generated using hilite.me -->


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">sqlite_to_csv</span>(sqlite_file, csv_file):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Writes contents of an SQLite smilite database to a CSV file.</span>

<span style="color: #DD4422">    Keyword arguments:</span>
<span style="color: #DD4422">        sqlite_file (str): Path to an existing SQLite database file</span>
<span style="color: #DD4422">        csv_file (str): Path to the output CSV file</span>

<span style="color: #DD4422">    Example output CSV file contents:</span>

<span style="color: #DD4422">    ZINC_ID,SMILE,SIMPLE_SMILE</span>
<span style="color: #DD4422">    ZINC01234567,C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O</span>
<span style="color: #DD4422">    ZINC01234568,C[C@@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O,CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O</span>
<span style="color: #DD4422">    ...</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<p><br><br>
An example output CSV file from an SQLite smilite database is shown in the image below.
<img src="https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_1.png" alt="https://raw.github.com/rasbt/smilite/master/images/sqlite_to_csv_1.png" /></p>

<p><br>
<br></p>

<p><a name="contact"></a></p>


<h1> Contact</h1>

<p>If you have any questions or comments about smilite, please feel free to contact me via<br/>
eMail: <a href="mailto:se.raschka@gmail.com">se.raschka@gmail.com</a><br/>
or Twitter: <a href="https://twitter.com/rasbt">@rasbt</a></p>

<p><br>
<br></p>

<p><a name="changelog"></a></p>


<h1>Changelog</h1>

<p><strong>VERSION 2.1.0</strong></p>

<ul>
<li>Functions and scripts to fetch ZINC IDs corresponding to a SMILE string query</li>
</ul>

<p><strong>VERSION 2.0.1</strong></p>

<ul>
<li>Progress bar for add_to_sqlite.py</li>
</ul>

<p><strong>VERSION 2.0.0</strong></p>

<ul>
<li>added SQLite features</li>
</ul>


<p><strong>VERSION 1.3.0</strong></p>

<ul>
<li>added script and module function to compare SMILE strings across 2 files.</li>
</ul>


<p><strong>VERSION 1.2.0</strong></p>

<ul>
<li>added Python 2.x support</li>
</ul>


<p><strong>VERSION 1.1.1</strong></p>

<ul>
<li>PyPrind dependency fix</li>
</ul>


<p><strong>VERSION 1.1.0</strong></p>

<ul>
<li>added a progress bar (PyPrind) to <code>generate_zincid_smile_csv()</code> function</li>
</ul>
