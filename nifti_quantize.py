"""Read nifti and arbitrarily quantize the values."""

import os
import nibabel as nb
import numpy as np

# =============================================================================
# Parameters
NII_FILE = "/path/to/image.nii.gz"

# =============================================================================
# Load png
nii = nb.load(NII_FILE)
data = np.asarray(nii.dataobj)
# Quantize
idx1 = data > 175
idx2 = data > 125
idx3 = data > 25
idx4 = data == 0
data[idx4] = 0
data[idx3] = 100
data[idx2] = 150
data[idx1] = 200
# Save as Nifti
img = nb.Nifti1Image(data, affine=np.eye(4))
basename, ext = NII_FILE.split(os.extsep, 1)
nb.save(img, "{}_quantized.{}".format(basename, ext))
