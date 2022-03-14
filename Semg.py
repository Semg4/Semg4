import telebot
from telebot import types
import requests
import bs4

bot = telebot.TeleBot('5173440304:AAGOO6PhsDxOdKwCfpeOgHwPquwRd90jc3w')


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, text="Привет,	{0.first name}! Я тестовый бот для курса программирования на языке Пайтон".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text


if ms_text == "Главное меню" or ms_text == "Вернуться в главное меню":
    markup = types.ReplyReyboardMarkup(resize_keyboard=True)
    btn1 = types.ReyboardButton("Развлечения")
    back = types.KeybcardButton("Помощь")
    markup.add(btn1, back)
    bot.send_message(chat_id, text="Bы в главном меню", reply_markup=markup)
elif ms_text == "Развлечения":
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Прислать собаку")
    btn2 = types.KeyboardButton("Прислать анекдот")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, back)
    bot.send_message(chat_id, text="Paзвлeчeния", reply_markup=markup)
elif ms_text == "/dog" or ms_text == "Прислать собаку":
    contents = requests.get('https://random.dog/woof.json').soup()
    urlDOG = contents['url']
    bot.send_photo(chat_id, photo = urlDC3, caption = "Ваша собака:")
elif ms_text == "/joke" or ms_text == "Прислать анекдот":  #
    bot.send_message(chat_id, text=get_anekdot())


def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array anekdots[0]


bot.polling(none_stop=True, interval=0)
print()
