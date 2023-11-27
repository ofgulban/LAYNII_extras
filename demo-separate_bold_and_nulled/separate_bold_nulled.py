"""Separate bold and nulled volumes of an SS-SI-VASO nifti."""

import os
import nibabel as nb
import numpy as np

INPUT = "/Users/faruk/data/temp-renzo_phase_jolt/Sphase.nii.gz"

# =============================================================================
print("  Loading data...")
nii = nb.load(INPUT)
data = np.asarray(nii.dataobj)

bold = data[..., 0::2]
nulled = data[..., 1::2]

# -----------------------------------------------------------------------------
print("  Saving outputs...")
basename, ext = INPUT.split(os.extsep, 1)
out = nb.Nifti1Image(bold, affine=nii.affine, header=nii.header)
nb.save(out, "{}_bold.{}".format(basename, ext))

out = nb.Nifti1Image(nulled, affine=nii.affine, header=nii.header)
nb.save(out, "{}_nulled.{}".format(basename, ext))
