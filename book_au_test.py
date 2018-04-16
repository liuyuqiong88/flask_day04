# -*- coding: utf-8 -*-

import unittest
from book_au import *

class BookUnittest(unittest.TestCase):

    def setUp(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/flask_unittest'

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # 开启测试模式
        app.testing = True
        self.client = app.test_client()

        db.drop_all()
        db.create_all()

    def test_mysql_add(self):
        """测试添加数据库是否ok,
        测试逻辑：添加新的数据到数据库，然后查询出来，如果查询不出来说明逻辑错误"""
        new_author = Author(name = "琼琼")
        db.session.add(new_author)
        db.session.commit()

        author = Author.query.filter(Author.name== '琼琼').first()

        self.assertIsNotNone(author,"suthor is None")

    def tearDown(self):
        db.session.remove()
        db.drop_all()