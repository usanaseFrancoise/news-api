# import unittest
# from flask import current_app
# from app import create_app

# class BasicsTestCase(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app('development')
#         self.app_context = self.app.app_context()
#         self.app_context.push()

#     def tearDown(self):

#         self.app_context.pop()

#     def test_app_exists(self):
#         self.assertFalse(current_app is None)