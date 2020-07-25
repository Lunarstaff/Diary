# py_to_mysql.py

# 导入
import pymysql.cursors

# 建立连接
connection_to_198 = pymysql.connect(
    host='192.168.0.198',
    user='dataadmin',
    password='dataadmin',
    db='data_analysis',     # 数据库
    charset='utf8mb4',      # 数据库连接字符集
    cursorclass=pymysql.cursors.DictCursor  # 这个还要再看下
)

# 执行SQL事务
try:
    with connection_to_198.cursor() as cursor:
        # 插入新记录
        a = "INSERT INTO second_housing_transactions "
        b = "(CJ_AREA, CJ_DATE, CJ_NUM, DISTRICT, ID, PURPOSE) "
        c = "VALUES (%s, %s, %s, %s, %s, %s);"
        sql_insert = a + b + c
        print(sql_insert)
        cursor.execute(sql_insert, ('789.2', '2020-06-25', '9', '龙华', '999', '养殖'))
    # 提交事务
    connection_to_198.commit()

    with connection_to_198.cursor() as cursor:
        # Read a single record
        sql_query = "select * from second_housing_transactions WHERE `PURPOSE`=%s;"
        cursor.execute(sql_query, ('养殖',))
        result = cursor.fetchone()
        print(result)
finally:
    connection_to_198.close()

