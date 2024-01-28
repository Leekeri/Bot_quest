import telebot
from telebot import types

# Создаем экземпляр бота с помощью токена
bot = telebot.TeleBot('6964707293:AAH1uPDvnLgw-7HVFG39Q4PYpMpgwU89MRE')

# Обработчик команды /start для начала игры
@bot.message_handler(commands=['start'])
def welcome(message):
    # Отправляем приветственное сообщение
    bot.reply_to(message, 'Добро пожаловать в текстовую RPG-игру!')
    bot.reply_to(message, 'Чтобы начать игру, нажмите кнопку "Начать игру"')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик кнопки "Начать игру"
@bot.message_handler(func=lambda message: message.text == 'Начать игру')
def start_game(message):
    # Отправляем описание первой локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы находитесь в деревне. Впереди вас ждут приключения! Выбирайте правильно!\n'
                                      'Иначе для вас...Игра будет закончена. Удачи!')
    bot.send_photo(message.chat.id, open('деревня.png', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action1_button = telebot.types.KeyboardButton('Идти в лес!') #1
    action2_button = telebot.types.KeyboardButton('Выйти в город!') #2
    markup.add(action1_button, action2_button)
    bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Идти в лес!')
def action1(message):
    # Отправляем результат действия 1
    bot.reply_to(message, 'Вы выбрали Идти в лес!')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы вошли в лес. Впереди тропа. Вы услышали сзади шорох.')
    bot.send_photo(message.chat.id, open('лес.png', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action3_button = telebot.types.KeyboardButton('Повернуться...') #3
    action4_button = telebot.types.KeyboardButton('Бежать!') #4
    markup.add(action3_button, action4_button)
    bot.send_message(message.chat.id, 'Что будете делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Выйти в город!')
def action2(message):
    # Отправляем результат действия 2
    bot.reply_to(message, 'Вы выбрали Выйти в город!')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы вошли в город. К вам подошел странный житель.')
    bot.send_photo(message.chat.id, open('город.jpg', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action5_button = telebot.types.KeyboardButton('Поговорить с ним') #5
    action6_button = telebot.types.KeyboardButton('Игнорить и пойти дальше.') #6
    markup.add(action5_button, action6_button)
    bot.send_message(message.chat.id, 'Что собираетесь делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Повернуться...')
def action3(message):
    # Отправляем результат действия 3
    bot.reply_to(message, 'Вы выбрали Повернуться...')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Сзади вас стоит грифон.')
    bot.send_photo(message.chat.id, open('грифон.png', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action7_button = telebot.types.KeyboardButton('Развернуться и пойти дальше.') #7
    action8_button = telebot.types.KeyboardButton('Погладить его.') #8
    markup.add(action7_button, action8_button)
    bot.send_message(message.chat.id, 'Что будете делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Бежать!')
def action4(message):
    # Отправляем результат действия 4
    bot.reply_to(message, 'Вы выбрали Бежать!')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы выбежали к реке. Справа от вас оказался мост.')
    bot.send_photo(message.chat.id, open('река.png', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action9_button = telebot.types.KeyboardButton('Перейти через него') #9
    action10_button = telebot.types.KeyboardButton('Сначала проверить на надежность.') #10
    markup.add(action9_button, action10_button)
    bot.send_message(message.chat.id, 'Что собираетесь делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Поговорить с ним')
def action5(message):
    # Отправляем результат действия 5
    bot.reply_to(message, 'Вы выбрали Поговорить с ним.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Отлично! Он рассказал вам о чудесах этого города!')
    bot.send_photo(message.chat.id, open('чудеса.jpg', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action11_button = telebot.types.KeyboardButton('Поверить и удивиться!')
    action12_button = telebot.types.KeyboardButton('Не поверить и сказать, что это чушь.')
    markup.add(action11_button, action12_button)
    bot.send_message(message.chat.id, 'Что будете делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Игнорить и пойти дальше.')
def action6(message):
    # Отправляем результат действия 6
    bot.reply_to(message, 'Вы выбрали Игнорить и пойти дальше.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы пошли дальше, но житель разозлился и облил вас водой.')
    bot.send_photo(message.chat.id, open('вода.jpeg', 'rb'))

    # Отправляем клавиатуру с вариантами действий
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    action13_button = telebot.types.KeyboardButton('Ответить ему.') #13
    action14_button = telebot.types.KeyboardButton('Проигнорить и уйти.') #14
    markup.add(action13_button, action14_button)
    bot.send_message(message.chat.id, 'Что собираетесь делать?', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Развернуться и пойти дальше.')
def action7(message):
    # Отправляем результат действия 7
    bot.reply_to(message, 'Вы выбрали Развернуться и пойти дальше.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Грифон принял это за оскорбление...')
    bot.send_photo(message.chat.id, open('злой грифон.jpeg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Погладить его.')
def action8(message):
    # Отправляем результат действия 8
    bot.reply_to(message, 'Вы выбрали Погладить его.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Отлично! Он закинул вас на спину, и взлетел! Вокруг только красота и облака!')
    bot.send_photo(message.chat.id, open('облакагрифон.jpeg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы удачно завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Перейти через него')
def action9(message):
    # Отправляем результат действия 9
    bot.reply_to(message, 'Вы выбрали Перейти через него.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы упали в реку!')
    bot.send_photo(message.chat.id, open('рекачел.jpeg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы неудачно завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Сначала проверить на надежность.')
def action10(message):
    # Отправляем результат действия 10
    bot.reply_to(message, 'Вы выбрали Сначала проверить на надежность.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы проверили его. И оказалось, что он сломан! Вы спаслись.')
    bot.send_photo(message.chat.id, open('цветок.jpeg', 'rb'))
    # Завершение игры
    bot.send_message(message.chat.id, 'Вы удачно завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Поверить и удивиться!')
def action11(message):
    # Отправляем результат действия 11
    bot.reply_to(message, 'Вы выбрали Поверить и удивиться!')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вас приняли как родного!')
    bot.send_photo(message.chat.id, open('цветок.jpeg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы удачно завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Не поверить и сказать, что это чушь.')
def action12(message):
    # Отправляем результат действия 12
    bot.reply_to(message, 'Вы выбрали Не поверить и сказать, что это чушь.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вас не приняли, и выгнали из города.')
    bot.send_photo(message.chat.id, open('конец.jpg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы неудачно завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)

# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Ответить ему.')
def action13(message):
    # Отправляем результат действия 13
    bot.reply_to(message, 'Вы выбрали Ответить ему.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вас затащили в переулок и...')
    bot.send_photo(message.chat.id, open('переулок.jpegg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


# Обработчик выбора действия игроком
@bot.message_handler(func=lambda message: message.text == 'Проигнорить и уйти.')
def action14(message):
    # Отправляем результат действия 14
    bot.reply_to(message, 'Вы выбрали Проигнорить и уйти.')

    # Отправляем описание следующей локации и ее иллюстрацию
    bot.send_message(message.chat.id, 'Вы спокойно добрались до дома.')
    bot.send_photo(message.chat.id, open('счконец.jpeg', 'rb'))

    # Завершение игры
    bot.send_message(message.chat.id, 'Вы завершили игру. Спасибо за игру!')

    # Отправляем клавиатуру с кнопкой "Начать игру"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = telebot.types.KeyboardButton('Начать игру')
    markup.add(start_button)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_handler(message: types.Message):
    bot.send_message(message.chat.id, f"Ты прислал сообщение с текстом '{message.text}'\n"
                                      f"Но это не то, что нужно! Пожалуйста, играй по правилам!")


# Запуск бота
bot.polling()