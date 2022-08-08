from telebot import types
import telebot
from req import *

token = '5525191978:AAF4tWz2YZgaLQjlMTpWsm2EP8RiIVOzTW8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    greeting = f'Добро пожаловать {message.from_user.first_name} {message.from_user.last_name}, чтобы зарегестрироваться нажми на кнопку ☑ Регистрация ☑'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reg = types.KeyboardButton("☑ Регистрация ☑")
    connect_with_me = types.KeyboardButton("✉Связаться с cоздателем✉")
    markup.add(reg, connect_with_me)
    bot.send_message(message.chat.id, greeting, reply_markup=markup)


@bot.message_handler(commands=['reg'])
def reg(message):
    n_message = message.text.split(',')
    if len(n_message) == 2 and registration(n_message[0], n_message[1]):
        with open("PASSWORDS", "w") as f:
            f.write(', '.join(n_message))
        bot.send_message(message.chat.id, '✅Регистрация прошла успешно!✅')
    else:
        bot.send_message(message.chat.id, '❌Что то пошло не так❌')


@bot.message_handler()
def checker(message):
    if message.text == "☑ Регистрация ☑":
        bot.send_message(message.chat.id, 'Следущим сообщением пришли свой логин и пароль от дневника.ру\nВ данном формате: login, password')
        bot.register_next_step_handler(message, reg)
    dop_m = types.InlineKeyboardMarkup()
    dop_m.add(types.InlineKeyboardButton("🔴", url= "https://vk.com/szamaxin"))
    if message.text == "✉Связаться с cоздателем✉":
        bot.send_message(message.chat.id, "⬇ Нажими на кнопку ⬇", reply_markup=dop_m)


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
