# Matplotlib使用text Markup(一种文本标记语言)显现出来
# 具体的使用方法是将文本标记符方法在一对美元符号$内

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

plt.plot(t, s)

plt.title(r'$\alpha_i> \beta_i$', fontsize=20)

plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize=20)

plt.text(0.1, -0.5, r'$\sqrt{2}$', fontsize=10)

plt.xlabel('time(s)')
plt.ylabel('volts(mV')


plt.show()
