import numpy as np
import sympy as sy
from IPython.display import display
import scipy as sp

x = sy.symbols('x')
sy.init_printing()


def integral_trapezoidal(f, a, b, n):
    """
    Integração numérica por trapézios.
    n é o número de subintervalos
    a é o limite inferior
    b é o limite superior
    f é a função a ser integrada
    """
    h = (b - a) / n
    sum = 0
    for i in range(1, n):
        sum += f(a + i * h)
    return (h / 2) * (f(a) + 2 * sum + f(b))


def error_trapezoidal(f, a, b, n):
    """
    Calcula o erro do método de trapézios.
    """
    return abs(integral_trapezoidal(f, a, b, n) - integral_trapezoidal(f, a, b, 2 * n))


def q1(linf, linsup, n):
    def integrar(x):
        return x ** 3

    u = x ** 3
    print(integral_trapezoidal(integrar, linf, linsup, n))
    print(error_trapezoidal(integrar, linf, linsup, n))
    print(sy.integrate(u, (x, linf, linsup)))
    return None


def q2(linf, linsup, n):
    def integrar(x):
        return x ** 4

    u = x ** 4
    print(integral_trapezoidal(integrar, linf, linsup, n))
    print(error_trapezoidal(integrar, linf, linsup, n))
    print(sy.integrate(u, (x, linf, linsup)))
    return None


def q3(linf, linsup, n):
    def integrar(x):
        return x * 3 + 4

    u = x * 3 + 4
    print(integral_trapezoidal(integrar, linf, linsup, n))
    print(error_trapezoidal(integrar, linf, linsup, n))
    print(sy.integrate(u, (x, linf, linsup)))
    return None


def q4(linf, linsup, n):
    def integrar(x):
        return x ** 3 + x ** 2 + 3 * x + 4

    u = x ** 3 + x ** 2 + 3 * x + 4
    print(integral_trapezoidal(integrar, linf, linsup, n))
    print(error_trapezoidal(integrar, linf, linsup, n))
    print(sy.integrate(u, (x, linf, linsup)))
    return None


def linha(linf, linsup, n):
    def integrar(x):
        return (1+1.5*x**(-0.5)**2)**0.5

    u = (1+1.5*x**(-0.5)**2)**0.5
    print(integral_trapezoidal(integrar, linf, linsup, n))
    print(error_trapezoidal(integrar, linf, linsup, n))


linha(0, 3, 100)
