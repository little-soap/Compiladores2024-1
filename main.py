import sys
import logging
from antlr4 import *
from lexer.T1LexerLexer import T1LexerLexer

def readFile():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = T1LexerLexer(input, output)

    while (token := lexer.nextToken()).type is not Token.EOF:
        token_type = lexer.ruleNames[token.type -1]
        if (token_type not in str(['IDENT','CADEIA','NUM_INT','NUM_REAL'])):
            token_type = f"'{token.text}'"

        output.write(f"<'{token.text}',{token_type}>\n")

if __name__ == "__main__":
    try:
        readFile()
    except Exception as error:
        logging.error(error)