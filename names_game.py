NAMES = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
ANSWERS = {'привет':'уходи', 'здравствуйте':'Добрый день! Чем могу помочь?', 'йо': 'йо', 'yo':'yo!', 'хорошо':'серьезно?', 'отлично':'я рад за тебя'}


def find_person(user_name):
    index = 0
    max_index = len(NAMES)
    is_found = False 

    while index < max_index:
        if user_name == NAMES[index]:
            print(user_name, " нашелся!")
            is_found = True 
            break
        index = index + 1 

    if is_found == False:
        print(user_name + " отсутствует")

#input_name = input('Найти имя: ' )
#find_person(input_name)

def ask_user():
    while True:
        input_string = input("Как дела? ").lower()

        if input_string == 'пока':
            print('Давай, удачи!')
            break
        elif input_string in ANSWERS:
            print(ANSWERS.get(input_string))
        else:
            print('Попробуй еще раз!') 


ask_user()