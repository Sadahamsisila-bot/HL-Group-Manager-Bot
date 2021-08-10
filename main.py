import telebot


token = '1932163216:AAH-TIut-gjQiyimvd4nQvMB7Qw1sIT5-bw'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Hello','bye')
    bot.send_message(message.chat.id, 'Hello!', reply_markup=keyboard)



bot.message_handler(commands=['bye'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('tset 01')
    bot.send_message(message.chat.id, '/01!', reply_markup=keyboard)
bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Bye')
    bot.send_message(message.chat.id, '/bye!', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Three', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Four', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Five', callback_data=5))
    bot.send_message(message.chat.id, text="How much is 2 plus 2?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello again!')
        keyboard = telebot.types.ReplyKeyboardMarkup(True)

        keyboard.row('Test 01', 'test 02')
        bot.send_message(message.chat.id, 'bla bla bla!', reply_markup=keyboard)
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye!')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Answer accepted!')
    answer = 'You made a mistake'
    if call.data == '4':
        answer = 'You answered correctly!'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()
