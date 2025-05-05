from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests
import config

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💳 دفع عبر TON", callback_data="pay_with_ton")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"مرحبًا {user.first_name}! اضغط على الزر لبدء الدفع:", reply_markup=reply_markup)

def handle_payment(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"🔗 **أرسل المبلغ إلى هذا العنوان:**\n\n`{config.TON_WALLET_ADDRESS}`\n\nستتم المعالجة تلقائيًا بعد التأكيد.")

def check_payment(wallet_address, amount):
    # هنا ستتحقق من وجود الدفع عبر TON API (مثل Toncenter أو Tonapi)
    pass

def main():
    updater = Updater(config.BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_payment, pattern="pay_with_ton"))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
