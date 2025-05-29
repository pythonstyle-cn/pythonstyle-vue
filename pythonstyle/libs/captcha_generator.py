# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-12
'''
import random
from PIL import Image, ImageDraw, ImageFont
from pythonstyle.app import create_app
app = create_app()

class CaptchaGenerator:
    # 初始化参数
    def __init__(self, width=90, height=35, font_size=22, font_path=None, length=2):
        self.width = width
        self.height = height
        self.font_size = font_size
        if font_path == None:
            self.font_path = app.root_path+'/static/fonts/BoldItalic.otf'
        else:
            self.font_path = font_path
        self.length = length

    # 生成随机数学表达式
    def generate_expression(self):
        operators = ['+', '-', '*']
        expression = ''

        for i in range(0, self.length - 1):
            num = random.randint(1, 10)
            operator = random.choice(operators)
            expression += f'{num}{operator}'
        num = random.randint(1, 10)
        expression += str(num)
        return expression

    # 计算数学表达式的结果
    def calculate_result(self, expression):
        try:
            result = eval(expression)
            return result
        except:
            return None

    # 生成验证码图片
    def generate_captcha(self):
        # 创建画布
        image = Image.new('RGB', (self.width, self.height), color=(181, 217, 253))

        # 获取字体
        font = ImageFont.truetype(self.font_path, self.font_size)

        # 获取绘图对象
        draw = ImageDraw.Draw(image)

        # 绘制数学表达式
        expression = self.generate_expression()
        result = self.calculate_result(expression)
        if result is not None:
            text_width = draw.textlength(text=expression+'=?', font=font)
            text_x = (self.width - text_width) / 2
            draw.text((text_x, 8), expression+'=?', font=font, fill=(5, 90, 174))

            # 添加干扰线和点
            for i in range(0, 5):
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                x2 = random.randint(0, self.width)
                y2 = random.randint(0, self.height)
                draw.line((x1, y1, x2, y2), fill=(5, 90, 174))
                draw.point((random.randint(0, self.width), random.randint(0, self.height)), fill=(5, 90, 174))

        # 返回数学表达式和图片
        return result, image

    # 保存验证码图片
    def save_captcha(self, filename):
        result, image = self.generate_captcha()
        if result is not None:
            image.save(filename)