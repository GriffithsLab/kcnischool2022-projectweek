"""
Python script to send model fitting job sumissions for multiple subjects.
"""

# Importage 
import os
from copy import copy

# Define some variables
jobfile_str = 'rwwbatchjob_sub-%s.slurm'
outfile_str = 'rwwbatchres_sub-%s.h5'
slurmoutfile_str = 'rwwbatchres_sub-%s.out' 

pyfile_name = 'thepythonscripy.py'


subs =['9002', '9003', '9004', '9005', '9008', '9009', '9011', '9014',
       '9018', '9020', '9023', '9025', '9026', '9028', '9029', '9032',
       '9033', '9034', '9036', '9038', '9039', '9040', '9041', '9042',
       '9045', '9046', '9047', '9048', '9049', '9055', '9058', '9061',
       '9062', '9064', '9065', '9068', '9069', '9071', '9072', '9075',
       '9079', '9080', '9081', '9084', '9085', '9086', '9087', '9088',
       '9089', '9092', '9093', '9094', '9096', '9098']


# Template text for jobfile
jobfilecontents_str = """\ 
#!/bin/sh
#SBATCH --job-name='<JOBNAME>'
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --time=24:00:00
#SBATCH --mail-type=all
#SBATCH --mem=10G
#SBATCH --output='<SLURM_OUTFILE>'

# Run code
module load anaconda3
python <MY_SCRIPT> <SUB>
"""


for sub in subs:

    # Name the output files
    jobfile_name = jobfile_str %sub
    slurmoutfile_name = slurmoutfile_str %sub
    outfile_name = outfile_str %sub

    jobname = 'rwwbatch_sub-%s' %sub
 
    # Substitute the file contents 
    s = copy(jobfilecontents_str)
    s = s.replace('<JOBNAME>', jobname)
    s = s.replace('<SLURM_OUTFILE>', slurmoutfile_name)
    s = s.replace('<MY_SCRIPT>', pyfile_name)

    # Write the job file 
    F = open(jobfile_name, 'w+')
    F.write(s)
    F.close()
    print('\nSubmitting job file: ')
    print('\njobfile name: %s' %jobfile_name)
    print('\nsaving output to: %s' %outfile_name)


    # Submit job
    os.system('sbatch %s' %jobfile_name)



