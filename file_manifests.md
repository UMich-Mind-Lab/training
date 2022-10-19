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
```
$ python
Python 3.7.4 (default, Aug 13 2019, 20:35:49)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
```
*Note: `>>>` Indicates that we are using python*
----

**Python Tips**
The `print()` function provides an output of what is put within quotation marks in the parentheses
```python
>>> print("Hello, world.")
Hello, world.
```

One `=` sign assigns a variable to a name
You can print the variable if you put the assigned name into the `print()` function
```python
>>> mesg = "Hello, world."
>>> print(mesg)
Hello, world.
```

```python
>>> msg=mesg
>>> print(msg)
Hello, world.
```
```python
>>> mesg="Goodbye, cruel world"
>>> print(mesg)
Goodbye, cruel world
>>> print(msg)
Hello, world.
```

You can also assign a name to an integer variable 
The command ‘type()’ returns the variable type
```python
>>> m = 4
>>> type(m)
<class 'int'>
>>> type(msg)
<class 'str'>
```
There are 4 variable types: string, integer, 
`=` assigns a variable to a name, while `==` means 'equals to' 
```python
>>> n = "4"
>>> m==n
False
>>> n=4
>>> m==n
True
```

*Arrays:* multiple versions of the same types of data
*List:* can contain more than one type of data. Lists are identified by square brackets ‘[]’
```python
>>> lst = ["Hello", "Goodbye", "Yo"]
>>> print(lst)
['Hello', 'Goodbye', 'Yo']
```
----

**For Loops and Conditionals** 
```python
>>> for word in lst:
    print(word, ", world.")

Hello , world.
Goodbye , world.
Yo , world.
```
'Word’ = variable in list we are using in the for loop - in this case it 


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

**Trial**
'new' refers to the list of files we should have 
'lst' refers to the list of files we do have

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
>>> cntrl D
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

print("If I were Jared, I would be clever here. Done.")
```
----

**Review for making a python file executable as a program.**

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
