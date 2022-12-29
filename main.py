import telebot
from telebot import types
import pytube
from pytube import YouTube

bot = telebot.TeleBot('5900812537:AAG1NTV7NRtJQkASvdVorjLyfE_54JfUbRM')


@bot.message_handler(commands = ['start'])
def start(message):
    user_info = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, f'{user_info}, это бот который поможет тебе скачать видео из Youtube', parse_mode = 'html')
    bot.send_message(message.chat.id, f'Для того чтобы скачивание началось просто отпрпавь мне URL ссылку видео из YouTube ', parse_mode='html')


@bot.message_handler(commands = ['commands'])
def commands(message):
    user_info = f'{message.from_user.first_name} если ты забыл комманды то вот их список'
    bot.send_message(message.chat.id, user_info, parse_mode='html')
    bot.send_message(message.chat.id, f'Команда /start вернет тебя на первоначальное меню' ,  parse_mode = 'html')
    bot.send_message(message.chat.id, f'Команда /help также отправит тебе список команд' , parse_mode='html')
    bot.send_message(message.chat.id, f'Команда /commands , поможет тебе найти список команд ', parse_mode='html')


@bot.message_handler(commands = ['help'])
def help(message):
    user_info = f'{message.from_user.first_name} если ты забыл как все работает то вот их список а также тебе просто нужно отправить ссылку программа сама ее поймет'
    bot.send_message(message.chat.id, user_info, parse_mode='html')
    bot.send_message(message.chat.id, f'Команда /start вернет тебя на первоначальное меню' ,  parse_mode = 'html')
    bot.send_message(message.chat.id, f'Команда /help также отправит тебе список команд' , parse_mode='html')
    bot.send_message(message.chat.id, f'Команда /commands , поможет тебе найти список команд ', parse_mode='html')



@bot.message_handler()
def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    user_commands = types.KeyboardButton("/commands")
    start = types.KeyboardButton("/begin")
    markup.add(user_commands, start)
    if message.text == 'help':
        bot.send_message(message.chat.id, "Специальные комманды", reply_markup=markup)
    elif "download" in message.text:
        youtubeObject = YouTube(message.text[8:])
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            bot.send_message(message.chat.id, "Downloading begin", parse_mode='html')
            youtubeObject.download()
            bot.send_message(message.chat.id, "<b>Downloaded</b>", parse_mode='html')
            size = youtubeObject.filesize_mb
            title = youtubeObject.title
            filename = youtubeObject.default_filename
            bot.send_message(message.chat.id, f"Size of this file in mb {size}")
            bot.send_message(message.chat.id, f"Title of this video {title}")
            bot.send_message(message.chat.id, filename)
            video = open( filename , 'rb')
            bot.send_video(message.chat.id, video)

        except:
            bot.send_message(message.chat.id, "Something goes wrong", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, отправь комманду /help", parse_mode='html')


bot.polling(none_stop = True)



#download(link)