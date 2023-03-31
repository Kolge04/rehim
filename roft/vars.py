# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.
# Vars of the bot

import os


class RoftConfiguration:

    __roft_version__ = '1.5.8'

    ApiID = os.environ.get('API_ID', 15954332)
    ApiHASH = os.environ.get('API_HASH', "85adea6f1eaf068b707703b4846a9ced") 

    TelegramBot = os.environ.get('TELEGRAM', "5869735539:AAFJIEdqvHHptb875nstYUVxETh9WRpqC9E")
    SpecialUsers = int(os.environ.get('CREATOR_ID', "5134595693"))

    MongoDatabaseURI = os.environ.get('DATABASE_URI', "mongodb+srv://srnpxkb007:srnpxkb007@cluster0.i2tsrxy.mongodb.net/?retryWrites=true&w=majority")
    LogGroupChatID = int(os.environ.get('LOG_CHAT_ID', "-1001737573985")) 

    MusicDurationLimit = int(os.getenv("MusicDurationLimit", "3600"))
    CommandPrefixesBOT = list(os.getenv("CommandPrefixesBOT", '. / !').split())

    GeniusLyricsAPI = os.getenv('GeniusLyricsAPI', '1QNnajK5oSh2Ut_bJVXbKzwFV_BqyZxUssSpWdcjpVHr5qRcql0BMx3pMSVWSFoj')
    UserMustJoinChannel = os.getenv('UserMustJoinChannel', 'Teamabasofcom')


vars = RoftConfiguration() 
