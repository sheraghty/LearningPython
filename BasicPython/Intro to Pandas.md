# Overview #
Pandas is a commonly used python library for structuring data. This tutorial will go over the basics of the different data structures in python as well as some of the basic ways these data structures can be manipulated. Note for all of the code examples below, we will have the pandas library loaded as seen in the code block below. 
```python
import pandas as pd
```

# Data Structures #
## Series ##
A series is a one dimensional array with an associated array of labels. Thinking of this in terms of a spreadsheet or something along those lines, a series is basically one column with row labels. The easiest way to create a series is to use the `Series` funtion as below

```python
ser1 = pd.Series([19,40,99,201])
ser1
ser2 = pd.Series([19,40,99,201], index=['a','b','c','d']) # if we want to specify the index 
ser2
#We can also convert a dictionary into a series as below
dict_obj = {'Liberty': 32, 'Jets': 5, 'Mets': 90, 'Knicks': 52}
ser3 = pd.Series(dict_obj)
ser3
#Finally we can change the index of a series
ser2.index = ['e','f','g','h']
ser2
```

We can maniuplate a series in a number to either select specific values, apply logic, or apply math functions. See below for examples

```python
ser3['Liberty'] #only print a particular value based on the index
ser1[ser1 > 50] #filter series to only print values that are true
ser1 * 5 #Note the index values (rownames) stay the same
```
There are some other features of Series as well, but this will get us going for now.
## Dataframe ##
A dataframe in pandas is essentially the same as in `r` and both are basically spreadsheets where you have column and row names. Like spreadsheets or r dataframes, a pandas dataframe can accomodate columns or various data types (e.g. one column can be a string and other can be an integer). We can also create a dataframe from the command line or by reading in data frome an external source
```python
#First lets make a dataframe "by hand"
#Make a dataframe showing the name, place and nationality for the first 4 finishers in the mens 1500 final at the 2024 Olympic Games
data = {'Athlete': ['Kerr','Nguse','Jacob','Hocker'],
'Place': [2,3,4,1],
'Nationality': ['UK','USA','NOR','USA']}
df1 = pd.DataFrame(data)
```
Note: like with a series, we can modiy the index names.

Reading in data from an external source can be a little tricky depending on both the source of the data and the format that it is saved in. However, it is fairly easy if you have a csv file that is already present in your working directory. We'll practice reading in the EXAMPLE file, which shows the final standings of the 2024 WNBA season. 
