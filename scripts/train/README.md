# An Adult Proto-lexicon
## Phonotactic probability training data
*Yoon Mi Oh, Simon Todd, Clay Beckner, Jen Hay, Jeanette King, and Jeremy Needle*

## Contents

This directory contains data used to train phonotactic probability models.

Due to licensing restrictions, the only files available are based on morphs (with vowel length distinctions collapsed):

-  `morphs-shortvowels_unweighted.txt`: used to train morph-based models over types (i.e. without weighting)  
-  `morphs-shortvowels_weighted-tokens-raw.txt`: used to train morph-based models, where each morph type is weighted by the combined corpus-based raw/unsmoothed token frequencies of the words from the *Te Aka* dictionary that it occurs in  
  - Note: this will automatically exclude consideration of any words that do not occur in the corpora we consulted due to sampling error. It is therefore generally not recommended; these frequencies are mostly included as the foundation of the N-highest-frequency sampling scheme in Monte Carlo analyses.  
-  `morphs-shortvowels_weighted-tokens-raw.txt`: used to train morph-based models, where each morph type is weighted by the combined corpus-based smoothed token frequencies of the words from the *Te Aka* dictionary that it occurs in  
-  `morphs-shortvowels_weighted-words.txt`: used to train morph-based models, where each morph type is weighted by the number of word types from the *Te Aka* dictionary that it occurs in  

While we are not able to provide word types from the dictionary, we have included the file `words_corpora_freq-smoothing.txt`, which specifies the values used for frequency smoothing. Note that the values in this file represent all words in the corpora and dictionary, including proper nouns.  