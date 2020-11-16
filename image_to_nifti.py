"""Read 2D image to create nifti."""

import os
import nibabel as nb
import numpy as np
import cv2
from scipy.ndimage import zoom

# =============================================================================
# Parameters
PNG_FILE = "/path/to/image.png"

DOWNSAMPLING_FACTOR = 1/2

# =============================================================================
# Load png
data_in = cv2.imread(PNG_FILE)
data_in = np.asarray(data_in, dtype=float)
# Convert to grayscale (average R, G, B channels)
data_in = np.mean(data_in, axis=-1)
# Downsample
data_out = zoom(data_in, DOWNSAMPLING_FACTOR, mode="nearest",
                prefilter=False)
# Transpose
data_out = data_out[::-1, ::-1].T
# Save as Nifti
img = nb.Nifti1Image(data_out, affine=np.eye(4))
nb.save(img, "{}.nii.gz".format(os.path.splitext(PNG_FILE)[0]))
