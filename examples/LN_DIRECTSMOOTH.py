"""Rudimentary reimplementation of directional smoothing from LAYNII.

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_DIRECTSMOOTH.cpp
"""

import os
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter

# =============================================================================
# User defined parameters
NII = "/home/faruk/Git/PyLAYNII/sample_data/activity_map_example.nii.gz"

SIGMA = 5.0
AXIS = 2  # Can be 0=X, 1=Y, 2=Z
# =============================================================================
# Load data
nii = nb.load(NII)
data = nii.get_fdata()

# Derive parameters
basename = NII.split(os.extsep, 1)[0]
# =============================================================================
# Directional Gaussian filter
sigmas = np.zeros(3)
sigmas[AXIS] = SIGMA
data_smooth = gaussian_filter(data, sigma=sigmas)

# Save
out_img = nb.Nifti1Image(data_smooth, affine=nii.affine)
out_name = "{}_smooth_axis{}_sigma{}.nii.gz".format(
    basename, int(AXIS), int(SIGMA))
nb.save(out_img, out_name)

print("Finished.")
