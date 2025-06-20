"""Substitude one nifti header with another.

This is useful to fix corrupted nifti headers.
"""

import os
import nibabel as nb

# Nifti with correct header
INPUT1 = "/Users/faruk/data/video-Alejandro/mean_msk.nii"

# Nifti with incorrect header
INPUT2 = "/Users/faruk/data/video-Alejandro/sb_01_DS_SO_08mm_tra_mc_hpf.nii"

# =============================================================================
# Load nifti
nii1 = nb.load(INPUT1)
nii2 = nb.load(INPUT2)

# Create new nifti image
nii_out = nb.Nifti1Image(nii2.dataobj, header=nii1.header, affine=nii1.affine)

# Save
basename, ext = INPUT2.split(os.extsep, 1)
outname = "{}_hdrfixed.{}".format(basename, ext)
nb.save(nii_out, outname)

print("Finished.")