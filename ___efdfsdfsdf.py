people = {}
people['Kirill'] = {'city':'Moscow', 'temperature' : 20, 'wind' : 'North'}
people['Andrey'] = {'city':'NY', 'temperature' : 25, 'wind' : 'South'}
people['Maxim'] = {'city':'Kazan', 'temperature' : 15, 'wind' : 'North'}
people['Pavel'] = {'city':'Spb', 'temperature' : -1, 'wind' : 'South'}

#for ppl in people:
#	print(ppl, people.get(ppl))

in_name = input('Name: ')
print(people.get(in_name, 'Nothing'))