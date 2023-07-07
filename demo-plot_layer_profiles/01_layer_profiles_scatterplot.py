"""Plot simple layer profiles using the LayNii LN2_LAYERS outputs."""

import numpy as np
import nibabel as nb
import matplotlib.pyplot as plt

# Cortical depth file. This can be metric_equidist or metric_equivol
NII_METRIC = "/Users/faruk/data/video/new/04-plot_layer_profile/segmentation_rim-05_polished_metric_equivol.nii.gz"

# Region-of-interest (ROI) mask
NII_ROI = "/Users/faruk/data/video/new/04-plot_layer_profile/segmentation_rim-05_polished_perimeter_chunk.nii.gz"

# Scalar map, this can be your fMRI activation maps
NII_SCALAR = "/Users/faruk/data/video/new/04-plot_layer_profile/stats_task_unwarp_3X_NN.nii.gz"
MAP_INDEX = 0

TITLE = "Scatter plot\nEquivolume cortical depth layer profile"

# =============================================================================
# Load mask data first
nii_roi = nb.load(NII_ROI)
mask = np.asarray(nii_roi.dataobj, dtype=int)

# Load data
nii_metric = nb.load(NII_METRIC)
data_x = nii_metric.get_fdata()

nii_scalar = nb.load(NII_SCALAR)
data_y = nii_scalar.get_fdata()[..., MAP_INDEX]

# Only take the voxels within the ROI mask
data_x = data_x[mask != 0]
data_y = data_y[mask != 0]

# =============================================================================
# Plot
plt.scatter(data_x, data_y, alpha=0.01, marker=".", color="black")
plt.xlim((0, 1))
plt.ylim(np.percentile(data_y, (1, 99)))
plt.xlabel("Normalized cortical depth (0 = White matter)")
plt.ylabel("Voxel value")
plt.title(TITLE)

plt.show()

print("Finished.")