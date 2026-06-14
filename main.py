from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8949149888:AAGquaYRJn5Uq-yWoN3iO69Yb7v_flBbTrA"

classes = {
    "الأول متوسط": ["رياضيات", "عربي", "إنكليزي"],
    "الثاني متوسط": ["رياضيات", "كيمياء", "فيزياء"],
    "الثالث متوسط": ["أحياء", "كيمياء", "رياضيات"]
}

types = ["ملخص", "ملازمة", "كتاب", "أسئلة"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for c in classes.keys():
        keyboard.append([InlineKeyboardButton(c, callback_data=f"class|{c}")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🤖 أهلاً بك في بوت منصة مسار\n\nاختر صفك الدراسي:", reply_markup=reply_markup)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data.split("|")
    if data[0] == "class":
        selected_class = data[1]
        keyboard = []
        for subject in classes[selected_class]:
            keyboard.append([InlineKeyboardButton(subject, callback_data=f"subject|{selected_class}|{subject}")])
        await query.edit_message_text(f"📚 اختر المادة في {selected_class}", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data[0] == "subject":
        selected_class = data[1]
        subject = data[2]
        keyboard = []
        for t in types:
            keyboard.append([InlineKeyboardButton(t, callback_data=f"file|{selected_class}|{subject}|{t}")])
        await query.edit_message_text(f"📖 اختر نوع الملف لمادة {subject}", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data[0] == "file":
        await query.message.reply_text(f"📄 لا يوجد ملف حالياً لـ:\n\n{data[1]}\n{data[2]}\n{data[3]}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
