import re
import os
import argparse

def srilm_chunker(inPath):
    """Gets a chunk of information from a SRILM output file, representing everything
    corresponding to a single input."""
    with open(inPath, "r") as inFile:
        linegroup = list()
        for line in inFile:
            if line == "\n":
                yield linegroup
                linegroup = list()
            elif line.startswith("file"):
                return
            else:
                linegroup.append(line.strip())
                
def line_streamer(inPath):
    """A generator for stripped lines in a file"""
    with open(inPath, "r") as inFile:
        for line in inFile:
            yield line.strip()

def word_generator(inPath, wordlistPath, parsed=False):
    """A generator to process a chunk of information from SRILM, extracting the
    input word and its log-probability."""
    
    chunker = srilm_chunker(inPath)
    wordlist = line_streamer(wordlistPath)
    
    # Get the file one chunk at a time
    for linegroup in chunker:
        
        # Get key information
        word = next(wordlist).replace(" ", "")
        scoreline = linegroup[-1]
        logprob = re.search("(?<=\s)-?\d+\.?\d*", scoreline).group(0)
        
        # Adjustments if the phonotactic model assumes parsing of stimuli
        if parsed:
            # Remove morph boundaries from word
            word = word.replace("+", "")
            # Remove the logprob for the first transition (START morph boundary)
            firsttransline = linegroup[1]
            first_logprob = re.search("\[ (-\d\.\d+) \]", firsttransline).group(1)
            logprob = str(float(logprob) - float(first_logprob))
        
        # Yield
        yield(word, logprob)
    
    
def process_file(inPath, outDir, wordlistPath, parsed=False):
    """Convert a SRILM debug file to CSV format"""
    
    scoredWords = word_generator(inPath, wordlistPath, parsed)
    
    inDir, inFilename = os.path.split(inPath)
    inRoot = ".".join(inFilename.split(".")[:-1])
    
    outPath = "%s/%s.csv" % (outDir, inRoot)
    
    with open(outPath, "w") as outFile:
        
        # write header
        outFile.write("item,logprob")
        
        for scoredWord in scoredWords:
            outFile.write("\n" + ",".join(scoredWord))

                        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inPath")
    parser.add_argument("outDir")
    parser.add_argument("wordlistPath")
    parser.add_argument("--parsed", action="store_true")
    args = parser.parse_args()
    
    if "-shortvowels" in args.wordlistPath:
        args.wordlistPath = args.wordlistPath.replace("-shortvowels", "")
    elif "-longA" in args.wordlistPath:
        args.wordlistPath = args.wordlistPath.replace("-longA", "")
    if "_parsed" in args.wordlistPath:
        args.wordlistPath = args.wordlistPath.replace("_parsed", "")
    
    process_file(args.inPath, args.outDir, args.wordlistPath, parsed=args.parsed)