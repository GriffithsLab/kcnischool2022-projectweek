## Data download
## ----------------
import os, gdown, shutil

# Gdown download the ses-1 data
gdown.download(id='1pyDZ0i00gPlxJVziwuVcZ1j_kaPjWrau')
shutil.unpack_archive('ses1_partA.zip', '')
os.remove('ses1_partA.zip')
gdown.download(id='1nKqy_CskMJuly7tpXJOWcQdxFz8Kek8k')
shutil.unpack_archive('ses1_partB.zip', '')
os.remove('ses1_partB.zip')