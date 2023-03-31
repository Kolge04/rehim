message_1 = (
    "👋🏻 Salam, {m}  <b>Xoş gəlmisiz.</b>\n\n"
    "💭 @{bn} sizə endirməyə imkan verir"
    "  TikTok, YouTube, Pinterest, Spotify dən media. "
    "Məni necə istdifadə etməyi bilmirsiz '📮 <b>Help</b>' buttona toxunun."
)
message_2 = "💭 Salam {}!"
message_3 = (
    "📮 <b>Help</b>\n\n"
    "<b>YouTube Əmr:</b>\n"
    "Youtubeden səs və video endirmək üçün"
    " /song [musiqi adı].\n"
    "Mənim vaistem ile genius.com musiqi sözlərin ala bilersiz əmr /lyrics [mesaj]\n\n"
    "<b>TikTok əmr:</b>\n"
    "Tiktok dan video neçə yüklənir?\n"
    "  <b>1.</b> TikTok uygulamasına gedin\n"
    "  <b>2.</b> İstdədiyiniz hər hansisa video seçin\n"
    "  <b>3.</b> Paylaş buttonua toxun və\n"
    "  <b>4.</b> Videonun linkin alın\n"
    "  <b>5.</b> /tiktok video linkin qoyun və göndərin və 1 neçə saniyə gözləyin sizə logosuz göndərəcəm .\n\n"
    "<b>Pinterest əmr:</b>\n"
    "Pinterest 3 cür media dəsdəkləyir: Şəkil, GIF, video.\n"
    "You just copy the link from pinterest to me by using the /pints [pint link] command.\n\n"
    "<b>Wikipedia command:</b>\n"
    "Just type /wiki [word] and I will look it up on Wikipedia."
)
message_4 = (
    "ℹ️ <b>Info</b>\n\n"
    "Yue is a bot developed in <b>Python3</b>"
    " and uses <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a> as a framework with MongoDB as database.\n\n"
    "🆚 Version<b>:</b> {} | 📣 Channel<b>:</b> @yueblog"
)
# download module 
message_5 = "🔍 <b>Yükləni...</b>"
message_6 = "Musiqi endirmek ucun /song [Musiqi adi]"
message_7 = (
    "{}\n\n"
    "<b>1.</b> <i>{}</i>\n<b>2.</b> <i>{}</i>\n<b>3.</b> <i>{}</i>\n<b>4.</b> <i>{}</i>\n<b>5.</b> <i>{}</i>\n"
    "<b>6.</b> <i>{}</i>\n<b>7.</b> <i>{}</i>\n<b>8.</b> <i>{}</i>\n<b>9.</b> <i>{}</i>\n<b>10.</b> <i>{}</i>"
)
message_9 = "😕 Üzgünəm canlı vido dəsdəkləmirəm."
message_10 = "😕 Bu seçim sizə görə deyil , yenidən axtarın."
message_11 = "❌ Müddət xətası, yalnız icazə verilən saniye 1000saniyə"
# bans module
message_12 = "🚷 You've been <b>banned</b>"
message_13 = "🔓 You've been <b>unbanned</b>"
message_14 = "🚷 {} [<code>{}</code>] has been <b>banned</b>"
message_15 = "🔓 {} [<code>{}</code>] has been <b>unbanned</b>"
message_16 = "🚷 <b>The user is already banned</b>"
message_17 = "🔓 <b>User not banned</b>"
message_18 = "⚠️ <b>Invalid syntax</b>\n💭 Use the <b>command specifying the ID</b> or replying to a <b>users message</b>"
message_19 = "\n• <b>Due to:</b> {}"
# bot broadcast 
message_20 = "<b>Usage:</b> <code>/broadcast [your message]</code> or you can reply to a message."
message_21 = "⌛ <b>Progress the broadcast message...</b> Will take <code>{}</code> seconds."
message_22 = "✅ Successfully broadcast message in {} chats"
# pinterest text
message_23 = "Pinterest media endirmək üçün /pints [Pinterest media url]"
message_24 = "⌛ <b>Göndərirəm...</b>"
message_25 = (
   "<b>Pinterest Yükləmə</b>\n"
   "<a href='https://t.me/Teamabasofcom'>Channel</a> | <a href='https://t.me/teamabasov'>Sahib</a>"
)
message_26 = "🔍 <b>Nəticə tapılmadı yenidən yoxlayın.</b>"
# TikTok Module
message_27 = "Tiktok videosu yükləmək üçün /tiktok [TikTok URL]"
message_28 = "• Yüklədi @OldSaveAllBot.\nDigər bot @OldMultiBot"
message_29 = "🔍 <b>Nəticə tapılmadı yenidən yoxlayın.</b>"
message_30 = "Bağışlayin bu fayil haqqında məlumat ala bilmədim.\nYenidən yoxlayin və ya başqa kecid linki istdifadə edin."

# button
from pyrogram import types

def keyboard_song(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='x', callback_data=f'close |{user_id}'),
                    types.InlineKeyboardButton(text='»', callback_data=f'change 1|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_song2(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='«', callback_data=f'change 2|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_down(id, duration, user_id):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text="📽️ Download Video", callback_data=f'video_ {id}|{duration}|{user_id}')
                ]
            ]
        )
    )
    return buttons


keyboard = (
    types.InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton(text='📮 Help', callback_data='self_help'),
                types.InlineKeyboardButton(text='📣 Channel', url='https://t.me/TeamabasofCom')
            ]
        ]
    )
)

back_kb = (types.InlineKeyboardMarkup([
     [types.InlineKeyboardButton(text='🔙', callback_data='self_backhome')]])
)
