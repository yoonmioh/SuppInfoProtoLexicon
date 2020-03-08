#!/bin/bash

# score-nofreq_morphs.sh
#
# Score a stimulus set based on core morph phonotactics, without frequency weighting.
#
# SYNTAX: sh score-nofreq_morphs.sh <TRAIN> <STIMLIST> <LMDIR> <AUXDIR> <OUTDIR>
cd ~
cd /Applications/srilm-1.7.2/bin/macosx

TRAIN=$1
STIMLIST=$2
LMDIR=$3
AUXDIR=$4
OUTDIR=$5

TRAINFILE=$(basename -- "$TRAIN")
TRAINROOT="${TRAINFILE%.*}"
LM="${LMDIR}/${TRAINROOT}.lm"
DEBUG="${AUXDIR}/${TRAINROOT}.debug"

echo
echo "Estimating language model"

# first run SRILM to get a language model
./ngram-count -text $TRAIN -lm $LM -order 3 -wbdiscount -interpolate

# modify the language model to use morpheme boundary symbols and rule out adjacent boundaries and consonant-final morphemes
python modify-lm_morphs.py $LM

echo
echo "Scoring stimuli"

# use the language model to score the stimlist, over all possible segmentations
./ngram -lm $LM -ppl $STIMLIST -debug 2 -hidden-vocab morph-boundary.txt -no-eos -no-sos > $DEBUG

# reformat the output
python reformat-srilm-evaluation_morphs.py $DEBUG $OUTDIR $STIMLIST

echo
echo "Done"
