## Apriori Algorithm

Yagnesh L Pazhaniyappan, 114117098

### Task

To implement the Apriori algorithm and use it to mine category sets that are frequent in the input data. The minimum support to be used on 0.01

### Input

A dataset(“categories.txt”) that consists of the category lists of 77,185 places in the US. Each line corresponds to the category list of one place, where the list consists of a number of category instances (e.g., hotels, restaurants, etc.) that are separated by semicolons.

### Output

Two files named Pattern.txt in the folder /results, one having length 1 frequent categories and the other having all frequent category sets. 


### Running the Program

This Python program is written for the version 3.8 . Make sure you have atleast python 3.7 installed. 
No external libraries are necessary, this is a native implementation. 

__To run the program:__

Clone the repo

```bash 
git clone [git@github.com:yagneshlp/bdaAssignment2.git]
 cd bdaAssignemnt2
 python3 code.py
```

Wait for the program to finish executing. 
```bash
cd results
ls
```
You can find two folders with solutions to 2 sub parts of the task. 

_To view results for first part_
```bash
cd "part_A - L1 Frequent Categories"
nano patterns.txt
```
_To view results for second part_
```bash
cd "part_B - All Frequent Categories"
nano patterns.txt
```
