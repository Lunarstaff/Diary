# vipdownload.py

import requests
import os
import time
from multiprocessing import Pool

# 下载指定url的资源保存为二进制格式，文件后缀名为.ts
def download_ts(url_ts):
    # 显示子进程信息
    print("download_ts子进程ID为:{:*>15}".format(os.getpid()))
    response_ts = requests.get(url_ts)
    print("url_ts_code" + response_ts.code())
    save_name = os.getcwd() + "\\" + url_ts[-9: -3] + ".ts"
    with open(save_name, "wb") as fwo:
        fwo.write(response_ts.content)
        fwo.close()


# 循环下载ts文件
def get_ts_N(url_refer, N):
    # 显示主进程信息
    print("get_ts_N 主进程ID为：{:*>15}".format(os.getpid())) 
    for ts_i in range(N):
        ts_url_i = url_refer.format(ts_i)
        # 每开始一个循环就从进程池申请一个进程执行下载方法
        ts_pool.apply_async(download_ts, args=(ts_url_i,))
        print("ts_url_i:\n" + ts_url_i)
    # 调用join()方法会等待所有的子进程执行完毕，调用join()之前必须先调用close(),
    # 调用close()后就不能继续添加新的Process了。
    ts_pool.close()
    ts_pool.join()


# 执行windowns下的copy命令
def connect_ts():
    '''
    copy *.ts /B 18.mp4
    '''
    pass


# 主函数
if __name__ == "__main__":
    moive_url_in_aiqiyi = "https://www.iqiyi.com/v_19rw14hm0g.html"
    # 6位索引使用{}待填充
    url_down_refer = "https://youku.cdn7-okzy.com/20200220/17283_916f0aec/1000k/hls/9c32baea2dd{:0>6}.ts" 
    # 实例化进程池，最大进程数为3
    ts_pool = Pool(3)
    # 显示主进程信息
    print("get_ts_N 主进程ID为：{:*>15}".format(os.getpid())) 
    for ts_i in range(10):
        ts_url_i = url_down_refer.format(ts_i)
        # 每开始一个循环就从进程池申请一个进程执行下载方法
        ts_pool.apply_async(download_ts, args=(ts_url_i,))
        print("ts_url_i:\n" + ts_url_i)
    # 调用join()方法会等待所有的子进程执行完毕，调用join()之前必须先调用close(),
    # 调用close()后就不能继续添加新的Process了。
    ts_pool.close()
    ts_pool.join()