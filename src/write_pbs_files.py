"""
Write the pbs file (scheduler files for cluster) and a `./submit_ml_jobs.sh`
script to submit them.
"""
min_seed = 0
max_seed = 15  # The number of jobs is max-min
repetitions = 1000  # The total repetitions = max_seed * repetitions
noises = [0.05, 0]

pbs_filenames = []

for seed in range(min_seed, max_seed):
    for noise in noises:
        pbs_file = """#!/bin/bash
#PBS -q workq
#PBS -N {}-{}-{}
#PBS -P PR350
#PBS -o {}-{}.txt
#PBS -e {}-{}.txt
#PBS -l select=1:ncpus=16:mpiprocs=16
#PBS -l place=scatter:excl
#PBS -l walltime=70:00:00

export MPLBACKEND="agg"
# Run std
cd /scratch/smavak/ml-paper/src
/home/smavak/anaconda3/envs/ml-paper/bin/python main.py {} {} {}
""".format(seed, noise, repetitions,
           seed, noise,
           seed, noise,
           repetitions, seed, noise)
        filename = "pbs_files/ml-{}-{}-{}.pbs".format(seed, int(100 * noise),
                                                      repetitions)
        with open(filename, "w") as f:
            f.write(pbs_file)
        pbs_filenames.append(filename)

    with open("submit_ml_jobs.sh", "w") as f:
        for filename in pbs_filenames:
            f.write("qsub {}\n".format(filename))
