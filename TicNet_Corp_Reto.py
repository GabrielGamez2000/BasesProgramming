'''El presente codigo de programación recopila los retos del ciclo 1 de Fundamentos de Programación
es presentado por Gabriel Gamez Rojas para el grupo 202150-51654'''
#MODULOS IMPORTADOS

from os import system # importa lo necesario para borrar la consola cuando se necesita
import math #importa lo necesario para hacer calculos matematicos
import csv #importa lo necesario para el manejo de archivos 
import pandas as pd #importa lo necesario para manejo de de archivos

#FUNCIONES DEL CODIGO
def login(): #función para hacer el proceso de login o inicio de sesión - Incluye Easter Egg 
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI') 
    nombre_usuario='51654' # RF02: una variable cuyo valor es el codigo del grupo al que pertenezco "51654" - de forma predefinida
    contrasena='45615' #RF02: una variable cuyo valor es el codigo del grupo al que pertenezco de forma inversa "45615" - de forma predefinida
    nombre_usuario_easteregg='Tripulante2022'
    constraseña_easteregg='m1s10nt1c'
    nombre_digitado=input('Ingrese a continuacion el nombre de usuario: ') # RF02: variable51654 que capta el ingreso del nombre de usuario
    if nombre_digitado==nombre_usuario: #RF02: esta funcion valida que el nombre de usuario ingresado sea igual al solicitado
        contrasena_digitada=input('Ingrese a continuacion la contraseña de ingreso: ') #RF02: esta variable capta la contraseña de ingreso al sistema, esta dentro del if por la verificacion que se debe hacer
        if contrasena_digitada==contrasena: #RF02: esta funcion valida que la contraseña ingresada por el usuario sea igual a la solicitada
            #RF03: una vez ingresados usuario y contraseña, el programa solicita un captcha
            primer_termino=654 #RF03: el primer termino del captcha es los ultimos tres digitos del codigo del grupo "654"
            segundo_termino=((6*4)/(5+1))+1 #RF03: el segundo termino, es una serie de opraciones matematicas, cuyo resultado es igual al penultimo digito del codigo del curso "5"
            captcha=int((input('Ingrese a continuacion el captacha solicitado: captcha = 654 + 5: '))) #RF03: mediante esta funcion captamos el ingreso del valor del captcha que debe ser igual a "659"
            if captcha==primer_termino+segundo_termino: #RF03: con esta funcion validamos que el usuario ha ingresado coorectamente el captcha
                system('cls') #este comando borra la consola, para limpiar la interfaz
                print('Sesión iniciada') #RF04: mensaje de inicio de sesion
                pass
            else:
                borrar()
                print('Error') #RF03: error suscitado por ingresar incorrectamente el captcha
                quit()
        elif contrasena_digitada==constraseña_easteregg:
            print('Usted ha ingrasado al easter egg para calcular el promedio de unas latitudes')
            EasterEgg_3()
        else:
            borrar()
            print('Error') #RF02: Error suscitado por ingresar incorrectamente la contraseña
            quit()
    elif nombre_digitado==nombre_usuario_easteregg:
        print('Este fue mi primer programa y vamos por más')
        quit()
    else: 
        borrar()
        print('Error') #RF02: error suscitado por ingresar incorrectamente el usuario 
        quit()
def menú_principal(lista_menu_no_numerada): #con esta función se imprime en terminal la lista numerada de las opciones del menú
    print(
    str(' 1. '),lista_menu_no_numerada[0], ('\n'),
    str('2. '),lista_menu_no_numerada[1], ('\n'),
    str('3. '),lista_menu_no_numerada[2], ('\n'),
    str('4. '),lista_menu_no_numerada[3], ('\n'),
    str('5. '),lista_menu_no_numerada[4], ('\n'),
    str('6. '),lista_menu_no_numerada[5], ('\n'),
    str('7. '),lista_menu_no_numerada[6], ('\n'))
def cambiar_opciones(menu_opciones, opcion_favorita): #Con está función se hace el cambió de opciones favoritas en el menú opciones.
    aux=menu_opciones.pop(opcion_favorita-1)
    menu_opciones.insert(0,aux)
    return menu_opciones
def opcion_favorita(menu_opciones): #Escoger la opción favorita del usuario y colocarla en la primera opcion del menú principal
    opcion_favorita=int(input('Seleccione opción favorita: ')) #RF02:esta varibale captura la opcion favorita del usuario
    if 1<=opcion_favorita<=5:
        primera_adivinanza=int(input('Para confirmar porfavor responda: Los tienes en las manos y los tienes en los pies y enseguida sabrás qué número es: ')) #RF02:esta es la primera adivinanza para validar la opcion escogida
        if primera_adivinanza==5: #la respuesta a la primera adivinanza es 5
            segunda_adivinanza=int(input('Para confirmar porfavor responda: Represento las estaciones del año y los puntos cardinales, ¿Quien soy?: ')) #RF02:esta es la segunda adivinaza para la validacion, respuesta=4
            if segunda_adivinanza==4:
                borrar()
                menu_opciones=cambiar_opciones(menu_opciones,opcion_favorita)
            else: #RF02:error ocasionado si el usuario digita mal la 2 adivinanzas, se vuelve al menu original
                borrar_error()
        else: #RF02:error ocasionado si el usuario digita mal la 1 adivinanzas, se vuelve al menu original
            borrar_error()
    else:
        borrar_error()
        quit()
def EasterEgg_1(): #Easter egg para determinar si el usuario esta en el hemisferio norte o sur
    latitud_usuario=float(input('Dame una latitud y te diré cual hemisferio es…: '))
    if latitud_usuario>0:
        print('Usted está en hemisferio norte')
    elif latitud_usuario<0:
        print('Usted está en hemisferio sur')
    else:
        print('Usted esta en la linea del Ecuador')
    quit()
def EasterEgg_2():#Easter Egg para determinar el huso horario del usuario
    longitud_usuario=float(input('Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario: '))
    if -35.833<=longitud_usuario<=54.316:
        print('El huso horario es -3')
        quit()
    elif (-54.316<=longitud_usuario<=-35.833) or (54.316<=longitud_usuario<=67.402):
        print('El huso horario es -4')
        quit()
    elif (-67.401<=longitud_usuario<=-54.316) or (67.402<=longitud_usuario<=81.296):
        print('El huso horario es -5')
        quit()
def EasterEgg_3(): #Easter Egg para determinar el promedio de n latitudes ingresadas
    cantidad_latitudes=int(input('¿Cuantas latitudes hacen parte del calculo del promedio?: '))
    suma=0
    for i in range (cantidad_latitudes):
        latitud=float(input(f'Ingrese la {i+1} latitud: '))
        suma=suma+latitud
    promedio=suma/cantidad_latitudes
    promedio=round(promedio,3)
    print(f'El promedio de las latitudes ingresadas es: [{promedio}]')
    quit()
def borrar(): #funcion para borrar consola
    system('cls')
def borrar_error(): #funcion para borrar consola e imprimir mensaje de error
    system('cls')
    print('Error')
def error_coordenada(): #Función con la cual se imprime error cuando ingresa una coordenada fuera del rango estipulado
    borrar()
    print('Error coordenada')
    quit()
def actualizar_coordenada(opcion_actualizar_coordenada, matriz_coordenadas): #Función para actualizar coordenadas, cuando ya fueron ingresadas
    if 1<=opcion_actualizar_coordenada<=3:
        latitud_cnueva=float(input(f'Ingrese la latitud de la {opcion_actualizar_coordenada} coordenada: '))       
        if 9.757<=latitud_cnueva<=10.462:   
            longitud_cnueva=float(input(f'Ingrese la longitud de la {opcion_actualizar_coordenada} coordenada: '))
            if -73.623<=longitud_cnueva<=-72.987:
                matriz_coordenadas[opcion_actualizar_coordenada-1]=latitud_cnueva, longitud_cnueva
                borrar()
                print('Coordenadas actualizadas')
            else:
                borrar()
                print('Error actualización')
                quit()
        else:
            borrar()
            print('Error actualización')
            quit()
    elif opcion_actualizar_coordenada==0:
        borrar()
    else: 
        borrar()
        print('Error actualización')
        quit()
def calcular_distancia(zona_wifi_i,ubicacion_actual): #Función para calcular la distanacia entre la coordenada de posición del usuario, y un punto de de acceso wifi
    r=6371 #esta en kilometros
    lat2=zona_wifi_i[0]
    lat1=matriz_coordenadas[ubicacion_actual-1][0]
    lon2=zona_wifi_i[1]
    lon1=matriz_coordenadas[ubicacion_actual-1][1]
    deltalat = math.radians((lat2 - lat1))
    deltalon= math.radians((lon2 - lon1))
    operacion_1 = math.sin(deltalat/2) * math.sin(deltalat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(deltalon/2) * math.sin(deltalon/2)
    operacion_2 = 2 * math.atan2(math.sqrt(operacion_1), math.sqrt(1-operacion_1))
    distancia=operacion_2*r
    distancia=round(distancia,2)
    return distancia
def comparar_distancias(zona_wifi_1,zona_wifi_2,zona_wifi_3,zona_wifi_4,ubicacion_actual): #Función para comparar distancias y ordenar deacuerdo con cual es la mas cercana
    distancia_1=calcular_distancia(zona_wifi_1,ubicacion_actual)
    distancia_2=calcular_distancia(zona_wifi_2,ubicacion_actual)
    distancia_3=calcular_distancia(zona_wifi_3,ubicacion_actual)
    distancia_4=calcular_distancia(zona_wifi_4,ubicacion_actual)
    lista_distancias=[distancia_1,distancia_2,distancia_3,distancia_4]
    lista_zonas=[zona_wifi_1,zona_wifi_2,zona_wifi_3,zona_wifi_4]
    for i in range(5):
        for x in range (3):
            if lista_distancias[x]>lista_distancias[x+1]:
                aux=lista_distancias[x]
                lista_distancias[x]=lista_distancias[x+1]
                lista_distancias[x+1]=aux
                aux2=lista_zonas[x]
                lista_zonas[x]=lista_zonas[x+1]
                lista_zonas[x+1]=aux2
    #Se nos pide imprimir en pantalla unicamente las dos distancias mas cercanas pero ordenadas por cantidad de usuario de forma ascendente
    if lista_zonas[0][2]<lista_zonas[1][2]: #Cuando los usuarios del primer punto de acceso mas cercano son menores que las del segundo
        print('Zonas wifi cercanas con menos usuarios')
        print(f'La zona wifi 1: ubicada en [{lista_zonas[0][0]},{lista_zonas[0][1]}] a {lista_distancias[0]} kilometros, tiene en promedio {lista_zonas[0][2]} usuarios')
        print(f'La zona wifi 2: ubicada en [{lista_zonas[1][0]},{lista_zonas[1][1]}] a {lista_distancias[1]} kilometros, tiene en promedio {lista_zonas[1][2]} usuarios')
    else: #Cuando los usuarios del segundo punto de acceso más cercano son menores que las del primero
        print('Zonas wifi cercanas con menos usuarios')
        print(f'La zona wifi 1: ubicada en [{lista_zonas[1][0]},{lista_zonas[1][1]}] a {lista_distancias[1]} kilometros, tiene en promedio {lista_zonas[1][2]} usuarios')
        print(f'La zona wifi 2: ubicada en [{lista_zonas[0][0]},{lista_zonas[0][1]}] a {lista_distancias[0]} kilometros, tiene en promedio {lista_zonas[0][2]} usuarios')
        #Cuando la cantidad de usuarios activos del punto de acceso reorganiza la lista de zonas (colocando la segunda zona wifi mas cercana como la primera), debemos igualmente reordenar las listas que hacen parte de la matriz que se va a retornar
        aux=lista_zonas[0]
        lista_zonas[0]=lista_zonas[1]
        lista_zonas[1]=aux
        aux=lista_distancias[0]
        lista_distancias[0]=lista_distancias[1]
        lista_distancias[1]=aux
    #Creamos una matriz que alberga las dos listas de diatancias y lista de zonas organizada de acuerdo a los requerimeintos
    lista_distancias_y_zonas=[lista_distancias,lista_zonas]
    return lista_distancias_y_zonas
def direccion(opcion_distancia, ubicacion_actual, matriz_coordenadas, zonas): #Función que indica al usuario como guiarse para llegar al punto de acceso que escogió
    if zonas[opcion_distancia-1][0]>matriz_coordenadas[ubicacion_actual-1][0]:
        #indica norte
        if zonas[opcion_distancia-1][1]>matriz_coordenadas[ubicacion_actual-1][1]:
            #indica oriente
                print('Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte')
        else:
            #indica occidente
            print('Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte')
    else:
        #indica sur
        if zonas[opcion_distancia-1][1]>matriz_coordenadas[ubicacion_actual-1][1]:
            #indica oriente
                print('Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur')
        else:
            #indica occidente
            print('Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur')
def transporte(distancia,opcion_distancia): #Función que le indica al usuario cuanto tiempo le llevaria llegar al punto de acceso usando moto o bicicleta
    #para moto
    prom_moto=19.44
    tiempo_moto=(distancia[opcion_distancia-1]/prom_moto)*1000
    tiempo_moto=round((tiempo_moto/60),1)
    print(f'Usando moto como medio de trasporte, usted llegaria a la zona wifi en {tiempo_moto} minutos')
    #Para bicicleta
    prom_bicicleta=3.33
    tiempo_bici=(distancia[opcion_distancia-1]/prom_bicicleta)*1000
    tiempo_bici=round((tiempo_bici/60),1)
    print(f'Usando bibicleta como medio de trasporte, usted llegaria a la zona wifi en {tiempo_bici} minutos')
    recorrido=(distancia[opcion_distancia-1], 'moto', tiempo_moto)
    return recorrido
def imprimir_informacion(coordenada_actual,zona_wifi_cercana, recorrido): #Función que imprime en la terminal la información que el usuario a elegido durante la ejecución del programa y que sera guardada en el archivo csv
    print('Su ubicacion actual es:')
    print(f'latitud [{coordenada_actual[0]}], longitud [{coordenada_actual[1]}]')
    print('La zona wifi que elegió como punto de accéso es:')
    print(f'latitud [{zona_wifi_cercana[0]}], longitud [{zona_wifi_cercana[1]}], promedio usuarios [{zona_wifi_cercana[2]}]')
    print('El recorrido que debe hacer para llegar al punto de acceso es:')
    print(f'distancia [{recorrido[0]}] kilómetros, medio de transporte [{recorrido[1]}], tiempo promedio [{recorrido[2]}] minutos')
def exportar_archivo(informacion): #Función para guardar ls información que suministro el usuario en un archivo de texto .csv
    with open('Guardar_informacion.csv','w',newline='') as f:
        escribir=csv.writer(f)
        for k, v in informacion.items():
            escribir.writerow([k, v])
def actualiza_desde_archivo(): #Función para leer información correspondiente a los puntos de acceso que seran actualizados desde un archivo externo .csv
    try:
        archivo= pd.read_csv('Actualizar_matriz.csv',delimiter=";",header=0)
        print(archivo)
        datos=archivo.values.tolist()
        i=0
        for fila in datos:
            cont=0
            for columna in fila:
                if cont==0:
                    latitud=float(columna)
                if cont==1:
                    longitud=float(columna)
                if cont==2:
                    usuarios=int(columna)
                cont=cont+1
            zona_wifi_i=[latitud,longitud,usuarios]
            matriz_zonas_wifi[i]=zona_wifi_i
            i=i+1
            zona_wifi_1, zona_wifi_2,zona_wifi_3,zona_wifi_4 = matriz_zonas_wifi[0], matriz_zonas_wifi[1], matriz_zonas_wifi[2], matriz_zonas_wifi[3]
    except:
        print('lo sentimos, no hemos podido encontrar el archivo para actualizar el registro')
    return matriz_zonas_wifi

#CONTADOR - Sentencia util para el ciclo while del bloque principal del programa
contador=1 # definimos una variable que usaremos en un ciclo while.

#MENÚ OCPCIONES DEL PROGRAMA - Correspondiente a las opciones por defecto de los requerimientos del programa
menu_opciones= ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zonas wifi más cercanas', 'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo', 'Elegir opcion de menú favorita', 'Cerrar sesión'] #RF01:esta es el menu por defecto 

#EASTER EGG 
#Cuando el usuario ingresa 2021 en el menu principal del programa se desbloquea un Easter Egg
EasterEgg1=2021
EasterEgg2=2022

#MATRIZ DE COORDENADAS
matriz_coordenadas=[] #crear la matriz de coordenadas, donde se guardan los datos ingrasados por el ususario.
for filas in range(3):
    matriz_coordenadas.append([0]*2) #cantidad de columnas por fila en la metriz de coordenadas de el reto 3

#MATRIZ DE ZONAS WIFI 
'''matriz de zonas wifi, o puntos de accesos en la zona de La Paz, cesar - Colombia'''
zona_wifi_1=[10.348,-73.051,0]
zona_wifi_2=[10.171,-73.136,0]
zona_wifi_3=[10.259,-73.069,67]
zona_wifi_4=[10.350,-73.043,45]
matriz_zonas_wifi=[zona_wifi_1,zona_wifi_2,zona_wifi_3,zona_wifi_4] #matriz de zonas wifi para el reto 4 RFO1

#BLOQUE PRINCIPAL DEL PROGRAMA

login() #hacer el login para ocmenzar a ejecutar el programa - correspondiente al reto 1

#Menu pricipal del programa - correspndiente al reto 2
while contador in range(1,4): #este ciclo while nos permitira realizar un Restart del programa cuando el usuario comenta mas de 3 errores al escoger una opcion
    print('')
    menú_principal(menu_opciones)
    opcion_escogida=int(input('Elija una opción: ')) #RF01:esta variable captura la opcion escogida por el usuario 
    #Deacuerdo a la elección del usuario se ejecuta una de las iguientes sentencias
    #Opcion escogida este entre 1 y 7
    if 1<=opcion_escogida<=7: #RF04:en el caso que el usuario escogiera una opcion entre 1 y 5, solo se muestra un mensaje de aceptacion
        borrar()
        print(f'Usted ha elegido la opción {opcion_escogida}')
        #Opcion escogida sea cambiar contraseña
        if menu_opciones[opcion_escogida-1]=='Cambiar contraseña': #RF01: el programa permite actualizar contraseña 
            confirmar_contrasena=int(input('Ingrese la contraseña actual para validar la informacion: '))
            if confirmar_contrasena==contrasena:
                borrar()
                nueva_contrasena=int(input('Ingrese la nueva contraseña: '))
                if nueva_contrasena!=contrasena:
                    borrar()
                    contrasena=nueva_contrasena #guardada la nueva contraseña
                    print('Contraseña guardada con exito')
                    contador=1
                else: 
                    borrar()
                    print('Error: contraseña ingresada es igual a la contraseña actual.') #error cuando la contraseña nueva es igual a la contraseña registrada
            else:
                borrar()
                print('Error') #error cuando el usuario valida su contraseña actual
        #Opcion escogida sea Ingresar coordenadas actuales
        if menu_opciones[opcion_escogida-1]=='Ingresar coordenadas actuales': #RF02 - RF03: el ususario ingresa o actualiza las coordenadas de 3 tres sitios
            if matriz_coordenadas[0][0]==0: #si no existe informacion previa en la matriz, toca llenar 
                #llenar la matriz de coordenadas
                print('Ingrese las coordenadas de los 3 lugares que mas frecuenta')
                for coord in range(3):#sentencia para llenar la matriz con las 3 coordendas 
                    latitud_c=float(input(f'Ingrese la latitud de la {coord+1} coordenada: '))       
                    if 9.757<=latitud_c<=10.462:   #las latitud de todas las coordenadas debe estar entre estos valores, si no da error
                        longitud_c=float(input(f'Ingrese la longitud de la {coord+1} coordenada: '))
                        if -73.623<=longitud_c<=-72.987:
                            matriz_coordenadas[coord]=latitud_c, longitud_c
                        else:
                            error_coordenada()
                    else:
                        error_coordenada()
                borrar()
                print('Coordenadas actualizadas')
                contador=1
            else: 
                #coordenadas ya ingresadas
                print('Las coordenadas registradas son:')
                for coord in range(3):
                    print(f'coordenada [latitud,longitud] {coord+1}: {matriz_coordenadas[coord]}')
                #cual coordenada esta ubicada mas al sur
                if matriz_coordenadas[0][0]<matriz_coordenadas[1][0] and matriz_coordenadas[0][0]<matriz_coordenadas[2][0]:
                    print('La coordenada 1 es la que está ubicada más al sur')
                elif matriz_coordenadas[1][0]<matriz_coordenadas[0][0] and matriz_coordenadas[1][0]<matriz_coordenadas[2][0]:
                    print('La coordenada 2 es la que está ubicada más al sur')
                else:
                    print('La coordenada 3 es la que está ubicada más al sur')
                #cual es el promedio de las coordenadas
                latitud_prom=(matriz_coordenadas[0][0]+matriz_coordenadas[1][0]+matriz_coordenadas[2][0])/3
                longitud_prom=(matriz_coordenadas[0][1]+matriz_coordenadas[1][1]+matriz_coordenadas[2][1])/3
                longitud_prom=round(longitud_prom, 3)
                latitud_prom=round(latitud_prom,3)
                print(f'La coordenada promedio de las coordenadas ingresadas al sistema es: [{latitud_prom}, {longitud_prom}]')
                #actualizar una coordenada
                opcion_actualizar_coordenada=int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: '))
                actualizar_coordenada(opcion_actualizar_coordenada, matriz_coordenadas) #funcion que actualiza una coordenada
                contador=1
        #Opción escogida sea Ubicar zona wifi más cercana
        if menu_opciones[opcion_escogida-1]=='Ubicar zonas wifi más cercanas': #al escoger en el menu principal, la opcion 3
            if matriz_coordenadas[0][0]!=0: #para poder ingresar a la opcion 3 se debe haber llenado la opcion 2
                for i in range (3):
                    print(f'coordenada [latitud,longitud] {i+1} : {matriz_coordenadas[i]}')
                ubicacion_actual=int(input('Por favor elija su ubicacion actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ')) #el usuario escoge ene que ubicacion de las que ingreso en la opcion 2, es su ubicacion actual
                borrar()
                if 1<=ubicacion_actual<=3: 
                    zona_wifi_1,zona_wifi_2,zona_wifi_3,zona_wifi_4=matriz_zonas_wifi[0],matriz_zonas_wifi[1],matriz_zonas_wifi[2],matriz_zonas_wifi[3]
                    distancias=comparar_distancias(zona_wifi_1, zona_wifi_2, zona_wifi_3, zona_wifi_4, ubicacion_actual) #funcion que compara la distancias que hay entre la ubicacion actual y las 4 de la amtriz de zonas wifi, imprime en panatalla las 2 mas cercanas
                    zonas=distancias[1] #sacar la lista de zonas wifi de el return de la funcion comparar
                    distancia=distancias[0] #sacar la lista de distancias del return de la funcion comparar
                    opcion_distancia=int(input('Elija 1 ó 2 para recibir indicaciones de llegada: '))#el usuario elege a cual de las coordenadas de la matriz de zonas wifi, gsta dirigirse
                    if 1<=opcion_distancia<=2:
                        borrar()
                        direccion(opcion_distancia, ubicacion_actual, matriz_coordenadas, zonas) #funcion que indica al usuario como dirigirse a la zona wifi
                        recorrido=transporte(distancia,opcion_distancia)
                        regresar=int(input('Presione 0 para salir: '))
                        if regresar==0:
                            borrar()
                            contador=1
                        else: #error por no ingresar 0 para regresar al menu principal
                            borrar()
                            quit
                    else: #error si ingresa una opcion diferente a 1 o 2, de las coordenadas mas cercanas
                        borrar()
                        print('Error zona wifi')
                        quit()
                else: #error si no escoge una opcion valida como ubicacion actual 
                    borrar()
                    print('Error ubicación')
                    quit()
            else:
                print('Error sin registro de coordenadas')
                quit()
        #Opción escogida sea Guardar archivo con ubicación cercana
        if  menu_opciones[opcion_escogida-1]=='Guardar archivo con ubicación cercana':
            if matriz_coordenadas[0][0]!=0 and ubicacion_actual!=0:
                coordenada_actual=(matriz_coordenadas[ubicacion_actual-1][0],matriz_coordenadas[ubicacion_actual-1][1])#organizando la ubicacion actual en un tupla
                zona_wifi_cercana=(zonas[opcion_distancia-1][0], zonas[opcion_distancia-1][1],zonas[opcion_distancia-1][2])
                recorrido=recorrido #esta informacion ya esta almacenada en la funcion trasporte que se relizo
                informacion={'actual': (coordenada_actual), 'zonawifi1' : (zona_wifi_cercana), 'recorrido':(recorrido)}
                imprimir_informacion(coordenada_actual,zona_wifi_cercana, recorrido)
                confirmacion=int(input('¿está de acuerdo con la información a exportar? Persione 1 para confirmar, 0 para regrear al menú principal: '))
                if confirmacion==1:
                    borrar()
                    print('Exportando archivo')
                    exportar_archivo(informacion)
                    quit()
                else:
                    borrar() 
                    contador=1
            else: 
                borrar()
                print('Error de alistamiento')
                quit()
        #Opción escogida sea Actualizar registros de zonas wifi desde archivo
        if menu_opciones[opcion_escogida-1]=='Actualizar registros de zonas wifi desde archivo':
            matriz_zonas_wifi=actualiza_desde_archivo()
            regresar=int(input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: '))
            if regresar==0:
                borrar()
                contador=1
        #Opción escogida sea Elegir opcion de menú favorita
        if menu_opciones[opcion_escogida-1]=='Elegir opcion de menú favorita': #RF02:esta sentencia se ejecuta cuando el usuario busca organizar las opciones del menu con su opcion favorita
            opcion_favorita(menu_opciones)
        #Opción escogida sea Cerrar sesión
        if menu_opciones[opcion_escogida-1]=='Cerrar sesión': #RF05:si el usuraio escoge la opcion 7, el programa cierra sesion y termina la ejecucion
            borrar()
            print('Hasta pronto')
            quit()#esta variable termina la ejecuacion del ciclo while, y por consecuente el programa
    #Opción escogida no es valida 
    elif opcion_escogida==EasterEgg1:
        EasterEgg_1()
    elif opcion_escogida==EasterEgg2:
        EasterEgg_2()
    else: #RF03:en el caso de que el usuario ingrese un dato no valido, se reinicia el programa desde el ciclo while, pero al equivocarse 3 veces se termina la ejecucion
        borrar_error()
        contador=contador+1 #esta variable recopila cuantos errores de ingreso ha cometido el usuario, hasta que se termina el proceso 