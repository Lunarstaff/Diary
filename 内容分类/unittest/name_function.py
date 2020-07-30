# name_function.py


# 这里就不要纠结中国和欧美的姓名对应关系了，下例中last为姓，first为名，middle为中间名
def get_formatted_name(first, last, middle=""):
    """接受姓和名，返回完整的姓名"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()

# str.title() 怎么用的？
# str.title() 会把字符串中每个单词的首字母改成大写的返回。上例中如果输入中文似乎没什么用了。


"""
help(str.title)
Help on method_descriptor:
title(...)
    S.title() -> str
    
    Return a titlecased version of S, i.e. words start with title case
    characters, all remaining cased characters have lower case.

"""
