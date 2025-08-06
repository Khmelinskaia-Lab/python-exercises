# python-exercises

A collection of python exercises for the Khmelinskaia Lab.

# Instructions for using this repository

Clone the repository to your system:
```
git clone git@github.com:Khmelinskaia-Lab/python-exercises.git
```

If you do not yet have a github account, get one [here](https://github.com/).\
If you need help setting up SSH keys for your GitHub account, look [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to create SSH keys and [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to add them to your GitHub account.

Move to the newly cloned repository directory and create a new branch for you to work on
```
cd python-exercises
git checkout -b <your-name-here>
```

**!!Note!!**: In case of any issues with this repository, please contact [Kevin O'Brien](mailto:kevin.obrien@cup.lmu.de).

&nbsp;<br>
# Exercise guidelines

The instructions for each homework are provided in place.\
You will be programming in Python 3.6 or higher.\
You should make use of the PEP8 conventions from the start -- this improves readability and helps a third party user understand the code.\
You can find details of PEP8 [here](https://www.python.org/dev/peps/pep-0008/#code-lay-out), but the TL;DR version is:

* Prefer spaces over tabs for indentation.
Indentation should be set to 4 spaces. 
* Limit all lines to 79 characters (including indentation).
Limit comments to 72 characters per line.
Use line breaks and backslashes.
* Variable/function/class names should be descriptive, i.e., do not use something like `a=1` or `new="blah"`.
* For variable/function names, use `lower_case_with_underscores`, for objects use `UpperCamelCase`.
* No unnecessary spaces, but spaces between operators, e.g., `c = (a + b) * (a - b)` is good, but `c = ( a + b ) * ( a - b )` is bad.
* No spaces around `=` for function arguments, e.g., `foo(r=real, i=imag)` is good, but `foo(r = real, i = imag)` is bad.
* For strings, pick either single quotes or double quotes and stick to it.

Most modern IDEs (e.g. VSCode, PyCharm) support automatic PEP8 checking functionality, but you'll have to enable it.

&nbsp;<br>
Exercises are outlined below with more detailed instructions to be found in the individual python files.\
Hope you have fun doing them!


&nbsp;<br>
# Homework set 1

This homework set covers loops, conditions, lists, dictionaries and tuples.\
The exercises are found in:

1. `src/hw1/01_prime_checker.py`
2. `src/hw1/02_common_factors.py`
3. `src/hw1/03_word_frequency.py`
4. `src/hw1/04_diamond.py`


&nbsp;<br>
# Homework set 2

This homework set is based on reading and manipulating a score file.\
You should be able to use much of the code you write here to analyze your own score files.

This homework set covers regular expressions, string manipulations, basic file handling, pandas dataframes, and argument parsing.\
The exercises are found in:

1. `src/hw2/01_decoy_score_search.py`
2. `src/hw2/02_fix_score_file.py`
3. `src/hw2/03_analyze_score_file.py`
4. `src/hw2/04_analyze_score_file_user_input.py`


&nbsp;<br>
# Homework set 3
There is a data file, `data/hw3/ref2015_wts` which will be used in this exercise set.

Since you will be required to write functions, please be sure to include multi-line descriptions of the function, specifically what the input parameters are, what the output will be and what the function does.\
See [here](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) for information on Google style docstrings.

It would also be nice to start including author information at the start of your files.\
For example, my files would have something like:
```
__author__ = "Alena Khmelinskaia"
__email__  = "myemail@domain.com"
```
This comes before your import statements.

This homework set covers function definitions, optional parameters, variable parameters, and lambda functions.\
The exercises are found in:

1. `src/hw3/01_common_factors_arbitrary_numbers.py`
2. `src/hw3/02_float_increment.py`
3. `src/hw3/03_alter_weights.py`
4. `src/hw3/04_num_bounds.py`


&nbsp;<br>
# Homework set 4
There is a data file, `data/hw4/3m1z_SymDock_score.sc` which will be used in this exercise set.

For concepts required for question 1, try [this tutorial](https://realpython.com/instance-class-and-static-methods-demystified/).\
If you have difficulty getting started, the question itself was inspired by [this](https://www.codexpedia.com/python/python-class-example/).

For question 3, python exceptions are explained well [here](https://realpython.com/python-exceptions/) -- I liked the figures as they make it really clear.\
In this question, you will have to find a built-in exception.\
[Here](https://docs.python.org/3.6/library/exceptions.html) is a list of all of them -- it should be fairly easy to find the one you need.

For question 4, you will need to install and import the `matplotlib` package.

This homework set covers class definitions, importing and using custom classes, exception handling and basic plotting with the `matplotlib` module.\
The exercises are found in:

1. `src/hw4/cylinder.py`
2. `src/hw4/02_compare_cylinders.py`
3. `src/hw4/03_randint_list.py`
4. `src/hw4/04_plot_score_vs_rmsd.py`

