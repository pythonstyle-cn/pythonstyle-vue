# -*- coding: utf-8 -*-
'''
    描述：该文件是一个公共函数库
    作者: chinacsj
    日期: 2024-01-30
'''
import uuid, base64, hashlib, math
from datetime import datetime
from flask import request,make_response,jsonify,session
from pythonstyle.libs.result import Result
import logging
logging.basicConfig(
        level=logging.DEBUG,  # 设置最低日志级别为DEBUG，显示所有日志级别的信息
        format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志显示的格式
        datefmt='%Y-%m-%d %H:%M:%S')  # 设置日期时间格式

def strToUper(string):
    '''
    描述：将字符串转换成大写字母
    :param string:
    :return:
    '''
    return str(string).upper()

def strTolower(string):
    '''
    描述：将字符串转换成大写字母
    :param string:
    :return:
    '''
    return str(string).lower()

def capitalize(string):
    '''
    描述：将字符串首字母大写
    :param string:
    :return:
    '''
    return str(string).capitalize()

def getRequest(name, request = request):
    '''
    描述：获取GET请求单个参数
    :param name:
    :param request:flask的模块
    :return:参数 param
    '''
    param = filter_xss(request.args.get(filter_xss(name)))
    return param

def getPage(name = 'page', request = request):
    '''
    描述：获取分页标识数据
    :param name: 传过来的page分页标识 默认page
    :param request: request
    :return: （int）page 默认 1
    '''
    page = 1
    if request.args.get(name) != None and request.args.get(name) != '':
        page = int(request.args.get(filter_xss(name)))
    return page

def getPageSize(name = 'page', request = request):
    '''
    描述：获取分页标识数据
    :param name: 传过来的page分页标识 默认page
    :param request: request
    :return: （int）page 默认 1
    '''
    pagesize = 20
    if request.args.get(name) != None and request.args.get(name) != '':
        pagesize = int(request.args.get(filter_xss(name)))
    return pagesize

def getHttpHeaders(name, request = request):
    '''
    描述：获取请求的单个头部信息
    :param name:头部参数
    :param request:flask的模块
    :return:headers 头信息
    '''
    try:
        headers = request.headers[name]
        return headers
    except Exception as error:
        logging.info(f'headers:{error}')


def getHttpAllHeaders(request = request):
    '''
    描述：获取请求的单个头部信息
    :param name:头部参数
    :param request:flask的模块
    :return:headers 头信息
    '''
    headers = request.headers
    return headers

def postRequest(name, request = request):
    '''
    描述：获取POST请求表单参数
    :param name:
    :param request:flask的模块
    :return:param
    '''
    param = filter_xss(request.form.get(name))
    return param

def getRequestJson(request = request):
    '''
    描述：获取get请求单个参数
    :param name:
    :param request:flask的模块
    :return:param
    '''
    # 获取发送过来的 JSON 数据
    data = {}
    if request.args.to_dict():
        data = request.args.to_dict()
    return data

def postRequestJson(request = request):
    '''
    描述：获取POST请求单个参数
    :param name:
    :param request:flask的模块
    :return:param
    '''
    data = {}
    if request.get_json():
        data = request.get_json()
    return data

def getFiles(name,request=request):
    '''
    描述：获取单个上传文件
    :param name:
    :param request:flask的模块
    :return:param
    '''
    data = {}
    if request.files[str(name)]:
        data = request.files[str(name)]
    return data

def getMultFiles(name,request=request):
    '''
    描述：获取多个上传文件
    :param name:
    :param request:flask的模块
    :return:param
    '''
    data = {}
    if request.files.getlist(str(name)):
        data = request.files.getlist(str(name))
    return data

def sendFiles(filepath, filename):
    '''
    描述：根据提供的文件路劲下载文件
    :param filepath:
    :return:
    '''
    return send_file(filepath, as_attachment=True, download_name=filename,mimetype='application/zip')

def isPost(request = request):
    '''
    描述：判断是否是POST提交数据
    :return:bool
    '''
    method_type = request.method == 'POST'
    return method_type

def isGet(request = request):
    '''
    描述：判断是否是 GET 提交数据
    :return:bool
    '''
    method_type = request.method == 'GET'
    return method_type

def isDelete(request = request):
    '''
    描述：判断是否是 DELETE 提交数据
    :return:bool
    '''
    method_type = request.method == 'DELETE'
    return method_type

def isPut(request = request):
    '''
    描述：判断是否是 PUT 提交数据
    :return:bool
    '''
    method_type = request.method == 'PUT'
    return method_type

def setResponse(data, code=200, headers={}, jsonify = jsonify):
    '''
    描述：设置GET请求响应参数
    :param response:Response
    :return:参数 param
    '''
    data = jsonify(data)
    response = make_response(data)
    response.status_code = code
    response.headers = headers

    return response

def http_uri():
    '''
    描述：获取请求的完整URL
    :return:
    '''
    url = request.url
    return url

def filter_xss(data):
    '''
    描述：过滤 POST/GET 参数中的 XSS 攻击
    :param data:
    :return:过滤后的 data
    '''

    if data != None:
        if type(data) == list:
            for item in data:
                if type(item) == int:
                    continue
                item = item.replace('&', '&amp;')
                item = item.replace('<', '&lt;').replace('>', '&gt;')
                item = item.replace('"', '&quot;').replace("'", '&#39;')
                item = item.replace('/', '')
                item = item.replace('\\', '')
                item = item.replace('\'', '')
        else:
            data = data.replace('&', '&amp;')
            data = data.replace('<', '&lt;').replace('>', '&gt;')
            data = data.replace('"', '&quot;').replace("'", '&#39;')
            data = data.replace('/', '')
            data = data.replace('\\', '')
            data = data.replace('\'', '')
    return data

def merge_configs(configBase, configEnv):
    '''
    描述：基础配置和运行环境配置合并
    :param configBase: 基础配置 application.yml
    :param configEnv:  运行环境配置 application-xxx.yml
    :return: configBase 最终返回合并后的配置
    '''
    if isinstance(configBase, dict) and isinstance(configEnv, dict):
        for key in configEnv:
            if key in configBase and isinstance(configBase[key], dict) and isinstance(configEnv[key], dict):
                merge_configs(configBase[key], configEnv[key])
            else:
                configBase[key] = configEnv[key]
    return configBase

def get_uuid():
    '''
    描述：基于随机数生成 UUID。完全随机生成的 UUID，不包含任何主机信息或时间信息。
        适合用于需要高度随机性的场景，如生成临时的会话标识符或令牌
    :return:uuid
    '''
    uuids = uuid.uuid4()
    return uuids

def image_to_base64(path):
    '''
    描述：将图片转换成base64
    :param path:图片路径
    :return:base64后的图片
    '''
    with open(path, "rb") as file:
        # 读取图片文件内容
        data = file.read()
        # 将图片文件内容进行 Base64 编码
        base64_data = base64.b64encode(data).decode("utf-8")
        return base64_data

def md5_encrypt(param):
    '''
    描述：实现md5加密
    :return encrypted_string
    '''
    # 创建一个 MD5 加密对象
    md5 = hashlib.md5()
    # 更新加密对象的内容为指定的字符串
    md5.update(param.encode('utf-8'))
    # 获取加密后的结果
    encrypted_string = md5.hexdigest()
    return encrypted_string

def get_cookies(name, request = request):
    return request.cookies.get(name)

def getCeil(number):
    return math.ceil(number)

def formatDate(datetime = datetime.now(), format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(format)

def dictNullToempty(dictData):
    # 将字典里面为Null的转换成空字符串
    for key, value in dictData.items():
        if value is None:
            dictData[key] = ''
    return dictData

def getRequestIp(request = request):
    # 优先尝试获取 X-Forwarded-For 中的客户端 IP
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # X-Forwarded-For 可能包含多个 IP 地址，以逗号分隔，选择第一个非本地 IP
        return x_forwarded_for.split(',')[0]

    # 如果没有 X-Forwarded-For，回退到 X-Real-IP 或 remote_addr
    return request.headers.get('X-Real-IP') or request.remote_addr

def getMillisecond(formate = "%Y%m%d%H%M%S%f"):
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间并精确到毫秒
    formatted_time = current_time.strftime(formate)
    return formatted_time

def is_has_children(dictionary):
    return 'children' in dictionary

def dateFormatStartAndEnd(date_interval):
    '''
    描述：根据时间标识 返回时间段
    :param day week month quarter year
    :param date_interval:
    :return: {xxxx-xx-xx xx:xx:xx}
    '''
    dtime = datetime.today()
    today = dtime.date()
    start_time = f'00:00:00'
    end_time = f'23:59:59'
    result = {
        'start':'',
        'end':f"{today} {end_time}"
    }
    # 获取今天的日期
    if date_interval == 'day':
        result['start'] = f"{today} {start_time}"
    # 获取今天之前七天的日期
    seven_days_ago = today - timedelta(days=7)
    if date_interval == 'week':
        result['start'] = f"{seven_days_ago} {start_time}"

    # 获取本月的第一天
    first_day_of_month = today.replace(day=1)
    if date_interval == 'month':
        result['start'] = f"{first_day_of_month} {start_time}"

    # 获取本季的第一天
    if date_interval == 'quarter':
        quarter = getSeasonData()
        result['start'] = f"{quarter['season_start']} {start_time}"
    # 获取今年的第一天
    current_year = datetime.today().year
    first_day_of_year = datetime(current_year, 1, 1).strftime('%Y-%m-%d')
    if date_interval == 'year':
        result['start'] = f"{first_day_of_year} {start_time}"
    return result

def getSeasonData():
    # 获取当前日期
    today = datetime.today()
    # 判断当前季节
    if 3 <= today.month <= 5:
        season_start = datetime(today.year, 3, 1)  # 春季开始
        season_end = datetime(today.year, 5, 31)  # 春季结束
        season_name = "春季"
    elif 6 <= today.month <= 8:
        season_start = datetime(today.year, 6, 1)  # 夏季开始
        season_end = datetime(today.year, 8, 31)  # 夏季结束
        season_name = "夏季"
    elif 9 <= today.month <= 11:
        season_start = datetime(today.year, 9, 1)  # 秋季开始
        season_end = datetime(today.year, 11, 30)  # 秋季结束
        season_name = "秋季"
    else:
        season_start = datetime(today.year, 12, 1)  # 冬季开始
        season_end = datetime(today.year + 1, 2, 28 if today.year % 4 != 0 else 29)  # 冬季结束
        season_name = "冬季"
    season ={
        'season_start':season_start.date(),
        'season_end':season_end.date(),
        'season_name':season_name
    }
    return season