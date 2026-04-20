print("БОТ ЗАПУЩЕН")
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8608585838:AAEsdQoyrEXBhubF2lMzWiwKjPvgNQb5es0"

keyboard = [
    ["📦 Услуги", "💰 Цены"],
    ["📞 Связаться"]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋 Я демо-бот.\nВыбери кнопку:",
        reply_markup=markup
    )
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 Услуги":
        await update.message.reply_text("Мы делаем: боты, сайты, автоматизацию")

    elif text == "💰 Цены":
        await update.message.reply_text("Цены от 100€")

    elif text == "📞 Связаться":
        await update.message.reply_text("Напишите ваш номер или @username 📲")

    elif "@" in text or text.isdigit():
        await update.message.reply_text("Спасибо! Мы скоро свяжемся с вами ✅")

    else:
        await update.message.reply_text("Нажми кнопку 👇", reply_markup=markup)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()


