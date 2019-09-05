import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

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

# total 3 flops making the arrays
a = -1 #np.ones(n)*float(input("Values of vector a (diagonal): "))
b = 2 #np.ones(n)*float(input("Values of vector b (below diagonal): "))
c = -1 #np.ones(n)*float(input("Values of vector c (over diagonal): "))
#b_temp = np.zeros(n)

def spes_algo(n):
    #n = int(input("Size of the matrix (10, 100 or 1000): "))
    x = np.linspace(0,1,n)
    h = 1/(n-1)
    q = (h**2)*f(x)
    t0 = time.time()
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    q_temp = np.zeros(n)
    u = np.zeros(n)

    ####    Forward sub   ####
    #b_temp[0] = b
    for i in range(1,n):
        #b_temp[i] = b - 1/b_temp[i-1]
        q_temp[i] = q[i]-q_temp[i-1]*a/b_temp[i-1]


    #### Backward ####
    u[-2] = q_temp[-1]/b_temp[-1]
    for i in range(2,n):          # 3*n flops
        u[-i] = (q_temp[-i] - a*u[-i+1])/b_temp[-i]
    t1 = time.time()
    total = t1-t0
    print('CPU time: %.5g s' % total)
    print('Grid size:',n)
    return u

def v(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

u_10 = spes_algo(1000)
u_100 = spes_algo(10000)
u_1000 = spes_algo(100000)
u_1000 = spes_algo(1000000)

#plt.plot(x,u)
#plt.plot(x,v(x))
#plt.legend(["Numerical solution","Closed-form solution"])
#plt.title("Grid size: %i, CPU time = %.3f s" % (n,total)); plt.grid()
#plt.show()

print(0.002372 - 0.0018089)

print(0.023866 - 0.018122)

print(0.24264 - 0.18424)

print(2.5207 -1.8112)



"""
special
CPU time: 0.0018089 s
Grid size: 1000
CPU time: 0.018122 s
Grid size: 10000
CPU time: 0.18424 s
Grid size: 100000
CPU time: 1.8112 s
Grid size: 1000000

"""
