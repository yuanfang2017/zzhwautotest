# -*- coding: utf-8 -*-
import os
import time, logging
_author_ = 'fannie'
_data_ = '2018/3/10 17:36'
# 获取文件路径
cur_path = os.path.dirname(os.path.relpath(__file__))
# 日志的存放路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件，就自动的创建一个新的
if not os.path.exists(log_path): os.mkdir(log_path)


class Log_message():
    # 类的初始化会调用的函数
    def __init__(self):
        self.logname= os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        # 创建一个logger
        self.logger = logging.getLogger()
        # 设置日志的级别
        self.logger.setLevel(logging.DEBUG)
        # 日志的输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写入到日志文件
        fh = logging.FileHandler(self.logname, 'a')
        # 设置日志的级别
        fh.setLevel(logging.DEBUG)
        # 设置日志的输出格式
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        # 添加handler
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 避免日志重复输出
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def debug(self, message):
            self.__console('debug', message)

    def info(self, message):
            self.__console('info', message)

    def warning(self, message):
            self.__console('warning', message)

    def error(self, message):
            self.__console('error', message)


if __name__ == "__main__":
    Log_message = Log_message()
    Log_message.info("---测试开始----")
    Log_message.info("操作步骤1,2,3")
    Log_message.warning("----测试结束----")