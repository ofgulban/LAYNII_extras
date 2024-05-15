"""Quick way of extracting a subset of voxels from a nifti image."""

import os
import nibabel as nb
import numpy as np

FILE = "/Users/faruk/data/demo-Tubingen/demo-bigbrain100um/segmentation_bigbrain_100um_occipital.nii.gz"

RANGE_X = slice(0, 400)
RANGE_Y = slice(40, 340)
RANGE_Z = slice(350, 700)

# =============================================================================
print("  Loading nifti...")
nii = nb.load(FILE)
data = np.asarray(nii.dataobj[RANGE_X, RANGE_Y, RANGE_Z], dtype=np.ushort)

print("  Saving nifti...")
basename, ext = FILE.split(os.extsep, 1)
out = nb.Nifti1Image(data, affine=nii.affine/10, header=nii.header)

# (Optional fix header voxel size)
out.header["pixdim"][1] = 0.1  # mm
out.header["pixdim"][2] = 0.1  # mm
out.header["pixdim"][3] = 0.1  # mm
out.header.set_data_dtype(np.ushort)

nb.save(out, "{}_roi.{}".format(basename, ext))

print("Finished.")
