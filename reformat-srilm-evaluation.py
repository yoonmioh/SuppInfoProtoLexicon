import sys
import re
import os

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

def word_generator(inPath, wordlistPath):
    """A generator to process a chunk of information from SRILM, extracting the
    input word, its length (in characters and in transitions), and its scores
    (log-probability and perplexity)."""
    
    chunker = srilm_chunker(inPath)
    wordlist = line_streamer(wordlistPath)
    
    # Get the file one chunk at a time
    for linegroup in chunker:
        
        # Get key information
        word = next(wordlist).replace(" ", "")
        scoreline = linegroup[-1]
            
        # Now extract key information
        length_chars = len(word)
        logprob, ppl, ppl1 = re.findall("(?<=\s)-?\d+\.?\d*", scoreline)
        
        # Yield
        yield(word, str(length_chars), logprob, ppl, ppl1)
    
    
def process_file(inPath, outDir, wordlistPath):
    """Convert a SRILM debug file (generated with -debug 1) to CSV format"""
    
    scoredWords = word_generator(inPath, wordlistPath)
    
    inDir, inFilename = os.path.split(inPath)
    inRoot = ".".join(inFilename.split(".")[:-1])
    
    outPath = "%s/%s.csv" % (outDir, inRoot)
    
    with open(outPath, "w") as outFile:
        
        # write header
        outFile.write("item,length,logprob,ppl,ppl1")
        
        for scoredWord in scoredWords:
            outFile.write("\n" + ",".join(scoredWord))

                        
if __name__ == "__main__":
    inPath, outDir, wordlistPath = sys.argv[1:]
    if "-shortvowels" in wordlistPath:
        wordlistPath = wordlistPath.replace("-shortvowels", "")
    elif "-longA" in wordlistPath:
        wordlistPath = wordlistPath.replace("-longA", "")
    if "_morphs" in wordlistPath:
        wordlistPath = wordlistPath.replace("_morphs", "")
    process_file(inPath, outDir, wordlistPath)