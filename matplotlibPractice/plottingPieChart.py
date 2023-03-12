from cv2 import exp
from matplotlib import pyplot as plt

plt.style.use('bmh')

entries = {'JavaScript': 59219, 'HTML/CSS': 55466,
           'SQL': 47544, 'Python': 36443, 'Java': 35917, }
slices = list()
labels = list()
explode = [0, 0, 0, 0.1, 0]

for lang, count in entries.items():
    slices.append(count)
    labels.append(lang)

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'lightgray'})

plt.title('Most Popular Programming Language')
plt.tight_layout()
plt.savefig('plots/pieChart.png')
plt.show()
