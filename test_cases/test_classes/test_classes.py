import requests
import unittest
class ClassesGet(unittest.TestCase):
    def setUp(self) -> None:
        self.url='http://127.0.0.1:8000/api/departments/T01/classes/'
    def tearDown(self) -> None:
        pass
    def get_classes(self):
        res=requests.get(self.url)
        try:
            self.assertEqual(200,res.status_code)
        except AssertionError as e:
            print(e)
        print('ok')

if __name__ == '__main__':
    unittest.main(verbosity=2)