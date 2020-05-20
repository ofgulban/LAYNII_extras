"""Rudimentary reimplementation of layer smoothing from LAYNII

Reference
---------
https://github.com/layerfMRI/LAYNII/blob/master/LN_LAYER_SMOOTH.cpp
"""

import os
import argparse
import numpy as np
import nibabel as nb
from scipy.ndimage import gaussian_filter
from pylaynii import __version__

def main():
    """Command line call argument parsing."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-input', metavar='path',
        help="Nifti file that will be smoothed. It should have same \
              dimensions as layer file.")

    parser.add_argument(
        '-layer_file', metavar='path',
        help="Nifti file that contains layer masks.")

    parser.add_argument(
        '-FWHM', type=int, required=False,
        metavar=20, default=20,
        help="Full width half maximum of Gaussian kernel. In voxel size units."
        )

    parser.add_argument(
        "-outfile", metavar='path', required=False,
        help="Alternative output path.")

    # Welcome message
    welcome_str = '{} v{}'.format('PyLAYNII', __version__)
    welcome_decor = '=' * len(welcome_str)
    print('{}\n{}\n{}'.format(welcome_decor, welcome_str, welcome_decor))

    # =========================================================================
    # Parameters
    args = parser.parse_args()
    NII1 = args.input
    NII2 = args.layer_file
    FWHM = args.FWHM
    SIGMA = FWHM / 2.35482004503
    if args.outfile is None:
        basename = NII1.split(os.extsep, 1)[0]
        OUT_NAME = "{}_layer_smooth_FWHM{}.nii.gz".format(
            basename, str(FWHM).replace('.', 'pt'))
    else:
        OUT_NAME = args.outfile

    print("Selected FWHM: {}".format(FWHM))
    print("Output path: {}".format(OUT_NAME))

    # =========================================================================
    # Load data
    nii = nb.load(NII1)
    data = nii.get_fdata()
    data_layers = nb.load(NII2).get_fdata()

    # Derive parameters
    dims = data.shape
    layers = np.unique(data_layers)

    # Masked Gaussian filter
    data_new = np.zeros(dims)
    for l in layers:
        idx_nonzero = data_layers == l
        mask = (idx_nonzero).astype("float")
        data_smooth = gaussian_filter(data * mask, sigma=SIGMA)
        mask_smooth = gaussian_filter(mask, sigma=SIGMA)
        data_new[idx_nonzero] += (
            data_smooth[idx_nonzero] / mask_smooth[idx_nonzero])

    # Save output image as nifti
    out = nb.Nifti1Image(data_new, affine=nii.affine)
    nb.save(out, OUT_NAME)

    print("Finished.")

if __name__ == "__main__":
    main()
