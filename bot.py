import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Загружаем переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Travel-бот. Чем могу помочь?\n\n"
        "Доступные команды:\n"
        "/start — начать диалог\n"
        "/help — помощь"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я помогу вам спланировать путешествие!\n\n"
        "Просто отправьте сообщение с деталями: "
        "куда хотите поехать, на какие даты, "
        "и какие у вас предпочтения.\n\n"
        "Также доступна команда /start для перезапуска диалога."
    )

# Обработка обычных текстовых сообщений
async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    # Пока просто возвращаем эхо-сообщение
    await update.message.reply_text(f"Вы написали: {user_text}")

if __name__ == "__main__":
    # Создаем приложение и указываем токен
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем хендлеры команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Регистрируем хендлер для любых текстовых сообщений (кроме команд)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

    print("Bot is running...")
    app.run_polling()
