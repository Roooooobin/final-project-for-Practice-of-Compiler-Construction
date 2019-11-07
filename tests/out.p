ssp 15
ldc i 1
str i 0 0
lod i 0 0
ldc i 1
grt i
fjp l1
lod i 0 0
inc i 1
str i 0 0
ujp l2
l1:
lod i 0 0
dec i 1
str i 0 0
l2:
lod i 0 0
out i
ldc c '\n'
out c
lod i 0 0
ldc i 0
equ i
fjp l3
lod i 0 0
inc i 1
str i 0 0
l3:
lod i 0 0
out i
ldc c '\n'
out c
hlt
