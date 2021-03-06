import numpy as np
import matplotlib.pyplot as plt
from math import pi

Lambda = 0.5
a = 20
b = 20
sintheta1 = np.linspace(-0.12, 0.12, 1201)
sintheta2 = np.linspace(-0.12, 0.12, 1201)

alpha = pi*a*sintheta1/Lambda
beta = pi*b*sintheta2/Lambda
ia = (np.sin(alpha)/alpha)**2
ib = (np.sin(beta)/beta)**2
ia = np.column_stack((ia, np.zeros((1201, 1))))
ib = np.column_stack((ib, np.zeros((1201, 1))))
i = np.dot(ia, ib.T)

plt.figure(figsize=(6, 6))

plt.subplot(2, 1, 1)
plt.axis([min(sintheta1), max(sintheta1), 0, 1])
plt.plot(sintheta1, ia[:, 0], label="$I$")
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
