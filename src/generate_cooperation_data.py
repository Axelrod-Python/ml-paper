"""
Runs a spatial tournament on a bi partite graph and writes data with the mean
cooperation rate of players of one cluster against all players
"""

import axelrod as axl
import pandas as pd
import numpy as np
import multiprocessing
import os
import csv

from players import players

def obtain_cooperation_matrix(filename, number_of_turns=200):
    data = []
    with open(filename, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row[2:4] + [int(a == "C") for a in row[4]])
    df = pd.DataFrame(data, columns=["player", "opponent"] + ["Round {}".format(n) for n in range(number_of_turns)])
    return np.array(df.groupby(["player", "opponent"]).mean())

def main(index, players=players, processes=None, seed=1, turns=200, repetitions=10000,
         noise=0):
    """
    index of the player in question
    """
    edges = [(index, j) for j, _ in enumerate(players)]

    if processes is None:
        processes = multiprocessing.cpu_count()

    prefix = "{}_{}_{}_{}".format(seed, int(100 * noise), repetitions,
                                  players[index])
    interactions_filename = "data/cooperation_{}_interactions.csv".format(prefix)
    output_filename = "data/cooperation_{}_array.gz".format(prefix)

    # Deleting the file if it exists
    try:
        os.remove(interactions_filename)
    except OSError:
        pass

    axl.seed(seed)  # Setting a seed
    assert axl.__version__ == "2.13.0"
    print("Axelrod version", axl.__version__)
    print(len(players), "Players")
    print("Seed", seed)
    print("Repetitions", repetitions)
    print("Noise", noise)
    print("Player", players[index])

    tournament = axl.SpatialTournament(players, edges=edges, turns=turns,
                                       repetitions=repetitions, noise=noise)

    tournament.play(filename=interactions_filename, processes=processes,
                    build_results=False, progress_bar=False)

    matrix = obtain_cooperation_matrix(interactions_filename)
    np.savetxt(fname=output_filename, X=matrix, delimiter=",")

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    repetitions = int(args[0])
    seed = int(args[1])
    noise = float(args[2])
    index = int(args[3])

    main(index=index, repetitions=repetitions, seed=seed, noise=noise)
