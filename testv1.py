



import pandas as pd
import openpyxl
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Я бот для списания реактивов. Введи /stop, чтобы остановить бота в любой момент.')
    
# Функция-обработчик команды /stop
def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Бот остановлен.')
    # Останавливаем бота
    updater.stop()
    
# Функция-обработчик текстового сообщения
# Функция-обработчик текстового сообщения
def handle_text(update, context):
    k = update.message.text
    df = pd.read_excel('test23.xlsx')
    names = df.iloc[:,1].tolist()
    names1 = df.iloc[:,2].tolist()
    names2 = df.iloc[:,3].tolist()

    tabl1 = [i for i in range(0, len(names)) if names[i]==k]

    for x in tabl1:
        update.message.reply_text(f'{names[x]} {names1[x]} {names2[x]}')
        update.message.reply_text(tabl1)
    k2 = update.message.text
    k2 = int(k2)
    update.message.reply_text(names1[k2])
    k3=int(names1[k2])
    k4=k3-1
    
    names1[k2] =k4
   
    df['value'] = names1
    df.to_excel('test23.xlsx', index=False)
    update.message.reply_text('списання відбулося ')
    

        
# Инициализация телеграм-бота
updater = Updater(token='6076255658:AAGV2i7mtGRnWrhD2feWLZSNIAzBFnImd-s', use_context=True)
dispatcher = updater.dispatcher

# Добавляем обработчики команд
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('stop', stop))

# Добавляем обработчик текстовых сообщений
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_text))

# Запускаем бота
updater.start_polling()
updater.idle()


