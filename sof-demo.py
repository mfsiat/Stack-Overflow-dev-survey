# 1st check for coding_as_hobby
# 2nd languageWorkedWith or popular language

import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)

    # creating a dictionary to track our
    # yes and no response
    # counts = defaultdict(int) # default dictonary
    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

        for language in languages:
            language_counter[language] += 1

print(language_counter.most_common(10))
