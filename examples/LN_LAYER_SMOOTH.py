"""Reimplementation of layer smoothing from LAYNII

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_LAYER_SMOOTH.cpp
"""

import os
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter

# =============================================================================
# User defined parameters
NII1 = "/home/faruk/Git/PyLAYNII/sample_data/activity_map_example.nii.gz"
NII2 = "/home/faruk/Git/PyLAYNII/sample_data/equi_dist_layers.nii.gz"

SIGMA = 20.  # Sigma of gaussian filter
# =============================================================================
# Load data
nii = nb.load(NII1)
data = nii.get_fdata()
data_layers = nb.load(NII2).get_fdata()

# Derive parameters
dims = data.shape
layers = np.unique(data_layers)
basename = NII1.split(os.extsep, 1)[0]

# =============================================================================
# Masked Gaussian filter
data_new = np.zeros(dims)
for l in layers:
    idx_nonzero = data_layers == l
    mask = (idx_nonzero).astype("float")
    data_smooth = gaussian_filter(data * mask, sigma=SIGMA)
    mask_smooth = gaussian_filter(mask, sigma=SIGMA)
    data_new[idx_nonzero] += data_smooth[idx_nonzero] / mask_smooth[idx_nonzero]

# Save
out = nb.Nifti1Image(data_new, affine=nii.affine)
nb.save(out, "{}_layer_smooth_sigma{}.nii.gz".format(basename, int(SIGMA)))

print("Finished.")
