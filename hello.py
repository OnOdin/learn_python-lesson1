name = 'Kirill'
print(name)

user_info = {'first_name':'Kirill', 'last_name':'Stepanov'}
print(user_info.get('first_name'))


first_name = input('Input your first name: ')
user_info['first_name'] = first_name

last_name = input('Input your last name: ')
user_info['last_name'] = first_name

print(user_info)
