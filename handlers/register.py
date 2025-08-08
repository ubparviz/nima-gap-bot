from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from config import states
from keyboards.location import get_location_keyboard
from keyboards.contact import get_contact_keyboard
from keyboards.gender import get_gender_keyboard
from data.SaveData import save_user_data, get_user_data, init_db


def start_register(update: Update, context: CallbackContext):
    init_db()
    update.message.reply_text("Ro'yxatdan o'tish uchun quyidagi malumotlaringiz kerak.")
    update.message.reply_text("Ismingizni yuboring")
    return states.NAME



def set_name(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    name = update.message.text

    if not name:
        update.message.reply_text("Iltimos, ismingizni yuboring.")
        return states.NAME
    
    save_user_data(chat_id, "name", name)

    update.message.reply_text("Ism qabul qilindi!")
    update.message.reply_text(
        "Gender tanlang:", 
        reply_markup = get_gender_keyboard()
    )
    
    return states.GENDER



def set_gender(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    gender = update.message.text

    if gender not in ["Erkak", "Ayol"]:
        update.message.reply_text("Iltimos, 'Erkak' yoki 'Ayol' dan birini tanlang.")
        return states.GENDER

    save_user_data(chat_id, "gender", gender)

    update.message.reply_text("Gender qabul qilindi")
    update.message.reply_text(
        "Joylashuvingizni yuboring:", 
        reply_markup = get_location_keyboard()
    )
    
    return states.LOCATION



def set_location(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    location = update.message.location

    if not location:
        update.message.reply_text("Iltimos, tugmani bosib yuboring.")
        return states.LOCATION
    
    loc = {
        "longitude": location.longitude,
        "latitude": location.latitude
    }
    save_user_data(chat_id, "location", loc)

    update.message.reply_text("Joylashuv qabul qilindi")
    update.message.reply_text(
        "Endi telefon raqamingizni yuboring:", 
        reply_markup = get_contact_keyboard()
    )

    return states.NUMBER



def set_number(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    contact = update.message.contact

    if not contact:
        update.message.reply_text("Iltimos, tugmani bosib yuboring.")
        return states.NUMBER
    
    save_user_data(chat_id, "number", contact.phone_number)
    update.message.reply_text("Telefon raqami qabul qilindi")

    user = context.user_data
    update.message.reply_html(
        text=f"Ro'yxatdan o'tganingiz uchun rahmat, <b>{user['name']}</b>!\n"
             f"Gender: <b>{user['gender']}</b>\n"
             f"Location: <b>{user['location']}</b>\n"
             f"Contact: <b>{user['number']}</b>"
    )
    update.message.reply_text("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!")
    
    context.user_data.clear()
    return ConversationHandler.END
