#!/bin/bash

#get mean value
3dROIstats -mask lo_layers.nii.gz -1DRformat -quiet -nzmean lo_BOLD_intemp.nii.gz > layer_t.dat

#columns are the layers 
#rows are the time points. 
