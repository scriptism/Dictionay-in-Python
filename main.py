names = ['amin', 'halim', 'shafiq','amin', 'halim', 'shafiq', 'sulaiman',
         'amin', 'halim', 'sulaiman', 'amin','rasul']

counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)

# Dictionary
bag = {}
bag['glasses'] = 5
bag['books'] = 3
bag['pens'] = 8
print(bag)

bag['books'] = bag['books'] + 2
bag['pens'] = bag['pens'] - 3
print(bag)

bag['new_item'] = 10
print(bag)