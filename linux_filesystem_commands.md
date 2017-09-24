# Linux commands to work with the filesystem


### File and directory names

You can name files and directories almost anything on a Linux machine,
however, we recommend that you limit yourself to using a restricted
set of characters, and that you establish some conventions.  The
recommended set of characters is

+ letters, both upper- and lowercase
+ numerals
+ the dash (`-`), the underscore (`_`), and the dot (.)

Note that a dot as the _first_ character will make a file or directory
hidden from listing commands and wildcards.  Many _dot files_ are for
configuration options or program data.

There are also two special directories, called dot (`.`) and dot-dot (`..`).
The dot directory is the directory that you are currently working from
(or are 'in').  The dot-dot directory is the one above the current
directory, or, if you're looking at its name, it's everything to the
left of the first `/` character as you move to the left from the right.

Other characters can be used, but may have special significance to some
programs and are therefore not recommended.

Some people will begin directory names with an upper-case letter, to make
them easily distinguishable in list of directory contents.

Windows uses the _extension_, that is the characters after the last dot
in a file name, to select which program is the default to use with the
file, but Linux does not use or enforce that.  However, you can make
life easier for humans by establishing naming conventions for the lab.
For example, naming files with `.sh` at the end will make shell scripts
easily identifiable.  Some programs that run on Linux _will_ want the
extension to match those on Windows, so stick with `.m` for MATLAB
scripts, `.py` for Python, `.txt` for text files, etc.  That will make
you happier if you copy them to and from Windows.  Much happier.


## Some commands

#### `pwd`: Print the present working directory
Typically used without options.
_Example_
```
$ pwd
```

#### `mkdir`: Used to create one or more directories

_Common options_

`-p` if you are trying to create a directory whose parent does not exist, create
all the necessary intermediate paths.

_Examples_
```
$ mkdir /tmp/test
$ mkdir /tmp/test/test2
$ mkdir -p /tmp/test2/subtest
```

#### `cd`: Change to a directory
_Common options_
Including a directory or file name or names causes `ls` to work on the given
files or directories.  Without any arguments, `cd` will change to your home
directory.  Using `-` (dash) as the directory name will change you to the
last most recent directory; that is, where you were prior to the most recent
`cd` command.
_Examples_
```
$ cd /tmp/test
$ cd ..
$ cd -
$ cd
```

#### `rmdir`: Used to remove empty directories

`-p` will remove parent directories if the contain only the path to the directory
being removed.  Recommended that you use this _only_ relative to the current
directory; i.e., `rmdir -p some/path` and never `rmdir -p /some/absolute/path`.

_Examples_
```
$ rmdir /tmp/test/test2
$ cd /tmp
$ rmdir -p /tmp/test2/subtest
```

#### `rm`: Used to remove a file or folder (usually non-empty)

The `rm` command in its simplest form removes a file.  It can also be
used to remove directories, empty or not.

_Common options_

`-r` instructs `rm` to remove all the files and folders in the provided
directory (or file) name.

`-i` instructs `rm` to prompt whether to delete each file before doing
so.

`-v` instructs `rm` to print a report of what it deleted.

_Examples_
```
$ rm  tmp.0xkT43
$ rm -rv subject02000
$ rm -ri DTI/sub001.bad
```


## Permissions and what they are for

### File permissions

Files will have permissions to say who can and cannot look at or in them,
who can remove or change them, who can run them as programs.  In a listing
that shows permissions, the permissions are specified by single letters:
`r` for read, `w` for write, `x` for execute, and `-` for no permission.
The permissions are set in groups of three, with position indicating to
whom they apply.  Here is an example of the permissions set for a file,
where the permissions are the first listed group of characters, `-rw-rw-r--.`.
```
$ ls -l README 
-rw-rw-r--. 1 grundoon users 0 Sep 24 12:08 README
```
The first `-` simply indicates that this is an ordinary file.  The next
three characters, `rw-` indicate that the owner of the file, a user named
`grundoon`, can read and write the file, and that it should not be considered
an executable (runnable) program.  The second set is the same as the first
`rw-` but applies to the group, in this case `users`.  The final set is
`r--`, which applies to all others not an owner or in the group, and means
they can only read, and cannot write or execute.  The final `.` characters
means that the may be additional permissions imposed by an _access control
list_, and those may change what you see in the directory listing.

It's worth making special note of the `x` permission on files.  Even if a
file contains the binary data needed to be run by the computer, if the `x`
permission is not set, Linux will not execute it.  On Linux computers,
it is also possible to write a program in a _scripting language_, like
Bash (the shell), or Python, or Perl, and insert a special line at the
top of the file that says which program understands the program.  When
the execute permission (sometimes referred to as the execute _bit_) is
set, the shell will read that line and start the right program to run
the script.

An example will help clarify this.  Suppose we have a file called
`hello.sh` that contains the following lines
```
#!/bin/bash
echo "Hello, there."
echo "I just printed something for you."
```
The first line says which progam understands all the following lines,
and the next two lines are anything that the program understands.  In
this case, the shell will hand over to another shell to run the commands.

Here is what the same program might look like if written for Python and
save in `hello.py`.
```
#!/usr/bin/python
print("Hello, there.")
print("I just printed something for you.")
```
If the execute permission is unset, those two scripts could still be
run, but you would need to provide the program name yourself.
```
$ bash hello.sh
$ python hello.py
```

### Directory permissions

In addition to the read and write permissions, directories need to have
the execute permission set for the users permitted to be able to change
into the directory.  If the `x` is not set, then they will be able list
the contents of the directory, but they will not be able to `cd` to it.

The group sticky bit, `s`, can be set so that new files and directories created
within a parent will inherit the group ownership of the parent.  See the `chmod`
command below for more information.


## Some more commands

#### `ls`: List the contents of a directory

_Common options_
`-d` will list only the directory name and not the contents.

`-l` will make a long listing that shows permissions, owner and group, and
the time last modified, among others.

`-lt` lists files sorted by modification time, with newest files appearing
at the top of the listing.

`-ltr` is the same as `-lt` except in reverse-chronological order, i.e., the
most recently modified files will appear at the bottom of the listing.

`-R` says `ls` should list the contents of all subdirectories as well as
the directory or directories given as arguments.  This is a good place
to remind you, or tell you, that Linux is case sensitive, so `-r` and
`-R` are completely different.

_Examples_
```
$ ls
$ ls -l
$ ls -d /tmp
$ ls -d /tmp/*
$ ls -ld /tmp /var /data/projects/*
$ ls -lt /tmp
$ ls -ltr /tmp
$ ls -R /tmp
```

#### `chmod`: Change the mode (permissions) of a file or directory

_Common options_
_Examples_


#### `cat`: Print the contents of a file or files
This will print the contents, no matter what they are (might be binary
and look like punctuation and make beeps), nor how big the file is.  Still
useful, but use caution.  One use is to get file contents onscreen to copy
and paste.

_Examples_
```
$ cat .bashrc
$ cat README INSTALL
```

#### `less`: Used to 'page' through a file one screen at a time.

Once a file is displayed by `less`, you can search for text by pressing the `/` key,
then entering the text to search.  Found matches will be highlighted.  You can
use `n` to go to the next match and `N` (Shift-N) to move to the previous match.
The `f` (or the spacebar, or possibly the page-down key) will move you forward one
screenfull; `b` (will move you back one screenfull; Return or the down-arrow will
move you one line forward.  To quit, use `q`.  This is a totally most-excellent
program to use to get used to reading `man` pages.

#### `touch`: Update the last modified time; create an empty file.

This is really handy to create files to test things like wildcards, to try
deleting or removing files to make sure all and only what you intend to remove
is.  In more advanced use, it can be used to trigger reprocessing of files that
use the modification time of the input file to decide whether processing needs
to be done or not.

## Wildcards

Wildcards are used when you want to specify only part of a name.  This can be
used frivolously as a typing shortcut, or to match pattern in the names of
a group of files (and remember, directories are files, too).  The most commonly
used wildcard is the `*` character, which by itself stands for 'zero or more
of anything'.  You can restrict the characters that it will match none or more
of by putting the characters inside square brackets before the `*`.  For example,
```
$ ls -d sub0[01]*
```
will list `sub001` and `sub00000` but not `sub020`, because `2` is not included
in the match set.  You can use a range or ranges inside the brackets.  For example,
`[0-9a-zA-z]` would match letters and numerals.  Zero or more can sometimes
lead to too many matches, and it is often better to try to be more specific.

The other wildcard character that the shell understands is tehe question mark.
It will match exactly one occurrence.  Consider the difference between these
two patterns: `sub*` and `sub???`.  The first will match anything that begins
with `sub`, whereas the second will match only if there are exactly three
characters.  Which would you want to use if you were removing subject
directories, but there were also a file called `subject_BMIs.txt` in the same
folder?

#### `cp`: Copy a file or files

The `cp` command copies a file.  If no path is given, then the new files is
in the same directory as the original.  A path can be given to either the
original or to the new file or both.  You do not have to be in the directory
of either file to copy a file.

_Common options_

`-r` when used with a directory name will copy the directory and all its
contents to the new location.

`-p` will copy the last modified date and time from the original to the new
file.  This is really helpful when reorganizing and the date may help people
when looking at directory listings.

_Examples_
```
$ cp dissertation.txt dissertation.txt.bak
$ cp ~/file.txt /tmp/test.txt
$ cp -r openfmri /tmp/openfMRI
$ cp -rp data/subject001/raw data/raw/subject001
```

#### `mv`: Move a file or files to another location or name

On Linux, renaming a file on the same file system may be the same as renaming
a file, so the simplest `mv` just renames a file.  `mv` is also used to
move files from one directory to another.  It can be used to move whole
directories to a new location as well.  If the target exists, `mv` will
happily overwrite it.

_Common options_

`-i` will cause `mv` to prompt whether you want to overwrite the new file if one
exists in the new location.

`-n` instructs `mv` not to overwrite an existing file.

_Examples_
```
$ mv tset.txt test.txt
$ mv data_dir study_dir
$ mv -i data_dir/anat study_dir/anat
$ mv -n data_dir/func study_dir/func
```

#### `rename`: Copy a file or files

_Common options_
_Examples_

