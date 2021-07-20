from telebot import TeleBot, types
import config
import keyboards
from functions import call_back, get_reply
example = config.example
from main import get, get_pages_count
bot = TeleBot(config.TOKEN)
# pytelegrambotapi
markup = types.InlineKeyboardMarkup(row_width=2)
users = {}
@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    img_company = "AgACAgIAAxkBAAEK6V1g9retNSgpkFJEgfmLmcQ565GcCwACZbIxGzNduUvfxlBIy9uU9wEAAwIAA3gAAyAE"
    text = f"<b>{message.from_user.first_name}</b>, Welcome to "
    text += "Telegram Bot of <a href = 'https://flipkart.com'>Flipkart.com</a>"
    text += "\n\nEnter the product name👇\nExample: `laptop`"
    bot.send_photo(id, img_company  ,caption=text,  parse_mode="html")
@bot.message_handler(commands=["page"])
def page(message):
    global change
    global users
    id = message.chat.id
    try:
        contents = users[id]
        change = bot.send_message(id,text="Change Page", reply_markup=keyboards.change_page_btn(contents))
    except:
        bot.send_message(id, f"The number of sheets is very large ({users[id]['results']})")

@bot.message_handler(content_types=['text'])
def text(message):
    global target
    global users
    id = message.chat.id
    send = bot.send_message(id, "<code>Loading...</code>",parse_mode="html")
    contents = {}
    try:
        contents["search_text"] = message.text
        contents["results"] = get_pages_count(message.text)
        contents[1] = get(0,message.text.lower(),1)
        users[id] = contents
        target = bot.send_photo(id, contents[1][1]["image"], caption=get_reply(contents,contents[1][1],1,1),parse_mode="Markdown",reply_markup=keyboards.btn(contents,1,1))

    except:
        bot.send_photo(id,
                       "AgACAgIAAxkBAAEK6WVg9ri3qIKo1kQiUUo4tnQrj7G0rAACZrIxGzNduUt_1h0oBv_V0AEAAwIAA20AAyAE",
                       caption="<b>Sorry, no results found!</b>",
                       parse_mode="html",
                       )
    bot.delete_message(id, send.message_id)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global target
    global change
    id = call.message.chat.id
    try:
        contents = users[id]
        if call.data[:3] == "?p=":
            page_id = int(call.data[3:])
            bot.delete_message(id,change.message_id)
            text = get_reply(contents, contents[page_id][1], page_id, 1)
            target = bot.send_photo(id, contents[page_id][1]["image"],caption=text,reply_markup=keyboards.btn(contents,page_id,1),parse_mode="Markdown")
        else:
            call_back(bot, call, target, types, contents, keyboards)
    except:
        bot.send_message(call.message.chat.id, "/start")
print("Starting...")
bot.polling(interval=1)
