# -*- coding: utf-8 -*-
'''
    描述：日志封装类
    作者: chinacsj@139.com
    日期: 2024-12-02
'''
import logging

class Logger:
    def __init__(self, name: str = "Logger", log_to_file: bool = False, log_file_name: str = "app_runtime.log"):
        """
        初始化 Logger 类
        :param name: 日志记录器的名称，默认为 "Logger"
        :param log_to_file: 是否将日志记录到文件，默认为 False
        :param log_file_name: 如果 log_to_file 为 True，指定日志文件的名称
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # 设置最低日志级别为 DEBUG

        # 创建日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 控制台输出 Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 如果 log_to_file 为 True，添加文件输出 Handler
        if log_to_file:
            file_handler = logging.FileHandler(log_file_name)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, msg: str):
        """记录调试级别日志"""
        self.logger.debug(msg)

    def info(self, msg: str):
        """记录信息级别日志"""
        self.logger.info(msg)

    def warning(self, msg: str):
        """记录警告级别日志"""
        self.logger.warning(msg)

    def error(self, msg: str):
        """记录错误级别日志"""
        self.logger.error(msg)

    def critical(self, msg: str):
        """记录严重错误级别日志"""
        self.logger.critical(msg)