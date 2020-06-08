import os
import nibabel as nb

# This image's position information will be manipulated
nii_source = "/path/to/BOLD_rest.nii"
# This image's position information will be copied
nii_target = "/path/to/T1_rest.nii"

# -----------------------------------------------------------------------------
# Load nifti images
nii1 = nb.load(nii_source)
nii2 = nb.load(nii_target)

# Create a new nifti
new = nb.Nifti1Image(nii1.dataobj, header=nii1.header, affine=nii2.affine())

basename, ext = nii_source.split(os.extsep, 1)
nb.save(new, "{}_headerfix.{}".format(basename, ext))
