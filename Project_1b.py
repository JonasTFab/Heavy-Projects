import numpy as np, matplotlib.pyplot as plt

def f(x):
    return 100*np.exp(-10*x)

n = int(input("Size of the matrix (10, 100 or 1000): "))
x = np.linspace(0,1,n)
h = 1/(n+1)
q = (h**2)*f(x)

a = np.ones(n)*float(input("Values of vector a (diagonal): "))
b = np.ones(n)*float(input("Values of vector b (below diagonal): "))
c = np.ones(n)*float(input("Values of vector c (over diagonal): "))
d = np.ones(n)
l = np.ones(n)
u = np.ones(n)
y = np.zeros(n)
v = np.zeros(n)

####    step 1 (decomposition)   ####
d[0] = a[0]
u[0] = c[0]
for i in range(1,n):
    l[i] = b[i]/d[i-1]
    d[i] = a[i] - l[i]*u[i-1]
    u[i] = c[i]


####    step 2 (forward substitution)   ####
y[0] = q[0]
for i in range(1,n):
    y[i] = q[i] - l[i]*y[i-1]


####    step 3 (backward substitution)   ####
v[-1] = y[-1]/d[-1]
for i in range(2,n+1):
    v[n-i] = (y[n-i]-u[n-i]*v[n-i+1])/d[n-i]


def u(x):       # closed-formed solution
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

plt.plot(x,v)
plt.plot(x,u(x))
plt.legend(["Numerical solution","Closed-form solution"])
plt.title("Grid size = %i" % n); plt.grid()
plt.show()
