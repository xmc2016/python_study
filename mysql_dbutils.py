# -*- coding: utf-8 -*-
'''
File Name: mysql_DBUtils.py
Author: minchao.xue
mail: minchao.xue@shuyun.com
Created Time: 2020/10/29 14:34
'''
import pymysql,os,configparser
#DictCursor以字典的形式返回操作结果
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB
# chardet 检测编码
import chardet,json
import numpy as np
#自处理TypeError: Object of type bytes is not JSON serializable 问题
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)

class Config(object):
    """
    [Mysql-Database]
    host=127.0.0.1
    user=root
    password=123456
    db=test_db
    charset=utf8
    """
    def __init__(self,config_filename="config.ini"):
        # 获取文件绝对路径
        file_path=os.path.join(os.path.dirname(__file__),config_filename)
        self.cf=configparser.ConfigParser()
        self.cf.read(file_path)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self,section):
        print(self.cf.options(section))
        return self.cf.options(section)
    # 返回该section 下所有键值
    def get_content(self,section):
        result = {}
        for option in self.get_options(section):
            value = self.cf.get(section,option)
            result[option] = int(value) if value.isdigit() else value
        return result

class BasePymysqlPool(object):
    def __init__(self,host,port,user,password,db_name):
        self.db_host = host
        self.db_port = int(port)
        self.user = user
        self.password = str(password)
        self.db = db_name
        self.cursor = None

class MyPymsqlPool(BasePymysqlPool):
    """
     MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现
    获取连接对象：conn = Mysql.getConn()
    释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None

    def __init__(self,conf_name=None):
        self.conf = Config().get_content(conf_name)
        print(self.conf)
        #super 继承父类,改写__init__方法，增加self.conf 属性
        super(MyPymsqlPool,self).__init__(**self.conf)
        #数据库构造函数,从连接池取出连接,并生成游标操作
        self._conn = self.__getConn()
        self._cursor = self._conn.cursor()

    def __getConn(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if MyPymsqlPool.__pool is None:
            __pool = PooledDB(creator=pymysql,
                             mincached=1,
                             maxcached=20,
                             maxconnections=20,
                             host=self.db_host,
                             user=self.user,
                             passwd=self.password,
                             db=self.db,
                             use_unicode=False,
                             charset="utf8",
                             cursorclass=DictCursor)
            return __pool.connection()

    def getAll(self,sql,param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def getOne(self,sql,param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def insertMany(self,sql,values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql,values)
        return  count

    def __query(self,sql,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count

    def update(self,sql,param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql,param)

    def insert(self,sql,param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql,param)

    def delete(self,sql,param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql,param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self,option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self,isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()


if __name__ == '__main__':
    mysql_conn=MyPymsqlPool("Mysql-Database")
    insert_values=[('标题1','hello'),('标题2','2020-10-29')]
    query_sql = "select * from novel;"
    insert_sql="insert into novel (`title`,`content`) values (%s,%s);"
    result = mysql_conn.getAll(query_sql)
    print(result)
    #cls=MyEncoder 处理返回值带中文情况
    json_str = json.dumps(result,cls=MyEncoder,ensure_ascii=False)
    print(json_str)
    mysql_conn.dispose()
