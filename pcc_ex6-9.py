#From Python Crash Course, this is Chapter 6, exercise 9
favorite_places={
    'Todoharu': ['Tokyo','Nara', 'Chicago'],
    'Nago':['Milan','Chicago','Lynchburg'],
    'Yasunori': ['San Francisco','Tokyo','Kyoto']
}
for person,places in favorite_places.items():
    print(person+ "'s favorite places are:")
    for place in places:
        print("\t" + place)
