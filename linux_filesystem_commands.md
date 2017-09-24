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


## 

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


### Directory permissions

In addition to the read and write permissions, directories need to have
the execute permission set for the users permitted to be able to change
into the directory.  If the `x` is not set, then they will be able list
the contents of the directory, but they will not be able to `cd` to it.

The group sticky bit, `s`, can be set so that new files and directories created
within a parent will inherit the group ownership of the parent.  See the `chmod`
command below for more information.

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



