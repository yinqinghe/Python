import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(5)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1, 2, 3, 4, 5])
plt.show()
