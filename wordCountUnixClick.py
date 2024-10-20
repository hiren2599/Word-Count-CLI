import click
from Utility.wordCountUtils import wordCountFunctionality

@click.command()
@click.argument("filename")
@click.option("-c", "--bytes", is_flag=True, show_default=True, default=False, help="Number of bytes in the file")
@click.option("-m", "--chars", is_flag=True, show_default=True, default=False, help="Number of characters in the file")
@click.option("-l", "--lines", is_flag=True, show_default=True, default=False, help="Number of lines in the file")
@click.option("-L", "--max-line-length", "maxLineLength", is_flag=True, show_default=True, default=False, help="Maximum line length in the file")
@click.option("-w", "--words", is_flag=True, show_default=True, default=False, help="Number of words in the file")
@click.option("-v", "--version", is_flag=True, show_default=True, default=False, help="Version Installed")
def wordCountCommand(filename, bytes, chars, lines, maxLineLength, words, version):
    if filename == '<stdin>':
        wordCountFunctionality(input(), filename, bytes, chars, lines, maxLineLength, words, version)
    else:
        with open(filename, 'r') as file:
            file_content = file.read()
            wordCountFunctionality(file_content, filename, bytes, chars, lines, maxLineLength, words, version)

if __name__ == '__main__':
    wordCountCommand()