## Data download
## ----------------
import os,gdown,shutil


# Gdown download the ses-2 data 
gdown.download(id='1qp3ZlEqnRZNJ9Ebm9iWFefpzuEn4EBoU')
shutil.unpack_archive('ses2-20220707T222549Z-002.zip', '')
os.remove('ses2-20220707T222549Z-002.zip')