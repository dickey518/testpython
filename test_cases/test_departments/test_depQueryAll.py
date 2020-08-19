import requests
import unittest
#设计用例
class TestDepQueryAll(unittest.TestCase):
    def test_depquery_all(self):
        url=r'http://127.0.0.1:8000/api/departments/'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depquery_all_byWrongMethod(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        res = requests.post(url)
        self.assertEqual(200, res.status_code)
    if __name__ == '__main__':
        unittest.main()
