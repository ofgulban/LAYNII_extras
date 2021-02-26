#!/bin/bash

# vector of magnetic field
x1=0
y1=0
z1=-1 

3dcalc -a $1'[0]' -b $1'[1]' -c $1'[2]' -overwrite -prefix angle.nii \
       -expr 'int(30 / 3.14159 * acos(('`expr $x1 `'*a+'`expr $y1 `'*b+'`expr $z1 `'*c)/(sqrt('`expr $x1 `'*'`expr $x1 `'+'`expr $y1 `'*'`expr $y1 `'+'`expr $z1 `'*'`expr $z1`' )*sqrt(a*a+b*b+c*c))))' 

3dcalc -a layers.nii -d angle.nii -overwrite -prefix angle.nii \
       -expr 'equals(a,2)*d' 

LN_LAYER_SMOOTH -layer_file layers.nii -input angle.nii -FWHM 1


3dcalc -a smoothed_angle.nii -overwrite -prefix angle.nii \
       -expr 'int(a)' 
#3dhistog -mask rim.nii -omit 1.5707963705062866 -nbin 50 -prefix output angle.nii


#get mean value
3dROIstats -mask angle.nii -1DRformat -quiet -nzmean $2 > dist_t.dat
#get standard deviation
3dROIstats -mask angle.nii -1DRformat -quiet -sigma $2 >> dist_t.dat
#get number of voxels in each layer
3dROIstats -mask angle.nii -1DRformat -quiet -nzvoxels $2 >> dist_t.dat
#format file to be in columns, so gnuplot can read it.
WRD=$(head -n 1 dist_t.dat|wc -w); for((i=2;i<=$WRD;i=i+2)); do awk '{print $'$i'}' dist_t.dat| tr '\n' ' ';echo; done > dist.dat

 
1dplot -sepscl dist.dat 


mv dist.dat ${2}_dist.txt
