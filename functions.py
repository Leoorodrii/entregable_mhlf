import numpy as np
import random
from variables import mi_var


dict_caracteres = {"vacio":" ", "barco":"O", "tocado":"X", "agua":"-"}
lista_caracteres = [" ", "O", "X", "-"]

def print_var(var):
    print(var)

def inicializar_tablero(tamaño=10):
    tablero = np.full((tamaño,tamaño), " ")
    return tablero

def colocar_barco(barco, tablero):
    for coordenada in barco:
        tablero[coordenada] = "O"
    return tablero 

def colocar_barcos(lista_barcos, tablero):
    for barco in lista_barcos:
        tablero = colocar_barco(barco, tablero)
    return tablero 

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Has acertado")
        tablero[casilla] = "X"
    elif tablero[casilla] == " ":
        print("Hay fallado")
        tablero[casilla] = "-"
    return tablero

def disparoMaquina(tablero):
    fila_random = random.randint(0,9) 
    columna_random = random.randint(0,9)
    if tablero[columna_random][fila_random] == "O":
        tablero[columna_random][fila_random] = "X"
    elif tablero[columna_random][fila_random] == " ":
        tablero[columna_random][fila_random] = "-"
    return tablero

def generar_b_aleatorio(eslora, tablero):  #LOGICA COLOCAR BARCO margenes y no pisar otro barco
    barco_random = []

    fila_random = random.randint(0,9) # 1º GUESS DE COORDENADAS PARA POSICIONAR EL BARCO
    columna_random = random.randint(0,9)
    orien = random.choice(["Norte", "Sur", "Este", "Oeste"])
    
    while contorno(fila_random, columna_random, orien, eslora, tablero)==False: # CHECK GUESS
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        orien = random.choice(["Norte", "Sur", "Este", "Oeste"]) # GENERA ALTERNATIVA

        
    barco_random.append((fila_random,columna_random)) # GUARDA COOD VALIDA

    while len(barco_random) < eslora: #FABRICA EL BARCO
        if orien == "Norte":
            fila_random = fila_random - 1
        if orien == "Sur":
            fila_random = fila_random + 1
        if orien == "Este":
            columna_random = columna_random + 1
        if orien == "Oeste":
            columna_random = columna_random - 1

        barco_random.append((fila_random,columna_random))

    return barco_random

def contorno (fila_random, columna_random, orien, eslora, tablero): # COND. PARA QUE NO TOQUE BARCO 
    respuesta=True  
    
    if orien=='Norte':
        ### Comprobar limites
        if 0>fila_random-eslora+1:
            return False
        ### Comprobar que no hay barcos
        for x in range(columna_random-1, columna_random+2):
            for y in range(fila_random+1, fila_random-eslora-1, -1):
                try:
                    if tablero[y][x]!=' ':
                        respuesta=False
                        return respuesta
                        break
                except IndexError:
                    pass
                    
    if orien=='Sur':
        ### Comprobar limites
        if tablero.shape[1]<fila_random+eslora:
            return False
        ### Comprobar que no hay barcos
        for x in range(columna_random-1, columna_random+2):
            for y in range(fila_random-1, fila_random+eslora+1):
                try:    
                    if tablero[y][x]!=' ':
                        respuesta=False
                        return respuesta
                        break 
                except IndexError:
                    pass
                
    if orien=='Este':
        ### Comprobar limites
        if tablero.shape[0]<columna_random+eslora:
            return False
        ### Comprobar que no hay barcos
        for y in range(fila_random-1, fila_random+2):
            for x in range(columna_random-1, columna_random+eslora+1):
                try: 
                    if tablero[y][x]!=' ':
                        respuesta=False
                        return respuesta
                        break
                except IndexError:
                    pass
                    
    if orien=='Oeste':
        ### Comprobar limites
        if 0>columna_random-eslora+1:
            return False
        ### Comprobar que no hay barcos
        for y in range(fila_random-1, fila_random+2):
            for x in range(columna_random+1, columna_random-eslora-1, -1):
                try:
                    if tablero[y][x]!=' ':
                        respuesta=False
                        return respuesta
                        break  
                except IndexError:
                    pass
    
    return respuesta
           
def tablero_maquina (tableroMaquina):
    for x in range(tableroMaquina.shape[0]):
        for y in range(tableroMaquina.shape[1]):
            celda = tableroMaquina[x][y] 
            if celda =='O':
                tableroMaquina[x][y]=' '
                
    print(np.transpose(tableroMaquina))  ###########################################################################################      MAL INDENTADO
                


def quedan_barcos(tablero):
    for y in range(mi_var):
        for x in range(mi_var):
            celda = tablero[x][y]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != 'vacio' and celda != 'tocado' and celda != 'agua':
                return True
    # Acabamos de recorrer toda la matriz y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
    return False