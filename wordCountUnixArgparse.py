import argparse
from wordCountUtils import wordCountFunctionality

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="filename for which details to generated")
    parser.add_argument("-c", "--bytes", help="Number of bytes in the file", action='store_true')
    parser.add_argument("-m", "--chars", help="Number of characters in the file", action='store_true')
    parser.add_argument("-l", "--lines", help="Number of lines in the file", action='store_true')
    parser.add_argument("-L", "--maxLineLength", help="Maximum line length in the file", action='store_true')
    parser.add_argument("-w", "--words", help="Number of words in the file", action='store_true')
    parser.add_argument("-v", "--version", help="Version Installed", action='store_true')

    args = parser.parse_args()
    filename = args.filename

    if filename == '<stdin>':
        wordCountFunctionality(input(), filename, args.bytes, args.chars, args.lines, args.maxLineLength, args.words, args.version)
    else:
        with open(filename, 'r') as file:
            file_content = file.read()
            wordCountFunctionality(file_content, filename, args.bytes, args.chars, args.lines, args.maxLineLength, args.words, args.version)

if __name__ == '__main__':
    main()