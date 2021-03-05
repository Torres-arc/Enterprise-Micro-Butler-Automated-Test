# 静态方法存放处
import os
from configparser import ConfigParser


def get_project_path():     # 获取项目路径
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def get_config(section, option):   # 获取config中的对应节，键的具体值,所以是双参数
    path = get_project_path() + '/config/config.ini'
    conf = ConfigParser()
    conf.read(path, encoding='utf-8')
    config_result = conf.get(section,option)
    # print(config_result)
    return config_result

# get_project_path()
# get_config('website', 'url')