from math import cos
from math import sqrt


def f(x):
    return sqrt(2*x)*cos(x*x)


def element_trapeze_formula(a, b, h):
    return ((f(a) + f(b))/2)*h


def complex_trapeze_formula(h, a, b):
    result = 0
    m = (b-a)/h
    xi = a
    xi1 = a + h
    for i in range(0, int(m)):
        result += element_trapeze_formula(xi, xi1, h)
        xi = xi1
        xi1 = xi + h
    return result


def element_38_formula(xi, xi1, xi2, xi3, h):
    return (3/8)*h*(f(xi) + 3*f(xi1) + 3*f(xi2) + f(xi3))


def complex_38_formula(h, a, b):
    result = 0
    m = (b-a)/(3*h)
    xi = a
    xi1 = xi + h
    xi2 = xi1 + h
    xi3 = xi2 + h
    for i in range(0, int(m)):
        result += element_38_formula(xi, xi1, xi2, xi3, h)
        xi = xi3
        xi1 = xi + h
        xi2 = xi1 + h
        xi3 = xi2 + h
    return result


def gauss():
    return (973/2223)*f(1.5) + (2500/9009)*f(1.11) + (1250/4389)*f(1.88)


def gauss_pogreshnost():
    return (5670/(2*3*4*5*6*7*8))*0.0003586628571428571


def main():
    print("Значение по формуле трапеций с шагом 0.1: " + str(complex_trapeze_formula(0.1, 1, 2)))
    print("Погрешность формулы трапеций с шагом 0.1: " + str(
        (1/3)*abs(complex_trapeze_formula(0.1, 1, 2) - complex_trapeze_formula(0.2, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле 3/8 с шагом 0.1: " + str(complex_38_formula(0.1, 1, 2)))
    print("Погрешность формулы 3/8 с шагом 0.1: " + str(
        (1/15)*abs(complex_38_formula(0.1, 1, 2) - complex_38_formula(0.2, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле трапеций с шагом 0.05: " + str(complex_trapeze_formula(0.05, 1, 2)))
    print("Погрешность формулы трапеций с шагом 0.05: " + str(
        (1/3)*abs(complex_trapeze_formula(0.05, 1, 2) - complex_trapeze_formula(0.1, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле 3/8 с шагом 0.05: " + str(complex_38_formula(0.05, 1, 2)))
    print("Погрешность формулы 3/8 с шагом 0.05: " + str(
        (1/15)*abs(complex_38_formula(0.05, 1, 2) - complex_38_formula(0.1, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле трапеций с шагом 0.025: " + str(complex_trapeze_formula(0.025, 1, 2)))
    print("Погрешность формулы трапеций с шагом 0.025: " + str(
        (1/3)*abs(complex_trapeze_formula(0.025, 1, 2) - complex_trapeze_formula(0.05, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле 3/8 с шагом 0.025: " + str(complex_38_formula(0.025, 1, 2)))
    print("Погрешность формулы 3/8 с шагом 0.025: " + str(
        (1/15)*abs(complex_38_formula(0.025, 1, 2) - complex_38_formula(0.05, 1, 2))))
    print("--------------------------------------------------------")
    print("Значение по формуле Гаусса: " + str(gauss()))
    print("Погрешность формулы Гаусса: " + str(gauss_pogreshnost()))


if __name__ == '__main__':
    main()
