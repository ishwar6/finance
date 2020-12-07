import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()


# Show the plot
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26],
           color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
plt.show()

fig, ax = plt.subplots(3, 1, figsize=(24, 20), sharex=True)
df.adj_close.plot(ax=ax[0])
ax[0].set(title='MSFT time series',
          ylabel='Stock price ($)')
df.simple_rtn.plot(ax=ax[1])
ax[1].set(ylabel='Simple returns (%)')
df.log_rtn.plot(ax=ax[2])
ax[2].set(xlabel='Date',
          ylabel='Log returns (%)')
