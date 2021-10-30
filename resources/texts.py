from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

starttext = "Hello {}. \n I'm Logo maker bot."
helptext = """
**Help for Bot**
× /logo `[logname]` = To make a logo."""
startbutton = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Help", callback_data="helpmenu"),
                    InlineKeyboardButton("Updates", url ="https://t.me/YN_TD")
                ]
            ]
        )

backtohome = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="startmenu")]])

closebutton = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Close", callback_data="close")]])                     