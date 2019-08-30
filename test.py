from project_1d import algo
import numpy as np
import matplotlib.pyplot as plt

N = 100
h, e, v, u, x = algo(N)
print(h,e)

plt.plot(x,u,"-o",label="u")
plt.plot(x,v,"-o",label="v")
plt.legend()
plt.grid()
plt.show()
