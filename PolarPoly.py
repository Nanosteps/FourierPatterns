'''
Created by Dr. A. Kaniyoor
2020-21

Chebyshev polynomials of the first kind
can be written as
T_n(cos x)=cos nx

'''

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)

for i in range(0,17,2):
    T=np.cos(i*theta)
    plt.polar(theta,T+i,'k')


plt.axis('off')
plt.show()
