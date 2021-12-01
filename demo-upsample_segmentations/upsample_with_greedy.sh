
REFERENCE="/path/to/higher_res_data.nii.gz"
INPUT="/path/to/rim.nii.gz"
OUTPUT="/path/to/rim_out.nii.gz"
AFFINE="eye.mat"

greedy -d 3 -rf ${REFERENCE} -ri LABEL 0.5mm -rm ${INPUT} ${OUTPUT} -r ${AFFINE} 
