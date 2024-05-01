import time, re, os
import webbrowser as web
import pyautogui as pg
import requests, platform, wikipedia, smtplib
import mouseinfo
from PIL import Image
from urllib.parse import quote

last = time.time()
pg.FAILSAFE = False
sleeptm = "None, You can use this function to print the remaining time in seconds."
path = ""
headless_mode = True

os.environ['DISPLAY'] = ':0'
now = datetime.now()

chour = now.strftime('%H')
mobile = input('Enter Mobile No of Receiver: ')
message = input('Enter Message you wanna send: ')
hour = int(input('Enter hour: '))
minute = int(input('Enter minute: '))

pywhatkit.sendwhatmsg(mobile, message, hour, minute)