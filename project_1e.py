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

n = int(input("Size of the matrix (n=10, 100 or 1000 (warning: n=1000 takes about 2 minutes to run)): "))
h = 1/(n+1)
x = np.linspace(0,1,n)
q = h**2*f(x)
A = tridiag(n)

t0 = time.time()
init = pylib()
LUdecomp = init.luDecomp(A)         # LU-decomp., pivot permutation, row interchange (+1/-1)
LUbacksub = init.luBackSubst(LUdecomp[0], LUdecomp[1], q)
T = time.time()-t0
print("CPU time: %.3f s" % (T))

def v(x):
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

plt.plot(x,LUbacksub)
plt.plot(x,v(x))
plt.legend(["Numerical (LU) solution","Closed-form solution"])
plt.grid(); plt.title("LU-decomposition, Grid size = %i, CPU time = %.3f s" % (n,T))
plt.show()
