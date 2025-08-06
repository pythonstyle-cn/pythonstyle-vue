from pythonstyle.libs.result import Result
from pythonstyle.libs.html import Html
from pythonstyle.config.log_config import Log
from pythonstyle.common import utils
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.role import RoleEntity
from pythonstyle.libs.redis import Redis
from pythonstyle.libs.jwt_manager import JWTManager
from pythonstyle.libs.session_manager import SessionManager
from pythonstyle.libs.param import Param
from pythonstyle.libs.upload import FileUpload
from pythonstyle.app import create_app
app = create_app()

class admin(Result):

    def index(self):
        logininfo = Redis().hdetall('login_data')
        data = [
            {"index": '你好', "test": 'index','login':logininfo},
        ]
        return Result.success(msg='操作成功', data=data)

    @Log
    def login(self):
        if utils.isPost():

            data = utils.postRequestJson()
            code_uuid = utils.filter_xss(data['uuid'])
            username = utils.filter_xss(data['username'])
            password = utils.filter_xss(data['password'])+'edsdkjjhnsdf'
            md5_password = utils.md5_encrypt(password)
            captchaEnabled = app.config['captchaEnabled']
            if captchaEnabled == True:
                code = data['code']
                try:
                    captcha_result = Redis().get('captcha_code:' + code_uuid).decode()
                except Exception as error:
                    return Result.error(code=1001, msg='登陆失败，请重试！！')

                if code != int(captcha_result):
                    return Result.error(code=1002, msg='验证码过期，登陆失败，请重试！！')

            try:
                userinfo = UserEntity.get_login_info(username, md5_password)
            except Exception as error:
                return Result.error(code=1003, msg='登陆失败，请重试！！')
            if userinfo == None:
                return Result.error(code=1004, msg='登陆失败，请重试！！')
            # 如果验证成功则保存登录信息到redis
            # 生成token
            Redis().hset('login_data', userinfo.user_id, code_uuid)
            payload = {'user_id': userinfo.user_id}
            jwt_manager = JWTManager()
            token = jwt_manager.generate_token(payload)
            #print(userinfo.user_id)
            SessionManager.set('user_id', userinfo.user_id)

            data = {
                "token": token
            }

            return Result.success(msg='登录成功！', data=data)
        else:
            return Result.error(203,msg='不允许直接访问！', data=[])

    def login_out(self):
        try:
            token = utils.getHttpHeaders('Authorization').replace('Bearer ', '')
            decoded_payload = JWTManager().verify_token(token)

            # 确保 decoded_payload 是字典类型
            if not isinstance(decoded_payload, dict):
                return Result.error(msg='无效的token')

            # 删除redis的用户信息以及token信息
            Redis().hdel('login_data', decoded_payload['user_id'])
            return Result.success(msg='退出登录成功！')

        except Exception as e:
            # 捕获可能的异常，如token验证失败等
            return Result.error(msg=f'退出登录失败: {str(e)}')

    def public_get_userinfo(self):
        user_id = self._get_user_id()
        # 获取用户信息
        userdata = UserEntity.get_user_roleinfo_by_id(user_id)
        if len(userdata) == 0:
            return Result.error(1007, msg='获取菜单失败，请联系管理员！', data=[])

        return Result.success(msg='操作成功！',data=userdata)

    # 修改个人信息
    def profile(self):
        if utils.isPost():
            data = utils.postRequestJson()
            user_id = self._get_user_id()

            nick_name = utils.filter_xss(data['nick_name'])
            remark = utils.filter_xss(data['remark'])
            email = utils.filter_xss(data['email'])
            param = {
                'user_id': user_id,
                'nick_name': nick_name,
                'email': email,
                'remark': remark,
            }
            result = UserEntity.edit_data(param)
            if result:
                return Result.success(msg='操作成功！')
            else:
                return Result.error(code=1006, msg='修改密码失败！')
        else:
            return Result.error(code=1007, msg='操作失败！')

    #修改密码
    def change_password(self):
        if utils.isPost():
            data = utils.postRequestJson()
            user_id = self._get_user_id()
            old_psd = utils.filter_xss(data['old_password'])  + 'edsdkjjhnsdf'
            old_password = utils.md5_encrypt(old_psd)
            userinfo = self._get_all_userinfo()
            psd = utils.filter_xss(data['password'])

            if old_password != userinfo['password']:
                return Result.error(code=1005, msg='原密码不对，请重新输入')

            password = utils.filter_xss(data['password']) + 'edsdkjjhnsdf'
            new_password = utils.md5_encrypt(password)
            param = {
                'user_id':user_id,
                'password':new_password
            }

            result = UserEntity.edit_data(param)
            if result:
                return Result.success(msg='操作成功！')
            else:
                return Result.error(code=1006, msg='修改密码失败！')
        else:
            return Result.error(code=1008, msg='操作失败！')

    #上传头像
    def public_upload_avtor(self):
        file = utils.getFiles('file')
        uploader = FileUpload(app.root_path)
        filepath = uploader.handle_upload(file)
        user_id = self._get_user_id()
        if filepath == None:
            return Result.error(code=400, msg='文件格式不合法！')
        param = {
            'user_id': user_id,
            'avatar': filepath
        }
        data = {
            'filepath':filepath
        }
        result = UserEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功！',data=data)
        else:
            return Result.error(code=1009, msg='操作失败！')


    def _get_all_userinfo(self):
        # 先获取token
        user_id = self._get_user_id()
        # 获取用户信息
        userdata = UserEntity.get_userinfo_by_id(user_id)
        return userdata


    def _get_user_id(self):
        try:
            token = utils.getHttpHeaders('Authorization').replace('Bearer ', '')
            jwt_manager = JWTManager()
            decoded_payload = jwt_manager.verify_token(token)
            user_id = decoded_payload['user_id']
            return user_id
        except Exception as e:
            return Result.error(code=401, msg='您还没有登录，请先登录！')