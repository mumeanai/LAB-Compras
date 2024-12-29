from compras import *
def test_lee_compras(datos):
    print("EJERCICIO 1")
    print(f"Número de registros leídos: {len(datos)}")
    print("Tres primeros registros:", datos[:3])
    print("Tres últimos resgistros: ", datos[-4:])
    
def test_compra_maxima_minima_provincia(datos):
    print("EJERCICIO 2")
    print("Importe máximo de la provincia de Huelva : ", compra_maxima_minima_provincia(datos, "Huelva")[0])
    print("Importe mínimo:", compra_maxima_minima_provincia(datos, "Huelva")[1])
    print("Importe máximo de la provincia de None : ", compra_maxima_minima_provincia(datos, None)[0])
    print("Importe mínimo:", compra_maxima_minima_provincia(datos, None)[1])

def test_hora_menos_afluencia(datos):
    print("EJERCICIO 3")
    print(f"La hora con menos afluencia es: {hora_menos_afluencia(datos)[0]} con {hora_menos_afluencia(datos)[1]}")

def test_supermercados_mas_facturacion(datos): 
    print('EJERCICIO 4')
    print('Los 2 supermercados con más facturación son:', supermercados_mas_facturacion(datos, 2))

def test_clientes_itinerantes(datos):
    print('EJERCICIO 5')
    print('Los clientes itinerantes que han comprado en más de 7 provincias son:', clientes_itinerantes(datos, 7))

def test_dias_estrella(datos):
    print('EJERCICIO 6')
    print('Los días estrella del supermercado Aldi de la provincia de Huelva son:', dias_estrella(datos, 'Aldi', 'Huelva'))
    
    
if __name__=='__main__':
    datos=lee_compras('data\compras.csv')
    test_lee_compras(datos)
    test_compra_maxima_minima_provincia(datos)
    test_hora_menos_afluencia(datos)
    test_supermercados_mas_facturacion(datos)
    test_clientes_itinerantes(datos)
    test_dias_estrella(datos)