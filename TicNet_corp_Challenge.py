'''This programming code compiles the challenges of "ciclo 1" of Programming Fundamental in the training process called MisionTic2020
Developed By: Gabriel Gamez Rojas for the class group 202150-51654'''
#IMPORTED MODULES

from os import system # import the functions to clear the console
import math #import math functions 
import csv #import the functions to manege csv files 
import pandas as pd #import also fuctions to manege csv files 

#CODE FUNCTIONS
def login(): #Function to perform the login process - Includes an Easter Egg 
    print('Welcome to the location system for WIFI public areas') 
    username_predefined='51654' #This is a variable that holds the predefined username, corresponding to the class code "51654"
    password_predefined='45615' # A variable that holds the predefined password, corresponding to the class code in the reverse "45615"
    easteregg_username='Tripulante2022' #A variable that holds the string that allows the user to access to an Easter Egg
    easteregg_password='m1s10nt1c' #Also alows the user to access to a different Easter Egg 
    username_entered=input('Enter the username: ') # RF02: varible that contains username input
    if username_entered==username_predefined: #Username validation
        password_entered=input('Enter the password: ') #A variable that contains password input
        if password_entered==password_predefined: #Password validation
            #once the username and password have been entered, the program requests a captcha
            first_term=654 #the first term of the captcha is the last three digits of the class code "654"
            second_term=((6*4)/(5+1))+1 #the second term is a series of mathematical operations, the result is equal to the penultimate digit of the class code "5"
            captcha=int((input('Enter the requested captacha: captcha = 654 + 5: '))) #the user's input must be "659"
            if captcha==first_term+second_term: #RF03: con esta funcion validamos que el usuario ha ingresado coorectamente el captcha
                system('cls') #este comando borra la consola, para limpiar la interfaz
                print('logged in successfully') # message of logged in
                pass
            else:
                clean_error() #Error if the captcha was missentered
                quit()
        elif password_entered==easteregg_password:
            print('You have entered the easter egg to calculate the average of some latitudes')
            EasterEgg_3()
        else:
            clean_error()# Error if the password was missentered
            quit()
    elif username_entered==easteregg_username:
        print('This was my first programminf code, i\'m going for more')
        quit()
    else: 
        clean_error() #Error if the username was missentered
        quit()
def main_menu(unnumbered_menu_list): #Fuction that prints the organized and enumerate list of options of the program
    print(
    str(' 1. '),unnumbered_menu_list[0], ('\n'),
    str('2. '),unnumbered_menu_list[1], ('\n'),
    str('3. '),unnumbered_menu_list[2], ('\n'),
    str('4. '),unnumbered_menu_list[3], ('\n'),
    str('5. '),unnumbered_menu_list[4], ('\n'),
    str('6. '),unnumbered_menu_list[5], ('\n'),
    str('7. '),unnumbered_menu_list[6], ('\n'))
def change_options(menu_options, favorite_option): #Function that change the options positions, when the user choose his favorite one
    aux=menu_options.pop(favorite_option-1)
    menu_options.insert(0,aux)
    return menu_options
def favorite_option_selection(menu_options): #Function that allows the user to choose his favorite option and place it in the firs item of the main menu
    favorite_option=int(input('Choose your favorite option: ')) 
    if 1<=favorite_option<=5:
        first_riddle=int(input('To confirm please answer: You have it in your hands and you have it on your feet and you will immediately know what number it is: ')) #This is a riddle that validates the user's election, the answer is the number 5
        if first_riddle==5: 
            second_riddle=int(input('To confirm please answer: I represent the seasons of the year and the cardinal points, ¿who am I?: ')) #This is a riddle that validates one last time the user's election, the answer is the number 4
            if second_riddle==4:
                clean()
                menu_options=change_options(menu_options,favorite_option)
            else: #Error if the second riddle is missentered
                clean_error()
        else: #Error if the first riddle is missentered
            clean_error()
    else:
        clean_error()
        quit()
def EasterEgg_1(): #Easter egg that allows the user to know in which hemisphere he is located
    user_latitude=float(input('Give me your latitude and I\'ll tell you which hemisphere it is ...: ')) #Variable that holds theinput of the user latitud
    if user_latitude>0:
        print('You are in northern hemisphere')
    elif user_latitude<0:
        print('You are in the southern hemisphere')
    else:
        print('You are in the equator')
    quit()
def EasterEgg_2():#Easter Egg that allows the user to determine the time zone of a southamerican country
    user_longitude=float(input('enter a longitude in South America and I\'ll tell you its time zone:'))
    if -35.833<=user_longitude<=54.316:
        print('The time zone is -3')
        quit()
    elif (-54.316<=user_longitude<=-35.833) or (54.316<=user_longitude<=67.402):
        print('The time zone is -4')
        quit()
    elif (-67.401<=user_longitude<=-54.316) or (67.402<=user_longitude<=81.296):
        print('The time zone is -5')
        quit()
def EasterEgg_3(): #Easter Egg That allows the user to calculate the average of n latitudes that the user types
    latitudes_amount=int(input('How many latitudes are part of the calculation of the average?: '))
    sum=0
    for i in range (latitudes_amount):
        latitude=float(input(f'Enter the {i+1} latitude: '))
        sum=sum+latitude
    average=sum/latitudes_amount
    average=round(average,3)
    print(f'The average of the entered latitudes is: [{average}]')
    quit()
def clean(): #Function to makes easier to clear the console
    system('cls')
def clean_error(): #Also a function that mekes easier to clear the console, and further print an error message
    system('cls')
    print('Error')
def coordinate_error(): #Function that clear the console and print a error of coordinate mesage
    clean()
    print('Coordinate Error')
    quit()
def update_coordinate(option_update_coordinate, coordinate_array): #Fuctions that allows the user to update one of the coordinates that he had previously entered
    if 1<=option_update_coordinate<=3:
        new_latitude=float(input(f'Enter the latitude of the {option_update_coordinate} coordenate: '))       
        if 9.757<=new_latitude<=10.462:   
            new_longitude=float(input(f'IEnter the longitude of the {option_update_coordinate} coordenate: '))
            if -73.623<=new_longitude<=-72.987:
                coordinate_array[option_update_coordinate-1]= new_latitude, new_longitude
                clean()
                print('updated coordinates')
            else:
                clean()
                print('Update Error')
                quit()
        else:
            clean()
            print('Update Error')
            quit()
    elif option_update_coordinate==0:
        clean()
    else: 
        clean()
        print('Update Error')
        quit()
def calculate_distance(wifi_zone_i,current_location): #Function that calculates the idstance between the user's current location and the wifi access point that the user's elected
    r=6371 #the radius of the Earth in kilometers
    lat2=wifi_zone_i[0]
    lat1=coordinate_array[current_location-1][0]
    lon2=wifi_zone_i[1]
    lon1=coordinate_array[current_location-1][1]
    deltalatitudes = math.radians((lat2 - lat1))
    deltalongitudes= math.radians((lon2 - lon1))
    operation_1 = math.sin(deltalatitudes/2) * math.sin(deltalatitudes/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(deltalongitudes/2) * math.sin(deltalongitudes/2)
    operation_2 = 2 * math.atan2(math.sqrt(operation_1), math.sqrt(1-operation_1))
    disntance=operation_2*r
    disntance=round(disntance,2)
    return disntance
def compare_distances(wifi_zone_1,wifi_zone_2,wifi_zone_3,wifi_zone_4,current_location): #Function that calculate the distances between the wifi zones and the current location of the user, also organize the data according to the requirements 
    distance_1=calculate_distance(wifi_zone_1,current_location)
    distance_2=calculate_distance(wifi_zone_2,current_location)
    distance_3=calculate_distance(wifi_zone_3,current_location)
    distance_4=calculate_distance(wifi_zone_4,current_location)
    distances_list=[distance_1,distance_2,distance_3,distance_4]
    zones_list=[wifi_zone_1,wifi_zone_2,wifi_zone_3,wifi_zone_4]
    for i in range(5):
        for x in range (3):
            if distances_list[x]>distances_list[x+1]:
                aux=distances_list[x]
                distances_list[x]=distances_list[x+1]
                distances_list[x+1]=aux
                aux2=zones_list[x]
                zones_list[x]=zones_list[x+1]
                zones_list[x+1]=aux2
    #the program must print on the screen only the two closest distances but ordered by users amount, in ascending order
    if zones_list[0][2]<zones_list[1][2]: #When the closest wifi zone has the lowest users amount, the program just have to print the next part
        print('Nearby Wi-Fi zones with fewer users')
        print(f'The first wifi zone: located at [{zones_list[0][0]},{zones_list[0][1]}] about {distances_list[0]} kilometers, had a users average of {zones_list[0][2]} users')
        print(f'The second wifi zone: located at  [{zones_list[1][0]},{zones_list[1][1]}] about {distances_list[1]} kilometers, had a users average of {zones_list[1][2]} users')
    else: #When the second closest wifi zone has less users amount than the first one, the program print the next part
        print('Nearby Wi-Fi zones with fewer users')
        print(f'The first wifi zone: located at [{zones_list[1][0]},{zones_list[1][1]}] about {distances_list[1]} kilometers, had a users average of {zones_list[1][2]} users')
        print(f'The second wifi zone: located at  [{zones_list[0][0]},{zones_list[0][1]}] about {distances_list[0]} kilometers, had a users average of {zones_list[0][2]} users')
        #Also we need to reorganized the list, due to the change of positions
        aux=zones_list[0]
        zones_list[0]=zones_list[1]
        zones_list[1]=aux
        aux=distances_list[0]
        distances_list[0]=distances_list[1]
        distances_list[1]=aux
    #we set up a matrix that holds the both lists that were created in this function, to operate with them later
    distances_list_and_zones=[distances_list,zones_list]
    return distances_list_and_zones
def how_to_arrive(place_option, current_location, coordinate_array, zones): #Function that gives indications to the user, to guide him to the access point he selected
    if zones[place_option-1][0]>coordinate_array[current_location-1][0]:
        #When the user's latitude is less than the latitude of the wifi zone, the user should head north
        if zones[place_option-1][1]>coordinate_array[current_location-1][1]:
            #When the user's longitude is less than the longitude of the wifi zone, the user should head east
                print('To get to the Wi-Fi zone, go first to the east and then to the north')
        else:
            #When the user's longitude is greater than the longitude of the wifi zone, the user should head west
            print('To get to the Wi-Fi zone, go first to the west and then to the north')
    else:
        #When the user's latitude is greater than the latitude of the wifi zone, the user should head south
        if zones[place_option-1][1]>coordinate_array[current_location-1][1]:
            #When the user's longitude is less than the longitude of the wifi zone, the user should head east
                print('To get to the Wi-Fi zone, go first to the east and then to the south')
        else:
            #When the user's longitude is greater than the longitude of the wifi zone, the user should head west
            print('To get to the Wi-Fi zone, go first to the west and then to the south')
def transport(distance,place_option): #Function that print how long it will take to reach access point, using motorcycle or bicycle for transportation
    #Motorcycle
    motorcycle_average_speed=19.44
    motorcycle_time=(distance[place_option-1]/motorcycle_average_speed)*1000
    motorcycle_time=round((motorcycle_time/60),1)
    print(f'Using motorcycle as a means of transport, you will arrive at the wifi zone in {motorcycle_time} minutes')
    #Bicycle
    bicycle_average_speed=3.33
    bicycle_time=(distance[place_option-1]/bicycle_average_speed)*1000
    bicycle_time=round((bicycle_time/60),1)
    print(f'Using bicycle as a means of transport, you will arrive at the wifi zone in {bicycle_time} minutes')
    route=(distance[place_option-1], 'motorcycle', motorcycle_time)
    return route
def print_information(current_cordinate,nearby_wifi_zone, route): #Function that prints in the terminal the information that the user has chosen during the execution of the program and that will be saved in the csv file
    print('Your current location is:')
    print(f'latitude [{current_cordinate[0]}], longitude [{current_cordinate[1]}]')
    print('The wifi zone you chose as your access point is:')
    print(f'latitude [{nearby_wifi_zone[0]}], longitude [{nearby_wifi_zone[1]}], users average [{nearby_wifi_zone[2]}]')
    print('the route you must follow to reach the access point is:')
    print(f'distance [{route[0]}] kilometers, transport method [{route[1]}], time average [{route[2]}] minutes')
def export_file(information): #Function to save information provided by the user in a .csv file
    with open('Guardar_informacion.csv','w',newline='') as f:
        write_file=csv.writer(f)
        for k, v in information.items():
            write_file.writerow([k, v])
def update_from_file(): #Function to read information corresponding to the access points that will be updated from an external .csv file
    try:
        file= pd.read_csv('Actualizar_matriz.csv',delimiter=";",header=0)
        print(file)
        data=file.values.tolist()
        i=0
        for fila in data:
            cont=0
            for column in fila:
                if cont==0:
                    latitude=float(column)
                if cont==1:
                    longitude=float(column)
                if cont==2:
                    users=int(column)
                cont=cont+1
            wifi_zone_i=[latitude,longitude,users]
            wifi_zones_array[i]=wifi_zone_i
            i=i+1
            wifi_zone_1, wifi_zone_2,wifi_zone_3,wifi_zone_4 = wifi_zones_array[0], wifi_zones_array[1], wifi_zones_array[2], wifi_zones_array[3]
    except:
        print('Sorry, we couldn\'t find the file to update the register')
        quit()
    return wifi_zones_array

#Counter - Useful statement for the while loop of the main block of the program
counter=1 

#User an password predefined
username_predefined=51654
password_predefined=45615

#PROGRAM OPTIONS MENU - Corresponding to the default options of the program requirements
options_menu= ['Change Password', 'Enter current coordinates', 'Locate nearest Wi-Fi zones', 'Save file with nearest location', 'Update WiFi zone registers from file', 'Choose favorite menu option', 'Sign off'] #This is the main menu options

#EASTER EGG 
#When the user enters 2021 or 2022 in the main menu of the program, an Easter Egg is unlocked
EasterEgg1=2021
EasterEgg2=2022

#COORDINATE ARRAY
coordinate_array=[] #create the coordinate ARRAY, where the data entered by the user is stored.
for rows in range(3):
    coordinate_array.append([0]*2) #number of columns per row in the coordinate array

#WIFI ZONES ARRAY
'''array of Wi-Fi zones, or access points in the area of ​​La Paz, cesar - Colombia'''
wifi_zone_1=[10.348,-73.051,0]
wifi_zone_2=[10.171,-73.136,0]
wifi_zone_3=[10.259,-73.069,67]
wifi_zone_4=[10.350,-73.043,45]
wifi_zones_array=[wifi_zone_1,wifi_zone_2,wifi_zone_3,wifi_zone_4]

#MAIN PROGRAM BLOCK

login() #login to start running the program

#MAIN MENU OF THE PROGRAM
while counter in range(1,4): #this while loop STOPS the program when the user makes more than 3 errors when choosing an option
    print('')
    main_menu(options_menu)
    chose_option=int(input('Choose an option: ')) #This variable holds the option that the user selected
    '''According to the user's choice, one of the following sentences is executed '''
    #the chosen option must be between 1 and 7
    if 1<=chose_option<=7: 
        clean()
        print(f'You have chosen the  {chose_option} option')
        #When the selected option is 'Change Password'
        if options_menu[chose_option-1]=='Change Password': 
            confirm_password=int(input('Enter the current password to validate the information: '))
            if confirm_password==password_predefined:
                clean()
                new_password=int(input('Enter the new password: '))
                if new_password!=password_predefined:
                    clean()
                    contrasena=new_password #saves the new password
                    print('Password saved successfully')
                    counter=1
                else: 
                    clean()
                    print('Error: password entered is identical to current password.') #error when new password is identical to the registered password
            else:
                clean()
                print('Error') #error when user does not validate his current password
        #When the selected option is 'Enter current coordinates'
        if options_menu[chose_option-1]=='Enter current coordinates': 
            if coordinate_array[0][0]==0: #If there is no previous information in the array, the program allows the user to enter 3 coordinates
                #Fill the coordinate array
                print('Enter the coordinates of the 3 places you frequent the most')
                for coord in range(3):#statement to fill the array with the 3 coordinates
                    latitude_c=float(input(f'Enter the latitude of the {coord+1} coordinate: '))       
                    if 9.757<=latitude_c<=10.462:   #the latitude of all the coordinates must be between these values, if not, an error is printed and the execution of the program is terminated
                        longitude_c=float(input(f'Enter the longitude of the {coord+1} coordinate: '))
                        if -73.623<=longitude_c<=-72.987:
                            coordinate_array[coord]=latitude_c, longitude_c
                        else:
                            coordinate_error()
                            quit()
                    else:
                        coordinate_error()
                        quit()
                clean()
                print('Updated coordinates')
                counter=1
            else: 
                #coordinates already entered
                print('The registered coordinates are:')
                for coord in range(3):
                    print(f'coordinate [latitude,longitude] {coord+1}: {coordinate_array[coord]}')
                #which coordinate is located further south?
                if coordinate_array[0][0]<coordinate_array[1][0] and coordinate_array[0][0]<coordinate_array[2][0]:
                    print('Coordinate 1 is the one that is located furthest south')
                elif coordinate_array[1][0]<coordinate_array[0][0] and coordinate_array[1][0]<coordinate_array[2][0]:
                    print('Coordinate 2 is the one that is located furthest south')
                else:
                    print('Coordinate 3 is the one that is located furthest south')
                #what is the average of the coordinates?
                latitude_average=(coordinate_array[0][0]+coordinate_array[1][0]+coordinate_array[2][0])/3
                longitude_average=(coordinate_array[0][1]+coordinate_array[1][1]+coordinate_array[2][1])/3
                longitude_average=round(longitude_average, 3)
                latitude_average=round(latitude_average,3)
                print(f'The average coordinate of the coordinates entered into the system is: [{latitude_average}, {longitude_average}]')
                #update a coordinate
                option_update_coordinate=int(input('Press 1,2 or 3 to update the respective coordinate. Press 0 to return to the menu: '))
                update_coordinate(option_update_coordinate, coordinate_array) #Function that update the coordinate that the user selected
                counter=1
        #When the selected option is 'Locate nearest Wi-Fi zones'
        if options_menu[chose_option-1]=='Locate nearest Wi-Fi zones': 
            if coordinate_array[0][0]!=0: #to enter the functions of this option, you must fill in the coordinates of the previous option
                for i in range (3):
                    print(f'coordinate [latitude,longitude] {i+1} : {coordinate_array[i]}')
                current_location=int(input('Please choose your current location (1,2 or 3) to calculate the distance to the connection points: ')) #the user chooses which location from which he entered in option 2, it's his current location
                clean()
                if 1<=current_location<=3: 
                    wifi_zone_1,wifi_zone_2,wifi_zone_3,wifi_zone_4=wifi_zones_array[0],wifi_zones_array[1],wifi_zones_array[2],wifi_zones_array[3]
                    distances=compare_distances(wifi_zone_1, wifi_zone_2, wifi_zone_3, wifi_zone_4, current_location) #funcion que compara la distances que hay entre la ubicacion actual y las 4 de la amtriz de zonas wifi, imprime en panatalla las 2 mas cercanas
                    zones=distances[1] #remove the list of wifi zones from the return of the compare function
                    distancia=distances[0] #remove the list of distances from the return of the compare function
                    place_option=int(input('Choose 1 or 2 to receive arrival directions: '))#the user chooses which of the coordinates of the wifi zones array, he likes to go to
                    if 1<=place_option<=2:
                        clean()
                        how_to_arrive(place_option, current_location, coordinate_array, zones) #function that tells the user how to go to the Wi-Fi zone
                        route=transport(distancia,place_option)
                        to_return=int(input('Press 0 to exit: '))
                        if to_return==0:
                            clean()
                            counter=1
                        else: #error for not entering 0 to return to the main menu
                            clean()
                            quit
                    else: #error if you enter an option other than 1 or 2, of the closest coordinates
                        clean()
                        print('Wifi zone Error')
                        quit()
                else: #error if you don't choose a valid option as current location
                    clean()
                    print('Location Error')
                    quit()
            else:
                print('Error: no coordinate registration')
                quit()
        #When the selected option is 'Save file with nearest location'
        if  options_menu[chose_option-1]=='Save file with nearest location':
            if coordinate_array[0][0]!=0 and current_location!=0:
                current_cordinate=(coordinate_array[current_location-1][0],coordinate_array[current_location-1][1])#organizing the current location in a tuple
                nearby_wifi_zone=(zones[place_option-1][0], zones[place_option-1][1],zones[place_option-1][2])
                route=route #This information is already stored in the transport function that was performed
                information={'actual': (current_cordinate), 'zonawifi1' : (nearby_wifi_zone), 'route':(route)}
                print_information(current_cordinate,nearby_wifi_zone, route)
                confirmation=int(input('Do you agree with the information to be exported? Press 1 to confirm, 0 to return to the main menu: '))
                if confirmation==1:
                    clean()
                    print('Exporting file')
                    export_file(information)
                    print('File exported successfully')
                    quit()
                else:
                    clean() 
                    counter=1
            else: 
                clean()
                print('Enlistment error')
                quit()
        #When the selected option is 'Update WiFi zone registers from file'
        if options_menu[chose_option-1]=='Update WiFi zone registers from file':
            wifi_zones_array=update_from_file()
            return_2=int(input('Coordinate data for Wi-Fi zones has been updated, press 0 to return to the main menu:'))
            if return_2==0:
                clean()
                counter=1
        #When the selected option is 'Choose favorite menu option'
        if options_menu[chose_option-1]=='Choose favorite menu option': 
            favorite_option_selection(options_menu)
        #When the selected option is 'Sign off'
        if options_menu[chose_option-1]=='Sign off': #RF05:si el usuraio escoge la opcion 7, el programa cierra sesion y termina la ejecucion
            clean()
            print('See you soon')
            quit()
    #Eastereggs
    elif chose_option==EasterEgg1:
        EasterEgg_1()
    elif chose_option==EasterEgg2:
        EasterEgg_2()
    #When the selected option is invalid
    else: 
        clean_error()
        counter=counter+1 #This variable collects how many input errors the user has made, until the process is finished