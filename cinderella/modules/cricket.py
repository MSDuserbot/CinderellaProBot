import urllib.request

from bs4 import BeautifulSoup
from telethon import events
from cinderella import telethn as tbot
from telethon.tl import functions, types
from telethon.tl.types import *





@tbot.on(events.NewMessage(pattern="/cs$"))
async def _(event):
    

    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = ""
    for match in result:
        Sed += match.get_text() + "\n\n"
    await event.reply(
        f"<b><u>📡 Match information gathered successful 📡</b></u>\n\n\n<code>{Sed}</code>",
        parse_mode="HTML",
    )


__help__ = """
*live cricket score*
 🔱 /cs*:* Latest live scores from cricinfo
"""

__mod_name__ = "🏏 CRICKET 🏏"
