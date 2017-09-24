# Linux commands to work with the filesystem

## Directories

`mkdir`: Used to create directories

Common options

`-p` if you are trying to create a directory whose parent does not exist, create
all the necessary intermediate paths.

Examples
```
$ mkdir /tmp/test
$ mkdir /tmp/test/test2
$ mkdir -p /tmp/test2/subtest
```

`rmdir`: Used to remove empty directories

Common options

`-p` will remove parent directories if the contain only the path to the directory
being removed.  Recommended that you use this _only_ relative to the current
directory; i.e., `rmdir -p some/path` and never `rmdir -p /some/absolute/path`.

Examples
```
$ rmdir /tmp/test/test2
$ cd /tmp
$ rmdir -p /tmp/test2/subtest
```

### Directory permissions

Directories need to have the execute permission set for the users permitted to be
able to change into the directory.  The group sticky bit, `s`, can be set so
that new files and directories created within a parent will inherit the group
ownership of the parent.  See the `chmod` command below for more information.

## Files and directories

