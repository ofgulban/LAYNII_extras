"""Quick way of extracting a subset of voxels from a nifti image."""

import os
import nibabel as nb
import numpy as np

FILE = "/Users/faruk/data/test-JV_FRANGI/test-ssfmri_timeseries.nii.gz"

RANGE_X = slice(0, -1)
RANGE_Y = slice(0, -1)
RANGE_Z = slice(0, -1)
RANGE_T = slice(0, 2)

# =============================================================================
print("  Loading nifti...")
nii = nb.load(FILE)
data = np.asarray(nii.dataobj[RANGE_X, RANGE_Y, RANGE_Z, RANGE_T])

print("  Saving nifti...")
basename, ext = FILE.split(os.extsep, 1)
out = nb.Nifti1Image(data, affine=nii.affine, header=nii.header)

nb.save(out, "{}_roi.{}".format(basename, ext))

print("Finished.")
