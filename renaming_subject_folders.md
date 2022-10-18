I would make sure that folders like those for subjects that they
have numbers in them have the same number of digits.  We saw folders
with names like
```bash
MT-154
MT-3
MT-45
```
I think.  I would rename those so that they were, instead,
```bash
MT-0003
MT-0045
MT-0154
```
Not only is it safer to try to match an exact pattern, like
```bash
MT_[0-9][0-9][0-9][0-9]
```
which will only match four-digit subjects, than matching `MT_*`,
when you list or sort the folder names, now they come out in
numerical order instead of 'ASCII-betical', which is when you have
```bash
1
11
12
2
24
```

Here's a really short example of how to do this kind of renaming.
I have these folders
```bash
MT_154
MT_3
MT_45
```
There's a function (program) called 'printf' that will print something
using a format that you give it, hence the 'f' on the end.  Try these
examples to see what you get.
```bash
$ printf '%04d' 3
$ printf '%04d' 45
$ printf '%04d' 154
```
The stuff inside the quotes is called the format string, and it says
_how_ to print the thing (or things) that come after.  Each
thing that gets printed is formatted by a `%` sequence.  In this case
`%04d` is decoded like this:  The `4d` means print as plain digit in
a column `4` spaces wide.  The `0` in front of the `4` means use 0s
instead of spaces as the column filler, i.e., left-pad with 0s.

We saw the `cut` command before.  Let's see what we can do with just
one folder name, `MT_3`.
```bash
$ echo "MT_3" | cut -d _ -f 2
```
That get's us the 3.  Make sure that it also works with the other
numbers.  Especially when we're first getting to know a new command
or idea, it's good to 'handle' it -- try it different ways, with
different input, until we get both familiar with it and confident that
we can predict what it will do.  You have to pound a lot of different
sizes and shapes of nail into a lot of different materials before you
really get comfortable with a hammer.

We can't use a pipe with `printf` -- you should try it to verify that
I'm right -- so we need to save the 3 into a variable before we can
print it with the proper leading zeros.  We'll do it like this.
```bash
$ ID_NUM=$(echo "MT_3" | cut -d _ -f 2)
```
Remember the `$` here is the prompt, the `$` before the parentheses
`$(...)` means "take the output of what's in the parentheses", and
we're about to use it to mean regular variable. We can even re-use
the same variable name.
```bash
$ ID_NUM=$(printf '%04d\n' $ID_NUM)
```
So, now, what happens if we run the next set of commands?  We're just
printing a command, not actually doing it, so this is safe, and not
like in Marathon Man.
```bash
$ dir=MT_3
$ ID_NUM=$(echo "$dir" | cut -d _ -f 2)
$ ID_NUM=$(printf '%04d\n' $ID_NUM)
$ echo mv $dir "MT_$ID_NUM"
```
Bash shell variables can have letters, underscores, and numerals
in them, so there's a problem when you want to put one next to
something that could be part of the name, for example, if the
ID number is supposed to be followed by `t1` or `t2`.  So, to be
safe, you can put the _name_ of the variable inside curly braces,
like this, `${ID_NUM}`, and that makes it safe to do something like
```bash
MT_${ID_NUM}_t1
```
If the braces weren't there, then it would be looking for a variable
called `ID_NUM_t1`, see?

OK, we're almost cooking with gas!  Last we put a for loop around that thing.
```bash
$ for dir in $(ls -d MT_*); do
>     ID_NUM=$(echo "$dir" | cut -d _ -f 2)
>     ID_NUM=$(printf '%04d\n' $ID_NUM)
>     echo mv $dir "MT_$ID_NUM"
> done
mv MT_154 MT_0154
mv MT_3 MT_0003
mv MT_45 MT_0045
```
So, that's one way to rename all the subject folders so they have
the same number of digits in their name.  To actually do it, you
take out the `echo` in the last command, or add another line just like
it but without the `echo`.  I would probably do it like this
```bash
$ ls
$ for dir in $(ls -d MT_*); do
>     ID_NUM=$(echo "$dir" | cut -d _ -f 2)
>     ID_NUM=$(printf '%04d\n' $ID_NUM)
>     echo Running mv $dir "MT_$ID_NUM"
>     mv $dir "MT_$ID_NUM"
> done
$ ls
```
If you want to make a test, you can do this on a Linux machine.
```
$ mkdir /tmp/yourname
$ cd /tmp/yourname
$ for dir in MT_154 MT_3 MT_45 ; do
>     mkdir $dir
> done
```
Then you can play around with the stuff up above and not worry about
the real data.
