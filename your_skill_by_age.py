print('kirill'.upper())

user_age = float(input('Введите возраст: '))

if user_age < 6:
    print('Kindergarten')    
elif user_age < 18:
    print('School')
elif user_age < 23:
    print('University')
else:
    print('Sorry mate, you have to work!')