"""Separate bold and nulled volumes of an SS-SI-VASO nifti."""

import os
import nibabel as nb
import numpy as np

INPUT = "/Users/faruk/data/temp-renzo_phase_jolt/Sphase_bold_phase_jolt.nii.gz"

# =============================================================================
print("  Loading data...")
nii = nb.load(INPUT)
data = np.asarray(nii.dataobj)

temp = data[..., 0:240]
dims = temp.shape

temp = temp.reshape((dims[0], dims[1], dims[2], 6, 40))

temp = np.mean(temp, axis=3)

# -----------------------------------------------------------------------------
print("  Saving outputs...")
basename, ext = INPUT.split(os.extsep, 1)
out = nb.Nifti1Image(temp, affine=nii.affine, header=nii.header)
nb.save(out, "{}_AVG.{}".format(basename, ext))
