
friend={
    'first_name':'Zack',
    'last_name':'Z',
    'city':'Miramar Beach',
    'age': 23
}
friend2={
    'first_name':'Christian',
    'last_name':'R',
    'city':'Boston',
    'age':22
}
friend3={
    'first_name':'Tom',
    'last_name':'O',
    'city':'Lynchburg',
    'age':24
}
people=[friend,friend2,friend3]
for person in people:
    full_name=person['first_name']+ " "+ person['last_name']
    print("This is what I know about " + full_name + ".")
    print("They are " + str(person['age']) + " years old and live in " + person['city'])
