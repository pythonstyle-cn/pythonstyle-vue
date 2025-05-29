# pythonstyle-vue
PythonStyle是一个企业级开发平台，基于flask基础，采用MVC架构，统一入口，自动实现访问路由。内置模块包含：用户管理、部门管理、角色管理、菜单及按钮授权、日志管理、登录模块等。  

>一个轻量级python WEB MVC开发框架
>一个轻量级python WEB MVC开发框架

>官网地址：https://pythonstyle.cn

>前后端分离版演示地址： https://demo1.pythonstyle.cn/

>前后端混合版演示地址： https://demo2.pythonstyle.cn/
>混合开发版暂时不是开源版本，需要下载请前往官网注册下载

>演示账号：admin 密码：admin123

### 主要特性  

 * 支持多数据源，通过ymal简单配置即可实现。
 * 支持前后端分离部署，前端使用VUE3。
 * 支持模板混合模式开发。
 * 支持日志记录，通过@Log装饰器即可简单实现。
 * 支持基于RBAC的权限管理，前端可以精确到别扭权限设置。

![a](https://www.pythonstyle.cn/static/uploadfiles/03e591292b883f3a83fae756d1d1b33f4f23584b380211c04b67e18eeaee6fb2.png)  
![a](https://www.pythonstyle.cn/static/uploadfiles/f7206e4d647528bd3a2fc11c0e17a0395f66af70eefc2dda3d19645957d4f0f4.png)  
![a](https://www.pythonstyle.cn/static/uploadfiles/38336bfa36bffb21a7ff5c97e7c130420dcc83a33cf7e20c8274f1c7f8e60f4d.png) 
![a](https://www.pythonstyle.cn/static/uploadfiles/6bcad7ba1646c0e79f2fc4f0fcfa24b62eb279239e2a776a27f79f1c92ed0ca7.png) 
![a](https://www.pythonstyle.cn/static/uploadfiles/8c99ccc1fafd84f086b8e7a4dfb508aa98660f4754bdb7728c3f98bb1f885e3f.png)
![a](https://www.pythonstyle.cn/static/uploadfiles/90c38805133b628efb99632b7fc29e5102eb3f200d272cd55532813338235680.png)
### 技术选型

- 系统环境
  - python 3.10
- 主框架
  - flask 3.0.2
  - werkzeug 3.0.1
- 持久层
  - PyMySQL 1.1.0
  - pony 0.7.17	
- 视图层
  - jinja2 3.1.3
# 项目结构
```pythonstyle
my_python_project                                        #项目名称
│   ├── main.py                                          #项目主文件入口
├── pythonstyle                                          #框架目录
|   ├── common                                           #工具函数库目录
|   |   └── utils.py                                     #默认内置工具函数库
|   ├── config                                           #配置文件目录
|   |   ├── configure.py                                 #配置加载装饰器
|   |   └── router.py                                    #默认MVC路径配置
|   ├── model                                            #模型初始化目录
|   |   └── model.py                                     #模型初始化执行
|   ├── libs                                             #工具类库目录
|   |   ├── application.py                               #应用初始化类
|   |   ├── db_factory.py                                #数据库工厂类
|   |   ├── html.py                                      #调用flask默认模板类
|   |   ├── http_response.py                             #HTTP请求响应类
|   |   ├── param.py                                     #MVC参数处理类
|   |   ├── result.py                                    #返回响应请求封装类
|   |   └── status_code.py                               #响应状态码类
|   ├── modules                                          #模块目录
|   |   ├── module_1                                     #自定义模块
|   |   |    ├── controller                              #模块控制器目录
|   |   |    |   └── className.py                        #控制器类  
|   |   |    ├── entity
|   |   |    |   └──entityName.py
|   |   ├── module_2                                     #自定义模块2控制器目录
|   |   ├── module_n                                     #自定义模块n控制器目录
│   └── app.py                                           #flask app 生成器
├── resource                                             #配置资源目录
│   ├── templates                                        #模板目录
|   |   ├── module_1                                     #对应的模块模板目录
|   |   |   └── index.html                               #模块对应的模板文件
│   ├── application.yml                                  #主配置文件
│   ├── application-dev.yml                              #开发环境配置文件
│   ├── application-pro.yml                              #生产环境配置文件
└── static                                               #静态资源
|   |   ├── css                                          #css 目录
|   |   ├── js                                           #js  目录
|   |   └── images                                       #images目录
├── logs                                                 #日志文件目录
└── doc                                                  #文档目录
```
> 基础框架缺少部分文件类
# 必要配置
1.修改项目运行配置，编辑resources目录下的application.yml
> PythonStyle的配置文件采用yml格式  
> 通用格式是：application.yml
```yml
#pythonstyle配置
pythonstyle:
  profiles:
    active: dev

# 开发环境配置
server:
  host: 127.0.0.1
  # 服务器的HTTP端口，默认为5000
  port: 8085
  debug: True


# 用户配置
user:
  password:
    # 密码最大错误次数
    maxRetryCount: 8
    # 密码锁定时间（默认10分钟）
    lockTime: 10

# token配置
token:
    # 令牌自定义标识
    header: Authorization
    # 令牌密钥
    secret: abcdefghijklmnopqrstuvwxyz
    # 令牌有效期（默认30分钟）
    expireTime: 30

#是否开启验证码
captcha:
  captchaEnabled: True
  
log:
  #是否开启登录日志
  loginEnabled: True
  #是否开启操作日志
  operationEnabled: True
```
> dev：表示开发环境  
> pro：表示生产环境，这个可以自定义xxx，对应的配置文件为application-xxx.yml  

2.修改数据库连接，编辑resources目录下的application-dev.yml
```yml
pythonstyle:
  datasource:
    mysql:
        # 主库数据源
        master:
          host: '127.0.0.1'
          port: 3306
          user: 'root'
          password: ''
          db: 'db_pythonstyle'
        # 从库数据源
        slave:
          # 从数据源开关
          host: '127.0.0.1'
          port: 3306
          user: 'root'
          password: ''
          database: 'db_pythonstyle_bak'

    sqlite:
      # 主库数据源
      master:
        filename: 'db.sqlite'
        create_db: True
        timeout: 5.0

    oracle:
      # 主库数据源
      master:
        user: root
        password: ''
        dsn: '127.0.0.1'

    postgres:
      # 主库数据源
      # 主库数据源
      master:
        host: '127.0.0.1'
        port: 3306
        user: 'root'
        password: ''
        database: 'db_pythonstyle'
        
    #配置redis数据库
    redis:
      host: localhost # Redis 服务器地址
      port: 6379 # Redis 服务器端口号
      database: 1 # Redis 数据库编号
      password: '' # Redis 访问密码
```
> 数据库支持4种数据库，mysql、sqlite、oracle、postgreSQL
3.修改服务器配置，编辑resources目录下的application.yml
```yml
# 开发环境配置
server:
  host: 127.0.0.1
  # 服务器的HTTP端口，默认为5000
  port: 5000
  debug: True
```
> host:表示当前服务器IP  
> port：表示端口号  
> debug：代表是否开启debug模式

4.修改日志配置和是否开启验证码，编辑resources目录下的application.yml
```yml
#是否开启验证码
captcha:
  captchaEnabled: True
log:
  #是否开启登录日志
  loginEnabled: True
  #是否开启操作日志
  operationEnabled: True
```
> 是否开启验证码 默认开启，在登录的时候会显示验证码  
> captchaEnabled: True  
> 是否开启登录日志 True表示开启，False表示关闭 默认开启  
> loginEnabled: True   
> 是否开启操作日志 True表示开启，False表示关闭  默认开启  
> operationEnabled: True

