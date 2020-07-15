# An Adult Proto-lexicon
## Phonotactic probability scripts
*Yoon Mi Oh, Simon Todd, Clay Beckner, Jen Hay, Jeanette King, and Jeremy Needle*

## Contents

This directory contains scripts used to calculate phonotactic probabilities, used in the analysis.

Scripts should be run in a POSIX shell and require SRILM and Python.

- `modify-lm_parsed.py`: a script for modifying a language model trained on morphs for the assumption that participants attempt to parse stimuli into morphs  
- `morph-boundary.txt`: the character used to represent morph boundaries (+)  
- `reformat-srilm-evaluation.py`: a script for extracting phonotactic probabilities from a .DEBUG file output by SRILM  
- `score-parsed.sh`: a script for evaluating morph-based phonotactic probabilities of stimuli, assuming that participants attempt to parse stimuli into morphs, where the training data are types that should all be weighted equally  
- `score-parsed_weighted.sh`: a script for evaluating morph-based phonotactic probabilities of stimuli, assuming that participants attempt to parse stimuli into morphs, where the training data are types with associated weights (e.g. frequencies)  
- `score-unparsed.sh`: a script for evaluating word-based phonotactic probabilities of stimuli, or morph-based phonotactic probabilities assuming that participants do not parse stimuli into morphs, where the training data are types that should all be weighted equally  
- `score-unparsed_weighted.sh`: a script for evaluating word-based phonotactic probabilities of stimuli, or morph-based phonotactic probabilities assuming that participants do not parse stimuli into morphs, where the training data are types with associated weights (e.g. frequencies)  
- `stimuli.txt`: the original stimuli for Exp2, in a format for processing by SRILM (phonological form, with phonemes separated by spaces). Used for `score-unparsed` scripts where the training data preserves vowel length distinctions  
- `stimuli-shortvowels.txt`: the stimuli for Exp2, with vowel length distinctions collapsed, in a format for processing by SRILM (phonological form, with phonemes separated by spaces). Used for `score-unparsed` scripts where the training data collapses vowel length distinctions  
- `stimuli-shortvowels_parsed.txt`: the original stimuli for Exp2, with vowel length distinctions collapsed and start/end morph boundaries added, in a format for processing by SRILM (phonological form, with phonemes separated by spaces). Used for `score-parsed` scripts where the training data collapses vowel length distinctions  
- `train/`: a directory containing files used to train phonotactic models. Due to licensing restrictions, the only files available are based on morphs (with vowel length distinctions collapsed).  

### Using the scripts

The following are arguments for all of the shell scripts:  
1. `<TRAIN>`: the path to the data that will be used to train the phonotactic model  
  - For unweighted training data (used with `score-parsed.sh` or `score-unparsed.sh`), the training data should be a plaintext file with a single column, no headings. Each row should contain a single word/morph, with a space between each phoneme character.  
  - For weighted training data (used with `score-parsed_weighted.sh` or `score-unparsed_weighted.sh`), the training data should be a plaintext file with two tab-delimited columns, no headings. Each row should contain the weight of a word/morph in the first column (e.g. frequency), and the word/morph itself in the second column, with a space between each phoneme character.  
2. `<STIMLIST>`: the path to the stimuli that will be scored  
  - Should be one of `stimuli.txt`, `stimuli-shortvowels.txt`, or `stimuli-shortvowels_parsed.txt`, depending on the type of model being trained  
3. `<LMDIR>`: the path to a directory where the language model files will be stored.  
  - Note there should be no trailing `/`  
4. `<AUXDIR>`: the path to the directory where debug files from scoring stimuli will be stored.  
  - Note there should be no trailing `/`  
5. `<OUTDIR>`: the path to the directory where the scored stimuli files will be stored.  
  - Note there should be no trailing `/`  

For example, to score the stimuli according to an unweighted morph-based phonotactic model that assumes participants attempt to parse stimuli into morphs, use the following code (assuming the directories `phonotactic-models`, `stimuli-scores`, and `stimuli-scores/auxiliaries` have been created):  
  >`sh score-parsed.sh train/morphs-shortvowels_unweighted.txt stimuli-shortvowels_parsed.txt phonotactic-models stimuli-scores/auxiliaries stimuli-scores`  