ssp 15
ldc i 0
str i 0 0
ldc i 100
str i 0 0
bl1:
lod i 0 0
ldc i 1000
les i
fjp el2
lod i 0 0
ldc i 100
div i
str i 0 4
lod i 0 0
ldc i 10
div i
lod i 0 0
ldc i 10
div i
ldc i 10
div i
ldc i 10
mul i
sub i
str i 0 8
lod i 0 0
lod i 0 0
ldc i 10
div i
ldc i 10
mul i
sub i
str i 0 12
lod i 0 4
ldc i 100
mul i
lod i 0 8
ldc i 10
mul i
add i
lod i 0 12
add i
lod i 0 4
lod i 0 4
mul i
lod i 0 4
mul i
lod i 0 8
lod i 0 8
mul i
lod i 0 8
mul i
add i
lod i 0 12
lod i 0 12
mul i
lod i 0 12
mul i
add i
equ i
fjp l3
lod i 0 0
out i
ldc c '\n'
out c
l3:
lod i 0 0
inc i 1
str i 0 0
ujp bl1
el2:
hlt
