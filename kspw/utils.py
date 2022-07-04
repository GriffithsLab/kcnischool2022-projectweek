

import os,sys,glob,numpy as np,pandas as pd

import nibabel as nib


def load_stockholm_data():

    """
    
   USage
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------=-------------------------------------------

    stuff = load_stockhom_data()

    schaf_idxs,schaf_labs,schaf_rgbs,subs,dwiconn_dfs,ptsrs_dfs,pcrs_dfs = stuff



    """


    data_dir = 'data'

    # Load the Schaefer parcellation
    # ------------------------------
    atlas_file = os.path.join(data_dir,'Schaefer2018_100Parcels_7Networks_order.dlabel.nii')

    assert os.path.isfile(atlas_file)

    img = nib.load(atlas_file)

    schaf_dat = img.get_data()[0].astype(int)
    imgax0 = img.header.get_axis(0)
    labsdict = imgax0.label[0]
    schaf_idxs,schaf_labs,schaf_rgbs = [],[],[]

    for k in labsdict.keys():
      schaf_idxs+=[k]
      schaf_labs+=[labsdict[k][0]]
      schaf_rgbs+=[labsdict[k][1]]


    ## Load the OpenNeuro data
    ## -------------------------
    pts_dir = os.path.join(data_dir, 'ptseries')
    dwiconn_dir = os.path.join(data_dir, 'dwiconn')
    si_dir = os.path.join(data_dir, 'subjinfo')
    
    all_dwiconn_fs = glob.glob(os.path.join(dwiconn_dir, '*.csv')) # dwi conmat fnames
    all_ptsrs_fs = glob.glob(os.path.join(pts_dir , '*rest*.ptseries*')) # rsfMRI ptseries fnames

    def getses(f): return int(f.split('_ses-')[1].split('_')[0])
    def getsub(f): return int(f.split('/')[-1].split('sub-')[1].split('_')[0])
  
    all_dwiconn_subs = [getsub(f) for f in all_dwiconn_fs]
    all_ptsrs_subs = [(getsub(f), getses(f)) for f in all_ptsrs_fs]

    subs = np.intersect1d([s[0] for s in all_ptsrs_subs],all_dwiconn_subs)
    dwiconn_fs = {s:f for f,s in zip(all_dwiconn_fs,all_dwiconn_subs) if s in subs}
    ptsrs_fs = {s:f for f,s in zip(all_ptsrs_fs,all_ptsrs_subs) if s[0] in subs}

    dwiconn_dfs = {s: pd.read_csv(f,header=None,sep=' ') for s,f in dwiconn_fs.items()}
    dwiconn_dfs = {s: df + df.T for s,df in dwiconn_dfs.items()} # Dict of all subj dwiconn dfs
    for sub,df in dwiconn_dfs.items(): df.index = schaf_labs[1:]; df.columns = schaf_labs[1:]

    ptsrs_dfs = {s: pd.DataFrame(nib.load(f).get_data(),columns=schaf_labs[1:]) for s,f in ptsrs_fs.items()}
    pcrs_dfs = {s: df.corr() for s,df in ptsrs_dfs.items()} # Dict of all subj ptseries dfs
    for sub,df in pcrs_dfs.items(): df.index = schaf_labs[1:]; df.columns = schaf_labs[1:]


    return (schaf_idxs,schaf_labs,schaf_rgbs,
            subs,dwiconn_dfs,ptsrs_dfs,pcrs_dfs)

