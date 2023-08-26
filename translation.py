from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """💠 I Will Short All Your Channels Link With Omnifly. Make Me Admin In Your Channel Withh All Rights And Follow Steps.

➡️ Example : `/batch Omnifly`

⚠️ You Can Also Use Channel ID Instead Of Channel Username

⚙️ Hit `/me` To Control Your Settings
"""

START_MESSAGE = """Hi There {} !

🔰 I Am A Powerful Link Shortener Robot With Fast Speed And A Lot Of Functions.

➡️ To Know More About Me Hit `/help` Command
➡️ To Link Your Shortener API Hit `/shortener_api` Command

Current Method : {}
"""

HELP_MESSAGE = """💠 Hey Welcome To Omnifly Bot, I Have Many eatures To Make Your Work Easier And Help You To Earn More 💰.

👉 Here Is The List Of My Features :

➡️ HyperLink And Hidden Link Support
➡️ Button Conversion Support
➡️ Domain Inclusion And Exclusion Options
➡️ Header And Footer Text Support
➡️ Replace Username Function
➡️ Banner Image Support
➡️ Batch Conversion For Channels
➡️ Channel Support For Admins Only

🔰 For Support Contact Here @J_shree_ram"""

ABOUT_TEXT = """
**💠 About Us 💠

🔰 I Am : omnifly.in.net RoBot

🔰 Our Support  : [Whatsapp](https://wa.me/917990556806) & [Telegram](https://t.me/brixflysupport)

🔰 Official Channel : @OmniflyLinks

🔰 Payment Proof : [Click Here](https://Omnifly.in.net/pages/payment-proofs)

❤️ Made With Love By Omnifly ❤️**
"""


METHOD_MESSAGE = """💠 Methods Available :

➡️ `Mdisk + Shortener (MDLINK)` - Change All The Links Of The Post To Your MDisk Account First And Then Short To Omnifly Link.

➡️ `Shortener` - Short All The Links Of The Post To Omnifly Link Directly.
    
👉 Current Method : {method}
    
Click Below Button To Set/Change Method :"""

CUSTOM_ALIAS_MESSAGE = """For Custom Alias :

This Feature Works Only In Private Mode Only.

**Format : [link] | [alias]**

Example : https://google.com | demolink"""


ADMINS_MESSAGE = """
List Of Admins Who Has Access To This Bot :
{admin_list}"""


CHANNELS_LIST_MESSAGE = """
Here Is A List Of The Channels :
{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Methods", callback_data="method_command"),
            InlineKeyboardButton("Batch", callback_data="cbatch_command"),
        ],
        [
            InlineKeyboardButton("Custom Alias", callback_data="alias_conf"),
            InlineKeyboardButton("Admins", callback_data="admins_list"),
        ],
        [
            InlineKeyboardButton("Channels", callback_data="channels_list"),
            InlineKeyboardButton("Home", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Method", callback_data="method_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Mdisk + Shortener", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
💠 Here Are Your Current Settings For This Bot :

➡️ Method : {method}

➡️ LinkShortify API : {shortener_api}

➡️ Mdisk API : {mdisk_api}

➡️ Username : @{username}

➡️ Header Text : {header_text}

➡️ Footer Text : {footer_text}

➡️ Banner Image:  {banner_image}
"""


MDISK_API_MESSAGE = """💠 To Add Or Update Your Mdisk API,
            
➡️ Example : `/mdisk_api 6LZq851sXoPHugiKQq`
            
⚠️ Get Your Mdisk API From @VideoToolMoneyTreebot

🔴 To Remove Mdisk API : `/mdisk_api remove`

👉 Current Mdisk API : `{}`

⚙️ Hit `/me` To Control Your Settings"""

SHORTENER_API_MESSAGE = """To Add Or Update Your Omnifly API,
            
➡️ Example : `/shortener_api 6LZq851sXofffPHugiKQq`

⚠️ Get Your Omnifly API From [Here](https://Omnifly.in.net/member/tools/api)

🔴 To Remove Omnifly API : `/shortener_api remove`

👉 Current Omnifly API : `{shortener_api}`

⚙️ Hit `/me` To Control Your Settings"""

HEADER_MESSAGE = """💠 To Set The Header Text For Every Message Caption Or Text.

➡️ Reply To Any Text With `/header` To Set It As Header

🔴 To Remove The Header Text : `/header remove`

👉 Current Header Text : {header_text}

⚙️ Hit `/me` To Control Your Settings"""

FOOTER_MESSAGE = """💠 To Set The Footer Text For Every Message Caption Or Text.

➡️ Reply To Any Text With `/footer` To Set It As Footer

🔴 To Remove The Footer Text : `/footer remove`

👉 Current Header Text : {footer_text}

⚙️ Hit `/me` To Control Your Settings"""

USERNAME_TEXT = """💠 To Replace Specific Username From Post.

➡️ Example : `/username Omnifly

🔴 To Remove The Username : `/username remove`

👉 Current Username : {username}

⚙️ Hit `/me` To Control Your Settings"""

BANNER_IMAGE = """💠 To Replace The Image From Post.

➡️ Example : /banner_image https://Omnifly.in.net/logo/white-green.png

⚠️ You Can Also Reply To Any Image With `/banner_image` To Set It As Banner Image.

🔴 To Remove The Banner Image : `/banner_image remove`

👉 Current Banner Image : {banner_image}

⚙️ Hit `/me` To Control Your Settings"""

INCLUDE_DOMAIN_TEXT = """💠 Bot Will Short Only Included Domains Only With This Command

➡️ Example : /include_domain t.me telegram.me

🔴 To Remove The Specific Included Domain : `/include_domain remove t.me`

🔴 To Remove All Included Domains : `/include_domain remove_all`

👉 Current Included Domains : {}

⚙️ Hit `/me` To Control Your Settings"""

EXCLUDE_DOMAIN_TEXT = """💠 Bot Will Not Short Excluded Domains With This Command

➡️ Example : /exclude_domain t.me telegram.me

🔴 To Remove The Specific Excluded Domain : `/exclude_domain remove t.me`

🔴 To Remove All Excluded Domains : `/exclude_domain remove_all`

👉 Current Excluded Domains : {}

⚙️ Hit `/me` To Control Your Settings"""

BANNED_USER_TXT = """
Usage : `/ban [User ID]`
Usage : `/unban [User ID]`

List Of Banned Users :
{users}"""
