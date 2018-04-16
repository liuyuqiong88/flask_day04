# -*- coding: utf-8 -*-
from . import cart_blue


@cart_blue.route('/cart')
def cart_info():

    return "cart info"