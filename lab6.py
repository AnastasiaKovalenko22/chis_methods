import math


def count_lambda_and_mu(h, n, x):
    lambda_value = []
    mu_value = []
    for _ in range(n+1):
        lambda_value.append(0)
        mu_value.append(0)
    lambda_value[1] = 1/(1+h)
    mu_value[1] = 4.1*h/(1+h)
    for i in range(1, n):
        lambda_value[i+1] = 1/((2+h*h)-lambda_value[i])
        mu_value[i+1] = (mu_value[i] - (4.1 * x[i] * (1 - x[i]) * h * h + 10.2 * h * h)) / ((2 + h * h) - lambda_value[i])
    return lambda_value, mu_value


def x_value(n, x0, xn):
    h = (xn-x0)/n
    res = []
    for i in range(n+1):
        res.append(x0 + i*h)
    return res


def y_value(lambda_, mu, n, yn):
    res = []
    for i in range(n+1):
        res.append(0)
    res[n] = yn
    for i in range(n-1, -1, -1):
        res[i] = lambda_[i+1]*res[i+1] + mu[i+1]
    return res


def main():
    print("N=10------------------")
    l, m = count_lambda_and_mu(0.1, 10, x_value(10, 0, 1))
    print("x")
    print(x_value(10, 0, 1))
    print("y")
    print(y_value(l, m, 10, math.e + (1/math.e) - 2))
    print("N=20------------------")
    l, m = count_lambda_and_mu(0.05, 20, x_value(20, 0, 1))
    print("x")
    print(x_value(20, 0, 1))
    print("y")
    print(y_value(l, m, 20, math.e + (1 / math.e) - 2))


if __name__ == '__main__':
    main()
