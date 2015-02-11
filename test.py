#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import app
import freeze


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_app(self):
        self.app.get('/')
        self.app.get('/1/')
        self.app.get('/999/')

    def test_freeze(self):
        freeze.freezer.freeze()


if __name__ == '__main__':
    unittest.main()
