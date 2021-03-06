import numpy as np
import matplotlib.pyplot as plt
from math import pi

Lambda = 0.5
d = 30
a = 10
n = 10
sintheta = np.linspace(-0.12, 0.12, 12000)

alpha = pi*a*sintheta/Lambda
beta = pi*d*sintheta/Lambda
id = (np.sin(alpha)/alpha)**2
id = id/max(id)
ii = (np.sin(n*beta)/np.sin(beta))**2
ii = ii/max(ii)
i = id*ii
ii = np.column_stack((i, i))

plt.figure(figsize=(6, 6))

plt.subplot(3, 1, (1,2))
plt.axis([min(sintheta), max(sintheta), 0, 1])
plt.plot(sintheta, id, label="$I_d$")
plt.plot(sintheta, i, label="$I$")
plt.xlabel("$\sin{\\theta}$")
plt.ylabel("$I/I_0$")
plt.title("Light-strength distribution")
plt.legend()

plt.subplot(8, 1, 7)
plt.pcolor(sintheta, np.array([0, 1]), ii.T, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(8, 1, 8)
plt.pcolor(sintheta, np.array([0, 1]), ii.T, cmap='jet')
plt.xlabel("$\sin{\\theta}$")
plt.yticks([])

plt.show()
