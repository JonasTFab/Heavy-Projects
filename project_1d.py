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
    x = np.linspace(0,1,n+2)[1:-1]
    h = 1/(n+1)
    q = (h**2)*f(x)
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    q_temp = np.zeros(n)
    u = np.zeros(n)
    v = analytic(x)

    ####    Forward sub   ####
    for i in range(1,n):
        #b_temp[i] = b - 1/b_temp[i-1]
        q_temp[i] = q[i]-q_temp[i-1]*a/b_temp[i-1]

    #### Backward ####
    u[-2] = q_temp[-1]/b_temp[-1]
    for i in range(2,n):          # 3*n flops
        u[-i] = (q_temp[-i] - a*u[-i+1])/b_temp[-i]

    ####  Calculate error
    eps_inside = max(abs((u[1:-1]-v[1:-1])/v[1:-1]))
    eps = np.log10(eps_inside)
    return h, eps_inside, v, u, x

if __name__ == '__main__':

    #### Compute error ####
    N = 6
    n = np.logspace(1,N,N) # ones(N)*10**exp
    h = np.zeros(N)
    error = np.zeros(N)
    t0 = time.time()

    fig, [ax1,ax2] = plt.subplots(2)

    for i in range(N:
        h[i], error[i], v, u, x = algo(int(n[i]))
        ax2.plot(x,u)
        ax2.plot(x,v)

        print("log10(h) = %.2e        rel. error = %.2e         time = " % (h[i],error[i]))


    ax1.loglog(h,error)
    ax1.set_xlabel("log10(h)"); plt.ylabel("Epsilon (relative error)")

    plt.show()
