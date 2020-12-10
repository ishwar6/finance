import matplotlib.pyplot as plt
x = [1, 2, 3, 32]  # list
y = [21, 33, 44, 13]
# plt.plot(x, y, label="First Line")
population_ages = [23, 64, 22, 32, 32, 34, 34, 89, 23, 64, 24, 24, 22, 55,
                   24, 24, 32, 42, 65, 84, 24, 23, 53, 46, 54, 234, 24, 72, 23, 74, 34]
ids = [x for x in range(len(population_ages))]
plt.bar(ids, population_ages)
# plt.plot([1, 2, 3, 53], [1, 2, 4, 5])
#plt.bar(x, y, label="runs", color="r")
#plt.bar([12, 11, 41, 35], [53, 13, 25, 34], label="balls", color="b")
# plt.legend()  # to make the label appear, we need this line
plt.show()
