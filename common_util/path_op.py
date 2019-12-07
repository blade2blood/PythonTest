# coding=utf-8
"""
路径操作函数
"""


def add_module_search_path(path):
    """
    添加模块搜索路径
    :param path:
    :return:
    """
    import sys
    sys.path.insert(0, path)


def get_abs_path(path="./"):
    """
    获取绝对路径
    :param path:
    :return:
    """
    import os
    return os.path.abspath(path)


def gen_all_file_name(path_name, need_type=None, join_path=True):
    """
    读取某个路径下所有文件名
    :param join_path: 是否需要和传入路径连接
    :param path_name: 路径名
    :param need_type: 需要的文件类型后缀
    :return:
    """
    import os
    names = os.listdir(path_name)

    for name in names:
        if not os.path.isdir(os.path.join(path_name, name)):
            if need_type and not name.endswith(need_type):
                continue
            yield os.path.join(path_name, name) if join_path else name
