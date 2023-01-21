EN:



Telegram Bot:

This is a Telegram bot written in Python that sends all messages that users write to the bot's administrator with information about when it was sent, who sent it, the sender's ID, and the text of the message. The bot only sends messages when the /idea command is entered and has an initial command /start when entered, it displays buttons (in this case, one button).

Getting Started:

These instructions will help you to set up and run the bot on your local machine.

Prerequisites:

Python 3.x;

Telegram bot token;

pip.

Installing:

Clone the repository to your local machine

'git clone https://github.com/BlazeDevelop/Telegram-Bot';

Create a virtual environment and activate it:

python -m venv venv;
source venv/bin/activate

Install the requirements:

pip install -r requirements.txt

Add your Telegram bot token to bot_token.py

TOKEN = 'YOUR_BOT_TOKEN'

Add your admin ID to config.py:

ADMIN_ID = 'YOUR_ADMIN_ID'

Run the bot:

python main.py

Built With:

Aiogram - A Python wrapper for the Telegram Bot API

Author:

Vladimir - Initial work - https://github.com/BlazeDevelop

License:

This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments:

Thanks to my friend for solving the problems that arose when creating the bot.

RU:



Telegram Бот:

Это Telegram бот, написанный на Python, который отправляет все сообщения, которые пишут пользователи администратору бота с информацией о том, когда оно было отправлено, кем было отправлено, айди отправителя и текст сообщения. Бот отправляет сообщения только при вводе команды /idea и имеет начальную команду /start, при вводе которой отображаются кнопки (в данном случае, одна кнопка).

Начало работы:

Эти инструкции помогут вам настроить и запустить бота на вашей локальной машине.

Требования:

Python 3.x
Токен Telegram бота
pip

Установка:

Клонируйте репозиторий на вашу локальную машину:

'git clone https://github.com/BlazeDevelop/Telegram-Bot'

Создайте виртуальное окружение и активируйте его:

python -m venv venv
source venv/bin/activate

Установите библиотеки:

pip install -r requirements.txt

Добавьте токен Telegram бота в bot_token.py:

TOKEN = 'YOUR_BOT_TOKEN'

Добавьте ID администратора в config.py:

ADMIN_ID = 'YOUR_ADMIN_ID'

Запустите бота:

python main.py

Использованные библиотеки:

Aiogram - обертка для Telegram Bot API на Python

Автор:

Владимир - Начальная работа - https://github.com/BlazeDevelop

Лицензия:

Этот проект лицензирован под лицензией MIT - см. файл LICENSE.md для подробной информации.

Благодарности:

Спасибо моему другу за решение проблем которые возникали при создании бота
