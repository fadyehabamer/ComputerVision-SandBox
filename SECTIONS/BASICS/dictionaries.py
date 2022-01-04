# A Dictionary === Object in JS

# Create dict
person = {
    'first_name': 'fady',
    'last_name': 'amer',
    'age': 21
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '01067065401'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict === spread operator in es6  === person2 = {...person}
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict === array of objects
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
