import discord
import asyncio
import time
import random
from colorama import Fore, Style
import pyfiglet
import os

os.system("cls" if os.name == "nt" else "clear")  # Konsolu temizle

banner = pyfiglet.figlet_format("XKX OWO BOT TOOL v0.3", font="slant")

print(Fore.BLUE + Style.BRIGHT + "="*80 + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + banner + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "="*80 + Style.RESET_ALL)



TOKEN = input("Token gir: ")
CHANNEL_ID = int(input("Kanal ID gir: "))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} aktif.")

    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("Kanal bulunamadı.")
        return

    while True:

        a = random.randint(15, 30)

        b = random.randint(1, 100)

        time.sleep(a)

        if b <= 33:
            await channel.send("wh")
        if 33 < b <= 66:
            await channel.send("wb")
        if 66 < b <= 100:
            owo = random.randint(1000, 10001)
            await channel.send("w cf " + str(owo))


client.run(TOKEN, bot=False)
