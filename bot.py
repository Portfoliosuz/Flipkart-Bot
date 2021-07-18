from telebot import TeleBot, types
import config
import keyboards
from functions import call_back, get_reply
example = config.example
from main import get_all
bot = TeleBot(config.TOKEN)
# pytelegrambotapi
markup = types.InlineKeyboardMarkup(row_width=2)
users = {}
@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    img_company = "AgACAgIAAxkBAAEK3Jlg8Y3oYl3gnv70_VXXPxtd2oZI6AACw7UxGyaxkUs8OhFDgx_g_gEAAwIAA3gAAyAE"
    text = f"<b>{message.from_user.first_name}</b>, Welcome to "
    text += "Telegram Bot of <a href = 'https://flipkart.com'>Flipkart.com</a>"
    text += f"\n\nEnter the product name👇\nExample: `laptop`{users}"
    bot.send_photo(id, img_company  ,caption=text,  parse_mode="html")
@bot.message_handler(commands=["page"])
def page(message):
    global change
    global users
    id = message.chat.id
    contents = users[id]
    try:
        change = bot.send_message(id,text="Change Page", reply_markup=keyboards.change_page_btn(contents))
    except:
        bot.send_message(id, "/start",)

@bot.message_handler(content_types=['text'])
def text(message):
    global target
    global users
    contents = get_all(message.text).get()
    id = message.chat.id
    users[id] = contents
    if contents:
        target = bot.send_photo(id, contents[1][1]["image"], caption=get_reply(contents,contents[1][1],1,1),parse_mode="Markdown",reply_markup=keyboards.btn(contents,1,1))
    else:
        bot.send_photo(id,
                       "AgACAgIAAxkBAAEK3Mxg8Zc_XW9pqsau1aZD76nrsEFupwAC0LUxGyaxkUtj4QvJbrFMbAEAAwIAA3MAAyAE",
                       caption="<b>Sorry, no results found!</b>",
                       parse_mode="html",
                       )
print("Starting...")
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global target
    global change
    global users
    id = call.message.chat.id
    contents =users[id]
    try:
        if call.data[:3] == "?p=":
            page_id = int(call.data[3:])
            bot.delete_message(id,change.message_id)
            text = get_reply(contents, contents[page_id][1], page_id, 1)
            target = bot.send_photo(id, contents[page_id][1]["image"],caption=text,reply_markup=keyboards.btn(contents,page_id,1),parse_mode="Markdown")
        else:
            call_back(bot, call, target, types, contents, keyboards)
    except:
        bot.send_message(call.message.chat.id, "/start")
bot.polling()
