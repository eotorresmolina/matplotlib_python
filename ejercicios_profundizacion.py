#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]

    fig1 = plt.figure('Figura 1')
    fig1.suptitle('$Funciones$ $Polinómicas.$')
    ax1 = fig1.add_subplot(3,1,1)
    ax2 = fig1.add_subplot(3,1,2)
    ax3 = fig1.add_subplot(3,1,3)
    
    ax1.plot(x, y1, color='r', label='$Y=x^2$')
    ax1.set_title('$Gráfico$ $Nro$ $1:$')
    #ax1.set_xlabel('$x$', fontsize=10)
    ax1.set_ylabel('Y1 = f(x)$', fontsize=10)
    ax1.grid(True)
    ax1.legend()

    ax2.plot(x, y2, color='g', marker='.', label='$Y=x^3$')
    #ax2.set_title('$Gráfico$ $Nro$ $2:$')
    #ax2.set_xlabel('$x$', fontsize=10)
    ax2.set_ylabel('Y2 = f(x)$', fontsize=10)
    ax2.grid(True)
    ax2.legend()

    ax3.plot(x, y3, color='b', label='$Y=x^4$')
    #ax3.set_title('$Gráfico$ $Nro$ $3:$')
    ax3.set_xlabel('$x$', fontsize=15)
    ax3.set_ylabel('Y3 = f(x)$', fontsize=10)
    ax3.grid(True)
    ax3.legend()

    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig2 = plt.figure('Figura 2')
    fig2.suptitle('$Funciones$ $Armónicas:$')
    ax1 = fig2.add_subplot(1,2,1)
    ax2 = fig2.add_subplot(1,2,2)

    ax1.scatter(x, y1, c='r', marker='^', label='$Y=sin(x)$')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title('$Función$ $Senoidal$')
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$Y1=f(x)$', fontsize=13)
    ax1.set_xlim(0, 4*np.pi)
    ax1.legend()
    ax1.grid(True)

    ax2.scatter(x, y2, c='darkblue', marker='o', label='$Y=cos(x)$')
    ax2.set_facecolor('whitesmoke')
    ax2.set_title('$Función$ $Cosenoidal$')
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$Y2=f(x)$', fontsize=13)
    ax2.set_xlim(0, 4*np.pi)
    ax2.legend()
    ax2.grid(True)

    plt.show()


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    fig3 = plt.figure('Figura 3')
    fig3.suptitle('$Lenguajes$ $de$ $Programación$')
    ax = fig3.add_subplot(1,1,1)
    ax.bar(lenguajes, performance, color='darkblue')
    ax.set_facecolor('black')
    ax.grid(ls='dashed')
    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig4 = plt.figure('Figura 4')
    fig4.suptitle('$Lenguajes$ $de$ $Programación$')
    ax = fig4.add_subplot()
    explode = (0.2, 0, 0, 0, 0, 0, 0)
    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(), 
    explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    
    ax.axis('equal')
    plt.show()


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valores de "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]

    # plot(signal_x, signal_y)
    signal_x = [x.get('X') for x in signal]
    signal_y = [y.get('Y') for y in signal]

    fig5 = plt.figure('Figura 5')
    fig5.suptitle('$Señal$ $Senoidal$')
    ax = fig5.add_subplot(1,1,1)
    ax.plot(signal_x, signal_y, color='darkgreen', linewidth=3.0)
    ax.set_xlabel('$signal$ $x$', fontsize=13)
    ax.set_ylabel('$signal$ $y$', fontsize=13)
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    plt.show(block=False)

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    # filter_signal_x = [....]
    # filter_signal_y = [....]

    filter_signal_x = [x.get('X') for x in signal if (abs(x.get('Y')) > 0.7)]
    filter_signal_y = [y.get('Y') for y in signal if (abs(y.get('Y')) > 0.7)]

    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?
    fig6 = plt.figure('Figura 6')
    fig6.suptitle('$Señales$ $Superpuestas$')
    ax = fig6.add_subplot(1,1,1)

    ax.plot(signal_x, signal_y, color='darkgreen', linewidth=3.0, label='$Señal$ $Original$')
    ax.scatter(filter_signal_x, filter_signal_y, color='blue', marker='x',
                linewidth=4.0, label='$Señal$ $Filtrada$')
    
    ax.set_xlabel('$signal$ $x$', fontsize=13)
    ax.set_ylabel('$signal$ $y$', fontsize=13)
    ax.set_facecolor('whitesmoke')
    ax.grid(ls='dashdot')
    ax.legend()
    plt.show(block=True)


if __name__ == '__main__':
    print("\n\nBienvenidos a otra clase de Inove con Python.\n\n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
