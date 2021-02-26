#!/bin/bash

# vector of magnetic field
x1=0
y1=0
z1=0 


min=100
max=131

#x1= awk 'BEGIN{print sin('`expr $min `')}'

for i in $(eval echo "{$min..$max}")
do
3dcalc -a $1'[1]' -b $1'[2]' -c $1'[0]' -overwrite -prefix rotating_${i}.nii \
       -expr 'int(30 / 3.14159 * acos((sin('`expr $i `'/5)*a+cos('`expr $i `'/5)*b+'`expr $z1 `'*c)/(sqrt(sin('`expr $i `'/5)*sin('`expr $i `'/5)+cos('`expr $i `'/5)*cos('`expr $i `'/5)+'`expr $z1 `'*'`expr $z1`' )*sqrt(a*a+b*b+c*c))))' 

done 


fslmerge -t roating.nii rotating_*.nii

3dcalc -a roating.nii'[0]' -b layers.nii -expr 'step(a)*equals(b,2)' -prefix masked_layers.nii  -overwrite

LN_LAYER_SMOOTH -layer_file masked_layers.nii -input roating.nii -FWHM 1 -mask
