import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

def analytic(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

def algo(n):
    # total 4 flops
    x = np.linspace(0,1,n)
    h = 1/(n+1)
    q = (h**2)*f(x)


    ####   Initilize vectors   ####
    a = -1#array(n, "upper diagonal")
    b = 2#array(n, "diagonal")
    c = -1#array(n, "lower diagonal")
    u = np.zeros(n)
    b_temp = np.zeros(n)
    q_temp = np.zeros(n)


    ####    step 2 (forward substitution)   ####
    t0 = time.time()
    b_temp[0] = b
    q_temp[0] = q[0]
    for i in range(1,n):
        b_temp[i] = b - a*c/b_temp[i-1]
        q_temp[i] = q[i]-a*q_temp[i-1]/b_temp[i-1]


    ####    step 3 (backward substitution)   ####
    u[-1] = 0
    for i in range(2,n):          # 3*n flops
        u[-i] = (q_temp[-i] - c*u[-i+1])/b_temp[-i]
    v = analytic(x)
    ####  Calculate error ####
    eps_inside = abs((v[1:-1] - u[1:-1]) / u[1:-1])
    #div = 10/2
    #eps_inside = abs((u[int(n/div)]-v[int(n/div)])/v[int(n/div)])
    eps = min(np.log10(eps_inside))
    return h, eps, time.time()


#### Compute error ####
N = 6
n = np.logspace(1,N,N)
#N = 300; n = 10**np.linspace(1,5,N)
h = np.zeros(N)
error = np.zeros(N)
t0 = time.time()

for i in range(0,N):
    h[i], error[i], t1 = algo(int(n[i]))
    #plt.plot(v[1:-1])
    #plt.show()
    print("log10(h) = %.2e        rel. error = %.2e         time = %.3f s" % \
                                    (np.log10(h[i]),(error[i]),t1-t0))



plt.plot(np.log10(h),error)
plt.xlabel("log10(h)"); plt.ylabel("Relative error (epsilon)")
plt.grid()

plt.show()
