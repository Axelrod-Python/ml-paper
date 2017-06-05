import axelrod as axl
import multiprocessing
import os

from players import players

def main(players=players, processes=None, seed=1, turns=200, repetitions=10000,
         noise=0):

    if processes is None:
        processes = multiprocessing.cpu_count()

    kind = "std" if noise == 0 else "noisy"
    prefix = "Standard" if noise == 0 else "Noisy ({})".format(noise)
    filename = "data/strategies_{}_{}_{}_interactions.csv".format(kind,
                                                               repetitions,
                                                               seed)
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

    tournament.play(filename=filename, processes=processes,
                    build_results=False, progress_bar=False)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    repetitions = int(args[0])
    seed = int(args[1])

    try:
        noise = float(args[2])
    except IndexError:
        noise = 0

    main(repetitions=repetitions, seed=seed, noise=noise)
