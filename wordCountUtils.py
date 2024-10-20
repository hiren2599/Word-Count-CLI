from pathlib import Path

def getWordCount(file_content):
    return len(file_content.split())

def wordCountFunctionality(file_content, filename, bytes, chars, lines, maxLineLength, words, version):
    isFlagUsed = False
    isVersionUsed = False
    finalOutput = ''

    if bytes:
        finalOutput += str(Path(filename).stat().st_size) + ' '
        isFlagUsed = True
    
    if chars:
        finalOutput += str(len(file_content)) + ' '
        isFlagUsed = True

    if lines:
        finalOutput += str(len(file_content.splitlines())) + ' '
        isFlagUsed = True

    if maxLineLength:
        finalOutput += str(len(sorted(file_content.splitlines(), key = lambda line: len(line))[0])) + ' '
        isFlagUsed = True

    if words:
        finalOutput += str(getWordCount(file_content)) + ' '
        isFlagUsed = True
    
    if version:
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