import numpy as np
from pylab import plt, mpl

plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'
np.set_printoptions(precision=4, suppress=True)

# Page 358, https://www.ipcc.ch/site/assets/uploads/2018/03/TAR-06.pdf

alfa = 5.35
beta = 0.0906
rando = 3.2
CWm2 = 0.81


# Baseline value , Co2 concentration at 1750
C0 = 278

# C is CO2 in ppm

def f(C, C0):
    return CWm2 * (alfa) * np.log(C/C0)

def f0(C, C0):
    return (alfa/rando) * np.log(C/C0)

def f1(C, C0):
    return (3 / np.log(2)) * alfa * np.log(C/C0)

def f2(C, C0):
    return CWm2 * alfa * np.log(C/C0) + beta * (np.sqrt(C) - np.sqrt(C0))

def g(C):
    return np.log( 1 + 1.2*C + 0.005*C**2 + 1.4*10**-6 * C**3)

def f3(C, C0):
    return g(C) - g(C0)

# C is CO2 in ppm
C = np.arange(100, 1550, 50)

tmp = np.diff(f(C, C0))

index = [0]

T = np.delete(tmp, index)

C = C[:-2]


plt.figure(figsize=(10,6))
plt.bar(C, T, width=10)


print(T)
print(C)


print(len(T))
print(len(C))

plt.show()