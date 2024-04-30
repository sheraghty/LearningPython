# Introduction #
It can useful to create scripts with general functions that can be easily run using external data (e.g. data not directly called in the script). There are several ways of doing this that range from using methods similar to positional and keyword type arguments. 

## Using positional type input ##
The easiest way to create scripts that take arguments is to use the `sys` module. Input is essentially used in the same way as a positional argument is used when defining a function. This sort of approach is not as user friendly as the approach discussed below. This is because one must look at the script to understand what the required inputs are so the user needs some level of expertise. 

For example, we can create a script that takes a fasta file as an input and then gets the length of each sequence. Note this also uses the `Bio` module. The below script will be saved as example.py
``` python
import sys
inFile = sys.argv[1]

lst_seq_len=[]
for seq_record in seqIO.parse(inFile, "fasta"):
  hold=len(seq_record)
  lst_seq_len.append.hold

print(lst_seq_len)
```
Then to run the script you would simply use the following code
``` bash
chmod 755 example.py #Gives permission for the file to run
./example.py example.fasta
./example.py example.fasta > out.txt #If you want to save the output in a given file 
```

## Using defined input ##
In this example, we'll be creating arguments for the script to take. This approach allows for the script to be very user friendly as the arguments can be give intuitive names and the given describtions and help messages. 
