import matplotlib.pyplot as plt
x = [1, 2, 3, 32]  # list
y = [21, 33, 44, 13]
# plt.plot(x, y, label="First Line")


# plt.plot([1, 2, 3, 53], [1, 2, 4, 5])
plt.bar(x, y, label="runs", color="r")
plt.bar([12, 11, 41, 35], [53, 13, 25, 34], label="balls", color="b")
plt.legend()  # to make the label appear, we need this line
plt.show()
