import telebot
from Config_ValuesMoneyBot import keys_ValuesMoneyBot,ValuesMoneyBot
from extensions import APIException,CryptoConverter

bot = telebot.TeleBot(ValuesMoneyBot)




@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}\n Для вызова помощи воспользуйтесь командой /help")


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Чтобы начать работу введите команду боту в следующем формате:\n<Имя валюты>\n\
<В какую валюту перевести>\n\
<количество вводимой валюты>\n\
\n\
Для просмотра всех доступных валют, воспользуйтесь командой /values")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys_ValuesMoneyBot.keys():
        text = '\n►'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values= message.text.split(' ')
        if len(values)!=3:
            raise APIException('Для ввода доступно только 3 параметра')
        quote, base, amount =values
        total_base= CryptoConverter.get_price(quote,base,amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя {e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:

        text = f'Цена {amount} {keys_ValuesMoneyBot[quote]} в {keys_ValuesMoneyBot[base]} - {total_base} {keys_ValuesMoneyBot[base]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
