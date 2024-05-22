
'''

Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''
import datetime
import html
import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)





async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    time_send = update.message.date
    time_send = time_send + datetime.timedelta(hours= 5, minutes= 30)
    formatted_time = time_send.strftime('%Y-%m-%d %H:%M:%S')
    text = formatted_time + f"\n You send me any file i will send you the size of the file in appropriate size🍌🍌🍌"
    await context.bot.send_message(user.id, f"{formatted_time}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)



def format_file_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 ** 2:
        size_in_kb = size_in_bytes / 1024
        return f"{size_in_kb:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        size_in_mb = size_in_bytes / (1024 ** 2)
        return f"{size_in_mb:.2f} MB"
    else:
        size_in_gb = size_in_bytes / (1024 ** 3)
        return f"{size_in_gb:.2f} GB"

# file_size_in_bytes = 10310
# formatted_size = format_file_size(file_size_in_bytes)
# print(f"File Size: {formatted_size}")


async def doc_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    document = update.message.document
    doc_size_str = format_file_size(document.file_size)
    text = (f"Hello {html.escape(user.full_name)} You have send me a file with the size of "
            f"<blockquote>{doc_size_str}</blockquote> "
            f"Its full bytes size is: <code>{document.file_size}</code> "
            f"Please resend a new document for size checking"
            )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)








def main() -> None:
    """Start the bot."""
    application = Application.builder().token("🍌🍌🍌").build()

    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.Document.ALL, doc_fun))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
