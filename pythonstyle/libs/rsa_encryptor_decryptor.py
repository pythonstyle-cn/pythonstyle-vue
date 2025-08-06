# -*- coding: utf-8 -*-
'''
    描述：RSA 加密解密封装
    作者: chinacsj@139.com
    日期: 2024-08-27
'''

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

class RSAEncryptorDecryptor:
    def __init__(self, key_size=2048):
        """
        初始化 RSAEncryptorDecryptor 类实例。
        :param key_size: RSA 密钥的大小（以位为单位）。默认大小为 2048 位。
        """
        self.key_size = key_size
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """
        生成一个新的 RSA 公钥和私钥对，并将其存储在类的实例中。
        - 私钥保存在 `self.private_key`
        - 公钥保存在 `self.public_key`
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
        )
        self.public_key = self.private_key.public_key()

    def save_keys_to_files(self, private_key_path: str, public_key_path: str):
        """
        将私钥和公钥保存到指定的文件路径。
        :param private_key_path: 私钥保存的文件路径。
        :param public_key_path: 公钥保存的文件路径。
        """
        # 导出私钥和公钥为 PEM 格式
        private_pem = self.get_private_key_pem()
        public_pem = self.get_public_key_pem()

        # 保存私钥
        with open(private_key_path, 'wb') as f:
            f.write(private_pem)

        # 保存公钥
        with open(public_key_path, 'wb') as f:
            f.write(public_pem)

    def load_private_key(self, private_key_pem: bytes):
        """
        从 PEM 编码的字节中加载私钥。
        :param private_key_pem: PEM 格式的私钥字节数据。
        """
        self.private_key = serialization.load_pem_private_key(private_key_pem, password=None)

    def load_public_key(self, public_key_pem: bytes):
        """
        从 PEM 编码的字节中加载公钥。
        :param public_key_pem: PEM 格式的公钥字节数据。
        """
        self.public_key = serialization.load_pem_public_key(public_key_pem)

    def load_keys_from_files(self, private_key_path: str, public_key_path: str):
        """
        从指定路径加载私钥和公钥。
        :param private_key_path: 私钥文件的路径。
        :param public_key_path: 公钥文件的路径。
        """
        # 从文件中加载私钥
        with open(private_key_path, 'rb') as f:
            private_key_pem = f.read()
            self.load_private_key(private_key_pem)

        # 从文件中加载公钥
        with open(public_key_path, 'rb') as f:
            public_key_pem = f.read()
            self.load_public_key(public_key_pem)

    def get_private_key_pem(self) -> bytes:
        """
        获取当前私钥的 PEM 编码字节表示。
        :return: 私钥的 PEM 编码字节数据。
        """
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    def get_public_key_pem(self) -> bytes:
        """
        获取当前公钥的 PEM 编码字节表示。
        :return: 公钥的 PEM 编码字节数据。
        """
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def encrypt(self, message: str) -> bytes:
        """
        使用加载的公钥加密消息。
        :param message: 需要加密的原始消息（字符串格式）。
        :return: 加密后的消息（字节格式）。
        :raises ValueError: 如果未加载公钥则引发异常。
        """
        if not self.public_key:
            raise ValueError("Public key is not loaded.")
        return self.public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt(self, encrypted_message: bytes) -> str:
        """
        使用加载的私钥解密消息。
        :param encrypted_message: 加密后的消息（字节格式）。
        :return: 解密后的原始消息（字符串格式）。
        :raises ValueError: 如果未加载私钥则引发异常。
        """
        if not self.private_key:
            raise ValueError("Private key is not loaded.")
        return self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

# # 使用示例
# rsa_cryptor = RSAEncryptorDecryptor()
#
# # 生成密钥对
# rsa_cryptor.generate_keys()
#
# # 保存密钥到指定路径
# private_key_path = "path/to/your/private_key.pem"
# public_key_path = "path/to/your/public_key.pem"
# rsa_cryptor.save_keys_to_files(private_key_path, public_key_path)
#
# # 从文件加载密钥
# rsa_cryptor.load_keys_from_files(private_key_path, public_key_path)
#
# # 加密
# message = "Hello, World!"
# encrypted_message = rsa_cryptor.encrypt(message)
# print("Encrypted:", encrypted_message.hex())
#
# # 解密
# decrypted_message = rsa_cryptor.decrypt(encrypted_message)
# print("Decrypted:", decrypted_message)
