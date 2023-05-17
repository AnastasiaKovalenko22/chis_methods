def f(x, y):
    return -2*x*(y+1)


def eiler(h, y0, x0, N):
    print("Эйлер N=" + str(N))
    yn = y0
    xn = x0
    for i in range(N):
        yn1 = yn + h*f(xn, yn)
        print(str(xn + h) + ";" + str(yn1))
        yn = yn1
        xn += h


def koshi(h, y0, x0, N):
    print("Коши N=" + str(N))
    yn = y0
    xn = x0
    for i in range(N):
        yn1 = yn + h * f(xn + h/2, yn + (h/2)*f(xn, yn))
        print(str(xn + h) + ";" + str(yn1))
        yn = yn1
        xn += h


#Разгон Рунге-Кутты для Адамса-Мултона
def razgon(h, xn, yn, N):
    k1 = h*f(xn,yn)
    k2 = h*f(xn+h, yn+k1)
    k3 = h*f(xn + h/2, yn + (1/4)*k1 + (1/4)*k2)
    yn1 = yn + (1/6)*k1 + (1/6)*k2 + (4/6)*k3
    print("y1= " + str(yn1))
    return yn1

def adams_multon(h, x0, y0, x1, y1, N):
    print("Адамс-Мултон N="+str(N))
    yn_1 = y0
    xn_1 = x0
    yn = y1
    xn = x1
    xn1 = xn + h
    for i in range(N-1):
        yn1 = (yn - (5/6)*h*xn1 + (2/3)*h*f(xn, yn) - h*(1/12)*f(xn_1, yn_1))/(1 + (5/6)*h*xn1)
        print(str(xn1) + ";" + str(yn1))
        yn_1 = yn
        xn_1 = xn
        yn = yn1
        xn = xn1
        xn1 += h

def main():
    eiler(0.1, 1, 0, 10)
    eiler(0.05, 1, 0, 20)
    eiler(1/30, 1, 0, 30)
    koshi(0.1, 1, 0, 10)
    koshi(0.05, 1, 0, 20)
    koshi(1/30, 1, 0, 30)
    y1 = razgon(0.1, 0, 1, 10)
    adams_multon(0.1, 0, 1, 0.1, y1, 10)
    y1 = razgon(0.05, 0, 1, 20)
    adams_multon(0.05, 0, 1, 0.05, y1, 20)
    y1 = razgon(1/30, 0, 1, 30)
    adams_multon(1/30, 0, 1, 1/30, y1, 30)


if __name__ == '__main__':
    main()
