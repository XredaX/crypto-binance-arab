from lib2to3.pgen2 import token
from telethon import TelegramClient, events, Button 
from configs import Config
from database import user

api_id = Config.API_ID
api_hash = Config.API_HASH
token = '5707050273:AAFZ8bMS0DC6DTKP9ZVz_bWqa_Av6Y0RAEg'
bot = TelegramClient('bot', api_id,  api_hash).start(bot_token=token)
print('START')

@bot.on(events.NewMessage())
async def send_welcome(event):
    chat_id = event.chat_id
    if str(chat_id) == '-1001779243506':
        msg = event.raw_text
        dataaccS = user.findacc1(collection='sig')
        message_id = dataaccS['message_id'] + 1
        text = 'Click in the button to see the signal'
        await bot.send_message(-1001527564174, text, buttons=[
                [Button.inline('✅ إضغط هنا', 'show')]])
        user.addsession(collection='sig', message_id=message_id, msg=msg)
    if str(chat_id) == '-1001527564174':
        dataaccS = user.findacc1(collection='sig')
        message_id = dataaccS['message_id'] + 1
        dataaccS = user.findacc2(collection='sig', message_id=message_id)

@bot.on(events.CallbackQuery)
async def handler(event):
    try:
        if event.data == b'show':
            dataaccS = user.findacc(collection='sig', message_id=event.message_id)
            await event.answer(dataaccS[0]['msg'], alert=True)
        except :
            pass

bot.start()
bot.run_until_disconnected()
