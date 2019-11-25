import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)

    # creating a dictionary to track our
    # yes and no response
    # counts = defaultdict(int) # default dictonary
    counts = Counter()

    for line in csv_reader:
        counts[line['Hobbyist']] += 1

total = counts['Yes'] + counts['No']
yes_pct = (counts['Yes'] / total) * 100
yes_pct = round(yes_pct, 2)

no_pct = (counts['No'] / total) * 100
no_pct = round(no_pct, 2)

print(f'Yes: {yes_pct}%')
print(f'No: {no_pct}%')
