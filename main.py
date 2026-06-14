from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8949149888:AAGquaYRJn5Uq-yWoN3iO69Yb7v_flBbTrA"

# هنا سنضع ملفاتك لاحقاً
# عندما ترسل لي الملف، سأعطيك الـ ID وتضعه هنا
my_files = {
    "أحياء": "ضَع_كود_الملف_هنا"
}

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        # البوت سيرد عليك فوراً بالكود الخاص بأي ملف ترسله له
        await update.message.reply_text(f"✅ كود الملف (File ID) هو:\n\n`{update.message.document.file_id}`", parse_mode='Markdown')
    else:
        await update.message.reply_text("أرسل لي ملف PDF الآن وسأعطيك الكود الخاص به.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, get_id))
app.run_polling()
