import telebot
import time as t
import datetime
import random

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, я бот, который будет кидать тебе расписание занятий. Ну, конечно, если ты с 231 группы.')
    t.sleep(2)
    bot.send_message(message.chat.id, 'Вот команды, которые я знаю:\n\nПары сегодня:\n/ls\n\nПары завтра:\n/tom\n\nВывод расписания по дням (текущая неделя):\n/mon \n/tue \n/wed \n/thu \n/fri\n\nМожно указать неделю, для вывода по дням\n/mon1 \n/tue2 \nи т.д.\n\nУзнать неделю:\n/week\n\nВремя начала-конца пар:\n/time\n\nКинуть монетку:\n/roll\n\nСправка: \n/help\n\nКупить автору кофе или чего покрепче:\n4402 7110 3617 3613\n5168 7573 8199 8535')
    # bot.send_message(message.chat.id, 'Пары сегодня:')
    # bot.send_message(message.chat.id, '/ls:')
    # bot.send_message(message.chat.id, 'Пары завтра:')
    # bot.send_message(message.chat.id, '/tom:')
    # bot.send_message(message.chat.id, 'Вывод расписания по дням (текущая неделя):')
    # bot.send_message(message.chat.id, "/mon \n/tue \n/wed \n/thu \n/fri")
    # bot.send_message(message.chat.id, 'Можно указать неделю, для вывода по дням:')
    # bot.send_message(message.chat.id, "/mon1 \n/tue2 и т.д.")
    #
    # bot.send_message(message.chat.id, 'Узнать неделю:')
    # bot.send_message(message.chat.id, "/week")
    #
    # bot.send_message(message.chat.id, 'Кинуть монетку:')
    # bot.send_message(message.chat.id, "/roll")


@bot.message_handler(commands=['mon1'])
def mon1(message):
    bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
    bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
    bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')


@bot.message_handler(commands=['mon2'])
def mon2(message):
    bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
    bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
    bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')


@bot.message_handler(commands=['tue1'])
def tue1(message):
    bot.send_message(message.chat.id, '2. Техн. засоби.\n    09:40.\n    Даскал.\n    5.416.')
    bot.send_message(message.chat.id, '3. JAVA.\n    11:20.\n    Горбатюк.\n    5.409.')


@bot.message_handler(commands=['tue2'])
def tue2(message):
    bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.407.\n    Лекция.')
    bot.send_message(message.chat.id, '5. ENGLISH.\n    14:40.\n    Саргатова.\n    8.1110.')


@bot.message_handler(commands=['wed1'])
def wed1(message):
    bot.send_message(message.chat.id, '3. Философия.\n    11:20.\n    Сухова.\n    4.201.\n    Лекция.')
    bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')


@bot.message_handler(commands=['wed2'])
def wed2(message):
    bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.416.')
    bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.318.\n    Лекция.')
    bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')


@bot.message_handler(commands=['thu1'])
def thu1(message):
    bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин\n    5.517.')
    bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.411.')


@bot.message_handler(commands=['thu2'])
def thu2(message):
    bot.send_message(message.chat.id, '3. Микропроц.\n    11:20.\n    Кринецький.\n    5.412а.')
    bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.409.')


@bot.message_handler(commands=['fri1'])
def fri1(message):
    bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Калиниченко\n    5.407.\n    Лекция.')
    bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.216.\n    Лекция.')
    bot.send_message(message.chat.id, '4. Числ. Методи.\n    13:00.\n    Глухов.\n    3.411.')


@bot.message_handler(commands=['fri2'])
def fri2(message):
    bot.send_message(message.chat.id, '1. Числ. Методи.\n    08:00.\n    Глухов.\n    3.120.')
    bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.407.')


@bot.message_handler(commands=['mon'])
def mon(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.\n")
        bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
        bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
        bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.\n")
        bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
        bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
        bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')


@bot.message_handler(commands=['tue'])
def tue(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.\n")
        bot.send_message(message.chat.id, '2. Техн. засоби.\n    09:40.\n    Даскал.\n    5.416.')
        bot.send_message(message.chat.id, '3. JAVA.\n    11:20.\n    Горбатюк.\n    5.409.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.\n")
        bot.send_message(message.chat.id, '2. Техн. засоби.\n    09:40.\n    Даскал.\n    5.416.')
        bot.send_message(message.chat.id, '3. JAVA.\n    11:20.\n    Горбатюк.\n    5.409.')


@bot.message_handler(commands=['wed'])
def wed(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.\n")
        bot.send_message(message.chat.id, '3. Философия.\n    11:20.\n    Сухова.\n    4.201.\n    Лекция.')
        bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.\n")
        bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.416.')
        bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.318.\n    Лекция.')
        bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')


@bot.message_handler(commands=['thu'])
def thu(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.\n")
        bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин\n    5.517.')
        bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.411.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.\n")
        bot.send_message(message.chat.id, '3. Микропроц.\n    11:20.\n    Кринецький.\n    5.412а.')
        bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.409.')


@bot.message_handler(commands=['fri'])
def fri(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.\n")
        bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Калиниченко\n    5.407.\n    Лекция.')
        bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.216.\n    Лекция.')
        bot.send_message(message.chat.id, '4. Числ. Методи.\n    13:00.\n    Глухов.\n    3.411.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.\n")
        bot.send_message(message.chat.id, '1. Числ. Методи.\n    08:00.\n    Глухов.\n    3.120.')
        bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.407.')


@bot.message_handler(commands=['week'])
def week(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.")
    else:
        bot.send_message(message.chat.id, "Вторая неделя.")


@bot.message_handler(commands=['roll'])
def roll(message):
    bot.send_message(message.chat.id, "Бросаю монетку. Решка - идти на пары, орел - сидеть дома.")
    random.seed()
    t.sleep(1)
    if random.random() > 0.5:
        bot.send_message(message.chat.id, "Выпала решка. Иди на пары. (Ну или перебрось:)")
    else:
        bot.send_message(message.chat.id, "Выпал орел. Сиди дома.")


@bot.message_handler(commands=['ls'])
def ls(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    today = datetime.datetime.today().weekday()
    bot.send_message(message.chat.id, "РАСПИСАНИЕ НА СЕГОДНЯ:")
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.")
        if today == 0:
            bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
            bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
            bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')
        if today == 1:
            bot.send_message(message.chat.id, '2. Техн. засоби.\n    09:40.\n    Даскал.\n    5.416.')
            bot.send_message(message.chat.id, '3. JAVA.\n    11:20.\n    Горбатюк.\n    5.409.')
        if today == 2:
            bot.send_message(message.chat.id, '3. Философия.\n    11:20.\n    Сухова.\n    4.201.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')
        if today == 3:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин\n    5.517.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.411.')
        if today == 4:
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Калиниченко\n    5.407.\n    Лекция.')
            bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.216.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Числ. Методи.\n    13:00.\n    Глухов.\n    3.411.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.")
        if today == 0:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
            bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
            bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')
        if today == 1:
            bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.407.\n    Лекция.')
            bot.send_message(message.chat.id, '5. ENGLISH.\n    14:40.\n    Саргатова.\n    8.1110.')
        if today == 2:
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.416.')
            bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.318.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')
        if today == 3:
            bot.send_message(message.chat.id, '3. Микропроц.\n    11:20.\n    Кринецький.\n    5.412а.')
            bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.409.')
        if today == 4:
            bot.send_message(message.chat.id, '1. Числ. Методи.\n    08:00.\n    Глухов.\n    3.120.')
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.407.')
    if today > 4:
        bot.send_message(message.chat.id, 'Сегодня выходной!')
        bot.send_message(message.chat.id, "Расписание на понедельник:")
        if weekNum % 2 == 0:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
            bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
            bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')
        else:
            bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
            bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
            bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')


@bot.message_handler(commands=['tom'])
def ls(message):
    weekNum = datetime.datetime.utcnow().isocalendar()[1]
    today = datetime.datetime.today().weekday()
    today += 1
    bot.send_message(message.chat.id, "РАСПИСАНИЕ НА ЗАВТРА:")
    if weekNum % 2 == 0:
        bot.send_message(message.chat.id, "Первая неделя.")
        if today == 0:
            bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
            bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
            bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')
        if today == 1:
            bot.send_message(message.chat.id, '2. Техн. засоби.\n    09:40.\n    Даскал.\n    5.416.')
            bot.send_message(message.chat.id, '3. JAVA.\n    11:20.\n    Горбатюк.\n    5.409.')
        if today == 2:
            bot.send_message(message.chat.id, '3. Философия.\n    11:20.\n    Сухова.\n    4.201.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')
        if today == 3:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин\n    5.517.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.411.')
        if today == 4:
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Калиниченко\n    5.407.\n    Лекция.')
            bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.216.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Числ. Методи.\n    13:00.\n    Глухов.\n    3.411.')
    else:
        bot.send_message(message.chat.id, "Вторая неделя.")
        if today == 0:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
            bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
            bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')
        if today == 1:
            bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.407.\n    Лекция.')
            bot.send_message(message.chat.id, '5. ENGLISH.\n    14:40.\n    Саргатова.\n    8.1110.')
        if today == 2:
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.416.')
            bot.send_message(message.chat.id, '3. Числ. Методи.\n    11:20.\n    Глухов.\n    3.318.\n    Лекция.')
            bot.send_message(message.chat.id, '4. Микропроц.\n    13:00.\n    Кринецький.\n    5.407.\n    Лекция.')
        if today == 3:
            bot.send_message(message.chat.id, '3. Микропроц.\n    11:20.\n    Кринецький.\n    5.412а.')
            bot.send_message(message.chat.id, '4. JAVA.\n    13:00.\n    Горбатюк.\n    5.409.')
        if today == 4:
            bot.send_message(message.chat.id, '1. Числ. Методи.\n    08:00.\n    Глухов.\n    3.120.')
            bot.send_message(message.chat.id, '2. Техн. Засоби.\n    09:40.\n    Даскал.\n    5.407.')
    if today > 4:
        bot.send_message(message.chat.id, 'Завтра выходной!')
        bot.send_message(message.chat.id, "Расписание на понедельник:")
        if weekNum % 2 == 0:
            bot.send_message(message.chat.id, '3. Метрология.\n    11:20.\n    Бортин.\n    5.517')
            bot.send_message(message.chat.id, '4. Философия.\n    13:00.\n    Сухова.\n    3.102.')
            bot.send_message(message.chat.id, '5. Метрология.\n    14:40.\n    Козлов.\n    5.515.\n    Лекция.')
        else:
            bot.send_message(message.chat.id, '2. Метрология.\n    09:40.\n    Бортин.\n    5.517.')
            bot.send_message(message.chat.id, '3. ENGLISH.\n    11:20.\n    Саргатова.\n    8.1110.')
            bot.send_message(message.chat.id, '4. Метрология.\n    13:00.\n    Козлов.\n    5.515.\n    Лекция.')

@bot.message_handler(commands=['time'])
def ls(message):
    bot.send_message(message.chat.id, '1 пара 08:00 - 09:20\n2 пара 09:40 - 11:00\n3 пара 11:20 - 12:40\n4 пара 13:00 - 14:20\n5 пара 14:40 - 16:00\n6 пара 16:20 - 17:40\n7 пара 18:00 - 19:20\n8 пара 19:40 - 21:00')

bot.polling()
