import axelrod as axl
import multiprocessing
import os

from players import players

def main(players=players, processes=None, seed=1, turns=200, repetitions=10000,
         noise=0):

    if processes is None:
        processes = multiprocessing.cpu_count()

    kind = "std" if noise == 0 else "noisy"
    prefix = "Standard" if noise == 0 else "Noisy"
    filename = "data/strategies_{}_{}_interactions.csv".format(kind,
                                                               repetitions)
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

    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions,
                                noise=noise)

    results = tournament.play(filename=filename, processes=processes,
                              progress_bar=False)
    plot = axl.Plot(results)
    plot.save_all_plots(prefix='assets/{}_{}'.format(kind, repetitions),
                        progress_bar=False,
                        title_prefix=prefix, filetype="pdf")
    results.write_summary('assets/{}_summary_{}.csv'.format(kind, repetitions))

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    repetitions = int(args[0])
    try:
        noise = float(args[1])
    except IndexError:
        noise = 0

    main(repetitions=repetitions, noise=noise)
