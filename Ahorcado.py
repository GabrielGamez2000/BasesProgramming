#realizar un programa que permita jugar al ahorcado, siguiendo estos requerimientos
'''Para tener en cuenta:
Representa las palabras en una matriz de tipo cadena de tamaño 5 x 5.
El usuario debe seleccionar una categoría y luego el programa, aleatoriamente, calcula una palabra de las opciones de la categoría seleccionada.
Seguidamente se muestra al usuario por medio de underlines "_" la cantidad de letras que tiene la palabra oculta que debe adivinar.
El usuario ira digitando una letra a la vez para tratar de adivinar las letras de la palabra.
Se debe hacer un control de intentos. Cada partida tendrá un mínimo de intentos y este control se hará por medio de la representación de un personaje ahorcado. Se hará usando la técnica vista en la sesión presencial, ASCII art.
Si el usuario adivina la palabra se muestra un mensaje de felicitación y se da la posibilidad de volver a escoger otra categoría para continuar jugando.
Si el usuario acumula el total de opciones fallidas, pierde y queda ahorcado en la imagen de seguimiento. Se muestra un mensaje de partida perdida y se lleva al usuario a seleccionar otra categoría para seguir jugando.'''
#Presentado por: Gabriel Gamez Rojas
import random
import time
from os import system

def figuras_ahorcado(figura):
    matriz_figuras=['''
        +-------+
        |       |
                |
                |
                |
                |
        =========''','''
        +-------+
        |       |
        0       |
                |
                |
                |
        =========''','''
        +-------+
        |       |
        0       |
        |       |
                |
                |
        =========''','''
        +-------+
        |       |
        0       |
       /|       |
                |
                |
        =========''','''
        +-------+
        |       |
        0       |
       /|\      |
                |
                |
        =========''','''
        +-------+
        |       |
        0       |
       /|\      |
       /        |
                |
        =========''','''
        +-------+
        |       |
        0       |
       /|\      |
       / \      |
                |
        =========''']
    print(matriz_figuras[figura])
def opcionrandom(categoria):
    return random.choice(categoria)
def comprobaciones_juego(vidas,palabra_usuario,figura):
    while vidas >0:
            fallas=0
            for letra in palabrasecreta:
                if letra in palabra_usuario:
                    print(letra,end='')
                else:
                    print('_', end='')
                    fallas+=1
            if fallas==0:
                system('cls')
                print('')
                print('Felicidades, Has ganado')
                time.sleep(5)
                system('cls')
                break
            print('')
            letra_usuario=input('Ingresa una letra: ')
            palabra_usuario+=letra_usuario
            if letra_usuario not in palabrasecreta:
                system('cls')
                print('la letra no corresponde')
                vidas-=1
                figura+=1
                print(f'te quedan {vidas} vidas')
                if figura<=6:
                    figuras_ahorcado(figura)
            if vidas==0:
                system('cls')
                print('has perdido')
                time.sleep(5)
                system('cls')
                break

categoria_paises=['colombia','mexico','canada','francia','inglaterra']
categoria_frutas=['mango','fresa','naranja','manzana', 'pera']
categoria_generosmusicales=['rock','bachata','clasico','reggaeton','balada']
categoria_animales=['perro','raton','elefante','murcielago','caballo']
categoria_peliculas=['titanic','avatar','inception','avengers','cruella']

matriz_palabras=[categoria_paises, categoria_frutas, categoria_generosmusicales, categoria_animales, categoria_peliculas] #crear la matriz de palabaras con las listas creadas
comenzar=True
while comenzar==True:
    print('Bienvenido al juego del ahorcado')
    time.sleep(2)
    categorias=['1.Paises','2.Frutas','3.Generos Musicales','4.Animales','5.Peliculas','0.Cerrar juego','6. Ver Respuestas']
    print('las categorias para jugar son:')
    for elements in categorias:
        print(elements)
    opcion_categoria=int(input('Escoja la categoria que desea jugar: '))
    if opcion_categoria==1:
        system('cls')
        print('Categoria "Paises"')
        palabrasecreta=opcionrandom(categoria_paises)
        palabra_usuario=''
        print('')
        vidas=6 #correspondiente al numero de dibujos
        figura=0
        figuras_ahorcado(figura)
        print(f'La palabra tiene {len(palabrasecreta)} letras')
        comprobaciones_juego(vidas,palabra_usuario,figura)
    elif opcion_categoria==2:
        print('Categoria "Frutas"')
        palabrasecreta=opcionrandom(categoria_frutas)
        palabra_usuario=''
        system('cls')
        print('')
        vidas=6 #correspondiente al numero de dibujos
        figura=0
        figuras_ahorcado(figura)
        print(f'La palabra tiene {len(palabrasecreta)} letras')
        comprobaciones_juego(vidas,palabra_usuario,figura)
    elif opcion_categoria==3:
        print('Categoria "Generos Musicales"')
        palabrasecreta=opcionrandom(categoria_generosmusicales)
        palabra_usuario=''
        system('cls')
        print('')
        vidas=6 #correspondiente al numero de dibujos
        figura=0
        figuras_ahorcado(figura)
        print(f'La palabra tiene {len(palabrasecreta)} letras')
        comprobaciones_juego(vidas,palabra_usuario,figura)
    elif opcion_categoria==4:
        print('Categoria "Animales"')
        palabrasecreta=opcionrandom(categoria_animales)
        palabra_usuario=''
        system('cls')
        print('')
        vidas=6 #correspondiente al numero de dibujos
        figura=0
        figuras_ahorcado(figura)
        print(f'La palabra tiene {len(palabrasecreta)} letras')
        comprobaciones_juego(vidas,palabra_usuario,figura)
    elif opcion_categoria==5:
        print('Categoria "Peliculas"')
        palabrasecreta=opcionrandom(categoria_peliculas)
        palabra_usuario=''
        system('cls')
        print('')
        vidas=6 #correspondiente al numero de dibujos
        figura=0
        figuras_ahorcado(figura)
        print(f'La palabra tiene {len(palabrasecreta)} letras')
        comprobaciones_juego(vidas,palabra_usuario,figura)
    elif opcion_categoria==0:
        system('cls')
        print('Hasta luego')
        break
    elif opcion_categoria==6:
        print(matriz_palabras)
        break
    else:
        system('cls')
        print('te has equivocado, escoge una categoria valida')