"""Read BrainVoyager FMR file format."""

import os
import numpy as np
import nibabel as nb
import bvbabel

FILES = [
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_01_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_02_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_03_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_04_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_05_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_06_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_07_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_08_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_09_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_10_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_11_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES2/S07_RUN_12_SCSTBL_MCSPM_LTR_THPGLMF6c_TDTS2.0dp_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_01_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_02_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_03_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_04_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_05_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_06_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_07_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_08_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_09_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_10_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_11_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    "/home/faruk/Documents/temp-aud_bstem/SES3/S07_RUN_12_SCSTBL_3DMCTS_LTR_THPGLMF6c_TDTS2.0dp_FLIRT_TU.fmr",
    ]

# =============================================================================
for i, f in enumerate(FILES):
    print(f"  {i+1}/{len(FILES)}")

    # Load fmr
    header, data = bvbabel.fmr.read_fmr(f)

    # Save nifti for testing
    basename = f.rsplit(".", 1)[0]
    outname = "{}_bvbabel.nii.gz".format(basename)

    # Export nifti (assign an identity matrix as affine with default header)
    img = nb.Nifti1Image(data, affine=np.eye(4))
    nb.save(img, outname)

print("Finished.")
