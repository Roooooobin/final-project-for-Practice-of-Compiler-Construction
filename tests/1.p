ssp 15
ldc i 1
str i 0 0
lod i 0 0
inc i 1
str i 0 0
bl1:
lod i 0 0
ldc i 5
les i
not
fjp el2
lod i 0 0
inc i 1
str i 0 0
ujp bl1
el2:
lod i 0 0
out i
ldc c '\n'
out c
hlt
