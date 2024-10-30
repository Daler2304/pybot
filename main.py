import telebot
from telebot import types
from config import *
import test
from apscheduler.schedulers.background import BackgroundScheduler

bot = telebot.TeleBot(TOKEN)

groups = {}


def send_daily_message():
    for i in groups:
        text = test.mark_down_v2(test.get_today_fan())
        bot.send_message(i, text, parse_mode='MarkdownV2')


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private' and message.from_user.id != ADMIN_ID:
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton('Добавить бота в группу', url='https://t.me/hspm_1_tiv_2_bot?startgroup=new')
        )
        bot.send_message(
            message.chat.id,
            "Этот бот может использоваться только в группах. Вы можете добавить меня, нажав на кнопку ниже:",
            reply_markup=markup
        )
    elif message.chat.type in ('group', 'supergroup'):
        groups[message.chat.id] = (message.chat.title, message.chat.username, message.chat.id)
        bot.delete_message(message.chat.id, message.message_id)
        text = test.mark_down_v2(test.get_today_fan())
        bot.send_message(message.from_user.id, text, parse_mode='MarkdownV2')


@bot.message_handler(commands=['stats'])
def stats(message):
    if message.from_user.id == ADMIN_ID:
        if len(groups) != 0:
            text = ''
            for i in groups:
                text += str(groups[i]) + '\n'
            bot.send_message(message.chat.id, text)
    else:
        bot.delete_message(message.chat.id, message.message_id)


scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_message, 'cron', hour=8, minute=0)
scheduler.start()


while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print(e)
