# author__ = 'wang'
# -*- coding: utf-8 -*-


from Config import config
import pymysql


# 定义一个执行数据库的方法
def exec_sql(sql, db=None):
    try:
        if db:
            conn = pymysql.connect(host=config.host, user=config.user, passwd=config.psw, port=config.port, db=db)
        else:
            conn = pymysql.connect(host=config.host, user=config.user, passwd=config.psw, port=config.port, db=config.db_name)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        r = cur.fetchall()
        cur.close()
        conn.close()
        return r
    except Exception as e:
        print('Mysql Error %d: %s' % (e.args[0], e.args[1]))
