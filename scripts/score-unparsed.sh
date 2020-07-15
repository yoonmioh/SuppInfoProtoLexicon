#!/bin/bash

# score-unparsed.sh
#
# Score a stimulus set based on whole-word or unparsed-morph phonotactics, without frequency weighting.
#
# SYNTAX: sh score-unparsed.sh <TRAIN> <STIMLIST> <LMDIR> <AUXDIR> <OUTDIR>

TRAIN=$1
STIMLIST=$2
LMDIR=$3
AUXDIR=$4
OUTDIR=$5

TRAINFILE=$(basename -- "$TRAIN")
TRAINROOT="${TRAINFILE%.*}"
LM="${LMDIR}/${TRAINROOT}.lm"
DEBUG="${AUXDIR}/${TRAINROOT}.debug"

# echo
# echo "Estimating language model"

# first run SRILM to get a language model
ngram-count -text $TRAIN -lm $LM -order 3 -wbdiscount -interpolate

# echo
# echo "Scoring stimuli"

# use the language model to score the stimlist
ngram -lm $LM -ppl $STIMLIST -debug 1 > $DEBUG

# reformat the output
python reformat-srilm-evaluation.py $DEBUG $OUTDIR $STIMLIST

# echo
# echo "Done"