import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from GUI import GUI

def taylor(fx, c, n):
    x = sp.Symbol('x')
    fx_exp = sp.sympify(fx)
    dx = []
    px = f'{fx}'
    for i in range(n):
        fx_exp = fx_exp.diff(x)
        dx.append(fx_exp / sp.factorial(i))
        px += '+' + str(dx[-1])
        if str(dx[-1]) == '0':
            break

    px = sp.sympify(px.replace('x', f'({x}-{c})'))  # Modifica la expresión para reemplazar 'x' por '(x - c)'
    f = sp.lambdify(x, px, 'numpy')

    return f, len(dx)

def graph(fx, c, n):
    # Variables
    f_original = lambda x: eval(fx)  # Utilizar eval para evaluar la expresión como cadena
    f_taylor, n_terms = taylor(fx, c, n)  # Aumenta el número de términos

    x_vals = np.linspace(-5, 5, 1000)  # Aumenta el número de puntos en el rango de x
    y_vals_original = f_original(x_vals)

    fig, ax = plt.subplots()
    line_original, = ax.plot(x_vals, y_vals_original, label='Función original')
    line_taylor, = ax.plot([], [], label='Aproximación de Taylor')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gráfico de la función')
    ax.legend()
    ax.grid(True)

    # Función de inicialización para la animación
    def init():
        line_taylor.set_data([], [])  # Línea inicialmente vacía para la aproximación de Taylor
        return line_taylor,

    # Función de actualización para animar las líneas
    def update(frame):
        t = frame / n_terms  # Tiempo normalizado en función del número de términos
        x_range = np.linspace(-5, 5, 1000)  # Aumenta el número de puntos en el rango de x
        y_vals_taylor = f_taylor(x_range)
        x_vals_anim = x_range[:int(t * len(x_range))]  # Valores de x para animación en función del tiempo
        y_vals_anim = y_vals_taylor[:int(t * len(x_range))]  # Valores de y para animación en función del tiempo
        line_taylor.set_data(x_vals_anim, y_vals_anim)
        return line_taylor,

    # Ajusta el número de fotogramas en función del número de términos para una animación más precisa
    frames = int(n_terms * 1.5)

    # Crear la animación
    animation = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=100)

    # Mostrar la animación
    return plt.show()


def __init__():
    GUI()
