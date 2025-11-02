#my first robot telegram. :D
#===============dictionary====================
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
#=============================================

#==================START=====================


TOKEN = "8098481666:AAH_3csG8fkutVzxMJSYUu66w1W_6JMZ39E"

#start Func
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name} کص میخوای؟")

#echo Func
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "اره":
        await update.message.reply_text("آخ گفتی منم میخوام :(")
    elif text == "نه":
        await update.message.reply_text("بکیرم")
    else:
        await update.message.reply_text("نفهمیدم میشه دوباره بگی؟")


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("bot is running...")
app.run_polling()
#=============================================
