import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_health_check(self):
        self.assertEqual(main.heath_check(), {'success': True})


if __name__ == '__main__':
    unittest.main()
