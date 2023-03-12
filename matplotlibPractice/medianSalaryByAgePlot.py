from plottingData import dev_x, dev_y
from matplotlib import pyplot as plt

# plotting the data
plt.plot(dev_x, dev_y)

# adding the title and lables
plt.xlabel('Age')
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) By Age")

# displaying the plot
plt.show()