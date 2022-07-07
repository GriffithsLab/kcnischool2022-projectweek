import os, sys, glob, numpy as np, pandas as pd
from matplotlib import pyplot as plt
import h5py

cwd = os.getcwd()
home = '/home/l/lcl_uotkcni22/lcl_uotkcni22s2133/kcnischool2022-projectweek'

sys.path.append(home)
os.chdir(home)

from kspw.utils import load_stockholm_data
from kspw.pytorrww import Model_fitting, h_tf, RNNWWD, plot_fit_parameters, plot_sim_states_outputs

stuff = load_stockholm_data()
schaf_idxs, schaf_labs, schaf_rgbs, schaf_dat, subs, dwiconn_dfs, ptsrs_dfs, pcrs_dfs = stuff
subsesses = list(pcrs_dfs.keys())

os.chdir(cwd)


def fitsub(sub):
    # model fitting
    sub = int(sub)

    sc = dwiconn_dfs[sub].values.copy()
    sc = np.log1p(sc) / np.linalg.norm(np.log1p(sc))
    ts = ptsrs_dfs[sub, 1].values.copy()
    fc_emp = np.corrcoef(ts.T)

    model = RNNWWD(input_size=2,
                   node_size=100,
                   batch_size=20,
                   step_size=0.05,
                   tr=2.5,
                   sc=sc,
                   fit_gains=True,
                   g_mean_ini=80,
                   g_std_ini=.1,
                   gEE_mean_ini=2.5,
                   gEE_std_ini=.1)
    F = Model_fitting(model, ts, num_epochs=80, learning_rate=0.02)
    output_train = F.train()
    output_test = F.test(20)

    print('Done')

    # write to file
    f = 'results_' + str(sub) + '.h5'
    H = h5py.File(f, 'w')
    H['sc'] = sc
    H['ts'] = ts
    H['fc_emp'] = fc_emp

    for k, v in output_train.items():
        H['output_train_' + k] = v

    for k, v in output_test.items():
        H['output_test_' + k] = v

    return sub, sc, ts, fc_emp, model, F, output_train, output_test


if __name__ == '__main__':
    sub = sys.argv[1]  # sub

    print('Running ' + sub)
    sub, sc, ts, fc_emp, model, F, output_train, output_test = fitsub(sub)
    print(sc)
