import axelrod as axl
import numpy as np

def main(filename):

    assert axl.__version__ == "2.13.0"

    prefix = "Standard" if "standard" in filename else "Noisy"
    results = axl.ResultSetFromFile(filename=filename, progress_bar=False)
    plot = axl.Plot(results)
    plot.save_all_plots(prefix="assets/{}".format(prefix), progress_bar=False,
                        title_prefix=prefix, filetype="pdf")
    results.write_summary("assets/{}_summary.csv".format(prefix))

    # Write the total scores per tournament for each player to "assets/".
    # This data is a #repetitions (rows) by #players (columns) array with
    # X_{ij} corresponding to the TOTAL score obtained by player j in repetition
    # i of the tournament.
    scores_per_tournament = np.array(results.scores).transpose()
    np.savetxt(fname="assets/{}_scores.gz".format(prefix),
               X=scores_per_tournament)

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
               X=payoff_matrix, delimiter=",")



if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    main(filename)
