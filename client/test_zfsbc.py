import unittest

import zfsbc

class TestZfsBackupClient(unittest.TestCase):

    def test_get_ssh_client(self):
        c = zfsbc._get_ssh_client('leon-desktop', 'leon', 22)
        stdin, stdout, stderr = c.exec_command('pwd')
        self.assertEqual(stdout.readlines(), ['/home/leon\n'])
        c.close()

if __name__ == '__main__':
    unittest.main()

