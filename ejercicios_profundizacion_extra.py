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
    print("\nBuscando la tendencia\n\n")

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

    # Desarrollo Usando Numpy:
   
    dataset = np.genfromtxt('ventas.csv', delimiter=',', dtype=int, skip_header=0)
    dataset = dataset[1:, :]    # Obtengo el dataset sin el header
    tendencia_facturacion_numpy = np.where(dataset[:, 5] != 0, 1, 0)

    # Ploteo:
    fig5 = plt.figure('Figura 5')
    fig5.suptitle('$Tendencia$ $de$ $Facturación$ $de$ $Electrodomésticos$ $a$ $lo$ $largo$ $del$ $Año$')
    ax = fig5.add_subplot(1,1,1)
    ax.plot(tendencia_facturacion_numpy, color='darkgreen', linewidth=3.1, label='1 - $Venta$  0 - $No$ $Venta$')
    ax.set_title('$Usando$ $Numpy$')
    ax.set_xlabel('$Meses$', fontsize=13)
    ax.set_ylabel('$Ventas$ $de$ $Electrodomésticos$', fontsize=13)
    ax.set_xlim(0, len(tendencia_facturacion_numpy))
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    ax.legend()
    plt.show(block=False)


    # Desarrollo Usando Compresión de Listas:
    
    with open('ventas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    lista_facturacion_electrodomesticos = [0 if row.get('Electrodomesticos') == '0' else 1 for row in data]
    
    # Ploteo:
    fig6 = plt.figure('Figura 6')
    fig6.suptitle('$Tendencia$ $de$ $Facturación$ $de$ $Electrodomésticos$ $a$ $lo$ $largo$ $del$ $Año$')
    ax = fig6.add_subplot(1,1,1)
    ax.plot(lista_facturacion_electrodomesticos, color='darkred', linewidth=3.1, label='1 - $Venta$  0 - $No$ $Venta$')
    ax.set_title('$Usando$ $Compresión$ $de$ $Listas$')
    ax.set_xlabel('$Meses$', fontsize=13)
    ax.set_ylabel('$Ventas$ $de$ $Electrodomésticos$', fontsize=13)
    ax.set_xlim(0, len(lista_facturacion_electrodomesticos))
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    ax.legend()
    plt.show(block=True)
    

def ej4():
    print("\nExprimiendo los datos\n\n")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categoría por separado. Nos debe quedar el total
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
    del año.
    '''

    # Desarrollo Usando Numpy:

    dataset = np.genfromtxt('ventas.csv', delimiter=',', dtype=int, skip_header=1)
    fact_alimentos_numpy = np.sum(dataset[:, 2], axis=0) 
    fact_bazar_numpy = np.sum(dataset[:, 3], axis=0)
    fact_limpieza_numpy = np.sum(dataset[:, 4], axis=0)
    fact_electrodom_numpy = np.sum(dataset[:, 5], axis=0)
    
    explode = [0, 0, 0, 0.1]

    # Ploteo:
    fig7 = plt.figure('Figura 7')
    fig7.suptitle('$Facturación$ $Total$ $a$ $lo$ $Largo$ $del$ $Año$', fontsize=15)
    ax = fig7.add_subplot()
    ax.set_title('Usando Numpy')
    ax.pie([fact_alimentos_numpy, fact_bazar_numpy, fact_limpieza_numpy, fact_electrodom_numpy], 
           labels=['Alimentos', 'Bazar', 'Limpieza', 'Electrodomésticos'], 
           shadow=True, autopct='%1.2f%%', startangle=90, explode=explode)
    
    ax.set_facecolor('lightyellow')
    ax.axis('equal')
    plt.show(block=False)


    # Desarrollo Usando Compresión de Listas:

    with open('ventas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    alimentos = [int(row.get('Alimentos')) for row in data]
    bazar = [int(row.get('Bazar')) for row in data]
    limpieza = [int(row.get('Limpieza')) for row in data]
    electrodomesticos = [int(row.get('Electrodomesticos')) for row in data]

    fact_alimentos = sum(alimentos)
    fact_bazar = sum(bazar)
    fact_limpieza = sum(limpieza)
    fact_electrodomesticos = sum(electrodomesticos)

    # Ploteo:
    fig8 = plt.figure('Figura 8')
    fig8.suptitle('$Facturación$ $Total$ $a$ $lo$ $Largo$ $del$ $Año$', fontsize=15)
    ax = fig8.add_subplot()
    ax.set_title('Usando Compresión de Listas')
    ax.pie([fact_alimentos, fact_bazar, fact_limpieza, fact_electrodomesticos], 
           labels=['Alimentos', 'Bazar', 'Limpieza', 'Electrodomésticos'], 
           shadow=True, autopct='%1.2f%%', startangle=90, explode=explode)
    
    ax.set_facecolor('lightgreen')
    ax.axis('equal')
    plt.show(block=True)


def ej5():
    print("\nAhora sí! buena suerte :)\n\n")

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

    # Desarrollo Usando Numpy:

    dataset = np.genfromtxt('ventas.csv', delimiter=',', dtype=int, skip_header=1)

    mask_mes_1 = dataset[:, 0] == 1
    mes_1 = dataset[mask_mes_1, 2:6]
    
    mask_mes_2 = dataset[:, 0] == 2
    mes_2 = dataset[mask_mes_2, 2:6]

    mes_3 = dataset[dataset[:, 0] == 3, 2:6]

    # Ploteo:
    fig9 = plt.figure('Figura 9')
    fig9.suptitle('Total de Ventas Usando Numpy', fontsize=15)
    ax1 = fig9.add_subplot(3,1,1)
    ax2 = fig9.add_subplot(3,1,2)
    ax3 = fig9.add_subplot(3,1,3)

    ax1.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomesticos'],
        [np.sum(mes_1[:, 0], axis=0), np.sum(mes_1[:, 1], axis=0), 
        np.sum(mes_1[:, 2], axis=0), np.sum(mes_1[:, 3], axis=0)], 
        label='Mes 1', color='darkblue')     
    ax1.set_facecolor('lightcyan')
    ax1.set_title('Mes 1', fontsize=12)
    ax1.legend()

    ax2.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomesticos'],
        [np.sum(mes_2[:, 0], axis=0), np.sum(mes_2[:, 1], axis=0), 
        np.sum(mes_2[:, 2], axis=0), np.sum(mes_2[:, 3], axis=0)], 
        label='Mes 2', color='darkgreen')     
    ax2.set_facecolor('whitesmoke')
    ax2.set_title('Mes 2', fontsize=12)
    ax2.legend()

    ax3.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomesticos'],
        [np.sum(mes_3[:, 0], axis=0), np.sum(mes_3[:, 1], axis=0), 
        np.sum(mes_3[:, 2], axis=0), np.sum(mes_3[:, 3], axis=0)], 
        label='Mes 3', color='red')     
    ax3.set_facecolor('lightyellow')
    ax3.set_title('Mes 3', fontsize=12)
    ax3.legend()

    plt.show(block=False)

    # Ploteo Utilizando Gráficos de Barras Agrupados y Apilados:
    fig10 = plt.figure('Figura 10')
    fig10.suptitle('Total de Ventas Usando Numpy')
    ax1 = fig10.add_subplot(2,1,1)
    ax2 = fig10.add_subplot(2,1,2)

    # Gráfico de Barras Agrupados:
    width = 1/6
    meses = np.array([1, 2, 3])

    ax1.bar(meses, [np.sum(mes_1[:, 0], axis=0), np.sum(mes_2[:, 0], axis=0), np.sum(mes_3[:, 0], axis=0)], 
            width=width, label='Alimentos')
    ax1.bar(meses + width, [np.sum(mes_1[:, 1], axis=0), np.sum(mes_2[:, 1], axis=0), np.sum(mes_3[:, 1], axis=0)], 
            width=width, label='Bazar')
    ax1.bar(meses + 2*width, [np.sum(mes_1[:, 2], axis=0), np.sum(mes_2[:, 2], axis=0), np.sum(mes_3[:, 2], axis=0)],
            width=width, label='Limpieza')
    ax1.bar(meses + 3*width, [np.sum(mes_1[:, 3], axis=0), np.sum(mes_2[:, 3], axis=0), np.sum(mes_3[:, 3], axis=0)], 
            width=width, label='Electrodomésticos')

    ax1.set_facecolor('lightgreen')
    ax1.set_title('Gráfico de Barras Agrupados')
    ax1.set_xticks(meses + width)
    ax1.set_xticklabels(['Mes 1', 'Mes 2', 'Mes 3'])
    ax1.legend()
    

    # Gráfico de Barras Apilados (Stack):
    meses_label = ['Mes 1', 'Mes 2', 'Mes 3']

    # Obtengo la Suma Total de lo facturado por mes de cada Categoría:
    facturacion_total_alimentos = np.array([np.sum(mes_1[:, 0], axis=0), np.sum(mes_2[:, 0], axis=0), 
                            np.sum(mes_3[:, 0], axis=0)])
    
    facturacion_total_bazar = np.array([np.sum(mes_1[:, 1], axis=0), np.sum(mes_2[:, 1], axis=0), 
                            np.sum(mes_3[:, 1], axis=0)])
    
    facturacion_total_limpieza = np.array([np.sum(mes_1[:, 2], axis=0), np.sum(mes_2[:, 2], axis=0), 
                            np.sum(mes_3[:, 2], axis=0)])
    
    facturacion_total_electrodomesticos = np.array([np.sum(mes_1[:, 3], axis=0), np.sum(mes_2[:, 3], axis=0), 
                            np.sum(mes_3[:, 3], axis=0)])

    ax2.bar(meses_label, facturacion_total_alimentos, label='Alimentos')
    ax2.bar(meses_label, facturacion_total_bazar, bottom=facturacion_total_alimentos, label='Bazar')
    ax2.bar(meses_label, facturacion_total_limpieza, bottom=facturacion_total_alimentos + facturacion_total_bazar,
            label='Limpieza')
    ax2.bar(meses_label, facturacion_total_electrodomesticos,
            bottom=facturacion_total_alimentos + facturacion_total_bazar + facturacion_total_limpieza,
            label='Electrodomésticos')

    ax2.set_title('Gráfico de Barras Apilados')
    ax2.set_facecolor('lightcyan')
    ax2.legend()

    plt.show(block=True)
      

    # Desarrollo Usando Compresión de Listas:

    with open('ventas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    mes_1_alimentos = [int(row.get('Alimentos')) for row in data if row.get('Mes') == '1']
    mes_2_alimentos = [int(row.get('Alimentos')) for row in data if row.get('Mes') == '2']
    mes_3_alimentos = [int(row.get('Alimentos')) for row in data if row.get('Mes') == '3']

    mes_1_bazar = [int(row.get('Bazar')) for row in data if row.get('Mes') == '1']
    mes_2_bazar = [int(row.get('Bazar')) for row in data if row.get('Mes') == '2']
    mes_3_bazar = [int(row.get('Bazar')) for row in data if row.get('Mes') == '3']

    mes_1_limpieza = [int(row.get('Limpieza')) for row in data if row.get('Mes') == '1']
    mes_2_limpieza = [int(row.get('Limpieza')) for row in data if row.get('Mes') == '2']
    mes_3_limpieza = [int(row.get('Limpieza')) for row in data if row.get('Mes') == '3']

    mes_1_electrodomesticos = [int(row.get('Electrodomesticos')) for row in data if row.get('Mes') == '1']
    mes_2_electrodomesticos = [int(row.get('Electrodomesticos')) for row in data if row.get('Mes') == '2']
    mes_3_electrodomesticos = [int(row.get('Electrodomesticos')) for row in data if row.get('Mes') == '3']

    # Ploteo:
    fig11 = plt.figure('Figura 11')
    fig11.suptitle('Total de Ventas Usando Compresión de Listas', fontsize=15)
    ax1 = fig11.add_subplot(3,1,1)
    ax2 = fig11.add_subplot(3,1,2)
    ax3 = fig11.add_subplot(3,1,3)

    ax1.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomésticos'], [sum(mes_1_alimentos), sum(mes_1_bazar),
            sum(mes_1_limpieza), sum(mes_1_electrodomesticos)], color='darkred', label='Mes 1')
    ax1.set_title('Mes 1')
    ax1.legend()
    ax1.set_facecolor('lightcyan')

    ax2.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomésticos'], [sum(mes_2_alimentos), sum(mes_2_bazar),
            sum(mes_2_limpieza), sum(mes_2_electrodomesticos)], color='darkcyan', label='Mes 2')
    ax2.set_title('Mes 2')
    ax2.legend()
    ax2.set_facecolor('lightyellow')

    ax3.bar(['Alimentos', 'Bazar', 'Limpieza', 'Electrodomésticos'], [sum(mes_3_alimentos), sum(mes_3_bazar),
            sum(mes_3_limpieza), sum(mes_3_electrodomesticos)], color='darkblue', label='Mes 3')
    ax3.set_title('Mes 3')
    ax3.legend()
    ax3.set_facecolor('lightgreen')

    plt.show(block=False)

    # Ploteo Utilizando Gráficos de Barras Agrupados y Apilados:

    fig12 = plt.figure('Figura 12')
    fig12.suptitle('Total de Ventas Usando Compresión de Listas.')
    ax1 = fig12.add_subplot(2,1,1)
    ax2 = fig12.add_subplot(2,1,2)

    fact_alimentos = [sum(mes_1_alimentos), sum(mes_2_alimentos), sum(mes_3_alimentos)]
    fact_bazar = [sum(mes_1_bazar), sum(mes_2_bazar), sum(mes_3_bazar)]
    fact_limpieza = [sum(mes_1_limpieza), sum(mes_2_limpieza), sum(mes_3_limpieza)]
    fact_electrodomesticos = [sum(mes_1_electrodomesticos), sum(mes_2_electrodomesticos), 
                            sum(mes_3_electrodomesticos)]

    # Gráfico de Barras Apilados (Stack):
    ax1.bar(['Mes 1', 'Mes 2', 'Mes 3'], fact_alimentos, label='Alimentos')
    ax1.bar(['Mes 1', 'Mes 2', 'Mes 3'], fact_bazar, bottom=fact_alimentos, label='Bazar')
    ax1.bar(['Mes 1', 'Mes 2', 'Mes 3'], fact_limpieza, bottom=[sum(num) for num in zip(fact_alimentos, fact_bazar)], 
        label='Limpieza')
    ax1.bar(['Mes 1', 'Mes 2', 'Mes 3'], fact_electrodomesticos,
        bottom=[sum(num) for num in zip(fact_alimentos, fact_bazar, fact_limpieza)], label='Electrodomesticos')

    ax1.set_facecolor('lightgrey')
    ax1.set_title('Gráfico de Barras Apilados (Stack)')
    ax1.legend()

    # Gráfico de Barras Agrupados:
    width = 1/6
    
    ax2.bar(meses, [sum(mes_1_alimentos), sum(mes_2_alimentos), sum(mes_3_alimentos)], width=width, 
            label='Alimentos')
    ax2.bar(meses + width, [sum(mes_1_bazar), sum(mes_2_bazar), sum(mes_3_bazar)], width=width, 
            label='Bazar')
    ax2.bar(meses + 2*width, [sum(mes_1_limpieza), sum(mes_2_limpieza), sum(mes_3_limpieza)], width=width, 
            label='Limpieza')

    ax2.bar(meses + 3*width, [sum(mes_1_electrodomesticos), sum(mes_2_electrodomesticos), sum(mes_3_electrodomesticos)], 
            width=width, label='Electrodomésticos')

    ax2.set_facecolor('whitesmoke')
    ax2.set_title('Gráfico de Barras Agrupados')
    ax2.set_xticks(meses + width)
    ax2.set_xticklabels(['Mes 1', 'Mes 2', 'Mes 3'])
    ax2.legend()

    plt.show(block=True)



if __name__ == '__main__':
    print("\n\nEjercicios de práctica.\n\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
