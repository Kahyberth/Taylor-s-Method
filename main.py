import sympy as sp
import matplotlib.pyplot as plt
from sympy.plotting import plot
import numpy as np
from matplotlib.animation import FuncAnimation
from GUI import GUI



def taylor(fx, c, n):
    x = sp.Symbol('x')
    fx_exp = sp.sympify(fx)
    dx = []
    px = fx_exp.subs("x",c)
    for i in range(1,n+1):
        fx_exp = fx_exp.diff(x)
        dx.append(fx_exp.subs('x',c))
        print(i)
        px = px+dx[-1].subs('x',c)*((x-c)**i)/sp.factorial(i)
        if str(dx[-1]) == '0':
            break

    f = plot(fx,px,(x, c-3, c+3),title="Polinomio de Taylor")



def __init__():
    GUI()