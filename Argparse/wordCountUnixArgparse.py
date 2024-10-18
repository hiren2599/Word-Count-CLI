import argparse
from pathlib import Path

def getWordCount(file_content):
    return len(file_content.split())

def wordCountFunctionality(file_content):
    isFlagUsed = False
    isVersionUsed = False
    finalOutput = ''

    if args.bytes:
        finalOutput += str(Path(filename).stat().st_size) + ' '
        isFlagUsed = True
    
    if args.chars:
        finalOutput += str(len(file_content)) + ' '
        isFlagUsed = True

    if args.lines:
        finalOutput += str(len(file_content.splitlines())) + ' '
        isFlagUsed = True

    if args.maxlinelength:
        finalOutput += str(len(sorted(file_content.splitlines(), key = lambda line: len(line))[0])) + ' '
        isFlagUsed = True

    if args.words:
        finalOutput += str(getWordCount(file_content)) + ' '
        isFlagUsed = True
    
    if args.version:
        finalOutput += 'version - 1.0.0 '
        isFlagUsed = True
        isVersionUsed = True
    
    if not isFlagUsed:
        finalOutput += str(len(file_content.splitlines())) + ' '
        finalOutput += str(getWordCount(file_content)) + ' '
        finalOutput += str(Path(filename).stat().st_size) + ' '
    
    if not isVersionUsed:
        finalOutput += filename
    
    print(finalOutput)


parser = argparse.ArgumentParser()

parser.add_argument("filename", help="filename for which details to generated")
parser.add_argument("-c", "--bytes", help="Number of bytes in the file", action='store_true')
parser.add_argument("-m", "--chars", help="Number of characters in the file", action='store_true')
parser.add_argument("-l", "--lines", help="Number of lines in the file", action='store_true')
parser.add_argument("-L", "--maxlinelength", help="Maximum line length in the file", action='store_true')
parser.add_argument("-w", "--words", help="Number of words in the file", action='store_true')
parser.add_argument("-v", "--version", help="Version Installed", action='store_true')

args = parser.parse_args()
filename = args.filename

if filename == '<stdin>':
    wordCountFunctionality(input())
else:
    with open(filename, 'r') as file:
        file_content = file.read()
        wordCountFunctionality(file_content)
        