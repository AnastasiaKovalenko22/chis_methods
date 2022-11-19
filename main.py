import math


def f(x):
    return (1/math.tan(x + 2)) - (x*x)


epsilon = 0.5 * pow(10, -5)

'''метод половинного деления'''


def check_sign(a, b):
    return a * b > 0


def half_division(func, a, b):
    c = b
    c_next = a
    count = 0
    while abs(c - c_next) > epsilon:

        c_next = c
        c = (a + b) / 2.0
        if check_sign(func(a), func(c)):
            a = c
        else:
            b = c
        count += 1
    return c, count


x, iterations_count = half_division(f, -1.7, -1.6)

print('половинное деление:  ' + str(x) + '  n: ' + str(iterations_count))

'''Метод Ньютона '''


def f_derivative(x):
    return -(1/pow(math.sin(x + 2), 2)) - 2*x


def newton(f, x0, derivative):
    xn = x0
    xn1 = xn - f(xn) / derivative(xn)
    count = 1
    while abs(xn1 - xn) > epsilon:
        xn = xn1
        xn1 = xn - f(xn) / derivative(xn)
        count += 1
    return xn1, count


x, iterations_count = newton(f, -1.7, f_derivative)

print('Ньютон:     ' + str(x) + '   n: ' + str(iterations_count))


'''Модифицированный метод Ньютона'''


def newton_modified(f, x0, derivative):
    xn = x0
    derivative_x0 = derivative(x0)
    xn1 = xn - f(xn) / derivative_x0
    count = 1
    while abs(xn1 - xn) > epsilon:
        xn = xn1
        xn1 = xn - f(xn) / derivative_x0
        count += 1
    return xn1, count


x, iterations_count = newton_modified(f, -1.7, f_derivative)

print('Ньютон мод: ' + str(x) + '  n: ' + str(iterations_count))


'''Метод подвижных хорд '''


def chords_move(f, a, b):
    x0 = a
    xn = b
    xn1 = xn - (f(xn) * (xn - x0)) / (f(xn) - f(x0))
    count = 1
    while abs(xn1 - xn) > epsilon:
        xn_1 = xn
        xn = xn1
        xn1 = xn - (f(xn) * (xn - xn_1)) / (f(xn) - f(xn_1))
        count += 1
    return xn1, count


x, iterations_count = chords_move(f, -1.7, -1.6)

print('хорд под:   ' + str(x) + '  n: ' + str(iterations_count))


'''Метод неподвижных хорд '''


def chords_no_move(f, a, b):
    x0 = a
    xn = b
    xn1 = xn - (f(xn) * (xn - x0)) / (f(xn) - f(x0))
    count = 1
    while abs(xn1 - xn) > epsilon:
        xn = xn1
        xn1 = xn - (f(xn) * (xn - x0)) / (f(xn) - f(x0))
        count += 1
    return xn1, count


x, iterations_count = chords_no_move(f, -1.7, -1.6)

print('хорд непод: ' + str(x) + '    n: ' + str(iterations_count))

'''Метод простой итерации '''


def iteration(fi, x0):
    xn = fi(x0)
    xn1 = fi(xn)
    count = 2
    while abs(xn1 - xn) > epsilon:
        xn = xn1
        xn1 = fi(xn)
        count += 1
    return xn1, count


def fi(x):
    return math.sqrt(1/math.tan(x + 2))


x, iterations_count = iteration(fi, -1.7)

print('итерация:   ' + str(x) + '  n: ' + str(iterations_count))
