# -*- coding: utf-8 -*-

import pymysql

class execute():

    def __init__(self,host,user,password,port,db):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.db=db

    #host = '192.168.16.42', user = 'customer', password = 'customer_test', port = 3322, db = 'customer'
    #获取数据库的数据
    def execute_data(self,sql):

        db = pymysql.connect(host=self.host,user=self.user,password=self.password,port=self.port,db=self.db)
        cursor = db.cursor()
        # 基本的sql插入語句

        print ('正在执行sql语句........')
        try:
            # 执行语句
            cursor.execute(sql)
            # 这里一定要用到commit()提交 不然完成不了信息的保存
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        # 关闭数据库
        cursor.close()
        db.close()
        #print cursor.fetchall()
        return(cursor.fetchall())



