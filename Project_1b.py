import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

# total 4 flops
n = int(input("Size of the matrix (10, 100 or 1000): "))
x = np.linspace(0,1,n)
h = 1/(n+1)
q = (h**2)*f(x)

def array(n, name_of_array):
    arr = input("Consistent(c) or random(r) numbers on vector %s ?: " % (name_of_array))
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


####   Initilize vectors   ####
a = array(n, "upper diagonal")
b = array(n, "diagonal")
c = array(n, "lower diagonal")
u = np.zeros(n)
b_temp = np.zeros(n)
q_temp = np.zeros(n)


####    step 2 (forward substitution)   ####
t0 = time.time()
b_temp[0] = b[0]
q_temp[0] = q[0]
for i in range(1,n):
    b_temp[i] = b[i] - a[i]*c[i-1]/b_temp[i-1]
    q_temp[i] = q[i]-a[i]*q_temp[i-1]/b_temp[i-1]


####    step 3 (backward substitution)   ####
u[-2] = q_temp[-1]/b_temp[-1]
for i in range(2,n):          # 3*n flops
    u[-i] = (q_temp[-i] - c[-i]*u[-i+1])/b_temp[-i]


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
