#!/bin/bash

inputMAF=$1

Rscript feature.matrix.R $inputMAF
python predict.ml.py ${inputMAF}
Rscript res.assembl.R ${inputMAF}
