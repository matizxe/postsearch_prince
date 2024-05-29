from info import *
from pyrogram import Client
from subprocess import Popen
import asyncio

User = Client(name="user", session_string=SESSION)
DlBot = Client(name="auto-delete",
               api_id=API_ID,
               api_hash=API_HASH,
               bot_token=BOT_TOKEN)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        await User.start()
        asyncio.create_task(run_check_up())
        print("Bot Started 👍🙂")

    async def stop(self, *args):
        await super().stop()
        await User.stop()

if __name__ == "__main__":
    bot = Bot()
    bot.run()
