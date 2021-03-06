# -*- coding: utf-8 -*-
# @Email   : youngqiankun@163.com

import os

if __name__ == '__main__':
    pass
    print(os.name)
    print(os.environ.get('FLASK_ENV'))
    print(os.environ.get('STARTUP_MODE'))

    info = os.uname()
    print(info)  # 获取详细信息
    print(info.sysname)  # 获取详细信息里面的系统名称
    print(info.nodename)  # 获取主机名
    print(os.environ)  # 获取系统环境变量

    import platform
    print(platform.architecture())
    print(platform.system())