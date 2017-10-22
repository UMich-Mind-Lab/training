# Why spaces are not good in names

When you type something on the command line, spaces are interpreted as separators.
They separate options from each other, but they are also used to separate the
items in a list.  This presents a problem if there are spaces in the path to
a file.  The directory name
```bash
./MTwiNS/MT_1/MRI Tasks/Twin 1
```
if given to a program will be interpreted as three things, not one,
and that is almost certainly never what you want.
```bash
$ ls MTwiNS/MT_1/MRI Tasks/Twin 1
ls: cannot access MTwiNS/MT_1/MRI: No such file or directory
ls: cannot access Tasks/Twin: No such file or directory
ls: cannot access 1: No such file or directory
```
To use a directory name with a space in it, you need to somehow indicate
that the space is part of the name and not a separator, as would be usual.
There are two ways to do that.  One is by _escaping_ the space, with the
backslash character.
```bash
$ ls ./MTwiNS/MT_1/MRI\ Tasks/Twin\ 1
1_faces_t1.edat2
```
and that is what using Tab-completion does for you when it completes a
directory or filename that contains a space.  Another way to indicate
that the space is part of the name is to quote the name.
```bash
$ ls "./MTwiNS/MT_1/MRI Tasks/Twin 1"
1_faces_t1.edat2
```
but that does not help you when the name may not be know ahead and you
have to gather them into a list for processing.
```bash
for twin in $(ls ./MTwiNS/MT_1/MRI Tasks) ; do
    ls $twin
done
```
Go ahead.  Try all your tricks to make that work!  There are ways to do it,
but they are probably more painful than not using spaces in directory or
filenames.

Whether you agree or not, the rest of this lesson assumes that spaces
are bad in names, and we will seek to expunge them.  We will also assume
that you have run these commands (entered without the usual prompt
indicator so you can copy-and-paste them.
```bash
for id in 1 23 154 ; do
    for twin in 1 2 ; do
        mkdir -p "/tmp/$LOGNAME/MTwiNS/MT_$id/MRI Tasks/Twin $twin"
        touch "/tmp/$LOGNAME/MTwiNS/MT_$id/MRI Tasks/Twin $twin/${id}_faces_t$twin.edat2"
    done
done
```
which will create a directory in `/tmp` with your name, and it will contain these
folders and files.
```bash
./MTwiNS
./MTwiNS/MT_54
./MTwiNS/MT_54/MRI Tasks
./MTwiNS/MT_54/MRI Tasks/Twin 1
./MTwiNS/MT_1
./MTwiNS/MT_1/MRI Tasks
./MTwiNS/MT_1/MRI Tasks/Twin 1
./MTwiNS/MT_1/MRI Tasks/Twin 1/1_faces_t1.edat2
./MTwiNS/MT_1/MRI Tasks/Twin 2
./MTwiNS/MT_1/MRI Tasks/Twin 2/1_faces_t2.edat2
./MTwiNS/MT_23
./MTwiNS/MT_23/MRI Tasks
./MTwiNS/MT_23/MRI Tasks/Twin 1
./MTwiNS/MT_23/MRI Tasks/Twin 1/23_faces_t1.edat2
./MTwiNS/MT_23/MRI Tasks/Twin 2
./MTwiNS/MT_23/MRI Tasks/Twin 2/23_faces_t2.edat2
./MTwiNS/MT_154
./MTwiNS/MT_154/MRI Tasks
./MTwiNS/MT_154/MRI Tasks/Twin 1
./MTwiNS/MT_154/MRI Tasks/Twin 1/154_faces_t1.edat2
./MTwiNS/MT_154/MRI Tasks/Twin 2
./MTwiNS/MT_154/MRI Tasks/Twin 2/154_faces_t2.edat2
```
You should `cd` to your directory in `/tmp` now, as the rest of the
examples assume you are in `/tmp/$LOGNAME`.

This is an excellent opportunity to use the `echo` command to help figure
things out.  Suppose you want to get the names of all the folders that are
int the `MRI Tasks` folder for each subject.  You might try something like
```bash
$ for twin_dir in $(ls -d MTwiNS/M*/*) ; do
>     echo $twin_dir
> done
```
But, that should get you
```bash
MTwiNS/MT_154/MRI
Tasks
MTwiNS/MT_1/MRI
Tasks
MTwiNS/MT_23/MRI
Tasks
```
which again illustrates that the space gets interpreted as a separator.  We
can get what we want, but to do so, we _save the pathname in a variable_ so
we can quote it.
```bash
$ for dir in MTwiNS/* ; do
>     subdir=$dir/$(ls $dir)
>     echo $subdir
>     ls "$subdir"
> done
```
But, we quickly get tortured when there is yet another level below that.
We try this,
```bash
$ for dir in MTwiNS/* ; do
>     subdir=$dir/$(ls $dir)
>     echo $subdir
>     ls "$subdir"
>     for twin_dir in $(ls "$subdir") ; do
>         echo $subdir/$twin_dir
>     done
> done
```
and we are unhappy.  So, let's see if we can figure out how to rename
folder with spaces to make our future selves happier.

I start by asking myself what I want to do.
> I want to rename a file with a space in its name so it does not
> have a space in it.
I don't know what the rest of the name will be, only that it will have
a space in it.  So, I have something like `Fine Name` but I want maybe
`Fine_Name` or `FineName`.

What is renaming?  It's taking one set of characters, `Fine Name` and
converting it into another set, `Fine_Name`, and using those with the
`mv` command.  Before we do the `mv`, we first have to convert one set
of characters to the other.  Now we are working on a different problem.

Let's stack those names on top of each other,
```
Fine Name
Fine_Name
```
and compare them.  We have `Fine` in both, and we have `Name` in both:
`(Fine)?(Name)`.  We could solve this problem if we can convert the
space to an underscore.  If you ask the Goog, you will find several
ways to do this.  Since this is only one character, we will use the
simplest way, the `tr` command.  As the `man` page sez,
```
NAME
       tr - translate or delete characters
```
and we again use our buddy, `echo`.
```bash
$ echo Fine Name | tr ' ' '_'
Fine_Name
```
or, if you wanted the space removed,
```bash
$ echo Fine Name | tr -d ' '
FineName
```
So, having solved that, we now need to use that to actually rename
the file.  Remember, up above, we found we can use `for dir in MTwiNS/MT*/M*`
to get the directory names.
```bash
$ for dir in MTwiNS/MT*/M* ; do
>     echo mv $dir $(echo $dir | tr ' ' '_')
> done
mv MTwiNS/MT_154/MRI Tasks MTwiNS/MT_154/MRI_Tasks
mv MTwiNS/MT_1/MRI Tasks MTwiNS/MT_1/MRI_Tasks
mv MTwiNS/MT_23/MRI Tasks MTwiNS/MT_23/MRI_Tasks
```
So, let's try it without the `echo` in front of it.
```bash
$ for dir in MTwiNS/MT*/M* ; do
>    mv $dir $(echo $dir | tr ' ' '_')
> done
mv: target ‘MTwiNS/MT_154/MRI_Tasks’ is not a directory
mv: target ‘MTwiNS/MT_1/MRI_Tasks’ is not a directory
mv: target ‘MTwiNS/MT_23/MRI_Tasks’ is not a directory
```
Oh, yeah, we're back at that again.  We need the quotes.
```bash
$ for dir in MTwiNS/MT*/M* ; do
>    mv "$dir" $(echo $dir | tr ' ' '_')
> done
$ ls -d MTwiNS/MT*/M*
MTwiNS/MT_154/MRI_Tasks  MTwiNS/MT_1/MRI_Tasks  MTwiNS/MT_23/MRI_Tasks
```
If you prefer deleting the space instead of substituting the underscore,
change the `tr ' ' '_'` to `tr -d ' '`.

So, having done that, we of course find there is an easier way!  Let's
try it that way, instead.  We've gone and changed all the `MRI Tasks`
folders to `MRI_Tasks`, though, so wouldn't it be nice if we could
go back and start over easily?

## Digression on creating utility scripts of your own

You can make a `bin` directory in your home directory with
```bash
$ mkdir ~/bin
```
and any programs put into it will be in your path.  So, do that, then
create a file called `~/bin/make_twins_test.sh` and put this into it
```bash
#!/bin/ bash

if [ -d /tmp/$LOGNAME/MTwiNS ] ; then
    rm -r /tmp/$LOGNAME/MTwiNS
    echo Removed /tmp/$LOGNAME/MTwiNS
fi
for id in 1 23 154 ; do
    for twin in 1 2 ; do
        mkdir -p "/tmp/$LOGNAME/MTwiNS/MT_$id/MRI Tasks/Twin $twin"
        touch "/tmp/$LOGNAME/MTwiNS/MT_$id/MRI Tasks/Twin $twin/${id}_faces_t$twin.edat2"
    done
done
echo Created a fresh version of /tmp/$LOGNAME/MTwiNS
```
Then set the permissions so it is executable, and run it.
```bash
$ chmod +x ~/bin/make_twins_test.sh
$ ~/bin/make_twins_test.sh
Removed /tmp/grundoon/MTwiNS
Created a fresh version of /tmp/grundoon/MTwiNS
```

## Back to the main topic

Having now restored our test situation, the easier way is to use the
`rename` command.  The `man` page for `rename` tells us that we should
use `rename` like this:
```bash
SYNOPSIS
       rename [options] expression replacement file...
```
All of what we went through above is not lost because `rename` takes
pretty much the same arguments (the things after the command name) as
`tr`, namely `rename ' ' '_' filename`.  So, this,
```bash
$ for dir in MTwiNS/MT*/M* ; do
>    mv "$dir" $(echo $dir | tr ' ' '_')
> done
$ ls -d MTwiNS/MT*/M*
MTwiNS/MT_154/MRI_Tasks  MTwiNS/MT_1/MRI_Tasks  MTwiNS/MT_23/MRI_Tasks
```
becomes
```bash
$ rename ' ' '_' MTwiNS/MT*/M*
$ ls -d MTwiNS/MT*/M*
MTwiNS/MT_154/MRI_Tasks  MTwiNS/MT_1/MRI_Tasks  MTwiNS/MT_23/MRI_Tasks
```
Now, you rename the `Twin 1` and `Twin 2` directories so they do not
have spaces in the names.

I will note here, that you should run `make_twins_test.sh ` again, then
try
```bash
$ rename ' ' '_' MTwiNS/MT*/M*/Twin*
```
to see what happens when you try to use `rename` if there is a directory
with spaces in the name of what you're trying to change.
