ssp 15
ldc i 3
str i 0 0
ldc i 4
str i 0 4
lod i 0 0
lod i 0 0
ldc i 2
div i
ldc i 2
mul i
sub i
ldc i 1
equ i
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
hlt
