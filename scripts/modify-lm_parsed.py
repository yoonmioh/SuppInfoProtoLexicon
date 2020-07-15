import sys
import re

def modify_lm(inPath):
    """Alter a language model trained on isolated morphemes, to produce a language
    model that can be used for morphologically decomposing stimuli and evaluating
    their phonotactics.
    The language model is assumed to be in ARPA format (as output by SRILM).
    This altering involves:
        - changing the SOS and EOS symbols both to +, representing a morpheme boundary
          (they have to be collapsed in order to find the most likely segmentation
           with SRILM's hidden-ngram function, because it assumes at most one hidden
           symbol between each observed symbol)
        - blocking insertion of a morpheme boundary after another morpheme boundary
          (+ +), or after a consonant (C +), by setting the corresponding bigram
          costs (log10 probabilities) to -99
    Overwrites the input file in-place.
    """

    CONSONANTS = 'ptkmnNwrfh' # Morpheme boundaries are not possible after consonants
            
    cache = ""
        
    with open(inPath, "r") as inFile:

        boundary_data = dict()
        completed_consonants = list()

        for line in inFile:

            # Decrease the number of unigrams by 1
            if line.startswith("ngram 1"):
                old_number = int(line.strip().split("=")[1])
                new_number = old_number - 1
                line = "ngram 1=%s\n" % new_number

            # Increase the number of bigrams by 1 + the number of consonants
            elif line.startswith("ngram 2"):
                old_number = int(line.strip().split("=")[1])
                new_number = old_number + 1 + len(CONSONANTS)
                line = "ngram 2=%s\n" % new_number

            # Add bigram for + + (cost -99; no alpha)
            elif line.strip() == "\\2-grams:":
                additional_line = "-99\t+ +\n"
                line += additional_line

            # Catch unigram line for </s>
            elif re.match("-\d+\.\d+\t</s>$", line):
                prob = line.split("\t")[0]
                boundary_data["p"] = prob
                line = None

            # Catch unigram line for <s>
            elif re.match("-\d+\t<s>\t-\d\.\d+$", line):
                alpha = line.split("\t")[-1].strip()
                boundary_data["alpha"] = alpha
                line = None

            # Add bigram for C + for all consonants (cost -99; no alpha)
            else:
                consline = re.match("-\d+\.\d+\t([%s]) [ptkmnNwrfhaeiouAEIOU]\t-?\d+\.\d+$" % CONSONANTS, line)
                if consline:
                    consonant = consline.group(1)
                    if consonant not in completed_consonants:
                        additional_line = "-99\t%s +\n" % consonant
                        line = additional_line + line
                        completed_consonants.append(consonant)

            # Create unigram line when possible
            if line is None and len(boundary_data) == 2:
                line = "%(p)s\t+\t%(alpha)s\n" % boundary_data

            # Replace boundaries with +
            if line and "s>" in line:
                line = line.replace("<s>", "+").replace("</s>", "+")

            # Write line
            if line:
                cache += line

    # Write to file
    with open(inPath, "w", newline="") as outFile:
        outFile.write(cache)
                
if __name__ == "__main__":
    inPath = sys.argv[1]
    modify_lm(inPath)