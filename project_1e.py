import numpy as np
import matplotlib.pyplot as plt
import time
from computationalLib import pylib

def f(x):               # 3 flops
    return 100*np.exp(-10*x)

def tridiag(n):             # tridiag matrix with 2 on diag and -1 directly below and over diag
    A = np.zeros((n,n))
    for i in range(n-1):
        A[i,i] = 2
        A[i,i+1] = -1
        A[i+1,i] = -1
    A[n-1,n-1] = 2
    return A

n = int(input("Size of the matrix (10, 100 or 1000): "))
h = 1/(n+1)
x = np.linspace(0,1,n)
q = h**2*f(x)
A = tridiag(n)

t0 = time.time()
init = pylib()
LUdecomp = init.luDecomp(A)         # LU-decomp., pivot permutation, row interchange (+1/-1)
LUbacksub = init.luBackSubst(LUdecomp[0], LUdecomp[1], q)
print("CPU time: %.3f s" % (time.time()-t0))

def v(x):
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

plt.plot(x,LUbacksub)
plt.plot(x,v(x))
plt.legend(["Numerical solution","Closed-form solution"])
plt.grid(); plt.title("Quadratic grid size: %i" % n)
plt.show()
