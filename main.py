from ast import main
from crypt import methods
from http import server
import json
import os
from unicodedata import name
import telebot
import logging
from config import *
from flask import Flask , request


bot = telebot.TeleBot(bot_token)
server = Flask (__name__)
logger = telebot.logger
logger = set.Level(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.name
    bot.reply_to(message, f"Hello,{username}!")

@server.route(f"/{bot_token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data(). decode ("utf-8")
    update = telebot.types.Update_json(json_string)
    bot.process_new_updates([update])
    return "!" , 200







if __name__ =="__main__":
    bot.remove_webhook()
    bot.set_webhook(url=app_url)
server.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
