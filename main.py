#IMPORTAMOS COSITAS
import numpy as np
from functions import *
from variables import mi_var
eslora=4
jugar=1

#WHILE DE PARTIDA
while jugar==1:
    
    #INICIALIZAMOS
    tableroMaquina = inicializar_tablero()
    tableroJugador= inicializar_tablero()
    
    #FN COLOCAR BARCO RD Maquina
    for eslora in range(1,5):
        for i in range(eslora,5):
            barco_aleatorio = generar_b_aleatorio(eslora,tableroMaquina)
            tableroMaquina = colocar_barco(barco_aleatorio, tableroMaquina)
    
        #FN COLOCAR BARCO RD Uusuario
    for eslora in range(1,5):
        for i in range(eslora,5):
            barco_aleatorio = generar_b_aleatorio(eslora,tableroJugador)
            tableroJugador = colocar_barco(barco_aleatorio, tableroJugador)
    print("#########¡COMIENZA LA PARTIDA!############")
    print("########### TU TABLERO: ##################")
    print(tableroJugador)
    
    while quedan_barcos(tableroMaquina) and quedan_barcos(tableroJugador):
        print('Introduce las coordenadas para disparar en la coordenada x: ')
        x =int(input())
        print('Introduce las coordenadas para disparar en la coordenada y: ')
        y = int(input())
        casilla=(x,y)
        tableroMaquina=disparar(casilla, tableroMaquina)
        print('########### TABELERO MÁQUNA ##############')
        tablero_maquina (tableroMaquina)
        
        tableroJugador= disparoMaquina(tableroJugador)
        print('########## TABELERO JUGADOR ##############')
        print(np.transpose(tableroJugador))
    
    
    

    
    ### Preguntar si se quiere seguir jugando
    print('¿Quieres jugar otra partida? (0 = no, 1= yes):')
    jugar = int(input())
    while jugar!= 0 and jugar!= 1:
        print('¿Quieres jugar otra partida? (0 = no, 1= yes):')
        jugar = int(input())

      
        
    '''

    tablero = disparar((1,3), tablero)
    tablero = disparar((1,4), tablero)
    tablero = disparar((1,5), tablero)
    tablero = disparar((1,6), tablero)
    tablero = disparar((3,4), tablero)
    print(tablero)

    print_var(mi_var)'''