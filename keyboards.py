from telebot import types

def btn(contents, page_id, content_id):
    markup = types.InlineKeyboardMarkup()
    data = f"{page_id},{content_id}"
    keys = contents.keys()

    if len(contents[page_id].keys())-1 <= content_id:
        if page_id +1 <= contents["results"]:
            markup.add(
                types.InlineKeyboardButton(
                    text="⬅️",
                    callback_data="LEFT." +data
                ),
                types.InlineKeyboardButton(
                    text=f"{page_id+1} - 🗒",
                    callback_data="RIGHT." +data
                )
            )
        else:
            markup.add(
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data="LEFT." +data
                                        ),
            )
    elif 1 >= content_id:
        if page_id > 1:
            markup.add(
                types.InlineKeyboardButton(
                    text=f"{page_id-1} - 🗒",
                    callback_data="LEFT." + data
                ),

                types.InlineKeyboardButton(
                    text="➡️",
                    callback_data="RIGHT." + data
                     ),
            )
        else:
            markup.add(

                types.InlineKeyboardButton(
                    text="➡️",
                    callback_data="RIGHT." + data
                ),
            )
    else:
        markup.add(
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data="LEFT." +data
            ),
            types.InlineKeyboardButton(text="➡️",
                                       callback_data="RIGHT." +data
            )
        )
    return markup

def change_page_btn(contents):
    markup = types.InlineKeyboardMarkup(row_width=5)
    contents_ = contents["results"] +1
    row = (contents_-1)//5
    column = contents_ - 5*row -1
    a = 1
    for i in range(1,row +1):
        markup.add(
            types.InlineKeyboardButton(text=a, callback_data=f"?p={a}"),
            types.InlineKeyboardButton(text=a+1, callback_data=f"?p={a+1}"),
            types.InlineKeyboardButton(text=a+2, callback_data=f"?p={a+2}"),
            types.InlineKeyboardButton(text=a+3, callback_data=f"?p={a+3}"),
            types.InlineKeyboardButton(text=a+4, callback_data=f"?p={a+4}"),
        )
        a += 5

    if column == 1:
        markup.add(
            types.InlineKeyboardButton(text=contents_-1, callback_data=f"?p={contents_-1}")
                   )
    elif column ==2:
        markup.add(
            types.InlineKeyboardButton(text=contents_-2, callback_data=f"?p={contents_-2}"),
            types.InlineKeyboardButton(text=contents_-1, callback_data=f"?p={contents_-1}")
        )

    elif column == 3:
        markup.add(
        types.InlineKeyboardButton(text=contents_-3, callback_data=f"?p={contents_-3}"),
        types.InlineKeyboardButton(text=contents_-2, callback_data=f"?p={contents_-2}"),
        types.InlineKeyboardButton(text=contents_-1, callback_data=f"?p={contents_-1}")
    )
    elif column == 4:
        markup.add(
        types.InlineKeyboardButton(text=contents_-4, callback_data=f"?p={contents_-4}"),
        types.InlineKeyboardButton(text=contents_-3, callback_data=f"?p={contents_-3}"),
        types.InlineKeyboardButton(text=contents_-2, callback_data=f"?p={contents_-2}"),
        types.InlineKeyboardButton(text=contents_-1, callback_data=f"?p={contents_-1}"),
    )


    return markup




