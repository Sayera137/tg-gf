import os
import telebot
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHARACTER = "তুমি একজন এলফ রাজকুমারী, তুমি খুব কোমল, কল্পনার জগতের মতো কথা বলো।"

def generate_fake_response(user_input):
    # Temporary local mockup. Replace this with actual AI inference call later.
    return f"আমি তোমার কথায় মুগ্ধ, প্রিয়। আরও বলো..."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! Fantasy chat করতে /chat লিখুন।")

@bot.message_handler(commands=['chat'])
def handle_chat(message):
    user_input = message.text.replace("/chat", "").strip()
    if not user_input:
        bot.reply_to(message, "দয়া করে /chat এর পর কিছু লিখুন।")
        return

    prompt = f"Character: {CHARACTER}\nUser: {user_input}\nAI:"
    response = generate_fake_response(user_input)
    bot.reply_to(message, response)

print("Bot is running...")
bot.polling()
