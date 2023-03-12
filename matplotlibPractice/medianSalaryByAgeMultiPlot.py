from plottingData import dev_x as ages_x, py_dev_y, dev_y, js_dev_y
from matplotlib import pyplot as plt

plt.plot(ages_x, py_dev_y, color='#1e90ff',
         marker='o', linewidth=3, label="Python Devs")
plt.plot(ages_x, js_dev_y, color='#1e909e', linewidth=2,
         marker='v', label="Javascript Devs")
plt.plot(ages_x, dev_y, color='#000000',
         linestyle="--", marker='.', linewidth=3, label="All Devs")

print("Available styles \n", plt.style.available)
plt.style.use('bmh')

# for changing the line style
fmt = '[color][marker][line]'

plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) By Age')

# will add the part which will help us identify each plot
plt.legend()

# adding a grid in to the plot
plt.grid(True)

# adjusting padding for better view
plt.tight_layout()

# saving the plot as a picture 
plt.savefig('plots/plot.png')

plt.show()