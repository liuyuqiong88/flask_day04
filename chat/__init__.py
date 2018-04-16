# -*- coding: utf-8 -*-

from flask import Blueprint


chat_blue = Blueprint('chat',__name__)

from views import *