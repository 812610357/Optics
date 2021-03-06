import numpy as np
import matplotlib.pyplot as plt
from math import pi

Lambda = 0.5
d = 30
a = 15
n = 10
sintheta = np.linspace(-0.06, 0.06, 12000)

alpha = pi*a*sintheta/Lambda
beta = pi*d*sintheta/Lambda
id = (np.sin(alpha)/alpha)**2
id = id/max(id)
ii = (np.sin(n*beta)/np.sin(beta))**2
ii = ii/max(ii)
i = id*ii
ii = np.column_stack((i, i))

plt.plot(sintheta, id, label="$I_d$")
plt.plot(sintheta, i, label="$I$")
plt.ylabel("$I/I_0$")
plt.xlabel("$\sin{\\theta}$")
plt.title("Light-strength distribution")
plt.legend()

plt.show()
