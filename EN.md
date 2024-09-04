<h1 align="center">EATHER Fun Bot</h1>

<h2 align="center">This bot is designed to entertain you and your friends in Telegram chats!</h2>

### That's what he can do:

1. **It remembers everything that happens in the chat: phrases, texts, photos, videos, GIFs and stickers (even premium).**
2. **In the course of your dialogue, he has a probability of about 30% to send you one of the things that he remembered.**
3. **If you write the «/send» command or say «втык», it will send you one of the memorized messages with 100% probability.**

**The bot is primarily intended for a Russian-speaking audience, but you can use it in other languages as well.**

**At the moment, the bot combines data from all chats into one list. Therefore, we do not recommend using it for commercial purposes. In the future, we plan to release an update that will allow you to share data across different chats.**

<h2 align="center">Methods and functions:</h2>

```python
@bot.message_handler(commands=['start'])  # "/start" command handler
def start(message):  # The method of the /start command handler

@bot.message_handler(commands=['send'])  # "/send" command handler
def send(message):  # The method of the /send command handler

@bot.message_handler(content_types=['text'])  # Text handler
def handle_text(message):  # Method of processing incoming text messages

@bot.message_handler(content_types=['animation'])  # GIFs handler
def handle_gif(message):  # Method of processing incoming GIFs

@bot.message_handler(content_types=['photo'])  # Photo handler
def handle_photo(message):  # Method of processing incoming photos

@bot.message_handler(content_types=['video'])  # Video handler
def handle_video(message):  # Method of processing incoming videos

@bot.message_handler(content_types=['sticker'])  # Stickers handler
def handle_sticker(message):  # The method of processing incoming stickers

def handle_messages(messages):  # Update processing method (all incoming messages)

def choice_send(message):  # Method for sending a random phrase/text/photo, etc.
```

<h2 align="center">Installation and configuration:</h2>
### First of all, you need to have Python 3-full on your device, as well as Pip for it.

```shell
sudo apt-get upgrade
sudo apt-get update
sudo apt-get -y install python3-full
sudo apt install python3-pip
```

### After installing Python 3-full, you need to install the following libraries for your Python3:
1. **telebot, pyTelegramBotAPI** - the library necessary for the successful operation of the bot in Telegram. Without this library, you will not be able to run the bot without errors.
```shell
pip install telebot
pip install pyTelegramBotAPI
```

2. **PyYAML** - the library required for correct operation ConfigController.py
```shell
pip install PyYAML
```

3. **requests** - required library for pyTelegramBotAPI operation
```shell
pip install requests
```

### After installing all the components, you need to configure the bot using text editors or IDE.
- **First, open the file in your editor main.py , find the variable "TOKEN" and insert the TOKEN of your Telegram bot, which you should have previously created, into its value.**
- **Wherever you see the path to the "config" folder, specify the path to the existing directory where the chat data files will be stored. For example, on line 12 and 13: instead of 'configs', write '/root/config'**
- **After the work is done, save all changes and launch the bot using the following command:**
```shell
python3 main.py
```

### If Python 3 writes you an error when starting that any of the libraries are missing, follow the instructions and install it.

<h2 align='center'>About me</h2>
<i><b>Developer of the bot - LuckyDevv</b></i><br>
<b>Telegram - <a href='https://t.me/luckydevv'>@luckydevv</b></a><br>
<b>VK - <a href='https://vk.com/luckydevv'>@luckydevv</a></b><br>
<b>Discord - <a href='https://discordapp.com/users/972994261979107369'>@luckydevv</a></b>
