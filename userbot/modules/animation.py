import asyncio
from random import choice
from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import register as own_cmd
from userbot.modules.ping import absen
from userbot.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="bulan$")
async def _(event):
    event = await edit_or_reply(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ayiin_cmd(pattern="sayang$")
async def _(event):
    e = await edit_or_reply(event, "I LOVEE YOUUU ð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG KAMU ððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA ð")
    await e.edit("ðððð")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("SAYANG KAMUð")


@ayiin_cmd(pattern=r"dino(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`ð                        ð¦`")
    await typew.edit("`ð                       ð¦`")
    await typew.edit("`ð                      ð¦`")
    await typew.edit("`ð                     ð¦`")
    await typew.edit("`ð   `LARII`          ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ðWOARGH!   ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                    ð¦`")
    await typew.edit("`ð                     ð¦`")
    await typew.edit("`ð  Huh-Huh           ð¦`")
    await typew.edit("`ð                   ð¦`")
    await typew.edit("`ð                  ð¦`")
    await typew.edit("`ð                 ð¦`")
    await typew.edit("`ð                ð¦`")
    await typew.edit("`ð               ð¦`")
    await typew.edit("`ð              ð¦`")
    await typew.edit("`ð             ð¦`")
    await typew.edit("`ð            ð¦`")
    await typew.edit("`ð           ð¦`")
    await typew.edit("`ð          ð¦`")
    await typew.edit("`ð         ð¦`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`ð       ð¦`")
    await typew.edit("`ð      ð¦`")
    await typew.edit("`ð     ð¦`")
    await typew.edit("`ð    ð¦`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`ð§ð¦`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@ayiin_cmd(pattern="gabut$")
async def _(event):
    e = await edit_or_reply(event, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("ðððð")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("ðððð")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¶                                 ð¢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("ð¢                       ð¶")
    await e.edit("ð¢                      ð¶")
    await e.edit("ð¢                     ð¶")
    await e.edit("ð¢                    ð¶")
    await e.edit("ð¢                   ð¶")
    await e.edit("ð¢                  ð¶")
    await e.edit("ð¢                 ð¶")
    await e.edit("ð¢                ð¶")
    await e.edit("ð¢               ð¶")
    await e.edit("ð¢              ð¶")
    await e.edit("ð¢             ð¶")
    await e.edit("ð¢            ð¶")
    await e.edit("ð¢           ð¶")
    await e.edit("ð¢          ð¶")
    await e.edit("ð¢         ð¶")
    await e.edit("ð¢        ð¶")
    await e.edit("ð¢       ð¶")
    await e.edit("ð¢      ð¶")
    await e.edit("ð¢     ð¶")
    await e.edit("ð¢    ð¶")
    await e.edit("ð¢   ð¶")
    await e.edit("ð¢  ð¶")
    await e.edit("ð¢ ð¶")
    await e.edit("ð¢ð¶")
    await e.edit("ð¶ð¢")
    await e.edit("ð¶ ð¢")
    await e.edit("ð¶  ð¢")
    await e.edit("ð¶   ð¢")
    await e.edit("ð¶    ð¢")
    await e.edit("ð¶     ð¢")
    await e.edit("ð¶      ð¢")
    await e.edit("ð¶       ð¢")
    await e.edit("ð¶        ð¢")
    await e.edit("ð¶         ð¢")
    await e.edit("ð¶          ð¢")
    await e.edit("ð¶           ð¢")
    await e.edit("ð¶            ð¢")
    await e.edit("ð¶             ð¢")
    await e.edit("ð¶              ð¢")
    await e.edit("ð¶               ð¢")
    await e.edit("ð¶                ð¢")
    await e.edit("ð¶                 ð¢")
    await e.edit("ð¶                  ð¢")
    await e.edit("ð¶                   ð¢")
    await e.edit("ð¶                    ð¢")
    await e.edit("ð¶                     ð¢")
    await e.edit("ð¶                      ð¢")
    await e.edit("ð¶                       ð¢")
    await e.edit("ð¶                        ð¢")
    await e.edit("ð¶                         ð¢")
    await e.edit("ð¶                          ð¢")
    await e.edit("ð¶                           ð¢")
    await e.edit("ð¶                            ð¢")
    await e.edit("ð¶                             ð¢")
    await e.edit("ð¶                              ð¢")
    await e.edit("ð¶                               ð¢")
    await e.edit("ð¶                                ð¢")
    await e.edit("`GABUT`")


@ayiin_cmd(pattern=r"terkadang(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@ayiin_cmd(pattern=r"mf$")
async def _(event):
    await edit_or_reply(event, "`mf g dl` **ã(ã;_ _)ã=3** ")


@ayiin_cmd(pattern=r"(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "cinta":
        await event.edit(input_str)
        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 4%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 8%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 20%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 36%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 52%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 84%\nâââââââââââââââââââââââââ `",
            "`Mengirim Cintaku.. 100%\nâââââââââCINTAKUâââââââââââ `",
            "`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You ð`",
        ]
        animation_interval = 2
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@ayiin_cmd(pattern=r"gombal(?: |$)(.*)")
async def _(event):
    typew = edit_or_reply(event, "`Hai, I LOVE YOU ð`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUUðð`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@ayiin_cmd(pattern="helikopter(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "â¬â¬â¬.â.â¬â¬â¬ \n"
        "ââââââââ \n"
        "â¢â¤ ââââââââââââ¢â¤ \n"
        "ââ â ââ âââââââââââ¬ \n"
        "â¥ââââââ¤ \n"
        "âââ©âââ©ââ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ \n"
        "â¬ââ¬ Hallo Semuanya :) \n"
        "â¬ââ¬â»/ \n"
        "â¬ââ¬/â \n"
        "â¬ââ¬/ \\ \n",
    )


@ayiin_cmd(pattern="tembak(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "_/ï¹\\_\n" "(Ò`_Â´)\n" "<,ï¸»â¦â¤â Ò\n" r"_/ï¹\_" "\n**Mau Jadi Pacarku Gak?!**",
    )


@ayiin_cmd(pattern="bundir(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "`Dadah Semuanya...`          \nããããã|"
        "\nããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ããããã| \n"
        "ãï¼ï¿£ï¿£ï¼¼| \n"
        "ï¼ Â´ï½¥ ãã |ï¼¼ \n"
        "ã|ãï¼ã | ä¸¶ï¼¼ \n"
        "ï¼ ãï½¥ãã|ããï¼¼ \n"
        "ãï¼¼ï¼¿ï¼¿ï¼âª _ âª) \n"
        "ããããã ï¼µ ï¼µ\n",
    )


@ayiin_cmd(pattern="awk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "ââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââââ\n`Awkwokwokwok..`",
    )


@ayiin_cmd(pattern="ular(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââ\n"
        "âââââ\n"
        "ââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "âââââââ\n"
        "ââââââââ\n"
        "âââââââââ\n"
        "ââââââââââ\n"
        "âââââââââââ\n"
        "ââââââââââ\n"
        "âââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââ\n"
        "ââââââââââ\n"
        "ââââââââââââ\n"
        "ââââââââââââââ\n"
        "ââââââââââââââââ\n"
        "ââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "ââââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "âââââââââââââââââââ\n"
        "âââââââââââââââââââ\n",
    )


@ayiin_cmd(pattern="y(?: |$)(.*)")
async def _(event):
    await typew.edit(
        event,
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââââ\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â¡â\n"
        "â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ¡â¡â¡â¡â¡â¡â\n"
        "ââââââââââ¡â¡â¡â¡â¡â¡âââââââââ\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â\n"
        "ââââââââââââ¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡â¡ââ\n"
        "ââââââ¡â¡â¡â¡â¡â¡â¡ââââââââââ\n",
    )


@ayiin_cmd(pattern="tank(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âÛâââââââ]âââââââââââ \n"
        "âââââââââââââââââ¦\n"
        "[âââââââââââââââââââ]\n"
        "â¥ââ²ââ²ââ²ââ²ââ²ââ²ââ¤\n",
    )


@ayiin_cmd(pattern="babi(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "âââââ®â­ââââ­âââââ®\n"
        "âââââââââ­â«Ngok â\n"
        "âââ°âââââ¯â¯â°âââââ¯\n"
        "ââ­ââ»â®â²ââââââ®â­â®â\n"
        "ââââââ²â²â²â²â²â²â£ââ¯â\n"
        "ââ°ââ³â»ââ¯â²â²â²â²ââââ\n"
        "ââââ°ââ³âââ³âââ¯âââ\n"
        "âââââââ»âââ»âââââ\n",
    )


@own_cmd(pattern=r"^\Absendulu$", own=True)
async def _(event):
    await event.reply(choice(absen))


@ayiin_cmd(pattern="ajg(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "â¥âââââââââ­âââ®âââ³\n"
        "â¢â­â®â­ââââââ«ââââââ£\n"
        "â¢ââ°â«ââââââââââ°â«â£\n"
        "â¢â°ââ«ââââââ°â¯â°â³ââ¯â£\n"
        "â¢âââââ³â³âââââ³â«âââ£\n"
        "â¨âââââââââââââââ»\n",
    )


@ayiin_cmd(pattern=r"bernyanyi(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "**Ganteng Doang Gak Bernyanyi (à¸ËoË)à¸§**")
    sleep(2)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")
    sleep(1)
    await typew.edit("**âªâ(ã»oï½¥)ââªâ ( ï½¥oï½¥) â**")
    sleep(1)
    await typew.edit("**âªâ ( ï½¥oï½¥) ââªâ (ã»oï½¥) ââª**")


@ayiin_cmd(pattern=r"hua$")
async def _(event):
    e = await edit_or_reply(event, "Ø£â¿Ø£")
    await e.edit("â¥ï¹â¥")
    await e.edit("(;ï¹;)")
    await e.edit("(ToT)")
    await e.edit("(â³Ðâ³)")
    await e.edit("(à²¥ï¹à²¥)")
    await e.edit("ï¼ï¼ã¸ï¼ï¼")
    await e.edit("(Tï¼¿T)")
    await e.edit("ï¼Ïã¼Ïï¼")
    await e.edit("(ï¼´â½ï¼´)")
    await e.edit("(âï¹â)")
    await e.edit("ï¼ï½Ðï½ï¼")
    await e.edit("(Â´Ðâã½")
    await e.edit("(;Ð;)")
    await e.edit("ï¼>ï¹<ï¼")
    await e.edit("(TÐ´T)")
    await e.edit("(ã¤ï¹â)")
    await e.edit("à¼¼â¯ï¹â¯à¼½")
    await e.edit("(ãï¹ã½)")
    await e.edit("(ãAã½)")
    await e.edit("(â¥_â¥)")
    await e.edit("(TâT)")
    await e.edit("(à¼àº¶âà¼àº¶)")
    await e.edit("(âï¹â°)ï½¡")
    await e.edit("(à²¥_Êà²¥)")
    await e.edit("(ã¤Ð´â)")
    await e.edit("(âÍ_âÌ¥)")
    await e.edit("(à®ï¹à®`ï½¡)")
    await e.edit("à¼¼à²¢_à²¢à¼½")
    await e.edit("à¼¼ à¼àº¶ à·´ à¼àº¶à¼½")


@ayiin_cmd(pattern="huh(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`\n(\\_/)`" "`\n(â_â)`" "`\n />â¤ï¸ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`" "`\n(â_â)`" "`\n/>ð  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(â_â)`" "`\nð<\\  *Terimakasih`")


@ayiin_cmd(pattern=r"(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "ceritacinta":
        await event.edit(input_str)
        animation_chars = [
            "`Cerita â¤ï¸ Cinta` ",
            "  ð             ð \n/ð\\         <ð\\ \n ð               /|",
            "  ð          ð³ \n/ð\\       /ð\\ \n  ð            /|",
            "  ð            ð \n/ð\\         <ð> \n  ð             /|",
            "  ð         âºï¸ \n/ð\\      /ð\\ \n  ð          /|",
            "  ð          ð \n/ð\\       /ð\\ \n  ð           /|",
            "  ð   ð \n /ð\\/ð\\ \n   ð   /|",
            " ð³  ð \n /|\\ /ð\\ \n /     / |",
            "ð    /ð°\\ \n<|\\      ð \n /ð    / |",
            "ð \n/(),âð® \n /\\         _/\\/|",
            "ð \n/\\_,__ð« \n  //    //       \\",
            "ð \n/\\_,ð¦_ð  \n  //         //        \\",
            "  ð­      âºï¸ \n  /|\\   /(ð¶)\\ \n  /!\\   / \\ ",
            "`TAMAT ð`",
        ]
        animation_interval = 3
        animation_ttl = range(103)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 103])


@ayiin_cmd(pattern="(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "canda":
        await event.edit(input_str)
        animation_chars = [
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â   â    â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Kamu    â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â       â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Pasti   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__|â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Belum   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â          â¡\n  â â¢¿â£¯â â â (x)â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â    â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Mandi  â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __ â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â  â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Bwhaha  â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__| â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â   â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Canda   â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â ****â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        ]
        animation_interval = 1
        animation_ttl = range(11)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@ayiin_cmd(pattern="santet(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Mengaktifkan Perintah Santet Online....`")
    sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   â")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   âââââââââââââââââ")
    sleep(1)
    await typew.edit("`Target Berhasil Tersantet Online ð¥´`")


@ayiin_cmd(pattern="nah(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`\n(\\_/)`" "`\n(â_â)`" "`\n />ð *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(â_â)`" "`\nð<\\  *Tapi Bo'ong`")


# Alpinnnn Gans


@ayiin_cmd(pattern="(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "owner":
        await event.edit(input_str)
        animation_chars = [
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
            "â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬",
        ]
        animation_interval = 0.5
        animation_ttl = range(6)
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 6])


CMD_HELP.update(
    {
        "animasi": f"`{cmd}gabut` ; `{cmd}dino`\
    \nUsage: ntahlah gabut doang.\
    \n\n`{cmd}gombal`\
    \nUsage: buat bercanda\
    \n\n`{cmd}cinta`\
    \nUsage: mengirim cintamu ke seseorang.\
    \n\n`{cmd}sayang`\
    \nUsage: untuk jadi buaya.\
    \n\n`{cmd}terkadang`\
    \nUsage: Auk dah iseng doang.\
    \n\n`{cmd}helikopter` ; `{cmd}tank` ; `{cmd}tembak`\n`{cmd}bundir`\
    \nUsage: liat sendiri\
    \n\n`{cmd}y`\
    \nUsage: jempol\
    \n\n`{cmd}bulan` ; `{cmd}hati` ; `{cmd}bernyanyi`\
    \nUsage: liat aja.\
    \n\n`{cmd}awk`\
    \nUsage: ketawa lari.\
    \n\n`{cmd}lar` ; `{cmd}abi` ; `{cmd}ajg`\
    \nUsage: liat sendiri.\
    \n\n`{cmd}nah` ; `{cmd}huh` ; `{cmd}owner`\
    \nUsage: cobain.\
    \n\n`{cmd}bunga` ; `{cmd}buah`\
    \nUsage: animasi.\
    \n\n`{cmd}waktu`\
    \nUsage: animasi.\
    \n\n`{cmd}hua`\
    \nUsage: nangis.\
    \n\n`{cmd}ceritacinta` ; `{cmd}canda`\
    \nUsage: liat sendiri\
    \n\n`{cmd}santet`\
    \nUsage: Santet Online Buat Bercanda."
    }
)
