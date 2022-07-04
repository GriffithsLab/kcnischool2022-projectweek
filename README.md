# KCNI Sumer School 2022 - Whole-Brain + Cognitive Network Modelling Project Week


## Setup Intructions

```bash	
git clone https://github.com/griffithslab/kcnischool-projectweek

cd kcnischool-projectweek

gdown https://drive.google.com/drive/folders/1rlh75dpjOJxeS0WZPojuzjAwl5OENWrV -O subjinfo --folder --remaining-ok

gdown https://drive.google.com/drive/folders/1cu6bCLNEp_YR-8C3zm_v2B7_lXQM9Zg0 -O ptseries --folder --remaining-ok

gdown https://drive.google.com/drive/folders/12os_7xC10QUwJANBJb-5CXG1Gg_9YUgQ  -O dwiconn --folder --remaining-ok
```


```python
from kspw.pytorrww import Model_fitting,RNNWWD,plot_fit_parameters
```

```bash
wget https://github.com/ThomasYeoLab/CBIG/raw/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/HCP/fslr32k/cifti/Schaefer2018_100Parcels_7Networks_order.dlabel.nii
```

cd ..


```python
from kspw.pytorrww import Model_fitting,RNNWWD,plot_fit_parameters
```


ls * 





