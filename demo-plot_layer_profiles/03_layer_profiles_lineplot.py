"""Plot simple layer profiles using the LayNii LN2_LAYERS outputs."""

import numpy as np
import nibabel as nb
import matplotlib.pyplot as plt

# Cortical depth file. This can be metric_equidist or metric_equivol
NII_METRIC = "/Users/faruk/data/video-scottlee/aseg_rim_metric_equidist.nii.gz"

# Region-of-interest (ROI) mask
NII_ROI = "/Users/faruk/data/video-scottlee/rFFA_FWE05_resliced_GMmasked.nii.gz"

# Scalar map, this can be your fMRI activation maps
NII_SCALAR = "/Users/faruk/data/video-scottlee/con_002_resliced.nii.gz"
MAP_INDEX = 0

TITLE = "Line plot\nCortical depth layer profile"

NR_LAYERS = 21

# =============================================================================
# Load mask data first
nii_roi = nb.load(NII_ROI)
mask = np.asarray(nii_roi.dataobj, dtype=int)

# Load data
nii_metric = nb.load(NII_METRIC)
data_x = nii_metric.get_fdata()

nii_scalar = nb.load(NII_SCALAR)
if len(nii_scalar.shape) > 3:
	data_y = nii_scalar.get_fdata()[..., MAP_INDEX]
else:
	data_y = nii_scalar.get_fdata()

# Only take the voxels within the ROI mask
data_x = data_x[mask != 0]
data_y = data_y[mask != 0]

# Quantize the metric file into integer layers
data_x = data_x * NR_LAYERS
data_x = data_x.astype(int)
data_x_bins = np.arange(1, NR_LAYERS + 1)

# Average across bins
data_y_mean = np.zeros(NR_LAYERS)
for i in range(NR_LAYERS):
	data_y_mean[i] = np.mean(data_y[data_x == i])

# =============================================================================
# Plot
plt.plot(data_x_bins, data_y_mean)
plt.xlim((1, NR_LAYERS))
plt.xticks(np.arange(1, NR_LAYERS+1, 1))
plt.ylim(np.percentile(data_y, (1, 99)))
plt.xlabel("Normalized cortical depth (0 = White matter)")
plt.ylabel("Voxel value")
plt.title(TITLE)

plt.show()

print("Finished.")