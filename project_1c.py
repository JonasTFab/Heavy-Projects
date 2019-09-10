import numpy as np, matplotlib.pyplot as plt, random as r, time


def f(x):               # 3 flops
    return 100*np.exp(-10*x)

a = -1
b = 2
c = -1

def spes_algo(n):
    #n = int(input("Size of the matrix (10, 100 or 1000): "))
    x = np.linspace(0,1,n+2)[1:-1]
    h = 1/(n+1)
    q = (h**2)*f(x)
    index = np.linspace(1,n,n)
    b_temp = (index+1)/index
    q_temp = np.zeros(n)
    q_temp[0] = q[0]
    u = np.zeros(n)

    ####    Forward sub   ####
    t0 = time.time()
    for i in range(1,n):                    # 2*n flops
        q_temp[i] = q[i] + q_temp[i-1]/b_temp[i-1]

    #### Backward ####
    u[-1] = q_temp[-1]/b_temp[-1]
    for i in range(2,n+1):                  # 2*n flops
        u[-i] = (q_temp[-i] + u[-i+1])/b_temp[-i]

    t1 = time.time()
    total = t1-t0
    return u,x,total

def v(x):       # closed-formed solution, 7 flops
    return 1 - (1-np.exp(-10))*x - np.exp(-10*x)

if __name__ == '__main__':
    #### make plots ####
    k = 0
    steps = 50
    for i in range(1,7):
        for j in range(steps):
            print("%.1f %% finished" % (j/steps*100), end="\r")
            u,x,t = spes_algo(10**i)
            k += t
        average_time = k/steps
        print("Average time (special case running %i times) with grid size 10^%i x 10^%i:  %.4f s" % (steps, i, i, average_time))
        plt.plot(x,u,label=('n=10^%i' % i))


    x_an = np.linspace(0,1,30)
    plt.plot(x_an,v(x_an), "r.", label='Closed-form')
    plt.legend();plt.grid()
    plt.title("Numerical/closed-form comparison (special case)")
    plt.xlabel('x'); plt.ylabel('u(x)')
    plt.show()



    """
    Results
    0.001371455192565918
    Grid size: 3 x 3
    0.015735840797424315
    Grid size: 4 x 4
    0.15725901126861572
    Grid size: 5 x 5
    1.5743395566940308
    Grid size: 6 x 6
    """

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

    """t_general = np.array([0.0027681589126586914,0.02973027229309082,0.3003588438034058,3.0235891819000242])
    t_special = np.array([0.001371455192565918,0.015735840797424315,0.15725901126861572,1.5743395566940308])
    pros = t_special/t_general
    for i in range(len(pros)):
        print('%.4f' %(pros[i]))"""


    """
    Difference in computation time
    0.4954
    0.5293
    0.5236
    0.5207"""
