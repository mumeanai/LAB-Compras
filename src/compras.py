from collections import Counter, defaultdict
from typing import NamedTuple
import csv
from datetime import datetime

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

def lee_compras(ruta):
    '''
    recibe el nombre de un fichero y devuelve una lista de tuplas 
    de tipo Compra conteniendo todos los datos almacenados en el
    fichero. (1 punto)
    '''
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        
        res = []
        
        for dni, supermecado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = datetime.strptime(fecha_llegada, '%d/%m/%Y %H:%M')
            fecha_salida = datetime.strptime(fecha_salida, '%d/%m/%Y %H:%M')
            total_compra = float(total_compra)
            tupla = Compra(dni, supermecado, provincia, fecha_llegada, fecha_salida, total_compra)
            res.append(tupla)
        return res

def compra_maxima_minima_provincia(compras:list[Compra], provincia:str)->tuple[int,int]:
    '''
     recibe una lista de tuplas de tipo Compra y una provincia. 
     Devuelve una tupla que contiene el importe máximo y el mínimo de 
     las compras que se han realizado en la provincia dada como parámetro. 
     Si la provincia toma el valor None, se devuelve una tupla con el importe
     máximo y el mínimo calculados a partir de todas las compras. (1 punto)
    '''
    #ejercico2
    #Filtrar--calcular max y min de las compras segun el immport (key = lambda...)--- meter resultados en una tupla
    res = []
    for c in compras:
        if provincia == None or c.provincia == provincia:
            res.append(c.total_compra)
    maximo= max(res) 
    minimo=min(res)
    return (maximo, minimo)
    

def hora_menos_afluencia(compras:list[Compra])->tuple[datetime.hour]: 
    '''
    recibe una lista de tuplas de tipo Compra y devuelve una tupla con la 
    hora en la que llegan menos clientes y el número de clientes que llegan 
    a dicha hora. (1,5 puntos)
    '''   
    #ejercicio3
    #diccionario de conteo por horas--- sale un diccionario con las horas como clave, y un entero---usamos su .items para recorrer los elems del diccionario -- buscmaos el min
    contador = Counter(c.fecha_llegada.hour for c in compras)
    minimo=min(contador.items(), key = lambda t:t[1])
    return minimo
        
def supermercados_mas_facturacion(compras:list[Compra], n:int =3)->list[tuple[int, tuple[str, float]]]:
    '''
    recibe una lista de tuplas de tipo Compra y un número entero n, con 
    valor por defecto 3. Devuelve un ranking, es decir, una lista de tuplas
    (posición_ranking, (supermercado, facturación)) con las n marcas de 
    supermercados que más facturan, en orden decreciente de facturación. 
    El ranking debe empezar por la posición 1. (1,5 puntos)
    '''
    #ejercicio 4
    #hacer dicionario, con la facturizacion por supermercado, dict[supermencado, float]---uso .items para recorrer---ordeno key reverse--- hago un slicing par quedarme con los n primeros--- construir lista de ranking
    facturacion_por_supermercado = defaultdict(float)
    for c in compras:
        facturacion_por_supermercado[c.supermercado] += c.total_compra
    slicing= sorted(facturacion_por_supermercado.items(), key=lambda t:t[1], reverse=True)[:n]        
    return [(i + 1, supermercado) for i, supermercado in enumerate(slicing)]

def clientes_itinerantes(compras:list[Compra], n:int = 3)->list[tuple[int, list]]:
    '''
    recibe una lista de tuplas de tipo Compra y un entero n, y devuelve 
    una lista de tuplas con el dni del cliente y la lista de provincias 
    donde el cliente ha realizado sus compras, ordenadas alfabéticamente. 
    Solo se devolverán aquellos clientes que hayan comprado en un número 
    de provincias mayor que el parámetro n. (2 puntos)
    '''
    dni_provincias = defaultdict(set)
    for c in compras:
        dni_provincias[c.dni].add(c.provincia)

    res = []

    for dni, provincia in dni_provincias.items():
        provincias_ordenadas = sorted(provincia)
        dni_provincias[dni] = provincias_ordenadas
        if len(provincias_ordenadas)>n:
            res.append((dni,provincias_ordenadas))
            
    return res

def dias_estrella(compras:list[Compra], supermercado:str, provincia:str)->list[datetime.date]:
    '''
    recibe una lista de tuplas de tipo Compra, un supermercado y una provincia,
    y devuelve una lista ordenada cronológicamente con las "fechas estrella" 
    de ese supermercado en esa provincia. Se consideran "fechas estrella" 
    aquellos días en los que el supermercado factura más que el día anterior y 
    más que el día siguiente. (2 puntos)
    '''
    dias_estrella= []
    fecha_facturacion=defaultdict(float)
    for c in compras:
        if c.supermercado==supermercado and c.provincia==provincia:
            fecha = c.fecha_llegada.date
            fecha_facturacion[fecha] += c.total_compra
    
    orden_fechas=sorted(fecha_facturacion.items())
                        
    
    for f1,f2,f3 in zip(orden_fechas, orden_fechas[1:], orden_fechas[2:]):
        if f1[1]<f2[1] and f3[1]<f2[1]:
            dias_estrella.append(f2[0])
            
    return dias_estrella
