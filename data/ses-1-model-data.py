## Data download
## ----------------
import os,gdown,shutil


# Gdown download the ses-2 data 
gdown.download(id='1Le4Iq7vozVkA4oEVDS13OybEUeX51aVg')
shutil.unpack_archive('ses1-20220707T225637Z-001.zip', '')
os.remove('ses1-20220707T225637Z-001.zip')