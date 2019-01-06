import numpy as np
from matplotlib import pyplot

def OuSim(r0, K, theta, sigma, T, N):
    #a function to simulate the Ornstein–Uhlenbeck process
    dt = T/float(N)    
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + sigma*np.sqrt(dt)*np.random.normal()
        rates.append(rates[-1] + dr)

    #cumsum alternative to by pass the loop is under construction#
        
    return rates

r0 = 0.005
K = 0.20
theta = 0.01
sigma = 0.012
T = 1
N = 100

seed = 123
np.random.seed(seed)
print(*range(1, 10))

x = range(N+1)
y = OuSim(r0, K, theta, sigma, T, N)

pyplot.title(r'Short rate, $r_t$')
pyplot.ylabel('Sequence value')
pyplot.xlabel('No. of observations')
pyplot.plot(x, y)
pyplot.show()
