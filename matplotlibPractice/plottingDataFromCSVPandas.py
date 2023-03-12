from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import csv


plt.style.use('seaborn-darkgrid')

data = pd.read_csv('plottingData.csv')
LANGUAGE_RESPONSES = data['LanguagesWorkedWith']

LANGUAGE_COUNTER = Counter()

for response in LANGUAGE_RESPONSES:
    LANGUAGE_COUNTER.update(response.split(';'))

COUNTS = list()
LANGUAGES = list()

for item in LANGUAGE_COUNTER.most_common(15):
    LANGUAGES.append(item[0])
    COUNTS.append(item[1])

LANGUAGES.reverse()
COUNTS.reverse()

plt.barh(LANGUAGES, COUNTS)

plt.title("Most Popular Programming Languages")
plt.xlabel("Number Of People Who Use")

plt.tight_layout()
plt.savefig('plots/csvPandasPlot.png')
plt.show()
