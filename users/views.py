# -*- coding: utf-8 -*-
from . import user_blue

@user_blue.route('/userinfo')
def user_info():
    return 'user  info'