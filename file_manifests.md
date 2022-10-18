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

Review for making a python file executable as a program.

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
