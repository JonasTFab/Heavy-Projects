import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

# total 4 flops
n = int(input("Size of the matrix (10, 100 or 1000): "))
x = np.linspace(0,1,n)
h = 1/(n+1)
q = (h**2)*f(x)

# total 3 flops making the arrays
a = -1#np.ones(n)*float(input("Values of vector a (diagonal): "))
b = 2#np.ones(n)*float(input("Values of vector b (below diagonal): "))
c = -1#np.ones(n)*float(input("Values of vector c (over diagonal): "))
#b_temp = np.zeros(n)

index = np.linspace(1,n,n)
b_temp = (index+1)/index
q_temp = np.zeros(n)
u = np.zeros(n)
t0 = time.time()
####    Forward sub   ####
#b_temp[0] = b
for i in range(1,n):
    #b_temp[i] = b - 1/b_temp[i-1]
    q_temp[i] = q[i]-q_temp[i-1]*a/b_temp[i-1]
#### Backward ####
u[-2] = q_temp[-1]/b_temp[-1]
for i in range(2,n):          # 3*n flops
    u[-i] = (q_temp[-i] - a*u[-i+1])/b_temp[-i]


def v(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)
t1 = time.time()
total = t1-t0
print('CPU time:',total)

plt.plot(x,u)
plt.plot(x,v(x))
plt.legend(["Numerical solution","Closed-form solution"])
plt.title("Grid size = %i" % n); plt.grid()
plt.show()

"""
d[0] = a[0]
u[0] = c[0]
for i in range(1,n):            # 3*n flops
    l[i] = b[i]/d[i-1]
    d[i] = a[i] - l[i]*u[i-1]

l[i] = b[i]/d[i-1]
d[i] = a[i] - l[i]*u[i-1]
u[i] = c[i]

####    step 2 (forward substitution)   ####
y[0] = q[0]
for i in range(1,n):            # 2*n flops
    y[i] = q[i] - l[i]*y[i-1]


####    step 3 (backward substitution)   ####
v[-1] = y[-1]/d[-1]
for i in range(2,n+1):          # 3*n flops
    v[n-i] = (y[n-i]-u[n-i]*v[n-i+1])/d[n-i]"""
