<h1 align="center">EATHER Fun Bot</h1>

<h2 align="center">Этот бот создан, чтобы развлекать вас и ваших друзей в чатах Telegram!</h2>

### Вот что он умеет:

1. **Он запоминает всё, что происходит в чате: фразы, тексты, фотографии, видео, GIF и стикеры (даже премиум).**
2. **В процессе вашего диалога он с вероятностью около 30% отправит вам одно из того, что запомнил.**
3. **Если вы напишите команду «/send» или скажете «втык», он отправит вам одно из запомненных сообщений со 100% вероятностью.**

**Бот в первую очередь предназначен для русскоязычной аудитории, но вы можете использовать его и на других языках.**

**На данный момент бот объединяет данные из всех чатов в один список. Поэтому мы не рекомендуем использовать его в коммерческих целях. В будущем мы планируем выпустить обновление, которое позволит разделять данные по разным чатам.**

<h2 align="center">Методы и функции:</h2>

```python
@bot.message_handler(commands=['start'])  # "/start" command handler
def start(message):  # Метод обработчика команды /start

@bot.message_handler(commands=['send'])  # "/send" command handler
def send(message):  # Метод обработчика команды /send

@bot.message_handler(content_types=['text'])  # Text handler
def handle_text(message):  # Метод обработки входящих текстовых сообщений

@bot.message_handler(content_types=['animation'])  # GIFs handler
def handle_gif(message):  # Метод обработки входящих GIF

@bot.message_handler(content_types=['photo'])  # Photo handler
def handle_photo(message):  # Метод обработки входящих фото

@bot.message_handler(content_types=['video'])  # Video handler
def handle_video(message):  # Метод обработки входящих видео

@bot.message_handler(content_types=['sticker'])  # Stickers handler
def handle_sticker(message):  # Метод обработки входящих стикеров

def handle_messages(messages):  # Метод обработки Update (все входящие сообщения)

def choice_send(message):  # Метод для отправки случайной фразы/текста/фото и т.д.
```

<h2 align="center">Установка и настройка:</h2>

### В первую очередь, вам необходимо иметь Python3-full на своем устройстве, а также Pip для него.
```shell
sudo apt-get upgrade
sudo apt-get update
sudo apt-get -y install python3-full
sudo apt install python3-pip
```

### После установки Python3-full, вам необходимо установить следующие библиотеки для своего Python3:
1. **telebot, pyTelegramBotAPI** - библиотека, необходимая для успешной работы бота в Telegram. Без данной библиотеки, у вас не получится запустить бота без ошибок.
```shell
pip install telebot
pip install pyTelegramBotAPI
```

2. **PyYAML** - библиотека, необходимая для корректной работы ConfigController.py
```shell
pip install PyYAML
```

3. **requests** - обязательная библиотека для работы pyTelegramBotAPI

```shell
pip install requests
```

### После установки всех компонентов, вам необходимо настроить бота с помощью текстовых редакторов или IDE.
- **Для начала, откройте в своём редакторе файл main.py, найдите переменную "TOKEN" и вставьте в её значение TOKEN своего Telegram-бота, которого вы должны были предварительно создать.**
- **Везде, где видите путь к папке "configs", укажите путь к существующему каталогу, в котором будут хранится файлы с данными чата. Например, на строке 12 и 13: вместо 'configs' напишите '/root/configs'**
- **После проделанной работы, сохраняйте все изменения и запускайте бота при помощи следующей команды:**
```shell
python3 main.py
```

### Если при запуске Python3 напишет вам ошибку о том, что отсутствует какая-либо из библиотек, воспользуйтесь инструкцией и установите её.

<h2 align='center'>Обо мне</h2>
<i><b>Разработчик бота - LuckyDevv</b></i><br>
<b>Telegram - <a href='https://t.me/luckydevv'>@luckydevv</a></b><br>
<b>VK - <a href='https://vk.com/luckydevv'>@luckydevv</a></b><br>
<b>Discord - <a href='https://discordapp.com/users/972994261979107369'>@luckydevv</a></b>
