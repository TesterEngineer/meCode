#-*- coding:utf-8 _*-
"""
@author:Sam
@file: config.py
@time: 2018/07/{DAY}
"""

import  pymysql
from DB_test import  config

#获取连接
conn =pymysql.connect(**config.mysql_connect_info)

#获取游标
cur = conn.cursor()

#对db进行操作

'''
 add delete update select
'''

'''
sql ="insert into t_admin values(%s,%s,%s)"
value=('a41','liu','123')
value1=['b','liu1','123']
cur.execute(sql,value)
conn.commit()
'''
'''
sql ="insert into t_admin values(%s,%s,%s)"

#value=(['b','liu1','123'],['b1','liu2','123'],['b2','liu3','123'],['b3','liu4','123'])

#value=[('b11','liu1','123'),('b1','liu2','123'),('b2','liu3','123')]

value=[['c1','liu1','123'],['c2','liu1','123']]
cur.executemany(sql,value)
conn.commit()
'''

def update_mysql(*args):
    sql = "update t_admin set adminname=%s where adminId=%s"
    cur.executemany(sql,args)
    conn.commit()

def delete_db(*args):
    sql ="delete from t_admin where adminId=%s"
    cur.executemany(sql,args)
    conn.commit()



def select_dir(*args):
    sql = "select * from t_admin where adminname=%(u)s and adminpwd=%(p)s"
    cur.executemany(sql,args)
    return  cur.fetchone()

def select_all():
    sql="select * from t_admin"
    cur.execute(sql)
    result1 = cur.fetchone()
    result2 = cur.fetchmany()
    result = cur.fetchall()
    print("输出的数据是-----》",result)
    return result



## print_args({'u1':'hello','p':'1232'},name="张三")
def print_args(*args,**kwargs):
    print("args====",args)
    print("kwargs=====",kwargs)


'''
sql = "select * from t_admin"

result_data = cur.execute(sql)

print(result_data)
'''
# print(cur.fetchone())
# print(cur.fetchone())
# cur.scroll()

print("-----")
#print(cur.fetchmany(0))
#print(cur.fetchall())









if __name__ == "__main__":
    select_all()
    '''
    value=(['java_name','b'],['hello','b1'])
    for v in value:
        update_mysql(v)

   
    '''
    #delete_db('b2')
    '''
    result = select_dir({'u':'hello','p':'123'})
    print(result)
    # 关闭游标,关闭连接
    cur.close()
    conn.close()
    '''
   # print_args({'u':'hello','p':'123'})
   #print_args({'u1':'hello','p':'1232'},name="张三")
