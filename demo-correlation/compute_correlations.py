"""Compute voxel-wise timeseries correlations between two nifti files."""

import os
import nibabel as nb
import numpy as np
from scipy.stats import pearsonr


NII1 = "/Users/faruk/data/proj-phase_jolt_fmri/temp/Smagn_bold.nii.gz"
NII2 = "/Users/faruk/data/proj-phase_jolt_fmri/temp/Sphase_bold_phase_jump.nii.gz"

SUFFIX = "r"

# =============================================================================
print("  Loading data...")
nii1 = nb.load(NII1)
x = nii1.get_fdata()

nii2 = nb.load(NII2)
y = nii2.get_fdata()

# -----------------------------------------------------------------------------
print("  Computing correlations...")

# Calculate means
mean_x = np.mean(x, axis=-1)
mean_y = np.mean(y, axis=-1)

# Calculate numerator and denominators
numerator = np.sum((x - mean_x[..., None]) * (y - mean_y[..., None]), axis=-1)
denominator_x = np.sum((x - mean_x[..., None])**2, axis=-1)
denominator_y = np.sum((y - mean_y[..., None])**2, axis=-1)

# Calculate Pearson correlation coefficient
r = numerator / np.sqrt(denominator_x * denominator_y)

# -----------------------------------------------------------------------------
print("  Saving outputs...")
basename, ext = NII2.split(os.extsep, 1)
out = nb.Nifti1Image(r, affine=nii1.affine, header=nii1.header)
nb.save(out, "{}_{}.{}".format(basename, SUFFIX, ext))


