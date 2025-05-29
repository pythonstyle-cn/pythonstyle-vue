# -*- coding: utf-8 -*-
'''
    描述：验证码控制器
    作者: chinacsj@139.com
    日期: 2024-02-18
'''
from pythonstyle.common import utils
from pythonstyle.libs.result import Result
from pythonstyle.libs.redis import Redis
from pythonstyle.libs.captcha_generator import CaptchaGenerator
import logging
from pythonstyle.app import create_app
app = create_app()

logging.basicConfig(
        level=logging.DEBUG,  # 设置最低日志级别为DEBUG，显示所有日志级别的信息
        format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志显示的格式
        datefmt='%Y-%m-%d %H:%M:%S')  # 设置日期时间格式

class captcha(Result):
    def captcha_image(self):
        check_code_header =  utils.getHttpHeaders('Browser')

        if check_code_header != 'EQVR4n':
            return Result.error(201, msg=f'获取失败:{check_code_header}')
        captchaEnabled = app.config['captchaEnabled']
        if captchaEnabled != True:
            return Result.success(200, msg='操作成功', data={'captchaEnabled':captchaEnabled})
        generator = CaptchaGenerator()

        # 生成验证码图片并计算结果
        result, image = generator.generate_captcha()
        # 保存图片
        captcha_path = app.root_path+'/static/images/captcha.png'
        image.save(captcha_path)
        #生成uuid
        code_uuid = str(utils.get_uuid())
        verifyKey = 'captcha_code:'+ code_uuid
        #将图片转换成base64
        img = utils.image_to_base64(captcha_path)

        data = {
            'img':img,
            'uuid':code_uuid,
            'captchaEnabled':captchaEnabled
        }

        #将验证码缓存到redis 缓存时间2分钟
        try:
            Redis().set(verifyKey, result, 120)
        except Exception as error:
            logging.info(f"captcha:{verifyKey}，{result},{error}")
        return Result.success(200, msg='操作成功', data=data)
