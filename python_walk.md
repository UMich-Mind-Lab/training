# Getting file and directory names

## Using `os.walk()`

There are a bunch of ways to look at all the files and subdirectories under
a directory using Python.  The most 'intuitive' one is probably using the
'walk' function from the `os` library.  This is often used by importing the
os library, then calling it with `os.walk()`.

`os.walk(dir)` looks at every directory in `dir`, including `dir` itself, and
for each of them, it returns a 'tuple' (a list with unchangeable entries)
where the first element is the name of the current directory in the walk,
the second is the names of any subdirectories, and the third is the names
of any files in the directory.

`os.walk()` is what is called a _generator_,

```python
>>> os.walk(dir)
<generator object walk at 0x7fb99af5d2d0>
```

which means that it does not actually produce anything until it is asked
to do so.  The two main ways to do that are by using a `for` loop, which
we saw,

```python
>>> for dir, subdir, files in os.walk(dir):
...     print(dir)
```

or by using what is called a _list comprehension_, which here is a shorter way
to do a `for` loop.  Both are shown below.

So, suppose you have the following directory structure.

```
top
top/sub1
top/sub2
top/sub3
top/README
top/sub1/file1
top/sub1/file2
top/sub2/subsub
top/sub3/ssub/file
```

which can be created with these commands

```bash
for ii in 1 2 3 ; do
    mkdir -p top/sub$ii
done
echo "Test directory" > top/README
touch top/sub1/file{1,2}
mkdir top/sub2/subbsub
mkdir top/sub3/ssub
date > top/sub3/ssub/file
```

## For loops

```python
$ cd top
$ module load anaconda-3.7
$ python
>>> import os

# Store the name of the current directory in a variable
>>> the_dir = os.getcwd()

# Initialize an empty list
>>> subdir_list = []

# loop through the results of os.walk and store the tuple in x
>>> for x in os.walk(the_dir):
...     subdir_list.append(x)
...

# Check the number of entries
>>> len(subdir_list)
6
>>> for thing in subdir_list:
...   print(thing)
... 
('/tmp/bennet/top', ['sub3', 'sub2', 'sub1'], ['README'])
('/tmp/bennet/top/sub3', ['ssub'], [])
('/tmp/bennet/top/sub3/ssub', [], ['file'])
('/tmp/bennet/top/sub2', ['subbsub'], [])
('/tmp/bennet/top/sub2/subbsub', [], [])
('/tmp/bennet/top/sub1', [], ['file2', 'file1'])
```

The first line in the output is a tuple that contains the contents of the
`top` directory I made in `/tmp/bennet`.  Tuples are printed inside
parentheses instead of the square brackets used for lists.

The first item in the tuple is a string containing the name of the current
directory.  The second is a list of the subdirectories therein.  The third
is a list of the files therein.  So, the `top` directory has three
subdirectories and one file.

The second item is for the `top/sub3` directory, which contains one
subdirectory and no files; the third item is for the `top/sub3/ssub`
directory which has one file and no subdirectories.

If we want to generate a list of just the subdirectories, we should write
a program to extract from each of those tuples just the first entry.  If
we want to generate a list of all the files, we need to extract from
each entry the list of files, and then for each of those, join it to the
first entry, which is the directory in which the files appear.

So, for the third item, we join the first element to the only file.  For the
last item in the list above, we would join `'/tmp/bennet/top/sub1'` to
each of the two filenames.

## List comprehensions

I (bennet) have no idea why these are called this, but they are.  They are
functionally equivalent to a `for` loop.  I am not entirely comfortable
with these myself, but here is a simple one, which I will try to explain.

```python
[num for num in range(10)]
```

First, the `range` function returns a list of numbers.  If a single argument
is given, as 10 is above, then it returns a list from 0 to one less than the
number, i.e., 0--9.  The comprehension above has a list (the `range()`
function), set `num` successively to each element of that list (`for num in
list`), and finally the leftmost `num` is what is returned at each step.  By
enclosing all this in square brackets`[ ]`, this produces a list.  You could
also use `list(num for num in range(10))`.  That is, the result is the same
as the `for` loop above.

Here is the functionally equivalent list comprehension of the `for` loop
above.

```python
# Using a 'list comprehension'
>>> subdirs = [x for x in os.walk(the_dir)]

# Check the number of entries
>>> len(subdirs)
6
>>> for thing in subdirs:
...   print(thing)
... 
('/tmp/bennet/top', ['sub3', 'sub2', 'sub1'], ['README'])
('/tmp/bennet/top/sub3', ['ssub'], [])
('/tmp/bennet/top/sub3/ssub', [], ['file'])
('/tmp/bennet/top/sub2', ['subbsub'], [])
('/tmp/bennet/top/sub2/subbsub', [], [])
('/tmp/bennet/top/sub1', [], ['file2', 'file1'])
```

Finally, we can isolate the directory names by extracting the first item
from each tuple returned by `os.walk()`.  Tuples, like lists, have elements
that can be accessed by index, i.e., by their numeric position.  So, from
the comprehension example, we can use

```python
>>> for thing in subdirs:
...   print(thing[0])
... 
/tmp/bennet/top
/tmp/bennet/top/sub3
/tmp/bennet/top/sub3/ssub
/tmp/bennet/top/sub2
/tmp/bennet/top/sub2/subbsub
/tmp/bennet/top/sub1
```
to print just the first element of the tuple, here called `thing`.

If, instead of the subdirectories, we want a list of files, we would use

```python
>>> for thing in subdirs:
...     for file in thing[2]:
...         print(os.path.join(thing[0], file))
... 
/tmp/bennet/top/README
/tmp/bennet/top/sub3/ssub/file
/tmp/bennet/top/sub1/file2
/tmp/bennet/top/sub1/file1
```

