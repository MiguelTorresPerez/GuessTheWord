import requests
from bs4 import BeautifulSoup
import unidecode

def getWord():
    URL = 'https://dle.rae.es/?m=random'
    dicc = requests.get(URL)
    soup = BeautifulSoup(dicc.content, 'html.parser')
    results = soup.find(id="resultados")
    p = results.find('header', class_='f')
    p = p.text
    palabra = p.split(',', 1)[0]
    return palabra

def get_index_of_letter(letra, palabra):
    palabra = unidecode.unidecode(palabra)
    return [i for i, l in enumerate(palabra) if l == letra]

def asteriskear_bro(palabra):
    return len(palabra)*'*'


def intro():
    print('Bienvenido a guess the word.')   
    

def guess_the_word():
    palabra = getWord()
    palabra_asterisk = asteriskear_bro(palabra)
    intentos = 0
    intro()
    while True:
        if intentos >= 5:
            print('No hay mas intentos')
            print('La palabra era: '+palabra)
            seguirJugando()
        print('Tu palabra es: '+ palabra_asterisk)
        if palabra_asterisk == palabra:
                print('Has acertado la palabra!')
                seguirJugando()
        letra_guess = input('Introduce una letra: ')
        if letra_guess in palabra:
            indexes = get_index_of_letter(letra_guess, palabra)
            for index in indexes:
                palabra_asterisk = palabra_asterisk[:index] + letra_guess + palabra_asterisk[index+1:]
            print('Si, la letra '+letra_guess+' esta en la palabra')
        else:
            intentos += 1
            print('No, la letra '+letra_guess+' no esta en la palabra')
            print('Te quedan {} intentos'.format(5 - intentos))
    

def seguirJugando():
    decision = input('Otra palabra? ye/nop: ')
    if decision == 'ye'.lower():
        guess_the_word()
    else:
        import sys
        sys.exit(0)

        
guess_the_word()
