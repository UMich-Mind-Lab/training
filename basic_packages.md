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

We then add the directory that contains `calendar` to our `PYTHONPATH`,
and we can then

```python
import calendar
calendar.appointments.create('dentist')
```

or

```python
from calendar import appointments
appointments.create('hair')
```
