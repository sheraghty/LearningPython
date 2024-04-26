# Functions in Python #

Python has many built in functions and many more can be imported from various modules. However, some situations may require you to develope new functions. Defining functions in python is fairly straight forward 

# Basic functions #

The most basic function is one that does not take any inputs. Here the `def` command means define and lets python know a function is being defined. In this case, there is nothing  between the () because there are no arguments being defined in this fucntion. Since there are no arguments, the same thing will be returned everytime.

``` python
def hello_func():
  print("Hello from a function")

hello_func()
```

# Adding in arguments #
There are 5 types of arguments that can be added to python functions. 

## Default arguments ##
Default arguments are those that you give a default value. Default arguments however can be replaced by user input. 

``` python
def fav_monster(monster="Bigfoot"):
  print(monster)
```
Running the above command without an user input arguments (e.g. running it as `fav_monster()`) then the function will return the default value, which in this case is Bigfoot. However, if there is input provided then the function will return that new value instead. 
``` python
fav_monster("vampire")
```

## Positional and Keyword arguments ##

Positional arguments are those where the input order matters if a function requires multiple arguments. For example if there are three arguments a, b, and c then the user must have inputs match this order. See below for an example. 
``` python
def Monster_ranking(a,b,c):
  print("My first favorite monster is the", a)
  print("My second favorite monster is the", b)
  print("My third favorite monster is the", c)

Monster_ranking("Bigfoot","Mothman","Yeti")
Monster_ranking("Mothman","Yeti","Bigfoot") #Now the order is different 
```

Alternatively the order of keyword arguments does not matter because you need to specifically define the value of the argument when the fucntion is called. 
``` python
Monster_ranking(a="Bigfoot",b="Mothman",c="Yeti")
Monster_ranking(b="Mothman",c="Yeti",a="Bigfoot") #The order is the same
```

## Forcing argument type ##
Using special characters it is possible to force the arguments to be either postional or keywords. Any arguments before the `/` can only be a positional argument. Any arguments after the `*` can only be a keyword argument. 
``` python
def Example_fun(pos_only,/,pos_or_keyword,*,keyword_only):
  pass
```

## Arbitrary arguments ##
Sometimes one may not know how many arguments will be input into a function. Use a `*` before a postional argument and a `**` before a keyword argument to indicate that the given argument can be flexible in what is being accepted. In the case of the positional argument, the data is read into the function as a tuple. In the case of the keyword argument, the data is read in as a dictionary. 

``` python
def word_len(*a):
  for i in a:
    print("%s is %d characters long" % (i, len(i)))

word_len("Bigfoot","Mothman","Yeti")
```

``` python
def word_len_kw(**a):
  for i in a.values():
    print("%s is %d characters long" % (i, len(i)))
```
 

# Other Considerations #
A few final considerations. It is important to put different arguments types in the right order, otherwise python will throw up an error. The rules for argument order are as follows.
* Arguments with defaults, need to be specified before arguments without defaults when defining the function.
* Positional arguments need to come before keyword arguments when using the function.
* Keyword arguments can only be specified once by the user and also must match the arguments accepted by the function.
