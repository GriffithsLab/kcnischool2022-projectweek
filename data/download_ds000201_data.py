

## Data download
## ----------------
import os,gdown,shutil


# Gdown download the main data folders 

# DWI Conn Folder
print('\n\nDownloading DWI conn data........\n')
fileid = '1vga0J5HdpHwSpCbH6lwAInKGzzl_j8oo'
gdown.download(id=fileid,output='dwiconn_download.zip')
shutil.unpack_archive('dwiconn_download.zip', '')
os.remove('dwiconn_download.zip')

# Subj Info Folder
print('\n\nDownloading subj info data ........\n')
fileid = '1CcJBJ1kQigKn2lOT-PMQqMPm9afl4O89'
gdown.download(id=fileid,output='subjinfo_download.zip')
shutil.unpack_archive('subjinfo_download.zip','')
os.remove('subjinfo_download.zip')

# Ptseries folder
print('\n\nDownloading rsfMRI ptseries data.......\n')
fileid = '1CW9fHKJa1qCCwPsQWoymQNbWZsoDbntn'
gdown.download(id=fileid,output='ptseries_download.zip')
shutil.unpack_archive('ptseries_download.zip','')
os.remove('ptseries_download.zip')

# Schaefer parcellation
print('\n\nDownloading Schaefer parcellation data ........\n')
url = 'https://github.com/ThomasYeoLab/CBIG/raw/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/HCP/fslr32k/cifti/Schaefer2018_100Parcels_7Networks_order.dlabel.nii'
gdown.download(url, output='Schaefer2018_100Parcels_7Networks_order.dlabel.nii')


