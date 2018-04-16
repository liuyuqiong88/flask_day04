# -*- coding: utf-8 -*-

from . import chat_blue

@chat_blue.route('/chatinfo')
def chatinfo():
    return 'chat info'