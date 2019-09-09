import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

a = -1
b = 2
c = -1

def analytic(x):       # closed-formed solution, 7 flops
    return 1 - (1 - np.exp( - 10))*x - np.exp(-10*x)

def algo(n):
    x = np.linspace(0,1,n+2)[1:-1]
    h = 1/(n+1)
    q = (h**2)*f(x)
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    q_temp = np.zeros(n)
    q_temp[0] = q[0]
    u = np.zeros(n)
    v = analytic(x)

    t0 = time.time()
    ####    Forward sub   ####
    for i in range(1,n):                # 2*n flops
        q_temp[i] = q[i] + (q_temp[i-1]) / b_temp[i-1]

    #### Backward ####
    u[-1] = q_temp[-1]/b_temp[-1]
    for i in range(2,n+1):              # 2*n flops
        u[-i] = (q_temp[-i] + u[-i+1]) / b_temp[-i]

    ####  Calculate error ####
    eps_inside = max(abs((u-v)/v))
    eps = abs(np.log10(eps_inside))
    return h, eps_inside, time.time()-t0


#### Compute error ####
N = 7
n = np.logspace(1,N,N)
h = np.zeros(N)
error = np.zeros(N)


for i in range(N):
    h[i], error[i], t1, = algo(int(n[i]))
    print("log10(h) = %.2f        rel. error = %.2f         time = %.4f s" % \
                                    (np.log10(h[i]),np.log10(error[i]),t1))

plt.loglog(h,error)
plt.title("Relative error")
plt.xlabel("log10(h)"); plt.ylabel("Epsilon (log10|(u-v)/v|)")
plt.grid()

plt.show()
