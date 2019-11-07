ssp 15
ldc i 0
str i 0 0
ldc i 0
str i 0 4
ldc i 2
str i 0 0
bl1:
lod i 0 0
ldc i 100
leq i
fjp el2
ldc i 2
str i 0 4
bl3:
lod i 0 4
lod i 0 0
les i
fjp el4
lod i 0 0
lod i 0 0
lod i 0 4
div i
lod i 0 4
mul i
sub i
ldc i 0
equ i
fjp l5
ujp el4
l5:
lod i 0 4
inc i 1
str i 0 4
ujp bl3
el4:
lod i 0 4
lod i 0 0
equ i
fjp l7
lod i 0 0
out i
ldc c '\n'
out c
l7:
lod i 0 0
inc i 1
str i 0 0
ujp bl1
el2:
hlt
