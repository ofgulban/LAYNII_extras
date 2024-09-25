"""Read tuneup files."""

import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
import struct

FILE = "path"

basename, ext = os.path.splitext(FILE)
filename = os.path.basename(basename)
OUTNAME = "{}.txt".format(basename)

# =============================================================================
ds = pydicom.dcmread(FILE)

# =============================================================================
# Open the text file for writing
with open(OUTNAME, 'w', encoding='utf-8') as f:
    # Write some basic information about the DICOM file
    f.write("DICOM File Information:\n")
    f.write("========================\n")
    f.write(f"File: {FILE}\n\n")

    # Loop through all elements in the DICOM dataset
    for elem in ds:
        f.write(f"{elem.tag}: {elem.name} = {elem.value}\n")

# =============================================================================
# [CSA Data] seems to havee some numbers
tag = (0x7fe1, 0x1010)
byte_data = ds.get(tag).value

float_array = np.frombuffer(byte_data, dtype=np.float32)

# Plot
plt.plot(float_array)  # 'o' for circle markers to indicate points
plt.title(filename)
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

print("Finished.")