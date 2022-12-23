import requests
import telebot


TOKEN = '5945717332:AAE1y7AEs_w-L6wzoP3AiErL1ZOO0STEIi4'



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'type to a number to get somthing trivial about it')

@bot.message_handler(content_types=['text'])
def start(message):
    number = message.text
    try:
        number = int(number)
        response = requests.get(f"http://numbersapi.com/{number}")
        bot.send_message(message.chat.id,response.text)
    except:
        bot.send_message(message.chat.id,'please enter a number')

   

    
print("bot running!")


bot.polling(non_stop = True)
