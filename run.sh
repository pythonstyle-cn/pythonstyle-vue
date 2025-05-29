#!/bin/bash

AppName="main.py"
APP_HOME=`pwd`
LOG_DIR="./logs/"
LOG_FILE="$AppName.log"
VENV_PATH="/data/pyenv/py_pythonstyle_vue_310"  # Conda 虚拟环境路径

if [ "$1" = "" ];
then
    echo -e "\033[0;31m 未输入操作名 \033[0m  \033[0;34m {start|stop|restart|status} \033[0m"
    exit 1
fi

if [ "$AppName" = "" ];
then
    echo -e "\033[0;31m 未输入应用名 \033[0m"
    exit 1
fi

# 启动函数
start() {

	if [ ! -d "$LOG_DIR" ]; then
		mkdir -p "$LOG_DIR"
	fi
	if [ ! -f "$LOG_FILE" ]; then
		touch "$LOG_DIR/$LOG_FILE"
	fi

    # 1. 激活虚拟环境
	source /data/anaconda3/etc/profile.d/conda.sh
	PID=`conda activate $VENV_PATH && ps -ef |grep "$APP_HOME/$AppName"|grep -v grep|awk '{print $2}'`
	
    if [ -n "$PID" ]; then
        echo "$AppName is already running with PID $PID..."
    else
        echo "Starting $AppName..."
		conda activate $VENV_PATH
        nohup python3 $APP_HOME/$AppName > $APP_HOME/$LOG_DIR/$LOG_FILE 2>&1 &
        echo "$AppName started successfully..."
    fi
	# 3. 退出虚拟环境
    conda deactivate
}

# 停止函数
stop() {
	# 1. 激活虚拟环境
	source /data/anaconda3/etc/profile.d/conda.sh
    # 查找进程并杀死
    PID=`conda activate $VENV_PATH && ps -ef |grep "$APP_HOME/$AppName"|grep -v grep|awk '{print $2}'`
	echo "Stopping $AppName with PID $PID ..."
    if [ -n "$PID" ]; then
        kill -TERM $PID
        echo "$AppName (pid:$PID) stopping..."
        # 等待进程退出
        while [ -n "$PID" ]; do
            sleep 1
            PID=`conda activate $VENV_PATH && ps -ef |grep "$APP_HOME/$AppName"|grep -v grep|awk '{print $2}'`
        done
        echo "$AppName stopped."
    else
        echo "$AppName is not running."
    fi
	# 3. 退出虚拟环境
    conda deactivate
	
}

# 重启函数
restart() {
    stop
    sleep 2
    start
}

# 状态函数
status() {
    # 1. 激活虚拟环境
	source /data/anaconda3/etc/profile.d/conda.sh
    # 2. 执行命令
    PID=$(conda activate $VENV_PATH && ps -ef | grep "$APP_HOME/$AppName" | grep -v grep | wc -l)
    if [ "$PID" -gt 0 ]; then
        echo "$AppName is running with PID $PID..."
    else
        echo "$AppName is not running..."
    fi

    # 3. 退出虚拟环境
    conda deactivate
}

# 根据传入的参数执行相应的操作
case $1 in
    start)
    start;;
    stop)
    stop;;
    restart)
    restart;;
    status)
    status;;
    *)
	printf "\033[0;31m 无效的操作 \033[0m  \033[0;34m {start|stop|restart|status} \033[0m\n"
		exit 1
        ;;
esac
