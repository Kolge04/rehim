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

    ApiID = os.environ.get('API_ID', 12210813)
    ApiHASH = os.environ.get('API_HASH', "e42eeae11a2f96bcfc5ec3b46a30adad") 

    TelegramBot = os.environ.get('TELEGRAM', "6062022905:AAF3kB_R5vLKt6HyZfkHx8NcLaMtG9Hji8I")
    SpecialUsers = int(os.environ.get('CREATOR_ID', "5663585448"))

    MongoDatabaseURI = os.environ.get('DATABASE_URI', "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    LogGroupChatID = int(os.environ.get('LOG_CHAT_ID', "-1001814896088")) 

    MusicDurationLimit = int(os.getenv("MusicDurationLimit", "3600"))
    CommandPrefixesBOT = list(os.getenv("CommandPrefixesBOT", '. / !').split())

    GeniusLyricsAPI = os.getenv('GeniusLyricsAPI', '1QNnajK5oSh2Ut_bJVXbKzwFV_BqyZxUssSpWdcjpVHr5qRcql0BMx3pMSVWSFoj')
    UserMustJoinChannel = os.getenv('UserMustJoinChannel', 'sesizKOLGE')


vars = RoftConfiguration() 
