# Packages in python
There are a variety of packages that users can load in python to get additional functionality. Installing packages can be done in several ways based on personal peference. The easiest way to install and manage packages is to use `pip`. Conda is another popular method and offers added functionality with version control and creating different environments. See the [conda documentation](https://conda.io/activation) for further details on how to use conda for maximum effect.

## Loading Packages in python
Loading packages in python is fairly easy. After installing the necessary package(s) you can simply load them using the `import` command. See below for an example of how to load in the biopython package

``` Python
import Bio
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

