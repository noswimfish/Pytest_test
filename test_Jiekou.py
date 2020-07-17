# coding=utf-8
import pytest
from testPost import Post
import logging,sys
from testData import OperData

log = logging.getLogger(__name__)

class Test_Post():

    od=OperData()
    td=Post()

    @pytest.mark.skip(reason="不执行")
    def setup_function(self):

        self.od.del_data()

    @pytest.mark.skip(reason="不执行")
    def test_data1(self):

        response= self.td.test()
        dict = response.json()# 重点把json转化为字典
        #log.info(dict)
        try:
            log.info(dict['code'])
            assert dict['code'] == '0001'
            log.info('LoginRequest：接口执行成功')
        except Exception as e:
            log.info('LoginRequest：接口执行失败')
            raise e

    def test_data2(self):

        result=self.od.que_data()
        try:
            log.info(result)
            assert result == 990
            log.info('数据库校验：校验成功')
        except Exception as e:
            log.info('数据库校验：校验失败')
            raise e



if __name__=="__main__":
	pytest.main()







