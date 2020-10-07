#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimientos
adquiridos durante la semana.
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"


import csv
import numpy as np
from matplotlib import pyplot as plt
import numpy as np


'''
NOTA PARA TODOS LOS EJERCICIOS

Para la resolución de todos los problemas utilizará
el dataset "ventas.csv".

Desde ahora los de datos los generará c/u
con Numpy o comprensión de listas o ambos, queda
a su elección en cada caso. Si quiere usar Numpy
para todo, puede abrir el archivo directamente con Numpy
y trabajar sin pasar por listas o diccionarios.

TIP: Para abrir el archivo CSV con Numpy y que el header no
     quede mezclado con los datos utilizar:
     data = np.genfromtxt('ventas.csv', delimiter=',')
     # Borro la fila 0 del header, los nombres de las columnas
     data = data[1:,:]

NO están permitidos los bucles en la realización de estos ejercicios.

Descripción del dataset "ventas.csv"
- Este dataset contiene el importe facturado por un local
  en la venta de sus productos dividido en 4 categorías
- Se contabiliza lo vendido por categória al cerrar el día,
  el dataset está ordenado por mes y día
- El dataset contiene 3 meses (genéricos) de 30 días c/u

'''


def ej1():
    print('Comenzamos a divertirnos!\n')

    '''
    Para comenzar a calentar en el uso del dataset se lo solicita
    que grafique la evolución de la facturación de la categoría alimentos
    para el primer mes (mes 1) de facturación.
    Realice un line plot con los datos de facturación de alimentos del mes 1
    Deberá poder observar la evolución de ventas(y) vs días(x)

    TIP:
    1) Para aquellos que utilicen listas siempre primero deberan
    empezar filtrando el dataset en una lista de diccionarios que
    posee solo las filas y columnas que están buscando.
    En este caso todas las filas cuyo mes = 1 y solo la columna
    de día(x) y de alimentos(y).
    Una vez que tiene esa lista de diccionarios reducida a la información
    de interés, debe volver a utilizar comprensión de listas para separar
    los datos de los días(x) y de los alimentos(y)

    2) Para aquellos que utilicen Numpy, si transformaron su CSV en Numpy
    les debería haber quedado una matriz de 6 columnas y de 90 filas
    (recordar sacar la primera fila que es el header)
    mes | dia | alimentos | bazar | limpieza | electrodomesticos
    Luego si quisieramos acceder a solo la columna de los dias (col=1)
    podemos utilizar slicing de Numpy:
    dias = dataset[:, 1]
    ¿Cómo puedo obtener las filas solo del primer mes?
    Aplicando mask de Numpy:
    mes_1 --> col = 0
    filas_mes_1 = dataset[:, 0] == 1
    Obtengo solos los datos del mes uno
    mes_1 = dataset[filas_mes_1, :]

    x --> dias
    Obtengo solo los dias del mes1 de alimentos
    x = dataset[filas_mes_1, 1]
    o tambien puede usar
    x = mes_1[:, 1]

    y --> alimentos
    Obtengo solo los alimentos del mes1 de alimentos
    y = dataset[filas_mes_1, 2]
    o tambien puede usar
    y = mes_1[:, 2]

    '''

    # Desarrollo Usando Comprensión de Listas:

    # Obtengo mi lista de Diccionarios abriendo el archivos .csv
    with open('ventas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    # Filtro los datos creando una nueva lista para la Categoría "Alimentos" en el Mes 1.
    data_filtrada_reducida = [{'Dia': row.get('Dia'), 'Alimentos': row.get('Alimentos')}
                               for row in data if (row.get('Mes') == '1')]

    # Creo 2 Nuevas Listas que Separe los días del "Mes 1" y "Alimentos":
    lista_ventas_dias = [int(dia.get('Dia')) for dia in data_filtrada_reducida]
    lista_ventas_alimentos = [int(venta.get('Alimentos')) for venta in data_filtrada_reducida]
 
    # Ploteo:
    fig1 = plt.figure('Figura 1')
    fig1.suptitle('$Cantidad$ $de$ $Ventas$ $de$ $Alimentos$ $en$ $el$ $Mes$ $1$', fontsize=14)
    ax = fig1.add_subplot(1,1,1)
    ax.plot(lista_ventas_dias, lista_ventas_alimentos, color='darkblue', linewidth=2.0)
    ax.scatter(lista_ventas_dias, lista_ventas_alimentos, color='r', marker='o', linewidth=3.0)
    ax.set_title('$Usando$ $Comprensión$ $de$ $Listas$')
    ax.set_xlim(lista_ventas_dias[0], lista_ventas_dias[-1])
    ax.set_xlabel('$Días(x)$', fontsize=14)
    ax.set_ylabel('$Ventas$ $de$ $Alimentos$ $(y)$', fontsize=14)
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    plt.show(block=False)
    

    # Desarrollo Usando Numpy:
    data_numpy = np.genfromtxt('ventas.csv', dtype=int, delimiter=',', skip_header=1)
    
    # Aplico una Máscara para Obtener los Valores que Correspondan al Mes 1.
    mask_mes_1 = data_numpy[:, 0] == 1  
    
    # Obtengo los días correspondientes al Mes 1.
    dias_mes_1 = data_numpy[mask_mes_1, 1]

    # Obtengo la Cantidad de Ventas de Alimentos por día del Mes 1. 
    ventas_alimentos_mes_1 = data_numpy[mask_mes_1, 2]

    # Ploteo:
    fig2 = plt.figure('Figura 2')
    fig2.suptitle('$Cantidad$ $de$ $Ventas$ $de$ $Alimentos$ $en$ $el$ $Mes$ $1$', fontsize=14)
    ax = fig2.add_subplot(1,1,1)
    ax.plot(dias_mes_1, ventas_alimentos_mes_1, color='red', linewidth=2.0)
    ax.scatter(dias_mes_1, ventas_alimentos_mes_1, color='darkblue', marker='o', linewidth=3.0)
    ax.set_title('$Usando$ $Librería$ $Numpy$')
    ax.set_xlim(dias_mes_1[0], dias_mes_1[-1])
    ax.set_xlabel('$Días(x)$', fontsize=14)
    ax.set_ylabel('$Ventas$ $de$ $Alimentos$ $(y)$', fontsize=14)
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    plt.show(block=True)


def ej2():
    print('\nComenzamos a ponernos serios!\n\n')

    '''
    Queremos visualizar como ver la tendencia de venta de los alimentos
    a lo largo de todo el año.
    Para eso queremos utilizar el método "np.diff" para obtener la diferencia
    día a día de lo vendido.

    Se debe poder primero discriminar las ventas por la categoría Alimentos,
    1) en el caso de usar listas se debe generar una lista de solo
       ventas de aliementos de todo el año.
    2) En el caso de usar numpy no hace falta generar una lista/array aparte,
       pero si le resulta comodo puede hacerlo.

    Luego que tienen discriminadas las ventas por alimento aplicar el método
    np.diff
    tendencia = np.diff(mis ventas de alimentos)

    Graficar el valor obtenido con un Line Plot

    NOTA: Importante!, en este caso no disponen facilmente del eje "X" de diff,
    para simplificar el caso solamente graficar la variable "tendencia"
    plot(tendencia)

    '''

    # Desarrollo Usando Comprensión de Listas:

    with open('ventas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    # Obtengo la lista con la cantidad de ventas de los Alimentos a lo largo del año.
    alimentos = [int(row.get('Alimentos')) for row in data]
    
    # Obtengo la Tendencia usando la función "diff" de la librería Numpy:
    tendencia = np.diff(alimentos)
    
    # Ploteo:
    fig3 = plt.figure('Figura 3')
    fig3.suptitle('$Tendencia$ $de$ $Ventas$ $de$ $Alimentos$ $a$ $lo$ $largo$ $del$ $Año$')
    ax = fig3.add_subplot(1,1,1)
    ax.plot(tendencia, color='k', linewidth=2.6)
    ax.set_title('$Usando$ $Comprensión$ $de$ $Listas$')
    ax.set_xlabel('$Meses$', fontsize=13)
    ax.set_ylabel('$Ventas$ $de$ $Alimentos$', fontsize=13)
    ax.set_xlim(0, len(tendencia))
    ax.set_facecolor('lightcyan')
    ax.grid(ls='dashdot')
    plt.show(block=False)


    # Desarrollo Usando Numpy:

    dataset = np.genfromtxt('ventas.csv', delimiter=',', dtype=int ,skip_header=1)
    tendencia_numpy = np.diff(dataset[:, 2])

    # Ploteo:
    fig4 = plt.figure('Figura 4')
    fig4.suptitle('$Tendencia$ $de$ $Ventas$ $de$ $Alimentos$ $a$ $lo$ $largo$ $del$ $Año$')
    ax = fig4.add_subplot(1,1,1)
    ax.plot(tendencia_numpy, color='darkblue', linewidth=2.8)
    ax.set_title('$Usando$ $Numpy$')
    ax.set_xlabel('$Meses$', fontsize=13)
    ax.set_ylabel('$Ventas$ $de$ $Alimentos$', fontsize=13)
    ax.set_xlim(0, len(tendencia_numpy))
    ax.set_facecolor('lightyellow')
    ax.grid(ls='dashed')
    plt.show(block=True)


def ej3():
    print("Buscando la tendencia")

    '''
    Si observa el dataset, los electrodomésticos no siempre
    tienen facturación al finalizar el día.
    Deseamos que generen una nueva lista/array/columna
    en la cual coloquen un "1" si ese día se vendió electrodomésticos
    o un "0" sino se vendio nada (facturación = 0).
    Luego graficar utilizando Line Plot esta nueva lista/array/columna
    para visualizar la tendencia de cuantos días consecutivos hay
    ventas de electrodomésticos.

    '''


def ej4():
    print("Exprimiendo los datos")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categória por separado. Nos debe quedar el total
    facturado en alimentos, en bazar, en limpieza y en
    electrodomesticos por separado (son 4 valores)

    TIP:
    1) para los que usan listas, para poder obtener estos
    valores primero deberan generar una lista de cada categoría,
    para luego poder aplicar operaciones como sum.
    2) Para los que usan numpy pueden usar directamente np.sum
    y especificando el axis=0 estarán haciendo la suma total de la columna

    Con la información obtenida realizar un Pie Plot
    para visualizar que categoría facturó más en lo que va
    del año
    '''


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Ahora que ya hemos jugado un poco con nuestro dataset,
    queremos realizar 3 gráficos de columnas en una misma figura
    Cada gráfico de columnas deben tener 4 columnas que representan
    el total vendido de cada categoría al final del mes.
    Para poder hacer este ejercicio deben obtener primero
    total facturado por categoria por mes (deben filtrar por mes)
    Es parecido a lo realizado en el ejercicio anterior pero en vez
    de todo el año es la suma total por mes por categoría.

    Siendo que son 4 categorías y 3 meses, deben obtener al final
    12 valores, con esos 12 valores construir 3 listas/arrays
    para poder mostrar los 3 gráficos de columnas

    BONUS Track: Si están cancheros y aún quedan energías para practicar,
    les proponemos que en vez de realizar 3 gráficos de columnas separados
    realicen uno solo y agrupen la información utilizando gráfico de barras
    apilados o agrupados (a su elección)
    '''


if __name__ == '__main__':
    print("\n\nEjercicios de práctica.\n\n")
    ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
