#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7384767506:AAElEB0m8ZRvIj8h-WkgeETPghwyNfzcPz8")
    API_ID = int(os.environ.get("API_ID", "22118129"))
    API_HASH = os.environ.get("API_HASH", "43c66e3314921552d9330a4b05b18800")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5203820046")
