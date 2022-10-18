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

