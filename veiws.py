
from django.http import HttpResponse
from weather.bot import start
from telegram import bot, Update
def telegram_webhook(request):
    update = Update.de_json(request.body, bot.bot)


    start(update, None)

    return HttpResponse("Telegram Bot buyruqlari muvaffaqiyatli qabul qilindi.")
