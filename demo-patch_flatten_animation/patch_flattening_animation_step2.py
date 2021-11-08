"""Used in thingsonthings.org LN2_MULTILATERATE blog post."""

import os
import numpy as np
import pyvista as pv
import nibabel as nb

# Scalar file (e.g. activtion map or anatomical image)
FILE1 = "/path/to/step1.nii.gz"

OUTDIR = "/path/to/output"

# (Optional) Camera position
# CAMPOS = [(50.993896484375, 443.2642517089844, 53.0),
#           (64.5,            56.5,              53.0),
#           (0.0,             0.0,                1.0)]

CLIM = (0, 1)
# -----------------------------------------------------------------------------
# Load data
data1 = nb.load(FILE1).get_fdata()
nr_frames = data1.shape[-1]

# Colorbar
sargs = dict(width=0.5, height=0.1, vertical=False,
             position_x=0.05, position_y=0.05,
             font_family="courier",
             title_font_size=22,
             label_font_size=18,
             n_labels=3, fmt="%.0f")

frame_order = np.arange(nr_frames)
frame_order = np.hstack([frame_order, frame_order[::-1]])

opacity = np.ones(255)
opacity[0] = 0

for i, j in enumerate(frame_order):
    # Get data and clip it
    temp = np.copy(data1[..., j])
    pvdata = pv.wrap(temp)

    p = pv.Plotter(window_size=(640, 720))
    p.add_volume(pvdata, stitle="Layers",
                 cmap="Spectral", clim=CLIM, scalar_bar_args=sargs,
                 blending="composite", opacity=opacity, show_scalar_bar=False)
    p.add_text("LN2_MULTILATERATE\nanimated flattening\n[layers]",
               font="courier", font_size=16)
    p.set_background("black")
    p.camera_position = CAMPOS

    out_name = "frame-{}.png".format(str(i).zfill(3))
    p.show(screenshot=os.path.join(OUTDIR, out_name), interactive=False)
    p.close()

print("Finished.")
