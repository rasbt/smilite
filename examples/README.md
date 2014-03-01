## Example Files

#### zinc_ids.csv
CSV file consisting of one column with 1 ZINC ID per row.  
Used as input for `smilite.generate_zincid_smile_csv()` to download SMILE strings  
from the ZINC online database ([http://zinc.docking.org](http://zinc.docking.org)) and generates a 2-column CSV file with  
ZINC_ID,SMILE_str pairs.  
This function is implemented in the command line script: [../scripts/gen_zincid_smiles.py](../scripts/gen_zincid_smiles.py).

#### zid_smiles.csv
A 2-column CSV file with ZINC_ID,SMILE_str pairs that is generated when the function `smilite.generate_zincid_smile_csv()` is invoked or via the command line script: [../scripts/gen_zincid_smiles.py](../scripts/gen_zincid_smiles.py).

This CSV file can be used as input CSV file to check for SMILE string duplicates via the `smilite.check_duplicate_smiles()` function or the command line script [../scripts/comp_smile_strings.py](../scripts/comp_smile_strings.py).

#### comp_smiles.csv
A multi-column CSV file where  
- 1st column: ZINC ID  
- 2nd column: SMILE string  
- 3rd column: number of duplicates  
- 4th-nth column: ZINC IDs of duplicates  

This CSV file is the output of invoking the `smilite.check_duplicate_smiles()` function  
or the command line script [../scripts/comp_smile_strings.py](../scripts/comp_smile_strings.py).


#### comp_simple_smiles.csv

A multi-column CSV file where  
- 1st column: ZINC ID  
- 2nd column: simplified SMILE string  
- 3rd column: number of duplicates  
- 4th-nth column: ZINC IDs of duplicates  

This CSV file is the output of invoking the `smilite.check_duplicate_smiles()` function with the additional argument `compare_simplified_smiles=True`  
or the command line script [../scripts/comp_smile_strings.py](../scripts/comp_smile_strings.py) with the provided command line argument `simplify`.
