# -*- coding: utf-8 -*-
'''
    描述：JWT操作类 一般用于登录，接口统一安全认证，切记不能把敏感数据放入payload
    作者: chinacsj@139.com
    日期: 2024-02-20
'''
import jwt
from datetime import datetime, timedelta
from pythonstyle.libs.result import Result
from pythonstyle.common import utils

class JWTManager(Result):
    def __init__(self, secret_key = 'pythonstyle.com.cn'):
        self.secret_key = utils.md5_encrypt(secret_key)

    def generate_token(self, payload, expiration=timedelta(days=1)):
        '''
        描述：生成token
        @param payload数据载荷 需要验证的数据
        @expiration 过期时间 默认 1小时
        '''
        payload['exp'] = datetime.utcnow() + expiration
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return Result.error(401, "认证失败，请重试")
        except jwt.InvalidTokenError:
            return Result.error(401, "认证失败，请重试")

# # 使用示例
# if __name__ == "__main__":
#     secret_key = 'your_secret_key'
#     jwt_manager = JWTManager(secret_key)
#
#     # 生成 JWT
#     payload = {'user_id': 123, 'username': 'john_doe'}
#     token = jwt_manager.generate_token(payload)
#
#     print("生成的 JWT token:", token)
#
#     # 验证 JWT
#     try:
#         decoded_payload = jwt_manager.verify_token(token)
#         print("解码后的 payload 数据:", decoded_payload)
#     except Exception as e:
#         print(e)
