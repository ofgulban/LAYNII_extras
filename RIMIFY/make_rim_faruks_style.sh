
# input is binary_WMm, binary_CSF, binary_GM


fslmaths binary_CSF.nii.gz -mul 2 -add binary_WMm.nii.gz -add 1 -mul -1 -add 4 rim.nii

