import telebot

TOKEN = "7114600917:AAFtgoJK2jUmBBUTfhnnlyE3ThZdYesJ9Cc"
WEBAPP_URL = "https://cardbattle.onrender.com"  # Замени на свой домен

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = telebot.types.WebAppInfo(WEBAPP_URL)
    play_button = telebot.types.KeyboardButton(text="🎮 Играть", web_app=webapp_btn)
    keyboard.add(play_button)

    bot.send_message(
        message.chat.id,
        "👋 Привет, герой!\nДобро пожаловать в *Card Battle!*",
        parse_mode="Markdown",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    print("🤖 Бот запущен...")
    bot.infinity_polling()
