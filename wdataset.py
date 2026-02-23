import dataset


db = dataset.connect('sqlite:///nobel_winners.db')

wtable = db['winners']
winners = wtable.find()
winners = list(winners)
print(winners)