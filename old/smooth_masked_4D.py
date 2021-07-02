"""Rudimentary reimplementation of layer smoothing from LAYNII

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_LAYER_SMOOTH.cpp
"""

import os
import argparse
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter

# Input
NII1 = "/home/faruk/data/DATA_MRI_NIFTI/derived/sub-04/T1_wholebrain/99_B0_angles/sub-04_ses-T2s_MP2RAGE_uni_segm_rim_reg_v16_rim_streamline_vectors.nii.gz"
# Layers
NII2 = "/home/faruk/data/DATA_MRI_NIFTI/derived/sub-04/T1_wholebrain/99_B0_angles/sub-04_ses-T2s_MP2RAGE_uni_segm_rim_reg_v16_rim.nii.gz"
# Full width half maximum of Gaussian kernel. In voxel size units
FWHM = 20

# =========================================================================
# Parameters
SIGMA = FWHM / 2.35482004503
basename = NII1.split(os.extsep, 1)[0]
OUT_NAME = "{}_maskedsmooth_FWHM{}.nii.gz".format(
    basename, str(FWHM).replace('.', 'pt'))

print("Selected FWHM: {}".format(FWHM))
print("Output path: {}".format(OUT_NAME))

# =========================================================================
# Load data
nii = nb.load(NII1)
data = nii.get_fdata()
data_layers = np.asarray((nb.load(NII2).dataobj))

# Derive parameters
dims = data.shape
layers = np.unique(data_layers)

# Masked Gaussian filter
data_new = np.zeros(dims)
for t in dims[3]:
    for l in layers:
        idx_nonzero = data_layers == l
        mask = (idx_nonzero).astype("float")
        data_smooth = gaussian_filter(data[..., t] * mask, sigma=SIGMA)
        mask_smooth = gaussian_filter(mask, sigma=SIGMA)
        data_new[idx_nonzero] += (
            data_smooth[idx_nonzero] / mask_smooth[idx_nonzero])

# Save output image as nifti
out = nb.Nifti1Image(data_new, affine=nii.affine)
nb.save(out, OUT_NAME)

print("Finished.")
