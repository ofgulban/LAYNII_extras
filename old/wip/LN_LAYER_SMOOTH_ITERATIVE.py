"""Rudimentary reimplementation of layer smoothing from LAYNII

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_LAYER_SMOOTH.cpp
"""

import os
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter


def iterative_gauss_n(sigma_small, sigma_large):
    """Compute iterations of small sigma which is equal to using big sigma."""
    return int((sigma_large / sigma_small)**2.)


# =============================================================================
# User defined parameters
NII1 = "/home/faruk/data/DATA_MRI_NIFTI/derived/sub-05/T1_wholebrain/99_B0_angles/sub-05_ses-T2s_MP2RAGE_uni_segm_rim_reg_v06_rim_B0angdif.nii.gz"
NII2 = "/home/faruk/data/DATA_MRI_NIFTI/derived/sub-05/T1_wholebrain/99_B0_angles/sub-05_ses-T2s_MP2RAGE_uni_segm_rim_reg_v06_rim_GM.nii.gz"

SIGMA_LARGE = 2  # Sigma of gaussian filter
SIGMA_SMALL = 1
NR_ITER = iterative_gauss_n(SIGMA_SMALL, SIGMA_LARGE)
print("Nr. iterations is {}".format(NR_ITER))
# =============================================================================
# Load data
nii = nb.load(NII1)
data = nii.get_fdata()
data_layers = np.asarray((nb.load(NII2).dataobj))

# Derive parameters
dims = data.shape
layers = np.unique(data_layers)
basename = NII1.split(os.extsep, 1)[0]

# =============================================================================
# Iterative masked Gaussian filter
for i in range(NR_ITER):
    print("Iteration: {}".format(i))
    data_new = np.zeros(dims)
    for l in layers:
        idx_nonzero = data_layers == l
        mask = (idx_nonzero).astype("float")
        data_smooth = gaussian_filter(data * mask, sigma=SIGMA_SMALL)
        mask_smooth = gaussian_filter(mask, sigma=SIGMA_SMALL)
        data_new[idx_nonzero] += data_smooth[idx_nonzero] / mask_smooth[idx_nonzero]
    data = np.copy(data_new)

# Save
out = nb.Nifti1Image(data, affine=nii.affine)
nb.save(out, "{}_layer_smooth_sigma{}_iter{}.nii.gz".format(
    basename, int(SIGMA_LARGE), int(NR_ITER)))

print("Finished.")
