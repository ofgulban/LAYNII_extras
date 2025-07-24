"""Do opening closing operations on binary (0s and 1s) nifti data."""

import os
from scipy.ndimage import (morphology, generate_binary_structure,
                           binary_propagation)
from nibabel import load, save, Nifti1Image
import numpy as np

# User inputs
INPUT_FILE = "/path/to/binary_nifti_file.nii.gz"
SUFFIX = "close"

# =============================================================================
# Load data
nii = load(INPUT_FILE)
basename, ext = nii.get_filename().split(os.extsep, 1)
dirname = os.path.dirname(nii.get_filename())
orig = np.asarray(nii.dataobj)
data = np.asarray(nii.dataobj)

# -----------------------------------------------------------------------------
# Form morphology structure
struct = generate_binary_structure(3, 1)  # 1 jump neighbourbhood
# struct = generate_binary_structure(3, 3)  # 3 jump neighbourbhood

# Perform closing
data = morphology.binary_dilation(data, structure=struct, iterations=1)
data = morphology.binary_erosion(data, structure=struct, iterations=1)

# Perform opening
# data = morphology.binary_erosion(data, structure=struct, iterations=1)
# data = morphology.binary_dilation(data, structure=struct, iterations=1)

# -----------------------------------------------------------------------------
# Save as nifti
print('Saving...')
out = Nifti1Image(data.astype(int), header=nii.header, affine=nii.affine)
save(out, "{}_{}.{}".format(basename, SUFFIX, ext))

print('Finished.')
