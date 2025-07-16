import telebot

# 🔒 Token directly inside code — no variable needed
bot = telebot.TeleBot("7719608228:AAEUCVb9tPzMyhLoCH7zNoX_Q8gGhPeMlu8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome to @polxyz Poll Bot!\nType /poll to create a poll.")

@bot.message_handler(commands=['poll'])
def create_poll(message):
    question = "How was our service?"
    options = ['Excellent', 'Good', 'Poor']
    bot.send_poll(chat_id=message.chat.id, question=question, options=options, is_anonymous=False)

bot.polling()
