from plottingData import dev_x as ages_x, py_dev_y, dev_y, js_dev_y
from matplotlib import pyplot as plt
import numpy as np

X_INDEXES = np.arange(len(ages_x))
WIDTH: float = 0.25

plt.bar(X_INDEXES - WIDTH, py_dev_y, width=WIDTH, color='#1e90ff',
        label="Python Devs")
plt.bar(X_INDEXES, js_dev_y, width=WIDTH, color='#e5ae38',
        label="Javascript Devs")
plt.bar(X_INDEXES + WIDTH, dev_y, width=WIDTH, color='#454545',
        label="All Devs")

print("Available styles \n", plt.style.available)
plt.style.use('bmh')

# for changing the line style
fmt = '[color][marker][line]'

# adding the x-axis labels
plt.xticks(ticks=X_INDEXES, labels=ages_x)

plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) By Age')

# will add the part which will help us identify each plot
plt.legend()

# adjusting padding for better view
plt.tight_layout()

# saving the plot as a picture
plt.savefig('plots/bar.png')

plt.show()
