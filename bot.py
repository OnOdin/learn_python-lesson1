from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import random 

random_phases = ["Теперь, когда я знаю, что мир зависит от таких легкомысленных людей, как мы, я думаю, у меня есть повод для беспокойства.", "Вся его дальнейшая жизнь была словно попыткой доказать всему миру превосходство интеллекта над телом.","Отклонившись так сильно от темы, я не могу удержаться от того, чтобы не пойти еще чуть дальше."]


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def talk_to_me(bot, update):
    user_text = update.message.text 
    #print(user_text)

    logging.info("Message" + update.message.from_user.first_name + ' ' + update.message.from_user.last_name + user_text)
    update.message.reply_text(user_text)


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

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

main()