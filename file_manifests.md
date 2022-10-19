# Checking files against a manifest

The problem we are trying to solve is how to check that the
files in a directory match a list of those we think we should
have.  This is really two problems:  Do we have all the files
we think we should have?  Do we have any files we don't know
about?

1. We need to have a list of all the files that are supposed to
   be there.

1. We need a way to get a list of what is there.

1. We need a way to compare those two lists.

1. We need a way to meaningfully and helpfully report any
   differences.

We can use this as a framework for learning some useful
programming constructs with Python and shell programming.

This is also going to be a concern for our data management,
as much of what we do will be checking that files got created,
that they were named correctly, that a record of what was
right, what wrong, and what was done about the wrong is
created.

## Notes from first meeting

Load python module anaconda: ‘module load anaconda-3.7’
```
$ module load anaconda-3.7
```
`--version` command tells us which version of python we are currently using.
*Note:* The greatest difference between python packages = between v2 and v3. 
```
$ python --version
Python 3.7.4
```
Command `python` runs python / allows us to use python via the command prompt / PuTTY.
```bash
$ python
Python 3.7.4 (default, Aug 13 2019, 20:35:49)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The `>>>` is the Python prompt and indicates that Python commands
may be typed.  Each command should be followed by Return.  Some
commands will generate a `...` prompt, which indicates that the
command continues.  In the case of commands like `if` or `for`,
that is normal, and subsequent commands should be indented -- the
Python convention is indent four spaces.  You may also get that
prompt if you have an opening quote, or parenthesis, or bracket
without a closing one to match.


----

### Python Tips

The `print()` function provides an output of what is put within the parentheses.
That can be a variable name (unquoted) or a literal string (quoted).

```python
>>> print("Hello, world.")
Hello, world.
```

One `=` sign assigns a variable to a name.  You can print the variable if
you put the assigned name into the `print()` function.

```python
>>> mesg = "Hello, world."
>>> print(mesg)
Hello, world.
```

The command ‘type()’ returns the variable type.

```python
>>> m = 4
>>> type(m)
<class 'int'>
>>> type(msg)
<class 'str'>
```
There are 4 variable types that we will most commonly use: string, integer,
list, and dictionary.

Note that `=` assigns a variable to a name, while `==` tests whether the
thing on the right side is equal to the thing on the left side.  We created
the variable `m` above, and is the integer 4.  Here we create a variable
also with 4, but this time it is the character (string) `"4"`.  Then we
test whether they are equal.  Finally, we demonstrate that reusing a
variable name in a different assignment can change its type.

```python
>>> n = "4"
>>> m == n
False
>>> n = 4
>>> m == n
True
```

In other languages, there are typically "arrays", which contain multiple
values of the same type of data.  Python more commonly uses _lists_, which
are similar but can contain entries of different types.  List variables
are created by enclosing the values in square brackets ‘[]’; when an list
is printed, it is also printed with brackets.  You can tell that the
third element in list2 below is a number because when printed, it is
not enclosed in quotes.

```python
>>> lst = ["Hello", "Goodbye", "Yo"]
>>> print(lst)
['Hello', 'Goodbye', 'Yo']

>>> list2 = ["I", "have", 4, "values"]
>>> print(list2)
['I', 'have', 4, 'values']
```
----

### For Loops and Conditionals

```python
>>> for word in lst:
    print(word, ", world.")

Hello , world.
Goodbye , world.
Yo , world.
```

Using `if else`:
```python
>>> for word in lst:
    if word == "Yo":
        print(word, ", brudder!")
    else:
        print(word, ", world.")

Hello , world.
Goodbye , world.
Yo , brudder!
```

Using `if else,else if`:
```python
>>> for word in lst:
   if word == "Yo":
        print(word, ", brudder!")
    elif word == "Goodbye":
        print(word, ", cruel world")
    else:
        print(word, ", world")

Hello , world
Goodbye , cruel world
Yo , brudder!
```
----

### Trial

`new` refers to the list of files we should have 

`lst` refers to the list of files we do have

Below is an example of using the 'if, else' function to print variables in the ‘lst’ list that are missing in the ‘new’ list
```python
>>> for word in lst:
    if word in new:
        pass
    else:
        print(word, " is missing")

Hello  is missing
Goodbye  is missing
```


Below is an example of using the 'if, else' function to print variables in the ‘new’ list that are not in the ‘lst’ list
```python
>>> for word in new:
    if word in lst:
        pass
    else:
        print(word, " is extra")

Hey  is extra
Dude  is extra
```

Exit Python.
```python
>>> Ctrl-D
```
----

After checking to see whether python code works when running the software via PuTTY, you can create / edit python script.

Nano is an editor which can be used to write actual python script via PuTTY.

The command `"nano" <filename>.<filetype>`will allow you to do this. Example displayed below
```
$ nano compare.py
```

Below is an example of python code written using the nano editor tool on PuTTY
```
#!/usr/bin/env python

lst = ["hello", "goodbye", "yo"]
new = ['hey', 'yo', 'dude']

print("Looking for missing")

for word in lst:
    if word in new:
        pass
    else:
        print(word, " is missing")

print("Looking for missing")

for word in new:
    if word in lst:
        pass
    else:
        print(word, " is extra")

print("Done.")
```
----

### Review for making a python file executable as a program.

The first line should be

```
#!/usr/bin/env python
```

You should change the permissions with

```
$ chmod +x <filename>
```

## Practical application/exercise

Here is the list of files we are supposed to have.

```
dicom.tgz
eht1spgr_208sl.nii
ht1spgr_208sl.nii
t1spgr_208sl.nii
```

and here is a list of files from some subject.

```
dicom
eht1spgr_208sl.nii
ht1spgr_208sl.nii
t1spgr_208sl.nii
```

Using what we did in the first lesson, create a python
program file that creates a list for each of those above
and compares them.  It should print which files are missing
and which are extra.

Run the program using both methods; i.e.,

```
$ python file_compare.py
$ ./file_compare.py
```

For an extra nicety, the `dicom` in the second list is a
directory.  Add an extra test so that if `dicom.tgz` is
there it is considered right, if `dicom` is there, print
a message saying:  DICOM files are in a directory.  If
neither of those is there, then print a message saying
that the DICOM files are missing.

Example of colorized Python.
```python
>>> print("Hello, world")
Hello, world
```
