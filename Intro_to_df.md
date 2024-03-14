# Introduction #
It can often times be useful to get data and put it into a dataframe for further analysis. Here, we practice generating some basic data and then converting that output into a dataframe. To generate the data, we'll be parsing a fasta file via the `Bio` package and then doing the data wrangling and analysis with the `numpy` and `pandas` packages. Make sure these three packages are already been installed. 

The goal here will be to get some basic stats of a fasta file. We will first use an example fasta file and get info on the length of each sequence and then counts of each base. 

# Getting the data #
This can be done with any fasta file composed of genomic sequence data, although it may be most useful to use a genome assembly. First we will use the `Bio` python package to parse the fasta file and then get the length of each sequence 

``` python
from Bio import SeqIO
import pandas as pd 
import numpy as np

lst_seq_leng=[]
for seq_record in SeqIO.parse("example", "fasta"):
	hold=len(seq_record)
	lst_seq_leng.append(hold)
```
The above code block loops through the fasta file and then gets the length of each sequence. A slightly different approach will be required to get the number of A,T,C, and Gs in each of the sequences. Basically need to treat the sequence as a string and simply use the count function. 

``` python
lst_A=[]	
for seq_record in SeqIO.parse("example", "fasta"):
	hold=seq_record.seq.count("A")
	lst_A.append(tot_A)
```
