from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import random 
import ephem

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


def talk_to_me(bot, update):
    user_text = update.message.text 
    
    logging.info("Message by " + update.message.from_user.first_name + ' ' + update.message.from_user.last_name + "; Message: " + user_text)
    update.message.reply_text(user_text)

def handle_planet(bot, update):
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


def greet_user(bot, update):
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

def main():

    updater = Updater("465468320:AAHN4RR6C4cQVtsJi2trc1aL3WBfr4Ykgdw")
    init_map_constellations()

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", handle_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

main()