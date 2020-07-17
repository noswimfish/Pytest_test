# -*- coding: utf-8 -*-

import pymysql
from dboperation import execute

class OperData():

    exe=execute('192.168.16.42','customer','customer_test',3322,'customer')

    def del_data(self):
       self.exe.execute_data('')


    def que_data(self):
        query=self.exe.execute_data('select * from `t_cus_clue` limit 1 ')
        print (query[0][0])
        return query[0][0]






