
# input is binary_WMm, binary_CSF, binary_GM


3dcalc -a binary_CSF.nii -b a+i -c a-i -d a+j -e a-j -f a+k -g a-k -expr 'ispositive(a)*amongst(0,b,c,d,e,f,g)' -prefix pial.nii -overwrite
3dcalc -a binary_WMm.nii -b a+i -c a-i -d a+j -e a-j -f a+k -g a-k -expr 'ispositive(a)*amongst(0,b,c,d,e,f,g)' -prefix wm.nii -overwrite
3dcalc -a pial.nii -b wm.nii -c binary_GM.nii -preifx rim.nii -overwrite -expr 'a+2*c+3*b' 
