# Some notes about using Pandas

## Merging data

We had a circumstance where there were lines in one dataframe (from
a .csv file) for the same subject, each of which had a variable to
indicate what image was shown.  In a different file, the images were
coded for two traits of the image subject.

The task was to add the two traits columns from the second file to
the first.

This was done with the following sanitized code.
