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
    global name 
    name = message.from_user.first_name

    if message.chat.type == 'private':
        if message.text == '📒 Блокнот':
            with open("parameters.json", "r") as read_f:
                try:
                    data = json.load(read_f)
                except Exception as e:
                    data = []
            read_f.close()
            exists=False
            if len(data)!=0:
                for user in data:
                    if user['Name'] == name:
                        exists=True
            if not exists:

                bot.send_message(message.chat.id, "Заповніть наступні дані:")

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Чоловік", callback_data='sex1')
                item2 = types.InlineKeyboardButton("Жінка", callback_data='sex2') 
                markup.add(item1, item2)
     
                bot.send_message(message.chat.id, 'Оберіть стать.', reply_markup=markup) 

                markup1 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("14-16", callback_data='age1')
                item2 = types.InlineKeyboardButton("16-18", callback_data='age2') 
                item3 = types.InlineKeyboardButton("18-24", callback_data='age3') 
                item4 = types.InlineKeyboardButton("24-30", callback_data='age4') 
                markup1.add(item1, item2, item3, item4)
     
                bot.send_message(message.chat.id, 'Вкажіть Ваш вік', reply_markup=markup1) 

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
