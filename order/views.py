# -*- coding: utf-8 -*-

from . import orderblue

@orderblue.route('/order')
def order():
    return "orderinfo"