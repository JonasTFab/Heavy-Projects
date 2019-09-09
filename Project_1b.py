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

def gen_algo(n): #general algorithm
    ####   Initilize vectors   ####
    #n = int(input("Size of the matrix (10, 100 or 1000): "))
    x = np.linspace(0,1,n+2)[1:-1]
    h = 1/(n+1)
    q = (h**2)*f(x)
    a = np.ones(n)*-1#array(n, "upper diagonal")
    b = np.ones(n)*2#array(n, "diagonal")
    c = np.ones(n)*-1#array(n, "lower diagonal")
    u = np.zeros(n)
    b_temp = np.zeros(n)
    q_temp = np.zeros(n)


    ####    step 2 (forward substitution)   ####
    t0 = time.time()
    b_temp[0] = b[0]
    q_temp[0] = q[0]
    for i in range(1,n):                    # 6*n flops
        b_temp[i] = b[i] - a[i]*c[i-1]/b_temp[i-1]
        q_temp[i] = q[i]-a[i]*q_temp[i-1]/b_temp[i-1]


    ####    step 3 (backward substitution)   ####
    u[-1] = q_temp[-1]/b_temp[-1]
    for i in range(2,n+1):                  # 3*n flops
        u[-i] = (q_temp[-i] - c[-i]*u[-i+1])/b_temp[-i]
    t1 = time.time()
    total = t1-t0
    return u,x,total

def v(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)



#### make plots ####
k = 0
for i in range(1,7):
    for j in range(10):
        u,x,t = gen_algo(10**i)
        k += t
    average_time = k/10
    print("Average time (general case) with grid size 10^%i x 10^%i:  %.4f s"\
                                % (i, i, average_time))
    plt.plot(x,u,label=('n=10^%i' % i))

x_an = np.linspace(0,1,30)
plt.plot(x_an,v(x_an), "r.", label='Closed-form')
plt.title("Numerical/closed-form comparison (general case)")
plt.xlabel('x'); plt.ylabel('u(x)')
plt.legend(); plt.grid()
plt.show()




#### TIMER ####
"""k = 0
for i in range(3,7):
    for j in range(11):
        u,x,t = gen_algo(10**i)
        k += t
    average_time = k/10
    print(average_time)
    print('Grid size:',i,'x',i)"""

"""
produce some selected results
0.0027681589126586914
Grid size: 3 x 3
0.02973027229309082
Grid size: 4 x 4
0.3003588438034058
Grid size: 5 x 5
3.0235891819000242
Grid size: 6 x 6
"""
