# -*- coding: utf-8 -*-
'''
    描述：文件上传类
    作者: chinacsj@139.com
    日期: 2024-07-16
'''
import os
import hashlib
import time
import math
from datetime import datetime
import requests
from pythonstyle.libs.logger import Logger
from pythonstyle.app import create_app
app = create_app()

class FileUpload:
    def __init__(self, upload_folder = None):
        """
        初始化文件上传类。
        :param upload_folder: 上传目录的路径，如果没有指定，则使用默认的/static/uploadfiles。
        """
        self.default_upload_folder = f"/static/uploadfiles/{datetime.now().strftime('%Y/%m%d')}"
        self.allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'mkv', 'zip', 'rar', 'tar', 'gz', 'txt', 'xls', 'xlsx', 'doc', 'docx'}
        self.max_chunk_size = 2 * 1024 * 1024  # 设置为5MB

        self.upload_folder = app.root_path + self.default_upload_folder

        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)


    def set_allowed_extensions(self, extensions):
        """
        设置允许上传的文件扩展名。
        :param extensions: 允许的文件扩展名集合。
        """
        self.allowed_extensions = set(extensions)

    def set_max_chunk_size(self, size):
        """
        设置文件分片的最大大小。
        :param size: 文件分片的最大大小（字节）。
        """
        self.max_chunk_size = size

    def allowed_file(self, filename):
        """
        检查文件是否是允许的类型。
        :param filename: 文件名。
        :return: 如果文件类型被允许，则返回True，否则返回False。
        """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def secure_filename(self, filename):
        """
        生成安全的文件名。
        :param filename: 原始文件名。
        :return: 安全的文件名。
        """
        # 使用当前时间戳和文件名生成哈希值
        timestamp = str(time.time()).encode('utf-8')
        filename_bytes = filename.encode('utf-8')
        hash_object = hashlib.sha256(timestamp + filename_bytes)
        hashed_filename = hash_object.hexdigest()
        # 保留原始文件扩展名
        extension = filename.rsplit('.', 1)[1].lower()
        return f"{hashed_filename}.{extension}"

    def save_chunk(self, chunk, filepath, mode='ab'):
        """
        保存文件分片。
        :param chunk: 文件分片数据。
        :param filepath: 保存路径。
        :param mode: 文件打开模式，默认追加模式。
        """
        with open(filepath, mode) as f:
            f.write(chunk)

    def handle_upload(self, file):
        """
        处理文件上传。
        如果文件大小超过设定的分片阈值，则启用分片上传。
        :param file: 文件对象。
        :return: 文件保存路径，如果上传失败则返回None。
        """
        if file and self.allowed_file(file.filename):
            filename = file.filename
            secure_name = self.secure_filename(filename)
            filepath = os.path.join(self.upload_folder, secure_name)
            result_filepath = os.path.join(self.default_upload_folder, secure_name)
            # 检查文件大小
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)

            if file_size > self.max_chunk_size:
                # 超过分片阈值，启用分片上传
                identifier = secure_name
                chunk_number = 0
                # 计算文件总分片数
                file_total = self.calculate_number_of_chunks(file_size)
                while chunk := file.read(self.max_chunk_size):
                    self.handle_large_upload(chunk, identifier, chunk_number)
                    chunk_number += 1
                if file_total == chunk_number:
                    filepath = self.merge_chunks(identifier,filename)
                    return filepath
                else:
                    return None
            else:
                # 直接上传整个文件
                file.save(filepath)
                return result_filepath
        return None

    def handle_large_upload(self, chunk, identifier, chunk_number):
        """
        处理大文件分片上传。
        :param chunk: 文件分片数据。
        :param identifier: 上传标识符。
        :param chunk_number: 分片序号。
        :return: 分片保存路径，如果上传失败则返回None。
        """
        chunk_filename = f"{identifier}_chunk_{chunk_number}"
        filepath = os.path.join(self.upload_folder, chunk_filename)
        self.save_chunk(chunk, filepath)
        return filepath

    def merge_chunks(self, identifier, filename):
        """
        合并文件分片。
        :param identifier: 上传标识符。
        :param filename: 最终文件名。
        :return: 合并后的文件路径。
        """
        secure_name = self.secure_filename(filename)
        filepath = os.path.join(self.upload_folder, secure_name)
        result_filepath = os.path.join(self.default_upload_folder, secure_name)
        with open(filepath, 'wb') as output_file:
            chunk_number = 0
            while True:
                chunk_filename = os.path.join(self.upload_folder, f"{identifier}_chunk_{chunk_number}")
                if not os.path.exists(chunk_filename):
                    break
                with open(chunk_filename, 'rb') as chunk_file:
                    output_file.write(chunk_file.read())
                os.remove(chunk_filename)
                chunk_number += 1
        return result_filepath

    def calculate_number_of_chunks(self, file_size):
        # 计算总共需要分多少片
        total_chunks = math.ceil(file_size / self.max_chunk_size)
        return total_chunks

    def handle_multi_upload(self, files):
        """
        处理多文件上传。
        :param files: 文件对象列表。
        :return: 文件保存路径列表。
        """
        filepaths = []
        for file in files:
            filepath = self.handle_upload(file)
            if filepath:
                filepaths.append(filepath)
        return filepaths

    def download_file(self, filename):
        """
        下载文件。
        :param filename: 文件名。
        :return: 文件的流式响应，如果文件不存在则返回404。
        """
        secure_name = self.secure_filename(filename)
        filepath = os.path.join(self.upload_folder, secure_name)
        if os.path.exists(filepath):
            return self.stream_file(filepath, filename)
        return False

    def stream_file(self, filepath, original_filename):
        """
        流式传输文件以实现进度条。
        :param filepath: 文件的路径。
        :param original_filename: 原始文件名。
        :return: 文件的流式响应。
        """

        def generate():
            with open(filepath, 'rb') as f:
                while chunk := f.read(2048):
                    yield chunk

        return Response(generate(), headers={
            'Content-Disposition': f'attachment; filename={original_filename}',
            'Content-Type': 'application/octet-stream'
        })

    def download_image(self, image_url):
        """
        下载远程图片并保存到本地目录。
        :param image_url: 图片的URL。
        :return: 保存图片的本地路径。
        """

        try:
            # 发送HTTP GET请求获取图片

            response = requests.get(image_url, stream=True)
            response.raise_for_status()  # 如果请求失败，抛出异常

            # 获取图片的文件扩展名
            file_extension = image_url.rsplit('.', 1)[1].lower()
            if file_extension not in self.allowed_extensions:
                raise ValueError(f"不支持的文件类型: {file_extension}")

            # 获取图片的文件名并生成一个安全的文件名
            local_filename = self.secure_filename(image_url.split('/')[-1])

            # 保存图片到本地
            local_path = os.path.join(self.upload_folder, local_filename)
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    if chunk:
                        f.write(chunk)
            result_path = os.path.join(self.default_upload_folder, local_filename)
            return result_path
        except requests.exceptions.RequestException as e:
            print(f"下载图片时发生错误: {e}")
            return None
        except Exception as e:
            print(f"保存图片时发生错误: {e}")
            return None

