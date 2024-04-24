# Working with loops #

There are several different sort of loops that are useful in python. Generally loops are useful for when we want to iterative a command or series of commands over some seriesof data. Below shows examples of the different loops that can be used and the various ways these loops can be manipulated. 

## For loops ##
The for loop is used to iterate a over a given set of data. A simple example might be printing a series of numbers in order. 
``` python
n=10
for i in range(0,n):
  print(i)
``` 

It is also possible it iterate over a more complex ranges using things like lists for dictionaries in python
``` python
L=["bigfoot","mothman","aliens","yeti"] #make a list
for i in L:
  print(i)

#It is also possible to use the index of the list to iterate over either the entire list or a subset
for index in range(len(L)):
    print(L[index])

for index in range(0,2):
    print(L[index])

D=dict() #create an empty dictionary
D["NYK"]="New York Knicks"
D["NYJ"]="New York Jets"
D["NYM"]="New York Mets"

for i in D:
  print("%s:%s" % (i,D[i]))
```

## While loops ##
While loops are useful to doing some action while some condition is met. However care needs to be taken to make sure one does not create an infinite loop, where the condition is always true. If you do create an infinite loop by mistake, then you need to force quite. 

``` python
count = 0
while (count < 3):
    count = count + 1
    print(count)
else:
    print("done")
```

## Nested loops ##
It is possible to combine loops in a nested fashion (e.g. one loop contains the other). This can be useful when iteratiting over several sets of variables simultaneously.

``` python
for i in range(0,n):
  for f in range (0,n):
    print("%d-%d" % (i,f))
```

## Loop control ##

## Other considerations ##
One important note is when setting the range for loops the second number in a set range is not included. For instance in the first example, the loop only printed out numbers 0-9 despite the fact the value of n was 10. There are two soultions to this. One you can remeber this programming quirk and intentionally use it while programming. Alternatively, you can write loops in a way that is inclusive of the entire range. See below for some examples

One can simply add plus 1 to the end of the range to make it "inclusive
``` python
for i in range(0,n+1):
  print(i)
```

One can write the loop to be all items in some list,dictionary,string,etc
``` python
L=["bigfoot","mothman","aliens","yeti"] #make a list
for i in L:
  print(i)
```
