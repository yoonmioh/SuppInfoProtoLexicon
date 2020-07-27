# Non-Māori-speaking New Zealanders have a Māori proto-lexicon
## Exp2 stimulus phonotactic probabilities
*Yoon Mi Oh, Simon Todd, Clay Beckner, Jen Hay, Jeanette King, and Jeremy Needle*

## Contents

This directory contains phonotactic probabilities for the stimuli in Exp2, calculated in various ways from different training data.

Each file is in CSV format and contains two columns: `item`, which represents the stimulus (in a format that assigns each phoneme to a single character in the Latin alphabet); and `logprob`, which is the log-phonotactic-probability for the stimulus, including the END token (base 10).

The details of the calculation and training data for each file, as well as the stage of the Exp2 analysis they are introduced in, are as follows:

- `borrowings-shortvowels_types.csv`: probabilities from a word-based model, trained on 1,760 Māori borrowing word types in NZ English, with vowel length distinctions collapsed (introduced in Stage 4)  
- `dict_tokens.csv`: probabilities from a word-based model, trained on corpus-based tokens of all words in the *Te Aka* dictionary, with vowel length distinctions preserved (introduced in Stage 1)  
- `dict_types.csv`:  probabilities from a word-based model, trained on all word types in the *Te Aka* dictionary, with vowel length distinctions preserved (introduced in Stage 1)  
- `dict-longA_types.csv`: probabilities from a word-based model, trained on all word types in the *Te Aka* dictionary, with the /a~a:/ distinction preserved but all other vowel length distinctions collapsed (introduced in Stage 2)  
- `dict-shortvowels_types.csv`: probabilities from a word-based model, trained on all word types in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 2)  
- `morphs-shortvowels_tokens_parsed.csv`: probabilities from a morph-based model assuming participants attempt to parse stimuli into morphs, trained on corpus-based tokens of morphs from all words in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 5)  
- `morphs-shortvowels_types_parsed.csv`: probabilities from a morph-based model assuming participants attempt to parse stimuli into morphs, trained on morph types from all words in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 5)  
- `morphs-shortvowels_types_unparsed.csv`: probabilities from a morph-based model assuming participants do not parse stimuli into morphs, trained on morph types from all words in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 6)  
- `morphs-shortvowels_types-NBestWords-unweighted_parsed.csv`: probabilities from a morph-based model assuming participants attempt to parse stimuli into morphs, trained on unique/unweighted morph types from the 3,164 highest-frequency words in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 7)  
- `morphs-shortvowels_types-NBestWords-weighted_parsed.csv`: probabilities from a morph-based model assuming participants attempt to parse stimuli into morphs, trained on non-unique/weighted morph types from the 3,164 highest-frequency words in the *Te Aka* dictionary, with vowel length distinctions collapsed (introduced in Stage 7)  
- `rs_segmented.csv`: probabilities from a word-based model, trained on all tokens in spoken Māori corpora, with vowel length distinctions preserved (introduced in Stage 1)  
- `rs_unsegmented.csv`: probabilities from a speech-stream-based model, trained on all uninterrupted speech streams in spoken Māori corpora (not segmented into words), with vowel length distinctions preserved (introduced in Stage 1)  
- `NBestFixed-morph-shortvowels/`: a directory containing probabilities from morph-based models, trained on morph types from all words in the *Te Aka* dictionary that have frequency greater than or equal to *k* for *k* from 0 to 6, with vowel length distinctions collapsed (introduced in Stage 6). Subdirectories contain different probabilities, depending on whether participants are assumed to attempt to parse stimuli into morphs or not  
- `NBestFixed-word-shortvowels/`: a directory containing probabilities from word-based models, trained on word types in the *Te Aka* dictionary that have frequency greater than or equal to *k* for *k* from 0 to 8, with vowel length distinctions collapsed (introduced in Stage 3)  