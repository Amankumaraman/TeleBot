from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import uuid
from db import add_user_link
from db import init_db

async def create(update: Update, context: CallbackContext):
    """Generate a new UUID and store it in the database linked to the user's Telegram ID."""
    user_id = update.effective_user.id
    user_uuid = str(uuid.uuid4())
    add_user_link(user_id, user_uuid)

    # Generate the link to the web page that corresponds to the UUID
    link = f"http://localhost:5000/link/{user_uuid}"
    await update.message.reply_text(f"Your link: {link}")

def main():
    """Set up the Telegram bot and its command handlers."""
    init_db()
    # Replace this with your actual bot token
    application = Application.builder().token("7584158925:AAG6WXXgn4FzgfoA_ciOK6RmvvyIkshfUhc").build()

    # Add the /create command handler
    application.add_handler(CommandHandler("create", create))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
