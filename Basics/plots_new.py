import matplotlib.pyplot as plt
x = [1, 2, 3, 1]
y = [22, 3, 4, 33]
plt.plot(x, y, label="First Line")

plt.plot([1, 2, 3, 53], [1, 2, 4, 5])
plt.legend()  # to make the label appear we need this line
plt.show()