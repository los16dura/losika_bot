from datetime import datetime
import telebot
from telebot import apihelper, types

with open('token.txt', 'rt') as file:
    bot = telebot.TeleBot(file.read().strip())

#ход конём
def convert(text):
    ans = ' '.join(text) + '\n'
    ans += '\n'.join(text[1:])
    return ans.upper()


#Брат
def brat(text):
    ans = 'Брат, '+text+', брат'
    return ans


#Картавость
def rrr(text):
    ans = text.replace('р', 'г\'').replace('Р', 'Г\'')
    return ans


@bot.message_handler(commands=['start'])
def send_start(message):
    s_start = "Привет, это бот Лосика @Losik18\n\n"\
              "Он умеет пока немношк, но для всяких додиков ето полезно, так шо пользуйтесь.\n"\
              "(Нажмите /help , чтобы посмотреть список команд)\n\n"\
              "P.S. Скидывайте деньги на еду))"
    bot.send_message(message.chat.id, s_start)

@bot.message_handler(commands=['help'])
def send_help(message):
    s_help = "Чтобы вызвать команду в любом чате,нужно сначала ввести имя бота @botbratbot , затем текст,который вы хотите преобразовать, и в выпадающем меню вы увидите варианты написания\n\n"\
             "Пока он умеет:\n"\
             "Писать текст \"конём\" (см. 2сh)))\n"\
             "Писать \"по-братски\""

    bot.send_message(message.chat.id, s_help)


@bot.message_handler(content_types=['text'])
def eto_gde(message):
    text = message.text.lower()
    if (text.find('это где') != -1) or (text.find('ето где') != -1) or (text.find('ты где') != -1):
        bot.send_message(message.chat.id, 'в общаге?', reply_to_message_id=message.message_id)


@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    try:
        if not inline_query.query:
            return
        ans1 = convert(inline_query.query)
        ans2 = brat(inline_query.query)
        ans3 = rrr(inline_query.query)
        title1 = ans1.split('\n')[0]
        title2 = ans2
        title3 = ans3
        now = str(datetime.now())
        r1 = types.InlineQueryResultArticle('k' + now, title1, types.InputTextMessageContent(ans1))
        r2 = types.InlineQueryResultArticle('b' + now, title2, types.InputTextMessageContent(ans2))
        r3 = types.InlineQueryResultArticle('r' + now, title3, types.InputTextMessageContent(ans3), thumb_url='http://fb.ru/misc/i/gallery/40013/1161626.jpg')
        bot.answer_inline_query(inline_query.id, [r1,r2,r3])
    except Exception as e:
        print(e)


bot.polling(none_stop=True)
