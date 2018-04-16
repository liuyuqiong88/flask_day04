# -*- coding: utf-8 -*-

import unittest

from flask import json

from task.login import *


class TestLogin(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_user_password(self):
        client = app.test_client()
        response = client.post('/',data = {'username':'lala'})
        response_str = response.data
        response_dict = json.loads(response_str)

        code = response_dict.get('code')

        real_code ="-1"

        assert real_code == code , "errcode should be %s,but current_code is %s" %(real_code,code)



    def tearDown(self):
        pass