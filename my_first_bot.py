#my first robot telegram. :D
#===============dictionary====================
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
#=============================================

#==================START=====================


TOKEN = os.getenv("BOT_TOKEN")
#start Func
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name} شیر میخوای؟")

#echo Func
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "اره":
        await update.message.reply_text("آخ گفتی مسیبسشبیشسیب میخوام :(")
    elif text == "نه":
        await update.message.reply_text("مهم نیست برام")
    else:
        await update.message.reply_text("نفهمیدم میشه دوباره بگی؟")


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("bot is running...")

app.run_polling(
    allowed_updates=Update.ALL_TYPES,  # همه نوع پیام رو بگیر
    close_loop=False
)
#=============================================

