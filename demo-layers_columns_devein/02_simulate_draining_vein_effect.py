"""Simulate a simplistic draining vein effect on a layer image."""

import os
import numpy as np
import nibabel as nb

# Output nifti from 01_simulate_layers
FILE1 = "/home/faruk/Git/LAYNII_extras/demo-layers_columns_devein/M_brain_simulated_layers.nii.gz"
# Metric file generated by LN2_LAYERS
FILE2 = "/home/faruk/Git/LAYNII_extras/demo-layers_columns_devein/M_brain_rim_metric_equidist.nii.gz"

# Load image data
nii1 = nb.load(FILE1)
data = nii1.get_fdata()

nii2 = nb.load(FILE2)
norm_depth = nii2.get_fdata()  # Normalized cortical depth (0-1)

# Add draining vein effect multiplicatively
vein_multiplier = norm_depth / 10 + 1
data_new = data * vein_multiplier

# Save output
out = nb.Nifti1Image(data_new, affine=nii.affine)
nb.save(out, "/home/faruk/Git/LAYNII_extras/demo-layers_columns_devein/M_brain_draining_veins.nii.gz")
print("Finished.")
