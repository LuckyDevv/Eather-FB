import os
import random

import telebot
import ConfigController

TOKEN = ''  # Введите сюда токен своего Telegram-бота
bot = telebot.TeleBot(TOKEN)

last_choice = ''

if not os.path.exists('configs'):
    os.mkdir('configs')
gifsConfig = ConfigController.ConfigController('configs/gifs.json', ConfigController.ConfigType.JSON)
videosConfig = ConfigController.ConfigController('configs/videos.json', ConfigController.ConfigType.JSON)
imagesConfig = ConfigController.ConfigController('configs/images.json', ConfigController.ConfigType.JSON)
phrasesConfig = ConfigController.ConfigController('configs/phrases.json', ConfigController.ConfigType.JSON)
stickersConfig = ConfigController.ConfigController('configs/stickers.json', ConfigController.ConfigType.JSON)


@bot.message_handler(commands=['start'])  # "/start" command handler
def start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, open('info.txt', 'r', encoding='utf-8').read(), disable_web_page_preview=True)


@bot.message_handler(commands=['send'])  # "/send" command handler
def send(message):
    if message.chat.type != 'private':
        choice_send(message)


@bot.message_handler(content_types=['text'])  # Text handler
def handle_text(message):
    if message.chat.type != 'private':
        text = str(message.text).strip()
        if text.split(' ')[0].lower() == 'втык,':
            choice_send(message)
        else:
            if not phrasesConfig.exists(text):
                phrasesConfig.set(text)
                phrasesConfig.save()


@bot.message_handler(content_types=['animation'])  # GIFs handler
def handle_gif(message):
    if message.chat.type != 'private':
        gif_id = message.animation.file_id
        if not gifsConfig.exists(gif_id):
            gifsConfig.set(gif_id)
            gifsConfig.save()


@bot.message_handler(content_types=['photo'])  # Photo handler
def handle_photo(message):
    if message.chat.type != 'private':
        image_id = message.photo[-1].file_id
        if not imagesConfig.exists(image_id):
            imagesConfig.set(image_id)
            imagesConfig.save()


@bot.message_handler(content_types=['video'])  # Video handler
def handle_video(message):
    if message.chat.type != 'private':
        video_id = message.video.file_id
        if not videosConfig.exists(video_id):
            videosConfig.set(video_id)
            videosConfig.save()


@bot.message_handler(content_types=['sticker'])  # Stickers handler
def handle_sticker(message):
    if message.chat.type != 'private':
        sticker_id = message.sticker.file_id
        if not stickersConfig.exists(sticker_id):
            stickersConfig.set(sticker_id)
            stickersConfig.save()


def handle_messages(messages):
    for message in messages:
        if message.chat.type != 'private':
            text = str(message.text).strip()
            if text == '/start' or text == '/send' or text == '/send@eather_fun_bot' or text.split(' ')[0].lower().strip() == 'втык,':
                return
            chance = random.randint(1, 100)
            if 20 <= chance <= 50:
                choice_send(message)
        else:
            bot.send_message(message.chat.id, 'Бот не функционирует в личных сообщениях!')


def choice_send(message):
    global last_choice
    what_send = []
    phrases_all = phrasesConfig.get_all(True)
    stickers_all = stickersConfig.get_all(True)
    images_all = imagesConfig.get_all(True)
    videos_all = videosConfig.get_all(True)
    gifs_all = gifsConfig.get_all(True)
    if len(phrases_all) > 0:
        what_send.append('phrase')
    if len(stickers_all) > 0:
        what_send.append('sticker')
    if len(images_all) > 0:
        what_send.append('image')
    if len(videos_all) > 0:
        what_send.append('video')
    if len(gifs_all) > 0:
        what_send.append('gif')

    if len(what_send) > 0:
        choice = random.choice(what_send)
    else:
        return
    while choice == last_choice:
        choice = random.choice(what_send)
    last_choice = choice
    if choice == 'phrase':
        phrase = random.choice(phrases_all)
        bot.reply_to(message, phrase)
    elif choice == 'sticker':
        sticker = random.choice(stickers_all)
        bot.send_sticker(message.chat.id, sticker)
    elif choice == 'image':
        image = random.choice(images_all)
        bot.send_photo(message.chat.id, image)
    elif choice == 'video':
        video = random.choice(videos_all)
        bot.send_video(message.chat.id, video)
    elif choice == 'gif':
        gif = random.choice(gifs_all)
        bot.send_animation(message.chat.id, gif)


bot.set_update_listener(handle_messages)
bot.polling(none_stop=True)
