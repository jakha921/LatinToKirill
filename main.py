from transliterate import to_cyrillic, to_latin, transliterate
import telebot
import config   # get TOKKEN from config.py 

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer = 'Ассалому адейкум, Хуш келибсиз'
    answer += "\nЛотин Кирил(Кирил Лотин) таржима киладиетган ботга"
    answer += 'Таржима учун матн киритинг'
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    translation = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, translation(msg))

bot.infinity_polling()





