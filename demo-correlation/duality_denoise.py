"""Compute voxel-wise timeseries correlations between two nifti files."""

import os
import nibabel as nb
import numpy as np
from scipy.stats import pearsonr


NII1 = "/Users/faruk/data/proj-phase_jolt_fmri/temp/sub-3003_ses-fast_task-fncloc_run-1_part-mag_bold.nii.gz"
NII2 = "/Users/faruk/data/proj-phase_jolt_fmri/temp/sub-3003_ses-fast_task-fncloc_run-1_part-phase_bold_phase_jolt.nii.gz"


# =============================================================================
print("  Loading data...")
nii1 = nb.load(NII1)
x = nii1.get_fdata()

nii2 = nb.load(NII2)
y = nii2.get_fdata()

# -----------------------------------------------------------------------------
print("  Z scoring...")
mean_x = np.mean(x, axis=-1)
std_x = np.std(x, axis=-1)
z_score_x = (x - mean_x[..., None]) / std_x[..., None]

mean_y = np.mean(y, axis=-1)
std_y = np.std(y, axis=-1)
z_score_y = (y - mean_y[..., None]) / std_y[..., None]

# -----------------------------------------------------------------------------
print("  Computing residual...")
residual = z_score_x + z_score_y
denoised = z_score_x - residual
denoised = denoised * std_x[..., None] + mean_x[..., None]

# -----------------------------------------------------------------------------
print("  Saving outputs...")
basename, ext = NII2.split(os.extsep, 1)
out = nb.Nifti1Image(residual, affine=nii2.affine, header=nii2.header)
nb.save(out, "{}_residual.{}".format(basename, ext))

out = nb.Nifti1Image(denoised, affine=nii2.affine, header=nii2.header)
nb.save(out, "{}_denoised.{}".format(basename, ext))

print("Finished.")
