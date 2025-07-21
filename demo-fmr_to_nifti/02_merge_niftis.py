"""Merge timeseries after z scoring and adding back the mean image."""

import os
import numpy as np
import nibabel as nb
import bvbabel

# =============================================================================
# FILES = [
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_01_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_02_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_03_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_04_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_05_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_06_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_07_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_08_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_09_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_10_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_11_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_12_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU_bvbabel.nii.gz",
#     ]

# OUTNAME = "/home/faruk/Documents/temp-aud_bstem/SES2/S07_ALLRUNS_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.nii.gz"

# =============================================================================
FILES = [
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_01_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_02_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_03_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_04_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_05_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_06_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_07_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_08_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_09_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_10_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_11_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_12_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU_bvbabel.nii.gz",
    ]

OUTNAME = "/home/faruk/Documents/temp-aud_bstem/SES3/S07_ALLRUNS_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.nii.gz"

# =============================================================================
nr_runs = len(FILES)
nii_ref = nb.load(FILES[0])
dims = tuple(nii_ref.shape)
nr_volumes = dims[3]
dims_new = dims[0], dims[1], dims[2], dims[3]*nr_runs
data_new = np.zeros(dims_new)
data_mean = np.zeros((dims[0], dims[1], dims[2]))

for i, f in enumerate(FILES):
    print(f"  {i+1}/{nr_runs}")

    # Load nifti
    nii = nb.load(f)
    data = np.asarray(nii.dataobj)

    # Z score
    mean = np.mean(data, axis=-1)
    std = np.std(data, axis=-1)
    data = (data - mean[..., None]) / std[..., None]

    # Accumulate means
    data_mean += mean

    # Add to new array
    data_new[:, :, :, nr_volumes*i:nr_volumes*i+nr_volumes] = data

# Add back mean to translate values
print("  Adding back time mean over all runs...")
data_mean /= nr_runs
data_new += data_mean[..., None]

# Export nifti (assign an identity matrix as affine with default header)
print("  Saving...")
img = nb.Nifti1Image(data_new, affine=np.eye(4))
nb.save(img, OUTNAME)

print("Finished.")
