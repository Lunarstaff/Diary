# 数据库使用记录

我虚拟机里的Centos6.5，安装的mysql，root用户没有密码。
使用root用户登录：

```sql
[root@Lunar12 ~]# mysql -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 5.0.37-community-log MySQL Community Edition (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>

```

## 查询mysql版本信息

这一看还是5.0版本，太老旧了，打算把数据库升级。

```shell
[root@Lunar12 ~]# mysql -V
mysql  Ver 14.12 Distrib 5.0.37, for pc-linux-gnu (i686) using readline 5.0
```

## 升级MySQL
### 1、旧数据库数据备份

使用`mysqldump`命令把原数据库里的数据备份一下，保存成xxx.sql文件，以便升级后恢复数据。

```sql
-- mysqldump命令使用方法
mysqldump -u[用户名] -h[主机ip] -P[端口号] -p[用户密码] --all-databases > databases.sql（备份文件名）

-- 在sql客户端执行以下命令进行备份
mysqldump -u root -h 192.168.0.198 -P 3306 -p --all-databases > databases.sql

```
### 2、停止MySQL服务
```shell
[root@Lunar12 ~]# service mysql stop
Shutting down MySQL.                                       [确定]
```

### 3、卸载旧版本Mysql
```
yum remove mysql mysql-*

[root@Lunar12 ~]# yum remove mysql mysql-*
Loaded plugins: fastestmirror, security
Setting up Remove Process
No Match for argument: mysql-*
Determining fastest mirrors
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base                                                                                             | 3.7 kB     00:00
extras                                                                                           | 3.3 kB     00:00
Traceback (most recent call last):
  File "/usr/lib/python2.6/site-packages/urlgrabber/grabber.py", line 1118, in _hdr_retrieve
    self.size = int(length)
ValueError: invalid literal for int() with base 10: 'Location, Content-Length\r\n'
http://mirrors.aliyun.com/centos/6/extras/i386/repodata/4ed9c3c29ec1efb3a627dee58ae2c362c91cb83ea5a3d7ecbe58dba26ae8accf-primary.sqlite.bz2: [Errno 14] PYCURL ERROR 23 - "Failed writing header"
Trying other mirror.
http://mirrors.aliyuncs.com/centos/6/extras/i386/repodata/4ed9c3c29ec1efb3a627dee58ae2c362c91cb83ea5a3d7ecbe58dba26ae8accf-primary.sqlite.bz2: [Errno 12] Timeout on http://mirrors.aliyuncs.com/centos/6/extras/i386/repodata/4ed9c3c29ec1efb3a627dee58ae2c362c91cb83ea5a3d7ecbe58dba26ae8accf-primary.sqlite.bz2: (28, 'connect() timed out!')
Trying other mirror.
updates                                                                                          | 3.4 kB     00:00
Traceback (most recent call last):
  File "/usr/lib/python2.6/site-packages/urlgrabber/grabber.py", line 1118, in _hdr_retrieve
    self.size = int(length)
ValueError: invalid literal for int() with base 10: 'Location, Content-Length\r\n'
http://mirrors.aliyun.com/centos/6/updates/i386/repodata/2ef6a50242309ac12d7784ab4037de493a08a734ff85b0cea5a749288fbb8af3-primary.sqlite.bz2: [Errno 14] PYCURL ERROR 23 - "Failed writing header"
Trying other mirror.
http://mirrors.aliyuncs.com/centos/6/updates/i386/repodata/2ef6a50242309ac12d7784ab4037de493a08a734ff85b0cea5a749288fbb8af3-primary.sqlite.bz2: [Errno 12] Timeout on http://mirrors.aliyuncs.com/centos/6/updates/i386/repodata/2ef6a50242309ac12d7784ab4037de493a08a734ff85b0cea5a749288fbb8af3-primary.sqlite.bz2: (28, 'connect() timed out!')
Trying other mirror.
Package(s) mysql-* available, but not installed.
Resolving Dependencies
--> Running transaction check
---> Package MySQL-server-community.i386 0:5.0.37-0.rhel4 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

========================================================================================================================
 Package                               Arch                Version                       Repository                Size
========================================================================================================================
Removing:
 MySQL-server-community                i386                5.0.37-0.rhel4                installed                 29 M

Transaction Summary
========================================================================================================================
Remove        1 Package(s)

Installed size: 29 M
Is this ok [y/N]: y
Downloading Packages:
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
Warning: RPMDB altered outside of yum.
** Found 9 pre-existing rpmdb problem(s), 'yum check' output follows:
mod_perl-2.0.4-10.el6.i686 has missing requires of httpd-mmn = ('0', '20051115', None)
1:mod_ssl-2.2.15-29.el6.centos.i686 has missing requires of httpd
1:mod_ssl-2.2.15-29.el6.centos.i686 has missing requires of httpd = ('0', '2.2.15', '29.el6.centos')
1:mod_ssl-2.2.15-29.el6.centos.i686 has missing requires of httpd-mmn = ('0', '20051115', None)
mod_wsgi-3.2-3.el6.i686 has missing requires of httpd-mmn = ('0', '20051115', None)
2:postfix-2.6.6-2.2.el6_1.i686 has missing requires of libmysqlclient.so.16
2:postfix-2.6.6-2.2.el6_1.i686 has missing requires of libmysqlclient.so.16(libmysqlclient_16)
2:postfix-2.6.6-2.2.el6_1.i686 has missing requires of mysql-libs
webalizer-2.21_02-3.3.el6.i686 has missing requires of httpd
  Erasing    : MySQL-server-community-5.0.37-0.rhel4.i386                                                           1/1
  Verifying  : MySQL-server-community-5.0.37-0.rhel4.i386                                                           1/1

Removed:
  MySQL-server-community.i386 0:5.0.37-0.rhel4

Complete!
```

### 4、 检查是否卸载干净
移除命令执行后，可再看看是否有残余的mysql，输入命令：
```shell
[root@Lunar12 ~]# rpm -qa | grep mysql
[root@Lunar12 ~]#
或
yum list installed | grep mysql
```

还可以使用`rpm -e`来擦除应用信息（下文会涉及到）。

### 5、下载新的安装包

```shell
wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-community-server-8.0.20-1.el6.i686.rpm
·
·
·
100%[==============================================================================>] 560,672,772 2.47M/s   in 4m 18s

2020-06-20 05:30:56 (2.08 MB/s) - 已保存 “mysql-community-server-8.0.20-1.el6.i686.rpm” [560672772/560672772])

```

### 6、安装
```
[root@Lunar12 Download]# rpm -ivh mysql-community-server-8.0.20-1.el6.i686.rpm
```

注意提示，应该要先安装 mysql-community-libs、mysql-community-common、mysql-community-client才能 再安装mysql-community-server。
如果在安装client的时候提示有版本冲突，执行一下擦除：
```shell
[root@Lunar12 ~]# rpm -e --nodeps mysql
```

### 7、检查MySQL的安装状态
1、给mysql用户赋权
```
chown mysql:mysql -R /var/lib/mysql
```
初始化MySQL
```
[root@Lunar12 lib]# mysqld --initialize
```
初始化时报错：`--initialize specified but the data directory has files in it. Aborting.`说明mysql中的data目录已经有数据了。
- 1、在mysql配置文件中查看数据文件路径
```
[root@Lunar12 etc]# less /etc/my.cnf
# 文件中下面这里表示数据路径
datadir=/var/lib/mysql
```
- 2、在数据文件路径把数据文件备份，转移
```shell
[root@Lunar12 lib]# mv /var/lib/mysql /var/lib/mysql0620
```
- 3、再次启动MySQL
```shell
[root@Lunar12 lib]# service mysqld start
初始化 MySQL 数据库：                                      [确定]
正在启动 mysqld：                                          [确定]
```
- 4、查看MySQL版本
```shell
[root@Lunar12 lib]# mysql -V
mysql  Ver 8.0.20 for Linux on i686 (MySQL Community Server - GPL)
[root@Lunar12 lib]# mysqladmin --version
mysqladmin  Ver 8.0.20 for Linux on i686 (MySQL Community Server - GPL)
```

### 8、检查MySQL配置文件
- 1、找到mysqld（启劝程序）的路径：
```
[root@Lunar12 sbin]# which mysqld
/usr/sbin/mysqld
```
- 2、查看mysqld启动程序使用的配置文件路径
```
[root@Lunar12 ~]# /usr/sbin/mysqld --verbose --help |grep -A 1 'Default options'
Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf
```


### 9、MySQL日志
```
[root@Lunar12 log]# pwd
/var/log
[root@Lunar12 log]# less mysqld.log
```




### 10、mysq启动和关闭
1. mysql服务关闭：
- 找到`/usr/bin`目录下的`mysqladmin`，使用`shutdown`命令关闭mysql服务。
```shell
[root@Lunar12 bin]# ./mysqladmin shutdown
```
- 使用`service`服务关闭
```shell
[root@Lunar12 bin]# service mysql stop
Shutting down MySQL..                                      [确定]
```
2. 检查mysql服务的状态：
```shell
[root@Lunar12 bin]# ./mysqladmin status
./mysqladmin: connect to server at 'localhost' failed
error: 'Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)'
Check that mysqld is running and that the socket: '/tmp/mysql.sock' exists!
```
3. mysql服务启动：
- 使用`mysqld_safe`启动
```shell
[root@Lunar12 bin]# mysqld_safe
[1] 2598
Starting mysqld daemon with databases from /var/lib/mysql
```
- 使用`service`服务启动
```shell
[root@Lunar12 bin]# service mysql start
Starting MySQL                                             [确定]
```

### 11、用户管理

- 1、root用户初始密码
MySQL8.0安装启动时会初始化，在初始化时会给root用户一个初始密码，跟之前版本的mysql不一样。可以在启动日志中查找初始密码（在日志文件中查找关键字`root`）：

```
2020-06-19T23:35:49.082504Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.20) initializing of server in progress as process 2489
2020-06-19T23:35:49.106549Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2020-06-19T23:35:50.656310Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2020-06-19T23:35:53.699267Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: vfBaA9lT,uqV
```
使用root用户登录
```
[root@Lunar12 log]# mysql -uroot -pvfBaA9lT,uqV
```

- 2、修改root用户密码
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;
#修改加密规则为永不过期
执行语句时报错（大意是，设置的密码不符合当前的密码规则要求，白话就是密码太弱了）：
```shell
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```
处理方法：
先查看当前密码规则是什么
SHOW VARIABLES LIKE 'validate_password%';
但是执行这条语句时又提示，要先更新root用户的初始密码（醉了~）。
```shell
mysql> SHOW VARIABLES LIKE 'validate_password%';
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
mysql>
```
看来只能先设置一个复杂的密码，修改密码要求规则后再设置一个简单的密码了，我设置简单密码是自己平时测试使用时用起来方便。

重新给root用户设置一个复杂的密码：
```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Pac@2020' PASSWORD EXPIRE NEVER;
Query OK, 0 rows affected (0.03 sec)
```
成功了。
然后再来看密码要求规则：
```shell
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password.check_user_name    | ON     |
| validate_password.dictionary_file    |        |
| validate_password.length             | 8      |
| validate_password.mixed_case_count   | 1      |
| validate_password.number_count       | 1      |
| validate_password.policy             | MEDIUM |
| validate_password.special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.02 sec)
```
mysql 密码要求规则参数说明：
- 1、check_user_name 是否校验用户名（因为后面我想测试用户角色等，所以这里设置为开）
- 2、dictionary_file 指定字典文件路径（用于密码验证）
- 3、length  固定密码的总长度；（这里我设置为6）
- 4、mixed_case_count  整个密码中至少要包含大/小写字母的总个数；
- 5、number_count  整个密码中至少要包含阿拉伯数字的个数；
- 6、policy 指定密码的强度验证等级，默认为 MEDIUM；（这里我设置为0，只校验密码长度）
关于 policy 的取值：
0/LOW：只验证长度；
1/MEDIUM：验证长度、数字、大小写、特殊字符；
2/STRONG：验证长度、数字、大小写、特殊字符、字典文件；
- 7、validate_password_special_char_count 整个密码中至少要包含特殊字符的个数；

执行以下修改语句：
```
mysql> set global validate_password.length=6;
Query OK, 0 rows affected (0.00 sec)

mysql> set global validate_password.policy=LOW;
Query OK, 0 rows affected (0.00 sec)
```
检查修改后的密码规则：
```
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password.check_user_name    | ON    |
| validate_password.dictionary_file    |       |
| validate_password.length             | 6     |
| validate_password.mixed_case_count   | 1     |
| validate_password.number_count       | 1     |
| validate_password.policy             | LOW   |
| validate_password.special_char_count | 1     |
+--------------------------------------+-------+
7 rows in set (0.01 sec)
```
现在可以把root用户密码改成`123456`了：
```
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;
Query OK, 0 rows affected (0.00 sec)
```
刷新权限
```
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)
```

- 3、新增dbadmin用户
```sql
-- 添加dbadmin用户，dbadmin，允许全网段远程访问
create user 'dbadmin'@'%' identified  by 'dbadmin';
-- 给用户赋权
mysql> GRANT ALL ON *.* TO `dbadmin`@`%` WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)
```

- 4、新增dataadmin用户
新增一个dataadmin用户，用来做数据分析


- 5、用户管理的其他语句
    - 1、 查询用户
    ```sql
     select * from user;
    ```
    - 2、删除用户
    ```sql
    mysql> drop user 'teller';
    ERROR 1396 (HY000): Operation DROP USER failed for 'teller'@'%'
    mysql> drop user 'teller'@'192.168.0.105';
    Query OK, 0 rows affected (0.00 sec)
    ```
    - 3、

### 12、配置数据库远程访问
#### 选择远端数据库工具



### 13、创建用于数据分析的数据库  

使用dbadmin用户新增数据库 data_analysis  
```sql
mysql> create database data_analysis;
Query OK, 1 row affected (0.02 sec)
```
创建数据表
```sql
CREATE TABLE IF NOT EXISTS `secretary_info`(
`info_id` INT UNSIGNED,
`province_code` CHAR(10),
`province_name` CHAR(30),
`city_code` CHAR(10),
`city_name` CHAR(30),
`on_year` YEAR,
`secretary_name` CHAR(30),
`birth_year` CHAR(10),
`birth_month` CHAR(10),
`native_province_code` CHAR(10),
`native_province_name` CHAR(30),
`native_city_code` CHAR(10),
`native_city_name` CHAR(30),
`sex` CHAR(5),
`nation` CHAR(30),
`education` CHAR(20),
`is_party_school` CHAR(5),
`speciality_humanities` CHAR(5),
`speciality_social` CHAR(5),
`speciality_technology` CHAR(5),
`speciality_agriculture` CHAR(5),
`speciality_medical` CHAR(5),
`in_party_year` YEAR,
`work_years` TINYINT UNSIGNED,
PRIMARY KEY (`info_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

删除数据表
DROP TABLE table_name ;


插入数据

INSERT INTO runoob_tbl 
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("学习 PHP", "菜鸟教程", NOW());

新增dataadmin用户，给这个用户赋权，只能管理data_analysis数据库
```
-- 添加dataadmin用户，允许全网段远程访问
create user 'dataadmin'@'%' identified  by 'dataadmin';
-- 给用户赋权
mysql> GRANT ALL ON data_analysis.* TO 'dataadmin'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)

FLUSH PRIVILEGES;
```



数据源：

https://opendata.sz.gov.cn/





### 14、Python连接MySQL

安装PyMySQL库

导入

```python
import pymysql
```
建立连接
```python
connection_to_198 = pymysql.connect(
    host='192.168.0.198',
    user='dataadmin',
    password='dataadmin',
    db='data_analysis',
    charset='utf8mb4',  # 数据库连接字符集
    cursorclass=pymysql.cursors.DictCursor  # 这个还要再看下
)
```
执行SQL事务
```python
try:
    with connection_to_198.cursor() as cursor:
        # 插入新记录，SQL语句太长了，才用下面这个方法
        a = "INSERT INTO second_housing_transactions "
        b = "(CJ_AREA, CJ_DATE, CJ_NUM, DISTRICT, ID, PURPOSE) "
        c = "VALUES (%s, %s, %s, %s, %s, %s);"
        sql_insert = a + b + c
        print(sql_insert)
        cursor.execute(sql_insert, ('789.2', '2020-06-25', '9', '龙华', '999', '养殖'))
```
提交事务
```python
    connection_to_198.commit()
```


>查看当前数据库服务支持的字符集：
>`mysql> show character set;`
>查看当前数据库的字符集:
>`mysql> show variables like 'character%';`
>


select station_id, count(*) as test_times from reservoir_record group by station_id ORDER BY test_times desc