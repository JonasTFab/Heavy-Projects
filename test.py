



###### Tester 1d for en spesifikk x verdi for ulike step length ########




import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

# total 4 flops

# total 3 flops making the arrays
a = -1#np.ones(n)*float(input("Values of vector a (diagonal): "))
b = 2#np.ones(n)*float(input("Values of vector b (below diagonal): "))
c = -1#np.ones(n)*float(input("Values of vector c (over diagonal): "))
#b_temp = np.zeros(n)
def analytic(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

def algo(n):
    x = np.linspace(0,1,n)
    h = 1/(n+1)
    q = (h**2)*f(x)
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    q_temp = np.zeros(n)
    u = np.zeros(n)
    v = analytic(x)

    ####    Forward sub   ####
    for i in range(1,n):            # 3*n flops
        #b_temp[i] = b - 1/b_temp[i-1]
        q_temp[i] = q[i]-q_temp[i-1]*a/b_temp[i-1]

    #### Backward ####
    u[-2] = q_temp[-2]/b_temp[-2]
    for i in range(2,n):            # 3*n flops
        u[-i] = (q_temp[-i] - a*u[-i+1])/b_temp[-i]

    ####  Calculate error
    eps_inside = abs((u[int(n/2)]-v[int(n/2)])/v[int(n/2)])
    return h, eps_inside

#### Compute error ####
N = 1000
N_times = 10
n = np.linspace(N_times*1,N_times*N,N)
h = np.zeros(N)
eps_ins = np.zeros(N)

for i in range(N):
    h[i], eps_ins[i] = algo(int(n[i]))

plt.loglog(h,eps_ins)
plt.show()
