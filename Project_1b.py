import numpy as np, matplotlib.pyplot as plt

#n = int(input("Size of the matrix (10, 100 or 1000): "))
n = 100
h = 1/(n+1)

def f(x):
    return 100*np.exp(-10*x)


x = np.linspace(0,1,n)
d = h**2*f(x)
v = np.zeros(n)

#a = np.ones(n-1)*float(input("Values of vector a: "))
#b = np.ones(n)*float(input("Values of vector b: "))
#c = np.ones(n-1)*float(input("Values of vector c: "))
a = np.ones(n-1)*(-1)
b = np.ones(n)*2
c = np.ones(n-1)*(-1)


c_mark = np.zeros(n-1)
d_mark = np.zeros(n)

c_mark[0] = c[0]/b[0]
d_mark[0] = d[0]/b[0]


# Found this algorithm at https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
# But does it work tho
for i in range(1,n-1):
    c_mark[i] = c[i]/(b[i]-a[i]*c_mark[i-1])
    d_mark[i] = (d[i]-a[i]*d_mark[i-1]) / (b[i]-a[i]*c_mark[i-1])
    v[i] = d_mark[n-i-1] - c_mark[n-i-1]*v[n-i]

d_mark[-1] = (d[-1]-a[-1]*d_mark[-2]) / (b[-1]-a[-1]*c_mark[-2])
v[n-1] = d_mark[n-1]


def u(x):           # closed-form solution
    return 1-(1-np.exp(-10))*x - np.exp(-10*x)


plt.plot(x,v)
plt.plot(x,u(x))
plt.legend(["Numerical solution","Closed-form solution"])
plt.title("Grid size = %i" % n)
plt.show()
