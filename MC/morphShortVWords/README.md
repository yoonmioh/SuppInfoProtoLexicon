These scores are based on the following assumptions:  
- participants store word types  
- participants segment stored words into morphs (discounting full reduplicants)  
  > by consequence, a phonotactic model is computed over morphs, weighted by the number of word types they occur in  
- participants attempt to morphologically parse nonword stimuli  
  > by consequence, phonotactic scoring uses hidden morph boundaries  

The script used to compute scores is as follows (run from the parent directory):  
`sh score-freq_morphs.sh morphShortVWords/morphs/morphs_<N>.txt stimuli-shortvowels_morphs.txt morphShortVWords/models morphShortVWords/scores/auxiliaries morphShortVWords/scores`  
where `<N>` is the number of words that the morphs have been computed over (organized according to frequency bins)

Note: the scores over the full set of words are slightly different to the ones that I computed earlier, in `protolexicon-reanalysis`. I'm not sure what I did differently; but since we are no longer using those earlier scores, it shouldn't matter.