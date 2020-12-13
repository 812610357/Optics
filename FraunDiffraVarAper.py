import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ssp
from math import pi

Lambda = 0.5
d = 20
sintheta1 = np.linspace(-0.12, 0.12, 1201)
sintheta2 = np.linspace(-0.12, 0.12, 1201)
sintheta1 = np.tile(sintheta1, (1201, 1))
sintheta2 = np.tile(sintheta2, (1201, 1)).T
r = np.sqrt(sintheta1**2+sintheta2**2)

delta = pi*d*r/Lambda
i = (2*ssp.j1(delta)/delta)**2

plt.figure(figsize=(6, 6))

plt.subplot(2, 1, 1)
plt.axis([min(sintheta1[0, :]), max(sintheta1[0, :]), 0, 1])
plt.plot(sintheta1[600, :], i[600, :], label="$I$")
plt.ylabel("$I/I_0$")
plt.xlabel("$\sin{\\theta}$")
plt.title("Light-strength distribution")

plt.subplot(2, 2, 3)
plt.pcolor(sintheta1, sintheta2, np.sqrt(i), vmax=0.5, cmap='gray')
plt.xlabel("$\sin{\\theta_1}$")
plt.ylabel("$\sin{\\theta_2}$")

plt.subplot(2, 2, 4)
plt.pcolor(sintheta1, sintheta2, np.sqrt(i), vmax=0.5, cmap='jet')
plt.xlabel("$\sin{\\theta_1}$")
plt.ylabel("$\sin{\\theta_2}$")

plt.show()
