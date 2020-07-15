# An Adult Proto-lexicon
## Analysis dump states
*Yoon Mi Oh, Simon Todd, Clay Beckner, Jen Hay, Jeanette King, and Jeremy Needle*

## Contents

This directory contains dumped states from parts of the analysis that take a long time to run.

The states are split among two subdirectories:

- `clmm/`: a subdirectory containing ordinal mixed-effects regression models in RDS format, fit in `R` using the function `clmm` from the package `ordinal`  
- `monte-carlo/`: a subdirectory containing the AIC values of ordinal regression models fit during the word- and morph-based Monte Carlo analyses, in TXT format  