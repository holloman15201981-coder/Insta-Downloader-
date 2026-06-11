import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import yt_dlp

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="سڵاو! لینکێکی ئینستاگرام بنێرە بۆ دابەزاندنی.")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text="چاوەڕێ بکە، خەریکی دابەزاندنم...")
    
    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    await context.bot.send_video(chat_id=update.effective_chat.id, video=open('video.mp4', 'rb'))

if __name__ == '__main__':
    application = ApplicationBuilder().token('YOUR_TOKEN_HERE').build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_video))
    
    application.run_polling()
