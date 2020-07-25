# ndarray_001.py

import numpy as np

x1 = np.arange(1, 11, 2)    # 初始值、终值、步长
x2 = np.linspace(1, 9, 5)   # 初始值、终值、元素个数
print(x1)
print(x1.dtype)
print(x2)
print(x2.dtype)







# # 自定义数据类型
# personType = np.dtype(
#     {
#         'names':['name', 'age', 'chinese', 'math', 'english'],
#         'formats':['S32', 'i', 'i', 'i', 'f']
#     }
# )
# # 创建上面数据类型的数组
# peoples = np.array(
#     [
#         ("ZhangFei", 32, 75, 100, 90),
#         ("GuanYu", 24, 85, 96, 88.5),
#         ("ZhaoYun", 28, 85, 92, 96.5),
#         ("HuangZhong", 29, 65, 85, 100)
#     ],
#     dtype=personType
# )
#
# # 获取数组中的数据
# ages = peoples[:]['age']
# chineses = peoples[:]['chinese']
# maths = peoples[:]['math']
# englishs = peoples[:]['english']
# # 输出每科成绩的平均值
# print("age的平均值是{}".format(np.mean(ages)))
# print("chineses的平均值是{}".format(np.mean(chineses)))
# print("maths的平均值是{}".format(np.mean(maths)))
# print("ehglishs的平均值是{}".format(np.mean(englishs)))


# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b[1,2] = 99
# print(a.shape)  # 数组a的形状
# print(b.shape)  # 数组b的形状
# print(a.dtype)  # 数组a中元素的类型
# print(b)        # 打印输出数组b
