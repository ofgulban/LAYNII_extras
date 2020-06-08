import os
import nibabel as nb

nii_source = "/home/faruk/gdrive/data/toy_models/laynii_tests/copy_geom_example/another_exampls/180223_BOLD_rest.nii"
nii_target = "/home/faruk/gdrive/data/toy_models/laynii_tests/copy_geom_example/another_exampls/180223_T1_rest.nii"

# Load nifti images
nii1 = nb.load(nii_source)
nii2 = nb.load(nii_target)

# Create a new nifti
new = nb.Nifti1Image(nii1.dataobj, header=nii1.header, affine=nii2.affine())

basename, ext = nii_source.split(os.extsep, 1)
nb.save(new, "{}_headerfix.{}".format(basename, ext))
