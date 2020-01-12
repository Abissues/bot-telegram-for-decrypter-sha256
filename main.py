import os
import hashlib
import random
import time
import botogram
bot = botogram.create("your tocken")

@bot.process_message
def cracker(chat,message):
    if chat.type  in ("group", "supergroup"):
        return
    if message.text:
        with open('password.txt') as f:
            for line in f:
                line = line.strip()
                if hashlib.sha256(line.encode()).hexdigest() == message.text:
                    chat.send('password found --> ' + line)
                    break
           

            
if __name__ == "__main__":
    bot.run()
