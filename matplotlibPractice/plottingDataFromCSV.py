from matplotlib import pyplot as plt
import numpy as np
import csv

plt.style.use('seaborn-darkgrid')

with open('plottingData.csv') as csv_file:
    csv_data = csv.DictReader(csv_file)

    languages_counter = dict()

    for row in csv_data:
        for language in row['LanguagesWorkedWith'].split(';'):
            languages_counter[language] = languages_counter.get(
                language, 0) + 1

    LIMIT = 15
    LANGUAGES = list()
    COUNTS = list()

    for language, count in languages_counter.items():
        LANGUAGES.append(language)
        COUNTS.append(count)
        LIMIT -= 1

        if LIMIT == 0:
            break

    print(languages_counter)
    print(LANGUAGES, COUNTS)

plt.barh(LANGUAGES, COUNTS)

plt.title("Most Popular Programming Languages")
plt.xlabel("Number Of People Who Use")

plt.tight_layout()
plt.savefig('plots/csvPlot.png')
plt.show()
