import re

#####   RE.SEARCH()  #####
# usando regular expressions para buscar dados em arquivos, de forma
# equivalente aos métodos .find() e .startswith()
# re.serach retorna True/False

# buscar uma linha que contenha a string 'From:'
hand = open('box-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# buscar uma linha que comece com a string 'From:'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# buscar uma linha que começa com 'X' e mais qualquer outro caractere até os ':'
# O ponto significa qualquer caractere
# O asterisco significa qualquer quantidade de vezes

'^X.*:' # isso representa -> Linha que começa com X, seguido por 
        # quaisquer caracteres, em qualquer quantidade

# Exemplos que retornariam True:
'X-Sieve: CMU Sieve 2.3'
'X-DSPAM-Result: Innocent'
'X-DSPAM-Confidence: 0.8475'
'X-Content-Type-Message-Body: text/plain'

'^X-\S+:'   # isso representa -> Linha que começa com 'X-', seguido por 
            # qualquer caractere diferente de espaço, uma ou mais vezes até os ':'

# Exemplos:
'X-Sieve: CMU Sieve 2.3'                #True
'X-DSPAM-Result: Innocent'              #True
'X-Plane is behind schedule: two weeks' #False - Há um espaço após a palavra Plane


######  RE.FINDALL()  ######

# re.findall() retorna realmente os caracteres que foram pesquisados
# Exemplo:

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# Retorna todos os números entre 0 e 9 que estiverem na string, o sinal + 
# significa que podem retornar um ou mais números.

y = re.findall('[AEIOU]+',x) # Não tem uppercase na string, retorna lista vazia
print(y)

# Greedy matching:
x = 'From: Using the : character'
y = re.findall('^F.+:',x)   # retorno será: 'From: Using the :'
print(y)                    # greedy matching significa que não para no 
                            # primeiro resultado, retorna o quanto for possível
                            # dentro dos parâmetros da regex.

# Non-greedy matching:
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)  # Nesse caso o retorno será: 'From:'
print(y)                    # ou seja, traz apenas a primeira ocorrência

'''

CHEAT SHEET - Python REGEX


^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end

'''  