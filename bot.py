import telebot
import config


from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💪 Тренування")
    item2 = types.KeyboardButton("💤 Сон")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений для того, щоб допомагати перейти до здорового способу життя.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '💤 Сон':
            bot.send_message(message.chat.id, "Вкажіть час коли ви хочте лягати спати, Вам необхідно поспати 8 годин!")
        elif message.text == '💪 Тренування':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Біцепс", callback_data='biceps')
            item2 = types.InlineKeyboardButton("Ноги", callback_data='legs')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Оберіть тип сьогоднішнього тренування.', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю що відповісти 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'biceps':
                bot.send_message(call.message.chat.id, 'Розминка, та 10 віджиманнь')
            elif call.data == 'legs':
                bot.send_message(call.message.chat.id, 'Розминка та 20 присідань')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💪 Тренування",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
