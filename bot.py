import schedule
import telebot
import config
import foodlist as fl
import json
from time import sleep
from telebot import types
from threading import Thread
from user import User

name = "User"
sex = "pass"
age = 1
weight = 1
growth = 1
goals = "pass"
time01 = "pass"
id_chat = 1

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📒 Блокнот")
    item2 = types.KeyboardButton("🏆 Тренування")
    item3 = types.KeyboardButton("🍏 Харчування")
    item4 = types.KeyboardButton("💤 Сон")
 
    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений для того, щоб допомагати перейти до здорового способу життя.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    
    #check if user exists
    try:
        with open("userList.json", "r") as read_file:
            try:
                data = json.load(read_file)
            except Exception as e:
                data=[]
        read_file.close()
        exists=False
        if len(data)!=0:
            for user in data:
                if user['id']==message.chat.id:
                    exists=True
        if not exists:
            d = {"id":message.chat.id,"index":{"fmbt":0,"fmlh":0,"fmdr":0,"fwbt":0,"fwlh":0,"fwdr":0,"muscle":0,"waste":0},"menu":"MAIN"}
            data.append(d)
            with open("userList.json", "w") as write_file:
                json.dump(data, write_file)
            write_file.close()

    except Exception as e:
        print(repr(e))
    changeMenu("MAIN",message.chat.id)

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

                markup2 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("до 160 см", callback_data='gr1')
                item2 = types.InlineKeyboardButton("до 170 см", callback_data='gr2')
                item3 = types.InlineKeyboardButton("до 180 см", callback_data='gr3')
                item4 = types.InlineKeyboardButton("до 190 см", callback_data='gr4')
     
                markup2.add(item1, item2, item3, item4)
     
                bot.send_message(message.chat.id, 'Вкажіть вас зріст.', reply_markup=markup2) 

                markup3 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("до 45 кг", callback_data='w1')
                item2 = types.InlineKeyboardButton("до 55 кг", callback_data='w2')
                item3 = types.InlineKeyboardButton("до 65 кг", callback_data='w3')
                item4 = types.InlineKeyboardButton("до 80 кг", callback_data='w4')
     
                markup3.add(item1, item2, item3, item4)
     
                bot.send_message(message.chat.id, 'Вкажіть вашу вагу.', reply_markup=markup3) 

                markup4 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Схуднути", callback_data='g1')
                item2 = types.InlineKeyboardButton("Набрати вагу", callback_data='g2')
     
                markup4.add(item1, item2)
     
                bot.send_message(message.chat.id, 'Оберіть ціль для тренувань.', reply_markup=markup4)

            else:
                u1 = User(name, "None", weight, age, growth, goals)
                bot.send_message(message.chat.id, 'Ваші дані.')
                bot.send_message(message.chat.id, str(u1))
    
        elif message.text == '🍏 Харчування':
            changeMenu("FOOD",message.chat.id)
            bot.send_message(message.chat.id, 'Добре, я допоможу тобі з планом харчування.')
            sleep(1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🏃 Для схуднення") 
            item2 = types.KeyboardButton("🏋️ Для набору маси")
            back = types.KeyboardButton("◀️ Назад")
            markup.add(item1, item2, back)
     
            bot.send_message(message.chat.id, 'Обери, для чого саме меню тобі спланувати?', reply_markup=markup) 
        elif message.text == '🏃 Для схуднення':
            changeMenu("FOOD_WASTE",message.chat.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🥚Сніданок") 
            item2 = types.KeyboardButton("🍲Обід")
            item3 = types.KeyboardButton("🍗Вечеря")
            back = types.KeyboardButton("◀️ Назад")
            markup.add(item1, item2, item3, back)
     
            bot.send_message(message.chat.id, 'Обери бажане меню', reply_markup=markup) 
        elif message.text == '🏋️ Для набору маси':
            changeMenu("FOOD_MASS",message.chat.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🥚Сніданок") 
            item2 = types.KeyboardButton("🍲Обід")
            item3 = types.KeyboardButton("🍗Вечеря")
            back = types.KeyboardButton("◀️ Назад")
            markup.add(item1, item2, item3, back)
     
            bot.send_message(message.chat.id, 'Обери бажане меню', reply_markup=markup) 
        elif message.text == '🥚Сніданок':
            markup = types.InlineKeyboardMarkup(row_width=2)
            if currentMenu(message.chat.id)=="FOOD_WASTE": 
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwbt_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwbt_next')  
                img = open("images/breakfest.jpg", 'rb')
                caption = "Сніданок"
                text = fl.getText("fwbt",0)
            elif currentMenu(message.chat.id)=="FOOD_MASS":   
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmbt_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmbt_next')
                img = open("images/breakfest.jpg", 'rb')
                caption = "Сніданок"
                text = fl.getText("fmbt",0)
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, img, caption=caption)
            bot.send_message(message.chat.id, text, reply_markup=markup) 
        elif message.text == '🍲Обід':
            markup = types.InlineKeyboardMarkup(row_width=2)
            if currentMenu(message.chat.id)=="FOOD_WASTE":   
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwlh_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwlh_next')
                img = open("images/lunch.jpg", 'rb')
                caption = "Обід"
                text = fl.getText("fwlh",0)
            elif currentMenu(message.chat.id)=="FOOD_MASS":  
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmlh_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmlh_next') 
                img = open("images/lunch.jpg", 'rb')
                caption = "Обід"
                text = fl.getText("fmlh",0)
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, img, caption=caption)
            bot.send_message(message.chat.id, text, reply_markup=markup) 
        elif message.text == '🍗Вечеря':
            markup = types.InlineKeyboardMarkup(row_width=2)
            if currentMenu(message.chat.id)=="FOOD_WASTE": 
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwdr_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwdr_next')  
                img = open("images/dinner.jpg", 'rb')
                caption = "Вечеря"
                text = fl.getText("fwdr",0)
            elif currentMenu(message.chat.id)=="FOOD_MASS":  
                item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmdr_back')
                item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmdr_next')   
                img = open("images/dinner.jpg", 'rb')
                caption = "Вечеря"
                text = fl.getText("fmdr",0)
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, img, caption=caption)
            bot.send_message(message.chat.id, text, reply_markup=markup) 
        elif message.text == "◀️ Назад":
            current = currentMenu(message.chat.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            if current == "FOOD" or current == "TRAINING":
                changeMenu("MAIN",message.chat.id)
                item1 = types.KeyboardButton("📒 Блокнот")
                item2 = types.KeyboardButton("🏆 Тренування")
                item3 = types.KeyboardButton("🍏 Харчування")
                item4 = types.KeyboardButton("💤 Сон")
                markup.add(item1, item2, item3, item4)
            elif current == "FOOD_WASTE" or current == "FOOD_MASS":
                changeMenu("FOOD",message.chat.id)
                item1 = types.KeyboardButton("🏃 Для схуднення") 
                item2 = types.KeyboardButton("🏋️ Для набору маси")
                back = types.KeyboardButton("◀️ Назад")
                markup.add(item1, item2, back)
            bot.send_message(message.chat.id, "Повертаємось назад", reply_markup=markup)
        elif message.text == '💤 Сон':
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("4:00 - 6:00", callback_data='time1')
            item2 = types.InlineKeyboardButton("6:00 - 8:00", callback_data='time2')
            item3 = types.InlineKeyboardButton("8:00 - 10:00", callback_data='time3')
            item4 = types.InlineKeyboardButton("Вимкнути ранкові повідомлення", callback_data='time4')
  
            markup.add(item1, item2, item3, item4)
 
            bot.send_message(message.chat.id, 'Вкажіть час коли вам треба прокинутись.', reply_markup=markup)            
        elif message.text == '🏆 Тренування':
            changeMenu("TRAINING",message.chat.id)
            bot.send_message(message.chat.id, 'Добре, я допоможу тобі з режимом тренувань.')
            sleep(1)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("💪 Набрати м'язову масу") 
            item2 = types.KeyboardButton("🏃 Схуднути")
            item3 = types.KeyboardButton("📋 Тренувальні схеми")
            back = types.KeyboardButton("◀️ Назад")
            markup.add(item1, item2, item3, back)
     
            bot.send_message(message.chat.id, 'Обери, що саме ти бажаєш отримати?', reply_markup=markup) 
        elif message.text == "💪 Набрати м'язову масу":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='muscle_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='muscle_next')  
            img = open("images/muscle.jpg", 'rb')
            caption = "Вправи для набрання маси"
            text = fl.getText("muscle",0)
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, img, caption=caption)
            bot.send_message(message.chat.id, text, reply_markup=markup) 
        elif message.text == "🏃 Схуднути":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='waste_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='waste_next')  
            img = open("images/waste.jpg", 'rb')
            caption = "Вправи для схудення"
            text = fl.getText("waste",0)
            markup.add(item1, item2)
            bot.send_photo(message.chat.id, img, caption=caption)
            bot.send_message(message.chat.id, text, reply_markup=markup) 
        elif message.text == "📋 Тренувальні схеми":
            bot.send_message(message.chat.id, fl.getText("schema",0),parse_mode='html')
            sleep(1)
            bot.send_message(message.chat.id, fl.getText("schedule",0),parse_mode='html')
        else:
            print(message.text)
            bot.send_message(message.chat.id, 'Я не знаю що відповісти 😢')

@bot.callback_query_handler(func=lambda c: c.data == 'time1')
def callback_inline(call):
    try:
            
        global id_chat 
        id_chat = call.message.chat.id
        bot.send_message(call.message.chat.id, 'Вам слід лягти відпочивати о 21:00, я напишу вам о 5 ранку')
        global time01
        time01 = "05:00:00"
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Сон",
            reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Сон")
        alarm()

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'time2')
def callback_inline(call):
    try:

        global id_chat 
        id_chat = call.message.chat.id
        bot.send_message(call.message.chat.id, 'Вам слід лягти відпочивати о 23:00, я напишу вам о 7 ранку')
        global time01
        time01 = "07:00:00"
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Сон",
            reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Сон")
        alarm()

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'time3')
def callback_inline(call):
    try:

        global id_chat 
        id_chat = call.message.chat.id
        bot.send_message(call.message.chat.id, 'Вам слід лягти відпочивати о півночі, я напишу вам о 9 ранку')
        global time01
        time01 = "09:00:00"
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Сон",
            reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Сон")
        alarm()

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'time4')
def callback_inline(call):
    try:

        global id_chat 
        id_chat = call.message.chat.id
        bot.send_message(call.message.chat.id, 'Ранкові повідомлення вимкнені')
        global time01
        time01 = ""
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💤 Сон",
            reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Сон")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'sex1')
def callback_inline(call):
    global sex
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        sex = "Чоловік"    
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'sex2')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global sex
        sex = "Жінка"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)
        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'age1')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global age
        age = 15
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'age2')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global age
        age = 17
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'age3')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global age
        age = 20
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'age4')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global age
        age = 27
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'w1')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global weight
        weight = 45
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'w2')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global weight
        weight = 55
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'w3')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global weight
        weight = 65
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'w4')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global weight
        weight = 80
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'gr1')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global growth
        growth = 160
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'gr2')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global growth
        growth = 170
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'gr3')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global growth
        growth = 180
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'gr4')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global growth
        growth = 190
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

@bot.callback_query_handler(func=lambda c: c.data == 'g1')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global goals
        goals = "Схуднути"
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

    u1 = User(name, sex, weight, age, growth, goals)
    u1.add_user()
    bot.send_message(call.message.chat.id, 'Ваші дані')
    bot.send_message(call.message.chat.id, str(u1))


@bot.callback_query_handler(func=lambda c: c.data == 'g2')
def callback_inline(call):
    try:
        bot.send_message(call.message.chat.id, 'Дані передано')
        global growth
        goals = "Набрати вагу"
        # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📒 Блокнот", reply_markup=None)

        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Блокнот")

    except Exception as e:
        print(repr(e))

    u1 = User(name, sex, weight, age, growth, goals)
    u1.add_user()
    bot.send_message(call.message.chat.id, 'Ваші дані')
    bot.send_message(call.message.chat.id, str(u1))

@bot.callback_query_handler(func=lambda c: c.data == 'type1')
def callback_inline(call):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Сніданок") 
        item2 = types.KeyboardButton("Обід")
        item3 = types.KeyboardButton("Вечеря")
        back = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, back)
        bot.send_message(call.message.chat.id, 'Оберіть',reply_markup=markup)
        # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Їжа")

    except Exception as e:
        print(repr(e))

#Обробка функцій гортання списку
@bot.callback_query_handler(func=lambda c: True)
def callback_inline(call):
    try:
        markup = types.InlineKeyboardMarkup(row_width=2)
        #Їжа для схуднення
        if call.data == "fwbt_back":
            text = fl.getText("fwbt",scrollBack("fwbt",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwbt_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwbt_next')
            markup.add(item1, item2)
        elif call.data == "fwbt_next":
            text = fl.getText("fwbt",scrollNext("fwbt",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwbt_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwbt_next')
            markup.add(item1, item2)
        elif call.data == "fwlh_back":
            text = fl.getText("fwlh",scrollNext("fwlh",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwlh_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwlh_next')
            markup.add(item1, item2)
        elif call.data == "fwlh_next":
            text = fl.getText("fwlh",scrollNext("fwlh",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwlh_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwlh_next')
            markup.add(item1, item2)
        elif call.data == "fwdr_back":
            text = fl.getText("fwdr",scrollNext("fwdr",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwdr_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwdr_next')
            markup.add(item1, item2)
        elif call.data == "fwdr_next":
            text = fl.getText("fwdr",scrollNext("fwdr",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fwdr_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fwdr_next')
            markup.add(item1, item2)

        #Їжа для набору маси
        elif call.data == "fmbt_back":
            text = fl.getText("fmbt",scrollBack("fmbt",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmbt_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmbt_next')
            markup.add(item1, item2)
        elif call.data == "fmbt_next":
            text = fl.getText("fmbt",scrollNext("fmbt",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmbt_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmbt_next')
            markup.add(item1, item2)
        elif call.data == "fmlh_back":
            text = fl.getText("fmlh",scrollNext("fmlh",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmlh_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmlh_next')
            markup.add(item1, item2)
        elif call.data == "fmlh_next":
            text = fl.getText("fmlh",scrollNext("fmlh",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmlh_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmlh_next')
            markup.add(item1, item2)
        elif call.data == "fmdr_back":
            text = fl.getText("fmdr",scrollNext("fmdr",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmdr_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmdr_next')
            markup.add(item1, item2)
        elif call.data == "fmdr_next":
            text = fl.getText("fmdr",scrollNext("fmdr",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='fmdr_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='fmdr_next')
            markup.add(item1, item2)
        #Тренування для набору маси
        elif call.data == "muscle_next":
            markup = types.InlineKeyboardMarkup(row_width=3)
            text = fl.getText("muscle",scrollNext("muscle",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='muscle_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='muscle_next')  
            markup.add(item1, item2)
        elif call.data == "muscle_back":
            markup = types.InlineKeyboardMarkup(row_width=3)
            text = fl.getText("muscle",scrollBack("muscle",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='muscle_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='muscle_next')  
            markup.add(item1, item2)
        #Тренування для схуднення
        elif call.data == "waste_next":
            markup = types.InlineKeyboardMarkup(row_width=3)
            text = fl.getText("waste",scrollNext("waste",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='waste_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='waste_next')  
            markup.add(item1, item2)
        elif call.data == "waste_back":
            markup = types.InlineKeyboardMarkup(row_width=3)
            text = fl.getText("waste",scrollBack("waste",call.message.chat.id))
            item1 = types.InlineKeyboardButton("⬅️ Назад", callback_data='waste_back')
            item2 = types.InlineKeyboardButton("➡️ Вперед", callback_data='waste_next')  
            markup.add(item1, item2)
        if call.message.text!=text:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
            reply_markup=markup)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Інших пропозицій немає")
        
    except Exception as e:
        print(repr(e))

def msg():
    bot.send_message(id_chat, "Час прокидатися⏰")

def r_check_mes():
    while True:
        schedule.run_pending()
        sleep(1)

#Фунція прогортання списку вперед
def scrollNext(name,id):
    with open("userList.json", "r") as read_file:
        users = json.load(read_file)
    read_file.close()
    data = list(filter(lambda user: user['id'] == id, users))
    idx = users.index(data[0])
    i = data[0]['index'][name]
    if i<fl.getCount(name)-1:
        users[idx]['index'][name]=i+1
        with open("userList.json", "w") as write_file:
            json.dump(users, write_file)
        write_file.close()
        return i+1
    else:
        users[idx]['index'][name]=0
        with open("userList.json", "w") as write_file:
            json.dump(users, write_file)
        write_file.close()
        return 0

#Фунція прогортання списку назад
def scrollBack(name,id):
    with open("userList.json", "r") as read_file:
        users = json.load(read_file)
    read_file.close()
    data = list(filter(lambda user: user['id'] == id, users))
    idx = users.index(data[0])
    i = data[0]['index'][name]
    if i-1>=0:
        users[idx]['index'][name]=i-1
        with open("userList.json", "w") as write_file:
            json.dump(users, write_file)
        write_file.close()
        return i-1
    else:
        users[idx]['index'][name]=fl.getCount(name)-1
        with open("userList.json", "w") as write_file:
            json.dump(users, write_file)
        write_file.close()
        return fl.getCount(name)-1

#Фунція зміни поточного меню
#Потрібна для того, щоб кнопка "Назад" працювала відносно поточного меню
def changeMenu(name,id):
    with open("userList.json", "r") as read_file:
        users = json.load(read_file)
    read_file.close()
    data = list(filter(lambda user: user['id'] == id, users))
    idx = users.index(data[0])
    users[idx]['menu'] = name
    with open("userList.json", "w") as write_file:
        json.dump(users, write_file)
    write_file.close()

#Повертає поточне меню користувача
def currentMenu(id):
    with open("userList.json", "r") as read_file:
        users = json.load(read_file)
    read_file.close()
    data = list(filter(lambda user: user['id'] == id, users))
    return data[0]['menu']

def alarm():
    if time01 == "05:00:00":
        schedule.every().day.at("05:00").do(msg)    
        Thread(target=r_check_mes).start() 
    elif time01 == "07:00:00":
        schedul.every().day.at("07:00").do(msg)
        Thread(target=r_check_mes).start() 
    elif time01 == "09:00:00":
        schedule.every().day.at("09:00").do(msg)
        Thread(target=r_check_mes).start() 


if __name__ == "__main__": 
    # RUN
    bot.polling(none_stop=True)
