fruit = 'banana'
# print("fruit = 'banana'")
letter = fruit[1]
# print(f"\nPrimeira letra de fruit é '{letter}', e não a zerésima, se liga em :D\n")
'''
A expressão entre colchetes se chama índice, e é basicamente a posição de um certo caractere, lembrando que
isso se aplica no caso da variável possuir apenas um único valor, pois se a mesma variável fosse uma lista, então
o índicie representaria a posição de um elemento da lista, e não o caractere.
'''
i = 1
# print(fruit[i])  # Expressões usando variáveis também são legais;
# print(fruit[i + 1])  # Jamais poderá ser um número float, apenas inteiros.

# Temos uma função que retorna a quantidade de caracteres da string, chama-se: len; obs: a função len
# não conta o primeiro caractere como zero, e sim 1, ou seja, dentro de len não existe o zerésimo caractere.
length = len(fruit)  # <-- retorna 6

# Para se obter o último caractere da string basta executar essa instrução ↓;
last = fruit[length - 1]  # fruit possui 5 caracteres: b[0],a[1],n[2],a[3],n[4],a[5];
# print(last)
'''
Como havia falado antes, len não começa contando do zerésimo caractere, por isso, a instrução acima resultará em erro
de execução; porém as variáveis sim, elas começam contando do zerésimo caractere e por isso usamos -1, na expressão
acima
'''
# Também pode-se usar índices negativos para começar a contagem do último caractere, basta usar fruit[-1]
# print(fruit[-1])
# print(fruit[-6])  # Perceba que quando o índicie é negativo a contagem não começa de 0, afinal, 0 é o primeiro
# caractere

# ----------------------------------------------------------------------------------------------------------------------
# loop com usando operações com strings;

def soletre(s): #Uma função que imprime caractere de uma string um a um;
    index = 0
    while index < len(s):
        letter = s[index]
        print(letter)
        index += 1

soletre('Arquimestre')

print('-'*70)

def soletre_ao_contrário(s, índice = -1):  #Uma função que imprime os caracteres de trás pra frente
    while True:
        print(s[índice])
        size = len(s)*-1
        índice -=1
        if índice == size:
            break
    print(s[0])

soletre_ao_contrário('mestre assassino')
print('-'*70)

# Verificação de palíndromo em python:
def is_palindrome(word):
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

is_palindrome("tenet")
print('-'*70)
# Uma forma de fazer travessia com o loop for: ↓
for letter in fruit:
    print(letter)
'''
Cada vez que o programa passar pelo loop, o caractere seguinte na string é atribuído à variável letter, o loop continua
até que não sobre nenhum caractere;
'''
# Concatenação e um loop for para gerar uma série abecedária;
print('-'*70)

prefixes = 'J','K','L','M','N','Ou','P','Qu'; print(prefixes)
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)
print('-'*70)

# Fatiamento de stings;

s = 'Monty Python'
print(s)  # <--Retorna: 'Monty Python'
print(s[0:5])  # <--Retorna: 'Monty'
print(s[0:6])  # <--Retorna: 'Monty ' embora no console não apareça o espaço, ele existe;
'''
O operador [n:m] retorna a parte da string do "enésimo" caractere ao "emésimo",
incluindo o primeiro, porém, excluindo o último, veja o exemplo abaixo ↓;
'''
print(len(s)) #como sabemos, len() retorna a qtda. de caracteres sem
              # começar do zerésimo caractere
print(s[6:12])
print('-'*70)
'''
Dica para trabalhar com fatiamento de strings:

Em sua cabeça comece contando o zerésimo caractere como o primeiro, no caso de s, samebos que possui 11 caracteres
porém assim como a função len() o operador [n:m] tem uma lógica minimamente parecida, use isso ao seu favor;
'''
print(fruit[:3])  # <--Retorna 'ban', é como se eu dissesse: vá até a letra m;
print(fruit[3:])  # <--Retorna 'ana', é como se eu dissesse: vá de m até o fim;
print(fruit[3:3])  # <--Retorna uma string vazia, ela existe, representada por um espaço no console,
# porém com o comprimento zero,
print(fruit[:])  # <--Retorna a mesma coisa, pois basicamente a instrução recebe argumentos vazios;

#-----------------------------------------------------------------------------------------------------------------------
#Buscando ↓;
def find(word, letter):  # <-- Essa função retorna o índice da letra na primeira vez que ela aparece na palavra;
    index = 0            # <-- caso não apareça, retornará None.
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return None

print(find("banana","x"))
#print(find("banana"[3:], "n"))

print("-"*90)

#Métodos de strings:

word = "banana"

word_upper = word.upper()  # <-- Ao invocarmos este método, ele transforma todas as letras da string em maiúsculas.
                           #quando atribuímos uma variável a string, caso contrário não terá efeito

index = word.find("a")  # <-- O método find() encontra um caractere na string e retorna o seu índice.
index_false = word.find("x")  # <-- Caso ele não encontre o caractere; retornará: -1.

'''
Na verdade este método é mais geral que nossa função, porque ele também consegue encontrar substrings e seu índice,
que sempre será referente ao primeiro caractere, por exemplo: a string "banana" possui 5 caracteres, caso eu queira
encontar a substring 'na' nela, a função retornará o índice: 2.
'''
print(word.find('na'))
'''
O método find() pode receber um segundo argumento, o seu índice de onde deve começar, e um terceiro, que indica onde
deve parar, porém, eles são argumentos opcionais
'''
print(word.find("na",0,4))

#Expicando o operador in:
'''É um operador booleano e binário, que recebe duas strings, e retorna True se a primeira aparecer como uma substring
da segunda'''

print("a" in "banana")  # <-- retorna True.
print("x" in "banana")  # <-- retorna False.

a = "a"
fruit = "banana"

#A mesma lógica se aplica caso a substring ou a string estivessem atribuidas a uma variável:
print(a in fruit)

print("-"*150)

def count_letters_in_word(letter,word):  # <-- Uma função que retorna a quantidade de vezes que uma letra aparece em uma
    index = 0                            # palavra
    count = 0
    while index < len(word):
        if letter in word[index]:
            count += 1
        index += 1
    print(f'A letra: {letter}, aparece {count} vezes na palavra {word}!')

count_letters_in_word("a","banana")

print("-"*150)
def in_both(word1, word2):  # <-- Essa função imprime todas as letras de word1, que aparecem em word2.
    for letter in word1:
        if letter in word2:
            print(letter)

in_both("javascript","java")

# Comparação de Strings:
print("-"*150)
def comprove_se_é_banana(banana_plmds):
    banana_minuscula = banana_plmds.lower()
    if banana_minuscula < "banana":
        print(f"Sua palavra '{banana_minuscula}', é menor que banana\nsendo assim é melhor eu me matar mesmo, quero "
              f"nem saber nessa jolonga veia")
    if banana_minuscula > "banana":
        print(f"Sua palavra '{banana_minuscula}', é maior que banana\nsendo assim é melhor eu me matar mesmo, quero "
              f"nem saber nessa jolonga veia")
    else:
        print("Yes, bananassssssssssssssssssssss!, i love bananas.")

comprove_se_é_banana("danana")
print("-"*150)
def is_reverse(word1, word2):
    if len(word1) != len(word2)-1:
        return False

    i = 0
    j = len(word2)

    while j > 0:
        print(i, j)
        if word1[i] != word[j]:
            return False

        i += 1
        j -= 1
    return True

print(is_reverse("banana", "pizzas"))

# alguns métodos de strings; documentação em --> https://docs.python.org/3/library/stdtypes.html#string-methods.
print("-"*150)

str = "      abocanhe bem na artéria"

print(str.capitalize())  # <-- Retorna uma cópia da string com seu primeiro caractere em maiúscula;

print(str.replace('artéria','veia'))  # <-- Retorna uma cópia da string com uma fatia substituída;

print(str.strip())  # <-- Retorna uma cópia da string sem os espaços redundantes do início e do fim;

print(str.count("a"))  # <-- Retorna a qtde. de vezes que uma fatia aparece na string.

print("-"*150)
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True

def separa_ae():
    print("-"*150)
print(any_lowercase1("bAnana"))  # Esta função verifica se apenas a primeira letra é minúscula.
separa_ae()

print(any_lowercase2(" "))  # Sempre retornará True, pq 'c' é uma letra minúscula, e veja, ele retorna uma string
                            # 'True', e não a palavra reservada, no fim é uma pegadinha de muito MAL GOSTO.
separa_ae()
print(any_lowercase3("b "))  # Se nem todas as letras da string forem maiúsculas, sempre retornará True.

separa_ae()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'.upper()

def travessia_do_alfabeto(índice):
    print(alfabeto[índice])
    if alfabeto.find('z'):
        return
    travessia_do_alfabeto(índice +1)