# Primeiro trabalho de compiladores

## Aluno
Lucas Roberto da Silva - 760929  

### COMO EXECUTAR
    # Tenha instalado o runtime para python
    $ pip install antlr4-python3-runtime

    # Tenha instalado as ferramentas do ANTLR4
    $ pip install antlr4-tools

    # Gere o lexer
    $ antlr4 -Dlanguage=Python3 T1Lexer.g4 -o "lexer"

    # Teste o lexer manualmente
    $ py main.py "casos-de-teste\1.casos_teste_t1\entrada\1-algoritmo_2-2_apostila_LA.txt" "saida.txt"

    # Verifique a saída no arquivo saida.txt criado na pasta raiz do projeto

    # Utilize o corretor automático para executar todos os testes
    $ java -jar "corretor\corretor.jar" "build\exe.win-amd64-3.12\main.exe" gcc "temp" "casos-de-teste" "760929" t1