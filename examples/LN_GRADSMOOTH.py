"""Reimplementation of gradient based smoothing from LAYNII

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_GRADSMOOTH.cpp
"""

import os
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter
from numpy.linalg import eigh

# =============================================================================
# User defined parameters
NII1 = "/home/faruk/Git/PyLAYNII/sample_data/activity_map_example.nii.gz"
NII2 = "/home/faruk/Git/PyLAYNII/sample_data/activity_map_example.nii.gz"

# =============================================================================
# Load data
nii1 = nb.load(NII1)
data1 = nii1.get_fdata()
nii2 = nb.load(NII2)
data2 = nii2.get_fdata()

# Derive parameters
dims = data1.shape
nr_vox = np.prod(dims)
basename = NII2.split(os.extsep, 1)[0]

# =============================================================================
grad = np.transpose(np.asarray(np.gradient(data1)), (1, 2, 3, 0))
grad = np.reshape(grad, (nr_vox, 3))
struct = np.multiply(grad[:, None, :], grad[:, :, None])

eigvals, eigvecs = eigh(struct)


eigvecs.shape


# Masked Gaussian filter
# data_new = np.zeros(dims)
# for l in layers:
#     idx_nonzero = data_layers == l
#     mask = (idx_nonzero).astype("float")
#     data_smooth = gaussian_filter(data * mask, sigma=SIGMA)
#     mask_smooth = gaussian_filter(mask, sigma=SIGMA)
#     data_new[idx_nonzero] += data_smooth[idx_nonzero] / mask_smooth[idx_nonzero]
#
# # Save
# out = nb.Nifti1Image(data_new, affine=nii.affine)
# nb.save(out, "{}_layer_smooth_sigma{}.nii.gz".format(basename, int(SIGMA)))
#
# print("Finished.")
