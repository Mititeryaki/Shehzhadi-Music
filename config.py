import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("24350557"))
API_HASH = os.getenv("3f302840f638ac2900a3becc056b3c59")
SESSION = os.getenv("1AZWarzMBu0G321fQVgb3MoMm01-VMimRFypXDaImaDv48mHqDE6T_IYM7BGaqxnUWB__Aoo2mPMePrMx0yLFwRRziCUQUrNEIvybnOLLEEQkEUP6xIYFo3JUfCpcVfChD8ICverCrmQT0L-6tTMt5ALao6xqxug3WPW_8p19YeU5TldM1Fq_avo4KnfDDaMtkYq1GFd4MT9I0b3Z2EXKW2xxzQUxVdmrWAUse_GuAqWg4Vm7Hs7OnDDq-iYClO8qp2Hywa0TeGbd7gOFB4xdWGDfJkkFH_tc7n6pcyZDi3NCiEthj4kRmBUfVuH-TiJgzQyAGjvIfzC85_elYUbuI1GQrSKnHTM=")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("6537006429").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
