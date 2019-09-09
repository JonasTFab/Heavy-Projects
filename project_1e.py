import numpy as np
import matplotlib.pyplot as plt
import time
from computationalLib import pylib
from project_1c import spes_algo

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

def LU_decomp(n):
    h = 1/(n+1)
    x = np.linspace(0,1,n+2)[1:-1]
    q = h**2*f(x)
    A = tridiag(n)

    t0 = time.time()
    init = pylib()
    LUdecomp = init.luDecomp(A)         # LU-decomp., pivot permutation, row interchange (+1/-1)
    LUbacksub = init.luBackSubst(LUdecomp[0], LUdecomp[1], q)
    T = time.time()-t0
    return LUbacksub, T, x

def v(x):
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

def average_after_10_runs(n):
    N = 10
    time = np.zeros(N)
    for i in range(N):
        time[i] = LU_decomp(n)[1]
    avg_time = sum(time)/N
    return avg_time

def compare_methods(n):
    LU = LU_decomp(n)[0]
    s_al = spes_algo(n)[0]
    return abs(LU)-abs(s_al)

#diff10 = max(abs(compare_methods(10)))         # 1.11022302463e-16
#diff100 = max(abs(compare_methods(100)))       # 8.99280649946e-15
#diff1000 = max(abs(compare_methods(1000)))     # 1.66977542904e-13

#m = 10                  # WARNING: if n=1000, the algorithm should only run if you got plenty of time to spare
#avg_time_n10 = average_after_10_runs(m)
#print("Average time taken after 10 numerical calculations with n=%i: %.7f s" % (m,avg_time_n10))

LU_10, t10, x10 = LU_decomp(10); print("Time for n=10: %.4f s" % t10)
LU_100, t100, x100 = LU_decomp(100); print("Time for n=100: %.4f s" % t100)
#LU_1000, t1000, x1000 = LU_decomp(1000); print("Time for n=1000: %.4f s" % t1000)

plt.plot(x10,LU_10,label="LU(n=10)")
plt.plot(x100,LU_100,label="LU(n=100)")
#plt.plot(x1000,LU_1000,label="LU(n=1000)")
X = np.linspace(0,1,30)
plt.plot(X,v(X),"r.",label="Closed-form solution")
plt.legend()
plt.grid(); plt.title("LU-decomposition/closed-form comparison")
plt.show()
