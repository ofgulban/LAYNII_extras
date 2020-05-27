
3dcalc -a Ding_FLASH80_out_03.nii -b a+i -c a-i -d a+j -e a-j -f a+k -g a-k -expr 'ispositive(a)*amongst(0,b,c,d,e,f,g)' -prefix pial.nii -overwrite
3dcalc -a Ding_FLASH80_wm_05.nii -b a+i -c a-i -d a+j -e a-j -f a+k -g a-k -expr 'ispositive(a)*amongst(0,b,c,d,e,f,g)' -prefix wm.nii -overwrite
3dcalc -a Ding_FLASH80_wm_05.nii -b Ding_FLASH80_out_03.nii -expr 'step (1-a-b)' -prefix inner.nii
