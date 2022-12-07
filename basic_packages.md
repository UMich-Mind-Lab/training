# Creating a basic package for local use

The Python web site has a page on creating a Python package
that is oriented toward making it `pip` installable.  This
page is more about using a package as a way to bundle sets
of commands together to avoid defining a lot of functions
at the top of a file, and so that one can put the collections
into a directory suitable for inclusion in `PYTHONPATH`.

As an example, we'll take two functions from the file
`/nfs/turbo/lsa-lukehyde/MTwiNS/mri/bin/raw2bids.py` and
put them into a package.  We'll also convert comments to
docstrings.

## The original functions with comments

These are functions that are defined in the `raw2bids.py` file.

```python
# custom function to call subprocess to gzip -c and redirect
# output to specified file name this way we can copy and zip
# at the same time
def gzip_copy(inFile, outFile):
    print(f'gzip -c {inFile} > {outFile}...\n')
    os.makedirs(os.path.dirname(outFile), exist_ok=True)
    with open(outFile, 'w') as of:
        subprocess.run(['gzip', '-c', inFile], stdout=of)

# fslreorient2std will put the axes in standard RAS+. We can run
# the function and copy the file at the same time. However, if the
# scan DOES NOT need to have axes swapped (as evidenced by
# fslreorient2std transforming with an identity matrix), then we
# should just copy as normal, because fslreorient2std appears to not
# read FSLOUTPUT type correctly in this situation.
# (see https://github.com/nipy/nipype/issues/1683)

def run_fslreorient2std(inFile, outFile):
    os.makedirs(os.path.dirname(outFile), exist_ok=True)
    # run it first w/out outFile to check if transform matrix is identity matrix
    result = subprocess.run(['fslreorient2std', inFile], capture_output=True)
    if result.stdout == b'1 0 0 0\n0 1 0 0\n0 0 1 0\n0 0 0 1\n':
        print('subject already in standard space, will just copy the file.')
        if '.gz' in inFile:
            print(f'{inFile} > {outFile}\n')
            shutil.copy(inFile, outFile)
        else:
            gzip_copy(inFile, outFile)
    else:
        print(f'running fslreorient2std {inFile} > {outFile}...\n')
        result = subprocess.run(['fslreorient2std', inFile, outFile], capture_output=True)
        if result.stderr:
            print(f'\n{result.stderr}\n')
            gzip_copy(inFile, outFile)
```

We will look at making them available from an importable package so
that the `raw2bids.py` file is more readable, or at least so I think
it will be if all the functions do not have to be defined at the top.

## Outline of a minimal package directory

The minimal requirement for a package directory is two files: one
called `__init__.py` and one to contain the functions provided by
the package.  So, for example, suppose we are writing an appointment
calendar program.  We might start by calling the package `calendar`
and putting all the functions that manipulate appointments into a
file called `appointments.py`; e.g., `create(name)`, `cancel(name)`,
`modify(name)`, etc.  We would create a directory,

```bash
calendar/
    appointments.py
    __init__.py
```
and inside `__init__.py` we would put a line that says

```python
from calendar import appointments.py
```

For demonstration purposes, the contents of `appointments.py` are just

```
def create(name):
    """This is my create appointment docstring"""
    print(f"Creating the appointment called {name}")
```

We then add the directory that contains `calendar` to our `PYTHONPATH`,
and we can then

```python
import calendar
calendar.appointments.create('dentist')
```

or

```python
from calendar import appointments
appointments.create('dentist')
```

both of which would just print the string "Creating the appointment
called dentist".

## The raw2bids package: First try

So, let try to make a package out of just those two functions above.
Start by create the `raw2bids` directory.  For this first try, we
will put two placeholder function definitions into `raw2bids/tools.py`.
Note, I am changing the name of the function above to just
`reorient2std()`, as I think that will be clearer in usage.  If
you want to know how, you would look in the function's docstring,
which we'll get to in a bit.

```
def gzip_copy():
    print("I am gzip_copy")

def reorient2std():
    print("I am reorient2std")
```
and into `__init__.py`, we will put

```python
from raw2bids.tools import gzip_copy
from raw2bids.tools import reorient2std
```

Assuming that you put `raw2bids` into `$HOME/Python`, you would

```bash
export PYTHONPATH=$HOME/Python
```

and you can then

```python
>>> import raw2bids
>>> raw2bids.tools.gzip_copy()
I am gzip_copy

>>> from raw2bids import tools
>>> tools.gzip_copy()
I am gzip_copy

>>> from raw2bids.tools import gzip_copy
>>> gzip_copy
I am gzip_copy
```

## Comments versus docstrings

In both the above function definitions, there are comments above the
function definition to describe it or explain usage.  Those are different
from any comments inside the function that explain programming constructs
or why something is done as it is.

To access those comments, you have to edit the script, which is fine in
some contexts, but it might be better in other contexts to be able to
print those comments without getting out of Python and editing the file
that contains them.  For that reason, we should be preferring _docstrings_
over descriptive comments for functions.

You may want to take a look at the [official
documentation](https://peps.python.org/pep-0257/) for docstrings,
but for our purposes, converting the existing comments into
docstrings will be sufficient.

So, let's start with a simple example, our current definition of
`gzip_copy`.  Suppose we were to add the comment from the original
definition; that would look like this.

```python
# custom function to call subprocess to gzip -c and redirect
# output to specified file name this way we can copy and zip
# at the same time
def gzip_copy():
    print("I am gzip_copy")
```

To convert that to a docstring, remove the `#` and move the
text into a triple-quoted string at the top of the function.

```python
def gzip_copy():
    ```
    Custom function to call subprocess to gzip -c and redirect
    output to specified file name this way we can copy and zip
    at the same time
    ```
    print("I am gzip_copy")
```

Once that function is imported, you can then use

```python
>>> from raw2bids import tools
>>> print(tools.gzip_copy.__doc__)

    Custom function to call subprocess to gzip -c and redirect
    output to specified file name this way we can copy and zip
    at the same time
    
```

to print the docstring.  In this case, it isn't very helpful,
but the docstring should include the types of variables expected
as input and the contents and type of any values returned, which
would be useful.
