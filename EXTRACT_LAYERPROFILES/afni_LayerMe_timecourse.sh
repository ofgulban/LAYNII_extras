#!/bin/bash

#get mean value
3dROIstats -mask lo_layers.nii.gz -1DRformat -quiet -nzmean lo_BOLD_intemp.nii.gz > layers_mean.dat
#get standard deviation
3dROIstats -mask lo_layers.nii.gz -1DRformat -quiet -sigma  lo_BOLD_intemp.nii.gz > layer_std.dat

#columns are the layers 
#rows are the time points. 
