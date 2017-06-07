import axelrod as axl

def main(filename):

    assert axl.__version__ == "2.13.0"

    prefix = "Standard" if "standard" in filename else "Noisy"
    results = axl.ResultSetFromFile(filename=filename, progress_bar=False)
    plot = axl.Plot(results)
    plot.save_all_plots(prefix="assets/{}".format(prefix), progress_bar=False,
                        title_prefix=prefix, filetype="pdf")

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    main(filename)
