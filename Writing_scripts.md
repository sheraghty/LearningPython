# Writing python scripts
While python can be used interactivly in the terminal, it is typically advantageous to write scripts which can be run as necessary. Like writing bash scripts, python scripts start off a similar shebang

`
#!/usr/bin/python
`

This shebang indicates that the subsequent code is to be run using a python interpreter. There are some considerations depending on which version of python you want to run. The above line is fine when using the version of python that comes default with the terminal. However, if you want to use a specific conda environment you need to do one of several things. If you've already activated a conda environment then you can can simply change the shebang to the following

`
#!/usr/bin/env python
`

This shebang indicated that you want to use the currently loaded conda environment and not the default python that comes with terminal. Heres an example of a quick script that we will call hello.py. Note, the general convention is to name python scripts with the .py extension

``` Python
#!/usr/bin/env python
print("Hello World")
```

To run the script simply
``` Bash
./hello.py
```
