ssp 15
ldc i 0
str i 0 0
ldc i 0
str i 0 4
lod i 0 0
in i
str i 0 0
lod i 0 4
in i
str i 0 4
lod i 0 0
lod i 0 4
mul i
str i 0 8
lod i 0 0
lod i 0 4
grt i
fjp l1
lod i 0 0
lod i 0 4
add i
str i 0 0
lod i 0 0
lod i 0 4
sub i
str i 0 4
lod i 0 0
lod i 0 4
sub i
str i 0 0
l1:
bl3:
lod i 0 0
ldc i 0
neq i
fjp el4
lod i 0 0
str i 0 12
lod i 0 4
lod i 0 4
lod i 0 0
div i
lod i 0 0
mul i
sub i
str i 0 0
lod i 0 12
str i 0 4
ujp bl3
el4:
lod i 0 8
lod i 0 4
div i
out i
ldc c '\n'
out c
hlt
