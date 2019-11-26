# 1st check for coding_as_hobby
# 2nd languageWorkedWith or popular language

import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    total = 0

    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

        total += 1
for language, value in language_counter.most_common(10):
    language_pct = (value / total) * 100
    language_pct = round(language_pct, 2)

    print(f'{language}: {language_pct}%')



