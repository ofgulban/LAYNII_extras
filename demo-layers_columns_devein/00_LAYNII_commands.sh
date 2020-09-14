# Initial inputs
# -M_brain_rim.nii.gz
# -M_brain_activity.nii.gz

# Generate layers
./LN2_LAYERS -rim /home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim.nii.gz

# Generate columns
./LN2_COLUMNS -rim ./LN2_LAYERS -rim /home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim.nii.gz -midgm /home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim_midGM_equidist.nii.gz -nr_columns 33

# Devein
