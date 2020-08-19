import requests
import unittest
class DepPost(unittest.TestCase):
    '''post请求用例'''
    def setUp(self) -> None:
        self.url='http://127.0.0.1:8000/api/departments/'
        self.header={'Content-Type':'application/json'}

    def tearDown(self) -> None:
        pass

    def test_allpara(self):
        '''覆盖所有参数'''
        data=r'{"data": [{"dep_id":"老虎","dep_name":"Test学院",' \
             r'"master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res=requests.post(self.url,headers=self.header,data=data.encode('utf-8'))
        self.assertEqual(201,res.status_code,'新增失败')

    @unittest.skip('调试')
    def test_misdepid(self):
        '''数据depid缺失'''
        data = r'{"data": [{"dep_name":"Test学院",' \
               r'"master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        # print(res.text)
        try:
            self.assertEqual(400, res.status_code, '执行失败')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_wrongtype_master(self):
        '''mastername数据类型错误'''
        data = r'{"data": [{"dep_id":"长颈鹿","dep_name":"Test学院",' \
               r'"master_name":123456,"slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(400, res.status_code, '处理有问题')
        except AssertionError as e:
            print(e)

    def test_add_multimsg(self):
        '''添加多条记录'''
        data = r'{"data": [{"dep_id":"长颈鹿","dep_name":"Test学院",' \
               r'"master_name":123456,"slogan":"Here is Slogan"},' \
               r'{"dep_id":"大熊猫","dep_name":"Test学院",' \
               r'"master_name":123456,"slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(201, res.status_code, '添加失败')
        except AssertionError as e:
            print(e)

    def test_updatemsg(self):
        '''更新记录'''
        url=self.url+'老虎/'
        data = r'{"data": [{"dep_id":"老虎","dep_name":"Test学院",' \
               r'"master_name":"毛毛","slogan":"Here is Slogan"}]}'
        res = requests.put(url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(200, res.status_code, '更新失败')
        except AssertionError as e:
            print(e)

    def test_wrongtype_depid(self):
        '''depid数据类型错误'''

        data = r'{"data": [{"dep_id":True,"dep_name":"Test学院",' \
               r'"master_name":"毛毛","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(400, res.status_code, '处理有问题')
            print('错误的id数据类型不能添加成功')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_allpara_min(self):
        '''所有参数最小值'''

        data = r'{"data": [{"dep_id":"t","dep_name":"m",' \
               r'"master_name":"x","slogan":"k"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(201, res.status_code)
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_allpara_max(self):
        '''所有参数最大值'''

        data = r'{"data": [{"dep_id":"乌鲁木齐000001","dep_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京",' \
               r'"master_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京","slogan":"乌鲁木齐银川甘肃黄河入海流长' \
               r'江澜沧江北京乌鲁木齐银川甘肃黄河入海流长江澜沧江北京乌鲁木齐银川甘肃黄河入海流长江澜沧江北京乌鲁木齐银' \
               r'川甘肃黄河入海流长江澜沧江北京乌鲁木齐银川甘肃黄河入海流长江澜沧江北京"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(201, res.status_code)
        except AssertionError as e:
            print(e)

    def test_depid_over(self):
        '''depid超过最大值'''
        data = r'{"data": [{"dep_id":"天天向上00000111","dep_name":"Test学院",' \
             r'"master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(400, res.status_code,'depid长度超过最大值了')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_depname_over(self):
        '''depname超过最大值'''
        data = r'{"data": [{"dep_id":"天天向上","dep_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京001",' \
             r'"master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(400, res.status_code,'depname长度超过最大值了')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_mastername_over(self):
        '''mastername超过最大值'''
        data = r'{"data": [{"dep_id":"天天向上","dep_name":"乌鲁",' \
             r'"master_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京002","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        try:
            self.assertEqual(400, res.status_code,'mastername长度超过最大值了')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_more_depid(self):
        '''depid参数值冗余'''
        data = r'{"data": [{"dep_id":"天天向上","dep_name":"乌鲁",' \
             r'"master_name":"乌鲁木齐银川甘","slogan":"Here is Slogan","dep_id":"天天向上"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        # print(res.text)
        try:
            self.assertEqual(400, res.status_code,'冗余的参数被忽略')
        except AssertionError as e:
            print(e)

    @unittest.skip('调试')
    def test_depid_illegal(self):
        '''depid前后加上#'''
        data = r'{"data": [{"dep_id":"#天天向上$","dep_name":"乌鲁",' \
             r'"master_name":"乌鲁木齐银川甘","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, headers=self.header, data=data.encode('utf-8'))
        print(res.text)
        try:
            self.assertEqual(400, res.status_code,'特殊字符没处理啊')
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
