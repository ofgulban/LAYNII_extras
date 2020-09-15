"""Simulate a simplistic draining vein effect on a layer image."""

import os
import numpy as np
import nibabel as nb

# Output nifti from 01_simulate_layers
FILE1 = "/home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim_metric_equidist_simulated_layers.nii.gz"
# Metric file generated by LN2_LAYERS
FILE2 = "/home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim_metric_equidist.nii.gz"

# Load image data
nii1 = nb.load(FILE1)
data = nii1.get_fdata()

nii2 = nb.load(FILE2)
norm_depth = nii2.get_fdata()  # Normalized cortical depth (0-1)

# Add draining vein effect multiplicatively
vein_multiplier = norm_depth / 10 + 1
data_new = data * vein_multiplier

# Save output
basename, ext = FILE1.split(os.extsep, 1)
out = nb.Nifti1Image(data_new, affine=nii1.affine)
nb.save(out, "{}_draining_veins.{}".format(basename, ext))

# Add Gaussian noise
idx = data_new != 0
noise = np.random.normal(loc=0, scale=2, size=np.sum(idx))
data_new[idx] += noise
out = nb.Nifti1Image(data_new, affine=nii1.affine)
nb.save(out, "{}_brain_draining_veins_noised.{}".format(basename, ext))

print("Finished.")
