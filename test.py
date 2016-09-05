from wigx import Wigx
from pprint import pprint
import unittest


class MyTestCase(unittest.TestCase):
    url = "http://www.youdao.com/"

    def setUp(self):
        self.wigx = Wigx(self.url)

    def test(self):
        resp = self.wigx.get_result()
        pprint(resp)

if __name__ == '__main__':
    unittest.main()