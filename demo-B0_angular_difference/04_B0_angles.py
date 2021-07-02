"""Use LN2_LAYERS -steamlines output to compute B0 angular differences."""

import os
import numpy as np
import nibabel as nb

# File with scanner space affine transform
B0_REF = "/path/to/my_mp2rage.nii.gz"

# Vector file
STREAMLINES = "/path/to/mymp2rage_rim_streamline_vectors.nii.gz"

# Output directory
OUTDIR = "/path/to/my_results"

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
    print("  Output directory: {}\n".format(OUTDIR))


# Load nifti
nii1 = nb.load(REF)
data = np.asarray(nii1.dataobj)
idx = data != 0
dims = nii1.shape

# Affine
aff = nii1.affine
aff = np.linalg.inv(aff)

ref = np.array([[0, 0, 0], [0, 0, 1]])
new = nb.affines.apply_affine(aff, ref)
new = new[1, :] - new[0, :]
new /= np.linalg.norm(new)

# Prepare 4D nifti
vec_B0 = np.zeros(dims + (3,))
vec_B0[..., 0] = new[0]
vec_B0[..., 1] = new[1]
vec_B0[..., 2] = new[2]
vec_B0[~idx, :] = 0

# Save
filename = os.path.basename(REF)
basename, ext = filename.split(os.extsep, 1)
outname = os.path.join(OUTDIR, "{}_B0vector.{}".format(basename, ext))
img = nb.Nifti1Image(vec_B0, affine=nii1.affine, header=nii1.header)
nb.save(img, outname)

# -----------------------------------------------------------------------------
# Load vector nifti
nii2 = nb.load(STREAMLINES)
vec_local = np.asarray(nii2.dataobj)

# Angular difference
term1 = np.sum(vec_B0 ** 2., axis=-1)
term2 = np.sum(vec_local ** 2., axis=-1)
temp_dot = np.sum(vec_B0 * vec_local, axis=-1)
temp_angle = np.arccos(temp_dot / np.sqrt(term1 * term2))
temp_angle = temp_angle * 180 / np.pi;
temp_angle[~idx] = 0
temp_angle[np.isnan(temp_angle)] = 0
temp_angle[idx] = 90 - np.abs(temp_angle[idx] - 90)

# Save
filename = os.path.basename(STREAMLINES)
basename, ext = filename.split(os.extsep, 1)
outname = os.path.join(OUTDIR, "{}_B0angdif.{}".format(basename, ext))
img = nb.Nifti1Image(temp_angle, affine=nii1.affine, header=nii1.header)
nb.save(img, outname)

print("Finished.")
