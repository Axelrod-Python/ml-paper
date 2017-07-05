# Needs ml-paper env to be activated
# source activate ml-paper
all: ./src/data/
	 cd src; jupyter nbconvert --to notebook --execute --inplace main.ipynb --ExecutePreprocessor.kernel_name=python --ExecutePreprocessor.timeout=600
