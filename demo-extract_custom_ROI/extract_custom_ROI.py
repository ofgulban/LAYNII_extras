"""Quick way of extracting a subset of voxels from a nifti image."""

import os
import nibabel as nb
import numpy as np

FILE = "/home/faruk/biserver-faruk/temp-ale_greedy/sub-04_sess-01_acq-mp2rage_UNI_denoised_IIHC_res2x_bvbabel_SS_BFC.nii.gz"

# RANGE_X = slice(0, 400)
# RANGE_Y = slice(40, 340)
# RANGE_Z = slice(350, 700)

# =============================================================================
print("  Loading nifti...")
nii = nb.load(FILE)
# data = np.asarray(nii.dataobj[RANGE_X, RANGE_Y, RANGE_Z], dtype=np.ushort)
data = np.asarray(nii.dataobj)

print("  Saving nifti...")
basename, ext = FILE.split(os.extsep, 1)
out = nb.Nifti1Image(data, affine=np.eye(4)*0.35, header=nii.header)

print(np.eye(4)*0.35)

# (Optional fix header voxel size)
out.header["pixdim"][1] = 0.35  # mm
out.header["pixdim"][2] = 0.35  # mm
out.header["pixdim"][3] = 0.35  # mm
out.header.set_data_dtype(np.ushort)

nb.save(out, "{}_fixdim.{}".format(basename, ext))

print("Finished.")
