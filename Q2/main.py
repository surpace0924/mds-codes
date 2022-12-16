import math
import matplotlib.pyplot as plt
import numpy as np
  
def N1(l2):
    return math.comb(l2, l2//2)
  
def N2(l):
    c1 = 1/math.sqrt(5)
    c2 = ((1+math.sqrt(5))/2)**(l+2)
    c3 = (1-((1-math.sqrt(5))/(1+math.sqrt(5)))**(l+2))
    return c1 * c2 * c3
    
ls = range(1, 1000)
L1, L2 = [], []
for l in ls:
    L1.append(math.log(N1(2*l), 2)/(2*l))
    L2.append(math.log(N2(l), 2)/l)

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.plot(ls, [1 for l in ls], label="$C(L_1)$")
ax.plot(ls, L1, label="$L_1$")
ax.set_xlabel("number of $l$")
ax.set_ylabel("value")
plt.legend()
plt.show()


fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.plot(ls, [math.log((1+math.sqrt(5))/2, 2) for l in ls], label="$C(L_2)$")
ax.plot(ls, L2, label="$L_2$")
ax.set_xlabel("number of $l$")
ax.set_ylabel("value")
plt.legend()
plt.show()
