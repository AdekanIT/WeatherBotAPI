import telebot
import requests
import json
bot = telebot.TeleBot('6060564387:AAFvzXsK1Wek_95WDDgtSCBWhjxzeAqrbG4')
API = '11636a160dfba4af45ef3aeed64c8ad1'

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hi do u need information about weather? Give me the name of country: ')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Weather now: {temp}')
        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_sticker(message.chat.id, file)
    else:
        bot.reply_to(message, 'This country not exist!')

bot.polling(non_stop=True)


