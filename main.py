from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8949149888:AAGquaYRJn5Uq-yWoN3iO69Yb7v_flBbTrA"

# هنا وضعنا "المفتاح" الذي أرسلته لي
my_files = {
    "أحياء_أول_متوسط": "BQACAgIAAxkBAAMNai8EIa7wbbzwlgWmuIZKu7ngJacAAiCcAALB73hJWCWVwV6nTRI8BA"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("ملزمة أحياء - أول متوسط", callback_data="file|أحياء_أول_متوسط")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحباً بك في منصة مسار، اختر الملف المطلوب:", reply_markup=reply_markup)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data.split("|")
    if data[0] == "file":
        file_key = data[1]
        file_id = my_files.get(file_key)
        if file_id:
            await query.message.reply_document(document=file_id, caption=f"تفضل ملزمة: {file_key}")
        else:
            await query.message.reply_text("عذراً، الملف غير موجود حالياً.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
