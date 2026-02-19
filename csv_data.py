nobel_winners = [
    {'name': 'Albert Einstein', 'category': 'Physics', 'nationality': 'Swiss',  'gender': 'male','year': 1921},
    {'name': 'Marie Curie', 'category': 'Chemistry','nationality': 'Polish', 'gender': 'female', 'year': 1911}
]

f = open('nobel_winners.csv', 'w')

cols = nobel_winners[0].keys()
cols = sorted(cols)

with open('nobel_winners.csv', 'w') as f:
    f.write(','.join(cols) + '\n')

    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + '\n')


with open('nobel_winners.csv') as f:
  for line in f.readlines():
    print(line)