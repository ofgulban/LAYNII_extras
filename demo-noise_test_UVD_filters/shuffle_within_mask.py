"""Shuffle voxel within a mask."""

import os
import numpy as np
import nibabel as nb

# Values
NII1 = "/home/faruk/data2/test_LN2_UVD_FILTERS/sub-04_ses-T2s_part-mag_MEGRE_crop_ups2X_prepped_avg_composite_decayfixed_T2s.nii.gz"

# Mask
NII2 = "/home/faruk/data2/test_LN2_UVD_FILTERS/sub-04_ses-T2s_segm_rim_CS_LH_v02_perimeter_chunk.nii.gz"

# -----------------------------------------------------------------------------
# Load data
nii1 = nb.load(NII1)
data = np.asarray(nii1.dataobj)

nii2 = nb.load(NII2)
mask = np.asarray(nii2.dataobj)

# Shuffle voxels within mask
idx = mask > 0
temp = data[idx]
np.random.shuffle(temp)
data[idx] = temp

# Save output
basename, ext = NII1.split(os.extsep, 1)
out = nb.Nifti1Image(data, affine=nii1.affine, header=nii1.header)
nb.save(out, "{}_shuffled.{}".format(basename, ext))

print("Finished.")
