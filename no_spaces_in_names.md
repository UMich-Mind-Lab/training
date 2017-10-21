# Why spaces are not good in names

When you type something on the command line, spaces are interpreted as separators.
They separate options from each other, but they are also used to separate the
items in a list.  This presents a problem if there are spaces in the path to
a file.  The name
```
./MTwiNS/MT_1/MRI Tasks/Twin 1/1_faces_t1.edat2
```
if given to a program will be interpreted as three things, not one.
```
./MTwiNS/MT_1/MRI
Tasks/Twin
1/1_faces_t1.edat2
```
and that is almost certainly never what you want.  You can get around this
in some circumstances by using quotes, as in
```
ls "./MTwiNS/MT_1/MRI Tasks/Twin 1"
```
but that does not help you when you need to gather the names in the first
place, as in
```
for twin in $(./MTwiNS/MT_1/MRI Tasks) ; do
    ls $twin
done
```
Go ahead.  Try all your tricks to make that work!  There are ways to do it,
but they are probably more painful than not using spaces in directory or
filenames.

Whether you agree or not, the rest of this assumes that spaces are bad in
names, and we will seek to expunge them.  We will also assume that you
have folders and files that look like this.
```
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
