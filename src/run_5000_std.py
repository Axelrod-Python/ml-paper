import axelrod as axl
import os

turns = 200
repetitions = 5000

seed = 1
filename = "data/strategies_std_{}_interactions.csv".format(repetitions)

players = [s() for s in axl.strategies if "length"
           not in s.classifier["makes_use_of"]]
players.sort(key=lambda p:p.__repr__())


def main(players=players, processes=4):
    # Deleting the file if it exists
    try:
        os.remove(filename)
    except OSError:
        pass

    axl.seed(seed)  # Setting a seed
    assert axl.__version__ == "2.10.0"
    print("Axelrod version", axl.__version__)
    print(len(players), "Players")
    print("Seed", seed)

    tournament = axl.Tournament(players, turns=turns,
                                repetitions=repetitions)

    results = tournament.play(filename=filename, processes=processes,
                              progress_bar=False)
    plot = axl.Plot(results)
    plot.save_all_plots(prefix='assets/std_{}'.format(repetitions),
                        progress_bar=False,
                        title_prefix='standard')
    results.write_summary('assets/std_summary_{}.csv'.format(repetitions))

if __name__ == "__main__":
    import sys
    import multiprocessing
    processes = multiprocessing.cpu_count()

    main(processes=processes)
