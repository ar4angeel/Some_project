from telegram.ext import (CommandHandler, Filters, MessageHandler, Updater)
from telegram import (InlineKeyboardButton)
from like_a_bro.test import token_bot

#def start_bot(context, )

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i +n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

button_list = [
    InlineKeyboardButton("Хлебобулочное"),
    InlineKeyboardButton("Горячие блюда"),
    InlineKeyboardButton("")
]

def main():
    updater = Updater(token_bot, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(CommandHandler("age", ask_year))
    dp.add_handler(MessageHandler(Filters.text, count_years))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, birthMessageHendler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()