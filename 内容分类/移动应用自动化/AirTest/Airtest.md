### AirTest 
>官方参考文档  
>[AirtestIDE](http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/)  
>[AirTest](https://airtest.readthedocs.io/zh_CN/latest/index.html)

#### 环境搭建
- Python版本
推荐使用Python在3.2到3.6之间的版本

- 安装airtest和poco框架
在命令行使用`pip install airtest`和`pip install pocoui`安装。如果网络问官方PyPi安装失败请参考[第三方库安装.md](../Python 环境/第三方库安装.md)

#### 脚本编写
- 导入`airtest`的API
    ```python
    from airtest.core.api import *
    ```
- 连接设备  
使用`connect_device`来连接任意Android/iOS设备或者Windows窗口
    ```python
    connect_device("platform://host:port/uuid?param=value&param2=value2")
    '''
    platform: Android/iOS/Windows…
    host: Android平台是adb host，iOS下是iproxy host，其他平台请留空
    port: Android下是adb port，iOS下填写iproxy port，其他平台请留空
    uuid: 目标设备的uuid，例如Android下是序列号，windows下是窗口句柄，iOS是uuid
    param: 设备初始化的配置字段，例如cap_method/ori_method/…
    value: 设备初始化字段的值。
    '''
    ```
- 比如我这边连接一台Android设备
    ```python
    connect_device("Android:///67da04d1")
    ```

- 模拟输入
    - touch
    - swipe
    - text
    - keyevent
    - snapshot
    - wait

