from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from learnpython_environment import get_bot_key
import logging
import json
import random 
import ephem
import re
import operator
import time 

random_phases = ["Теперь, когда я знаю, что мир зависит от таких легкомысленных людей, как мы, я думаю, у меня есть повод для беспокойства.", "Вся его дальнейшая жизнь была словно попыткой доказать всему миру превосходство интеллекта над телом.","Отклонившись так сильно от темы, я не могу удержаться от того, чтобы не пойти еще чуть дальше."]
dic_constellations = {}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def init_map_constellations():

    for star in ephem._libastro.builtin_planets():
        try:
            body = getattr(ephem,star[2])()
            body.compute()
            dic_constellations[star[2].lower()] = ephem.constellation(body)
        except Exception as error:
            #print(error)
            pass

def parse_calculation_string(_string):
    operators = set('+-*/')
    op_out = []    #This holds the operators that are found in the string (left to right)
    num_out = []   #this holds the non-operators that are found in the string (left to right)
    buff = []
    for character_index in _string:  #examine 1 character at a time
        if character_index in operators:  
            #found an operator.  Everything we've accumulated in `buff` is 
            #a single "number". Join it together and put it in `num_out`.
            num_out.append(''.join(buff))
            buff = []
            op_out.append(character_index)
        else:
            #not an operator.  Just accumulate this character in buff.
            buff.append(character_index)
    num_out.append(''.join(buff))
    return num_out, op_out

def execute_calculations(_numbers,_operations):

    nums = list(_numbers)
    ops = list(_operations)

    operator_order = ('*/','+-')  #precedence from left to right.  operators at same index have same precendece.
                                  #map operators to functions.
    op_dict = {'*':operator.mul,
               '/':operator.truediv,
               '+':operator.add,
               '-':operator.sub}
    
    value = None
    for op in operator_order:                   #Loop over precedence levels
        while any(o in ops for o in op):        #Operator with this precedence level exists

            idx,oo = next((i,o) for i,o in enumerate(ops) if o in op) #Next operator with this precedence  

            ops.pop(idx)                        #remove this operator from the operator list

            values = map(float,nums[idx:idx+2]) #here I just assume float for everything

            value = op_dict[oo](*values)

            nums[idx:idx+2] = [value]          #clear out those indices

    return nums[0]

def get_result_of_calculation(main_calculation_pattern, _update):
    try:
        # https://stackoverflow.com/questions/13055884/parsing-math-expression-in-python-and-solving-to-find-an-answer?rq=1
        numbers_, operations_ = parse_calculation_string(main_calculation_pattern.replace('=',''))
        _result = execute_calculations(numbers_, operations_)
        return _result
    except Exception as error:
        print(error)

def translate_string_to_calculation_patter(_string, _update):
    dic_meaning = {}

    dic_meaning['ноль'] = '0'
    dic_meaning['один'] = '1'
    dic_meaning['два'] = '2'
    dic_meaning['три'] = '3'
    dic_meaning['четыре'] = '4'
    dic_meaning['пять'] = '5'
    dic_meaning['шесть'] = '6'
    dic_meaning['семь'] = '7'
    dic_meaning['восемь'] = '8'
    dic_meaning['девять'] = '9'

    dic_meaning['плюс'] = '+'
    dic_meaning['минус'] = '-'
    dic_meaning['разделить'] = '/'
    dic_meaning['умножить'] = '*'

    _string = _string.lower().replace("сколько будет ",'').replace("на ",'')
    result_string = ''

    for word in _string.split(' '):
        result_string = result_string + dic_meaning.get(word, '')

    return result_string

def chat_handler(bot, update):

    user_text = (update.message.text).lower()

    if re.search("сколько будет", user_text):
        
        calc_pattern = translate_string_to_calculation_patter(user_text, update) 
        _result = get_result_of_calculation(calc_pattern, update)
        update.message.reply_text("Answer: " + str(_result))

    elif re.search("\d+[\.\d+]?([+-/*](\d+[\.\d+]?))+=", user_text):
        
        _result = get_result_of_calculation(update.message.text, update)
        update.message.reply_text("Answer: " + str(_result))

    else:    
        update.message.reply_text(user_text)

#logging.info("Message by " + update.message.from_user.first_name + ' ' + update.message.from_user.last_name + "; Message: " + user_text)

def planet_handler(bot, update):
    try:

        user_text_words = (update.message.text).lower().split(' ')

        if len(user_text_words) == 2:

            constellation = dic_constellations.get(user_text_words[1], "Nothing")
            if constellation == "Nothing":
                update.message.reply_text("Nothing to say about your planet. Try again")
            else:    
                update.message.reply_text("Your planet is " +  user_text_words[1] + " in " + str(constellation) + " constellation!" )

        elif len(user_text_words) == 1:
            update.message.reply_text("Please, specify the name of the planet through a space. \n Example: '/planet Mars'")

    except Exception as error:
        print(error)

def word_cound_handler(bot, update):
    try:
        user_text_words = re.findall('[0-9a-zA-Zа-яА-Я]+', (update.message.text).replace('/wordcount',''))

        if len(user_text_words) == 0:
            update.message.reply_text("Something went wrong. Try add some words")
        elif len(user_text_words) == 1:
            update.message.reply_text( str(len(user_text_words)) +  " word")
        else:
            update.message.reply_text( str(len(user_text_words)) +  " words")

    except Exception as error:
        print(error)

def greet_user_handler(bot, update):
    try:
        #print('Вызван /start')
        #print("------------------------------------------------------------------------------------------------")
        #print("Info about User: ", update.message.from_user.first_name + ' ' + update.message.from_user.last_name)
        #print("------------------------------------------------------------------------------------------------")
        #print("Info about update: ", update)
        #print("------------------------------------------------------------------------------------------------")
    
        random_index = int(random.randint(0,len(random_phases)-1))
        update.message.reply_text("Сообщение отправил: " + update.message.from_user.first_name + ' ' + update.message.from_user.last_name)
        update.message.reply_text("Фраза дня: " + random_phases[random_index])

        #print(random_phases[random_index])
        #print("========================================================================================================")
    except Exception as error:
        print(error)

def next_full_moon_question_handler(bot, update):
    try:
        user_text_words = re.findall('[\d]{4}/[\d]{2}/[\d]{2}', (update.message.text).replace('/fullmoon ',''))

        if len(user_text_words) == 1:
            update.message.reply_text("Ближайшее полнолуние - " + str(ephem.next_full_moon(user_text_words[0])))    
        else:
            update.message.reply_text("Something went wrong. Try add only one date.") 

    except Exception as error:
        print(error)
    

def main():

    updater = Updater(get_bot_key())
    init_map_constellations()

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user_handler))
    dp.add_handler(CommandHandler("planet", planet_handler))
    dp.add_handler(CommandHandler("wordcount", word_cound_handler))
    dp.add_handler(CommandHandler("fullmoon", next_full_moon_question_handler))
    dp.add_handler(MessageHandler(Filters.text, chat_handler))

    print('- GO -')

    updater.start_polling()
    updater.idle()


main()