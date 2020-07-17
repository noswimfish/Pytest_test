# coding=utf-8
import requests
from ExcelControl import ExcelControl




class Post(ExcelControl):


    def test(self):
        self.open_excel(u'C:/Users/0219046/Desktop/世联集.xlsx',1)
        url=self.read_excel_sheet_value_with_key_name('Sheet1','接口1','地址')
        body=self.read_excel_sheet_value_with_key_name('Sheet1','接口1','参数')
        #print self.url,self.body
        header = "{'Coresponse.contentntent-type': 'application/json'}"
        response = requests.post(url, header, body)
        return response

    #接口2，请求参数为上一个接口的响应
    def test2(self):
        response=self.test()
        dict = response.json()
        brandTeamId = dict['rows'][0]['brandTeamId']
        body2 = {"build": brandTeamId}
        print (body2)

        self.open_excel(u'C:/Users/0219046/Desktop/世联集.xlsx',1)
        url=self.read_excel_sheet_value_with_key_name('Sheet1','接口1','地址')
        header = "{'Coresponse.contentntent-type': 'application/json'}"
        response = requests.post(url, header, body2)
        return response







