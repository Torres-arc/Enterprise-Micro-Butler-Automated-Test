# 静态方法存放处
import os
from configparser import ConfigParser
import win32api
import win32con


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


def get_download_path():    # 获取文件下载的储存地址
    download_path = get_project_path() + '\\Download'
    return download_path


def get_screen_size():      # 获取当前屏幕的大小
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    return x, y


def get_video_path():       # 获取录屏时的位置
    video_path = get_project_path() + '\\video'
    return video_path
