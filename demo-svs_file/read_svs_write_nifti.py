"""SVS file format is used in microscipy images."""

import os
import openslide
import nibabel as nb
import numpy as np

FILE = "/home/faruk/gdrive/collaborations/Onur_Gokturk/original_image.svs"

OUTDIR = "/home/faruk/Documents/temp-svs_file/"
NAME = "slice_data"

LEVEL = 3

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
    print("  Output directory: {}\n".format(OUTDIR))

# -----------------------------------------------------------------------------
# Open the SVS file
slide = openslide.OpenSlide(FILE)

# Get slide dimensions
width, height = slide.dimensions
print(f"Base dimensions: {width} x {height}")

# Specify region coordinates and level
level_width, level_height = slide.level_dimensions[LEVEL]
print(f"Level dimensions: {level_width} x {level_height}")

# Read the region from the slide
data = slide.read_region((0, 0), LEVEL, (level_width, level_height))

# Convert the image mode from RGBA to RGB
data = data.convert("RGB")

# Save the region as a JPEG image
outpath = os.path.join(OUTDIR, f"{NAME}_level-{LEVEL}.jpg")
data.save(outpath)

# Close the slide
slide.close()

# -----------------------------------------------------------------------------
# Convert to numpy array
data = np.asarray(data)

# Convert to grayscale
data = np.mean(data, axis=-1)

# Transform the data axes to look the same orientation as in ITKSNAP as in JPEG
data = data.T[::-1, ::-1]

# Save as nifti file
img = nb.Nifti1Image(data, affine=np.eye(4))
outpath = os.path.join(OUTDIR, f"{NAME}_level-{LEVEL}.nii.gz")
nb.save(img, outpath)

print("Finished.")
