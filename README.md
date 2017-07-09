# Reinforcement Learning Produces Dominant Strategies for the Iterated Prisoner’s Dilemma

This paper gives description of strategies trained using reinforcement learning
as well as a detailed analysis of their performance in a large tournament with
176 strategies.

This directory is structured as follows:

```
|--- main.tex  # Source file for the paper
|--- bibliograpy.bib  # Biblioraphy
|--- environment.yml  # Conda environment
|--- assets  # All tables, images, diagrams used in `main.tex`
|--- src
     |--- players.py  # All players used
     |--- abbreviations.py  # Abbreviations for some player names
     |--- reference_keys.csv  # Citation keys for each strategy
     |--- main.ipynb  # Notebook to obtain all `../assets`
     |--- main.py  # Main file to generate tournament data
     |--- generate_cooperation_data.py  # File to generate cooperation data
     |--- write_pbs_files.py  # Script to write pbs scheduler files
     |--- submit_ml_jobs.sh  # Auto written script to submit pbs files
     |--- pbs_files  # Automatically written files
          |--- ml-0-0-1000.pbs
          |--- ...
     |--- data  # Where data file are placed
```

## Building the article

# Building the article:

The following compiles the article using `Latexmk` version 4.41:

```
$ latexmk --xelatex main.tex
```

The bibliography is being built using `biblatex` which requires `biber`, that
comes bundled with some installs of `latex` but if you are having problems you
might need to run (on ubuntu, similarly for other systems):

```
$ sudo apt-get install biber
```

# Contributions

- Conceived of the study: MH VK
- Conducted experiments and trained strategies: VK MH MJ GK
- Analyzed the data and analytical methods: VK MH
- Wrote the paper: VK MH NG
- Created software: MH VK MJ GK
- Axelrod Library Core Team: VK OC MH

## Some original training code sources
- [EvolvedLookerUp](http://mojones.net/evolving-strategies-for-an-iterated-prisoners-dilemma-tournament.html) by mojones
- [EvolvedANN](https://gist.github.com/mojones/550b32c46a8169bb3cd89d917b73111a) by mojones
- [PSO Gambler](https://gist.github.com/GDKO/60c3d0fd423598f3c4e4) by GDKO
