# coding=utf-8
"""
日志函数
"""
import time


class FileLog(object):

    def __init__(self, file_name):
        self.fp = open(file_name, "w")

    def log(self, log_str, *log_args):
        log_info = log_str % log_args
        self.fp.write(log_info + "\n")

    def get_time(self):
        return time.strftime('[%Y-%m-%d] %H:%M:%S ', time.localtime(time.time()))

    def log_time(self, log_str, *log_args):
        log_info = self.get_time() + log_str % log_args
        self.fp.write(log_info + "\n")

    def log_finish(self):
        self.fp.close()
        self.fp = None

    def __call__(self, *args, **kwargs):
        self.log_time(*args)


def std_log(log_str, *log_args):
    print(log_str % log_args)


def file_log(file_name):
    return FileLog(file_name)
