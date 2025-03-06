import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Загружаем API-ключи из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я Travel-бот. Чем могу помочь?")

# Функция обработки текстовых сообщений
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    await update.message.reply_text(f"Вы сказали: {user_message}")

# Функция обработки ошибок
async def error_handler(update: object, context: CallbackContext):
    print(f"Произошла ошибка: {context.error}")

if __name__ == "__main__":
    # Создаем приложение Telegram-бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Обработчик ошибок
    app.add_error_handler(error_handler)

    print("Bot is running...")
    app.run_polling()
