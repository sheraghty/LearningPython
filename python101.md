# Packages in python
There are a variety of packages that users can load in python to get additional functionality. Installing packages can be done in several ways based on personal peference. The easiest way to install and manage packages is to use `pip`. Conda is another popular method and offers added functionality with version control and creating different environments. See the [conda documentation](https://conda.io/activation) for further details on how to use conda for maximum effect.

## Loading Packages in python
Loading packages in python is fairly easy. After installing the necessary package(s) you can simply load them using the `import` command. See below for an example of how to load in the biopython package

``` Python
import Bio
```

To see what version of any loaded packages, you can use the the following. Alternatively, they 

``` Python
print(__Bio.version__)
```

# Defining and using variables
Variables can be very useful in python and defining them is quite easy. Essentially, all you need to do is some variation of NAME = VALUE. The value you set for a variable can either be something you directly define (e.g. a particular number) or the result of a function. See below for some examples.

``` Python
test_numb = 4
test_seq = 'ATTACG'
test_seq_len = len(test_seq)
test_meth = 100*16
```

To see what a variable is defined as, you can use the `print` function as shown below 

``` Python
test_seq = 'ATTACG'
print(test_seq)
```

Another consideration when using variables is the variable type. Variables can either be strings (text), integers (whole numbers) or float (numbers with decimals). When defining strings you must put your desired value between a set of either double of single quotation marks. The advantage of double quotation marks is that it enables you to have strings that contain apostrophes (e.g. "Charles' shirt"). Neither integer or float variables require any special formatting. One can easily convert between variable types using a handful of functions as seen below. 

```python
test_numb = 4.1
int(test_numb) #note that the int function just chops of the decimal and does not round
str(test_numb)
```
It is also important to know what type of variable you're using because it can can how certain fucntions. For instance, doing mathematical opterations between strings and integers can result in vastly different outputs. For instance, adding two strings is the same as pasting them together, where as mathematical operations work as intended when using integers or float. See below for some examples 
```python
prefix1="super"
prefix2="para"
word1="natural"
word2="normal"
prefix1 + word1
prefix2 + word2
```
# Working with strings 
## Formatting
There are a number of built in functions associated with strings that are useful for quick formatting and basic analysis. Things like DNA, RNA, or protein sequences can be read in as string as seen in the examples above (although there are dedicated packages for this). Occassionally these sequences might not be all in the same case, which can create some problems. String characters can be converted to all caps or all lower case using the `upper()` and `lower()` functions respectively. Another common issue with strings is any spaces or special characters that might need to be removed. This can be easily accomplished using the `replace()` function. You can also chain multiple functions together, if you need to do something like replace a character and have all characters be in uppercase. Note none of these functions overwrite the original string variable, you need to manually set the output of the function to overwrite the original variable (or save to a new variable). See below for examples of formatting strings using these commands 

```python
test_seq="AtcatGGc G"
test_seq.upper()
test_seq.lower()
test_seq.replace(" ","") #This removes the space
test_seq.replace(" "."").upper() #removes space and then make all upper case
tes_seq = test_seq.replace(" "."").upper() #overwrites the original string with the output of the function
```
## Basic analysis 
Its relatively straightforward to do some basic analyses with strings, which might be of interest to biologists. For instance, getting the length of a sequence with the `len()` function or identifying the number of instances of a certain base or genomic motifif using the `count()` function. See below for some examples of how to do this

```python
seq_len = "ATCGCATGATCGAACG"
len(seq_len)
seq_len.count("CG") #count  every instance of CG in the sequence
```

We can make this slightly more complex and combine these two functions to get things like %GC for a sequence, which is something we might want to know for a sequence. 
```python
seq_len = "ATCGCATGATCGAACG"
(seq_len.count("C")+seq_len.count("G"))/len(seq_len) #Note to make this a % you would also need to multiple by 100
```

