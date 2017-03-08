import unittest


import client
from client import notifications
from client.notifications import Notifications

class TestNotifications(unittest.TestCase):

    def test_dict(self):
        n = Notifications('unittest_test_dict')
        n['test'] = 'my test'
        self.assertTrue('test' in n)
        self.assertEqual(n['test'], 'my test')

    def test_create(self):
        n = Notifications('unittest_test_create')
        n.create(
            'mynotificaction', 
            'unittest_test_create', 
            'This is a test notification. It shows up because you ran a unit test.'
        )
        n.show('mynotificaction')

    def test_create_callback(self):
        n = Notifications('unittest_test_create')
        n.create(
            'mynotificaction', 
            'unittest_test_create', 
            'This is a test notification. It shows up because you ran a unit test.'
        )
        
        

if __name__ == '__main__':
    unittest.main()

