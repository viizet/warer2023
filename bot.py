import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6919967646:AAFvfd-DH_LtO97IGoq0j9bJjFPgOqcGcEk")

API_ID = int(os.environ.get("API_ID", "26176218"))

API_HASH = os.environ.get("API_HASH", "4a50bc8acb0169930f5914eb88091736")

STRING = os.environ.get("STRING", "BAGPatoAjofF4Gtv6DQR89A3zRubbTBNSjiARQbtjuZZrzbFaA_qCLEU3YhITNKOCE_KBQwa-8Mlql-r6d6TuTCkADpt6ybHd3jb-gYTJCyx0mR3sbB4rBG-jII1_Dg0oumStAdnsFNczdPolY1OmZVv5wpNry6670vRXAZadG8DYkJcV2LLXeuGUTf9G7K6Fxf2mgWKAW3tY4_ZQfYFzOe_A2nY7HuTH8xQxfBlrkN5DsVsJtky3o50d4ZmZ5-GcTAa-4Gl_mSWOI9TEeN_Xij6ICVLr0MZQ50ON_F_QBN3E1hoSLV3PLp_B-qDy9VilHuLeizFOMwm2u4uGxyww-KqxRYxRgAAAABBXjeKAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
