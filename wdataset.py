import dataset


db = dataset.connect('sqlite:///nobel_winners.db')

'''
Resetar a tabela ->
wtable = db['winners']
wtable.drop()

wtable = db['winners']
print(wtable.find())
'''
nobel_winners = [
    {
    'category': 'Physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'gender': 'male',
    'year': 1921},
    {
    'category': 'Chemistry',
    'name': 'Marie Curie',
    'nationality': 'Polish',
    'gender': 'female',
    'year': 1911}
]

with db as tx:
    tx['winners'].insert_many(nobel_winners)
print(list(db['winners'].find()))    