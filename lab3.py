from __future__ import annotations

import copy
import numpy as np
from collections.abc import Sequence, MutableSequence


def gauss(matrix):
    n = len(matrix)
    matrix_clone = copy.deepcopy(matrix)

    for k in range(n):
        for i in range(n + 1):
            matrix_clone[k][i] = matrix_clone[k][i] / matrix[k][k]
        for i in range(k + 1, n):
            K = matrix_clone[i][k] / matrix_clone[k][k]
            for j in range(n + 1):
                matrix_clone[i][j] = matrix_clone[i][j] - matrix_clone[k][j] * K
        for i in range(n):
            for j in range(n + 1):
                matrix[i][j] = matrix_clone[i][j]

    for k in range(n - 1, -1, -1):
        for i in range(n, -1, -1):
            matrix_clone[k][i] = matrix_clone[k][i] / matrix[k][k]
        for i in range(k - 1, -1, -1):
            K = matrix_clone[i][k] / matrix_clone[k][k]
            for j in range(n, -1, -1):
                matrix_clone[i][j] = matrix_clone[i][j] - matrix_clone[k][j] * K

    answer = []
    for i in range(n):
        answer.append(matrix_clone[i][n])
    return answer


def bubble_max_row(m, col):
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def gauss_with_choice(m):
    n = len(m)
    for k in range(n - 1):
        bubble_max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    if is_singular(m):
        print('Бесконечное число решений')
        return

    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]

    return x


def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False


def jacobi(
        A: Sequence[Sequence[float]],
        b: Sequence[float],
        eps: float = 0.001,
        x_init: MutableSequence[float] | None = None, x=None):
    def summa(a: Sequence[float], x: Sequence[float], j: int) -> float:
        S: float = 0
        for i, (m, y) in enumerate(zip(a, x)):
            if i != j:
                S += m * y
        return S

    def norm(x: Sequence[float], y: Sequence[float]) -> float:
        return max((abs(x0 - y0) for x0, y0 in zip(x, y)))

    if x_init is None:
        y = [a / A[i][i] for i, a in enumerate(b)]
    else:
        y = x.copy()

    x: list[float] = [-(summa(a, y, i) - b[i]) / A[i][i]
                      for i, a in enumerate(A)]
    k = 0

    while norm(y, x) > eps:
        k += 1
        for i, elem in enumerate(x):
            y[i] = elem
        for i, a in enumerate(A):
            x[i] = -(summa(a, y, i) - b[i]) / A[i][i]
    return x, k


def gauss_seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)
    i = 0

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.linalg.norm(x_new - x) <= eps
        x = x_new
        i += 1

    return x, i


def main():
    A_with_b = [
        [-0.07, -0.41, -0.50, -2.39],
        [-0.13, 0.79, 0.42, 2.71],
        [1.71, 0.01, 0.20, 2.33]
    ]

    A_permutation_rows = [
        [1.71, 0.01, 0.20],
        [-0.13, 0.79, 0.42],
        [-0.07, -0.41, -0.50]
    ]

    b_permutation_rows = [
        2.33,
        2.71,
        -2.39
    ]

    epsilon = 0.5e-4

    print(gauss(A_with_b))
    print(gauss_with_choice(A_with_b))
    print(jacobi(A_permutation_rows, b_permutation_rows, epsilon))
    print(gauss_seidel(A_permutation_rows, b_permutation_rows, epsilon))


if __name__ == '__main__':
    main()