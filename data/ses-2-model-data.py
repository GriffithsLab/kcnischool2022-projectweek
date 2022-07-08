## Data download
## ----------------
import os, gdown, shutil

# Gdown download the ses-2 data
gdown.download(id='1kgeR2fAb0CxLKG8-0RBJmiMA2q2W3lax')
shutil.unpack_archive('ses2_partA.zip', '')
os.remove('ses2_partA.zip')

#part B
gdown.download(id='1-xrtNo-lvAm1iDx2UA6xOrezIdB9OE_S')
shutil.unpack_archive('ses2_partB.zip', '')
os.remove('ses2_partB.zip')