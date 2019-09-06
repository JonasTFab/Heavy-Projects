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
    return 1 - (1 - np.exp( - 10))*x - np.exp(-10*x)

def algo(n):
    #x = np.linspace(0,1,n)
    x = np.linspace(0,1,n+2)[1:-1]
    h = 1/(n+1)
    q = (h**2)*f(x)
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    #b_temp = (index-1)/index
    q_temp = np.zeros(n)
    q_temp[0] = q[0]
    u = np.zeros(n)
    v = analytic(x)

    t0 = time.time()
    ####    Forward sub   ####
    #for i in range(2,n):            # 3*n flops
    for i in range(1,n):
        #b_temp[i] = b - 1/b_temp[i-1]
        q_temp[i] = q[i] + (q_temp[i-1]) / b_temp[i-1]
        #q_temp[i] = q[i]+b_temp[i]*q_temp[i-1]
    #### Backward ####
    u[-1] = q_temp[-1]/b_temp[-1]
    for i in range(2,n+1):            # 3*n flops
        u[-i] = (q_temp[-i] + u[-i+1]) / b_temp[-i]
        #u[-i-1] = b_temp[i]*(q_temp[i-1]+u[i])
    #u[-1] = 0
    ####  Calculate error ####
    eps_inside = max(abs((u-v)/v))
    eps = abs(np.log10(eps_inside))
    return h, eps_inside, time.time()-t0#u,x

"""u_10,x_10 = algo(10)
u_100,x_100 = gen_algo(100)
u_1000,x_1000 = gen_algo(100000)
u_1000,x_1000 = gen_algo(1000000)
x_vec = np.linspace(0,1,1000)

plt.plot(x_10,u_10,label = 'n=10')
plt.plot(x_100,u_100,label = 'n=100')
plt.plot(x_1000,u_1000,label = 'n=1000')

plt.plot(x_vec,analytic(x_vec), label = 'Closed-form')
plt.title("Closed-form/numerical comparison");
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()"""
#### Compute error ####
N = 6
n = np.logspace(1,N,N)
h = np.zeros(N)
error = np.zeros(N)


for i in range(N):
    h[i], error[i], t1, = algo(int(n[i]))
    print("log10(h) = %.2e        rel. error = %.2e         time = %.3f s" % \
                                    (np.log10(h[i]),np.log10(error[i]),t1))

plt.loglog(h,error)
plt.title("Relative error")
plt.xlabel("log10(h)"); plt.ylabel("Epsilon")
plt.grid()

plt.show()
