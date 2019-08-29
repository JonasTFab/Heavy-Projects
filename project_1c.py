import numpy as np, matplotlib.pyplot as plt, random as r, time

def f(x):
    return 100 * np.exp(-10 * x)

n = int(input("Size of the matrix (10, 100 or 1000): "))
x = np.linspace(0,1,n)
h = 1/(n+1)
q = (h**2)*f(x)

"""def array(n):
    arr = input("Consistent(c) or random(r) numbers on vector?: ")
    if arr == "c" or arr == "C":
        arr = np.ones(n)*int(input("What integer?: "))
    elif arr == "r" or arr == "R":
        arr_start = int(input("Smallest integer in the random interval?: "))
        arr_end = int(input("Biggest integer in the random interval?: "))
        arr = np.ones(n)
        for i in range(n):
            arr[i] = r.randint(arr_start,arr_end)
    else:
        try:
            arr = np.ones(n)*int(arr)
        except:
            sys.exit("ERROR! You must insert a legal letter or integer.")
    return arr
a = array(n)
b = array(n)
c = array(n)"""

a = np.ones(n)*float(input("Values of vector a (diagonal): "))
b = np.ones(n)*float(input("Values of vector b (below diagonal): "))
c = np.ones(n)*float(input("Values of vector c (over diagonal): "))
d = np.ones(n)
l = np.ones(n)
u = np.ones(n)
y = np.zeros(n)
v = np.zeros(n)

t0 = time.time()
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

t1 = time.time()
total = t1-t0
print('CPU time:'total)

plt.plot(x,v)
plt.plot(x,u(x))
plt.legend(["Numerical solution","Closed-form solution"])
plt.title("Grid size = %i" % n); plt.grid()
plt.show()