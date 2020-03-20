import numpy as np
from scipy.linalg import solve

def seidel(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print (str(i).zfill(3))
        print(x)
    return x

'''___MAIN___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]

n = 20

print("\n\nІніціалізаця"),
print(x)
print("")
x = seidel(A, b, x, n)
print("\nВідповідь "),
print(x)
print("Правильна відповідь "),
print (solve(A, b))
print("\n")