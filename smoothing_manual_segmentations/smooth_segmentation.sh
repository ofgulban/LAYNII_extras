#!/bin/bash

#3dcalc -a wholefilled.nii -expr 'step(a-1)' -prefix GM_mask.nii

3dmask_tool -input GM_mask.nii -prefix less_bumps.nii -dilate_input -1 1 -overwrite
