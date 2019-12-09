# coding=utf-8
"""
日志函数
"""
import time
import pprint


class FileLog(object):

    def __init__(self, file_name):
        self.start_time = time.time()
        self.fp = open(file_name, "w")

    def log(self, log_str, *log_args):
        log_info = log_str % log_args
        self.fp.write(log_info + "\n")

    @classmethod
    def get_time(cls):
        return time.strftime('[%Y-%m-%d] %H:%M:%S ', time.localtime(time.time()))

    def log_time(self, log_str, *log_args):
        log_info = self.get_time() + (log_str % log_args)
        self.fp.write(log_info + "\n")

    def pp_obj_log(self, obj):
        pprint.pprint(obj, stream=self.fp)

    def pp_str_time_log(self, log_str, *log_args):
        pprint.pprint(self.get_time() + (log_str % log_args), stream=self.fp)

    def log_finish(self):
        self.fp.close()
        self.fp = None

    def log_finish_with_time(self):
        info = "总共耗时: %0.3f s" % (time.time() - self.start_time)
        self.log(info)
        self.log_finish()

    def __call__(self, *args, **kwargs):
        self.log_time(*args)


def std_log(log_str, *log_args):
    print(log_str % log_args)


def file_log(file_name):
    return FileLog(file_name)
