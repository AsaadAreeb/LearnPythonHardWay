##Getting things started##
# stuff = {'name': 'Asaad', 'age': 22, 'height': 5 * 12 + 2}
# print(stuff)

# print(stuff['age'])

# print(stuff['height'])

# print(stuff['name'])

# stuff['city'] = 'Mul'

# print(stuff['city'])

# stuff[1] = 'wow'

# stuff[2] = 'clean'

# print(stuff[1])

# print(stuff[2])

# print(f"whole dict: {stuff}")

# del stuff[1]
# del stuff[2]
# del stuff['city']

# print(f"dict after deleting some elements: {stuff}")

##EX 39##
# create a mapping of state to abbreviation
states = {
    'Punjab': 'PB',
    'Sindh': 'SD',
    'Khyber Pakhtunkhwa': 'KP',
    'Gilgit-Baltistan': 'GB',
    'Balochistan': 'BA'
}

# cerate a basic set of states and some cities in them
cities = {
    'PB': 'Multan',
    'SD': 'Karachi',
    'KP': 'Peshawar'
}

# add some more cities
cities['GB'] = 'Gilgit'
cities['BA'] = 'Quetta'

# print out some cities
print('-' * 10)
print("PB state has: ", cities['PB'])
print("SD state has: ", cities['SD'])

# print some states
print('-' * 10)
print("Sindh's abbreviation is: ", states['Sindh'])
print("Punjab's abbreviation is: ", states['Punjab'])

# do it by using the state then cities dict
print('-' * 10)
print("Balochistan has: ", cities[states['Balochistan']])
print("Gilgit-Baltistan has: ", cities[states['Gilgit-Baltistan']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might be not there
state = states.get('Azad Jammu & Kashmir')
if not state:
    print("Sorry, no Azad Jammu & Kashmir.")

# get a city with a default value
city = cities.get('AJK', 'Does Not Exist')
print(f"The city for the state 'AJK' is: {city}")