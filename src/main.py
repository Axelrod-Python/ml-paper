"""
Runs a tournament and writes:

    - interactions
    - summary
    - scores per tournament (rows) per player (columns)
    - wins per tournament (rows) per player (columns)
    - mean payoff matrix
    - mean stdv payoff matrix

to separate files with the prefix: `<seed>_<noise>_<repetitions>`.
"""

import axelrod as axl
import multiprocessing
import os
import numpy as np

from players import players

def main(players=players, processes=None, seed=1, turns=200, repetitions=10000,
         noise=0):

    if processes is None:
        processes = multiprocessing.cpu_count()

    prefix = "{}_{}_{}".format(seed, int(100 * noise), repetitions)
    filename = "data/{}_interactions.csv".format(prefix)

    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    axl.seed(seed)  # Setting a seed
    assert axl.__version__ == "2.13.0"
    print("Axelrod version", axl.__version__)
    print(len(players), "Players")
    print("Seed", seed)
    print("Repetitions", repetitions)
    print("Noise", noise)

    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions,
                                noise=noise)

    results = tournament.play(filename=filename, processes=processes,
                              progress_bar=False)


    # Write summary for each seed
    results.write_summary("assets/{}_summary.csv".format(prefix))

    # Write the total scores per tournament for each player to "assets/".
    # This data is a #repetitions (rows) by #players (columns) array with
    # X_{ij} corresponding to the TOTAL score obtained by player j in repetition
    # i of the tournament.
    scores_per_tournament = np.array(results.scores).transpose()
    np.savetxt(fname="assets/{}_scores.gz".format(prefix),
               X=scores_per_tournament, delimiter=",")

    # Write the total wins per tournament for each player to "assets/".
    # This data is a #repetitions (rows) by #players (columns) array with
    # X_{ij} corresponding to the TOTAL wins obtained by player j in repetition
    # i of the tournament.
    wins_per_tournament = np.array(results.wins).transpose()
    np.savetxt(fname="assets/{}_wins.gz".format(prefix),
               X=wins_per_tournament, delimiter=",")

    # Write the payoff of each player against every other player to "assets/".
    # This data is a #players (rows) by #players (rows) array with X_{ij}
    # corresponding to the mean score of player i against player j
    payoff_matrix = np.array(results.payoff_matrix)
    np.savetxt(fname="assets/{}_payoff_matrix.gz".format(prefix),
               X=payoff_matrix, delimiter=",")

    # Write the stdv payoff of each player against every other player to
    # "assets/". This data is a #players (rows) by #players (rows) array with
    # X_{ij} corresponding to the standard deviation of the score of player i
    # against player j
    payoff_stdev_matrix = np.array(results.payoff_stddevs)
    np.savetxt(fname="assets/{}_payoff_stdev_matrix.gz".format(prefix),
               X=payoff_stdev_matrix, delimiter=",")

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    repetitions = int(args[0])
    seed = int(args[1])
    noise = float(args[2])

    main(repetitions=repetitions, seed=seed, noise=noise)
