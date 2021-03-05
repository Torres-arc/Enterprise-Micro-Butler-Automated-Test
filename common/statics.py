# 静态方法存放处
import os
from configparser import ConfigParser
import win32api
import win32con
import xlwings as xw
import datetime
import time

lists = []


def get_project_path():  # 获取项目路径
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def get_config(section, option=None):  # 获取config中的对应节，键的具体值,所以是双参数
    path = get_project_path() + '/config/config.ini'
    conf = ConfigParser()
    conf.read(path, encoding='utf-8')
    if option is not None:
        config_result = conf.get(section, option)
    else:
        config_result = conf.items(section)
        config_result = dict(config_result)
    # print(config_result)
    return config_result


def get_download_path():  # 获取文件下载的储存地址
    download_path = get_project_path() + '\\Download'
    return download_path


def get_screen_size():  # 获取当前屏幕的大小
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    return x, y


def get_video_path():  # 获取录屏时的位置
    video_path = get_project_path() + '\\video'
    return video_path


# 读取userid信息
def get_userid_info(userid):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\idInfo.json'
    f = open(path, 'r', encoding='utf-8')
    dict_ = eval(f.read())
    f.close()
    return dict_[userid]


def dict_gets(dict2, objkey, default='无目标', judge=0):
    """
    :param dict2: 需要查找字典
    :param objkey: 目标字段
    :param default: 查找失败后的返回值
    :param judge: 状态判断
    :return: 字典里所有目标字段的值，list
    """
    # 判断是否为首次递归
    if judge == 0:
        lists.clear()

    tmp = dict2
    # 遍历接口所有数据
    for k, v in tmp.items():
        # 外层有符合的即添加
        if k == objkey:
            lists.append(v)
            continue
        else:
            # 内层为字典格式则直接递归
            if type(v).__name__ == 'dict':
                ret = dict_gets(v, objkey, judge=1)
                if ret is not default and ret != []:
                    if not ret == [] and ''.join(str(ret)) in lists and ret != lists:
                        lists.append(''.join(ret))
                    continue
                else:
                    continue
            # 内层为列表格式则先转换为字典，再进行递归
            elif type(v).__name__ == 'list':
                dicts = {}
                for i in range(len(v)):
                    dicts[i] = v[i]
                ret = dict_gets(dicts, objkey, judge=1)
                if ret is not default:
                    if not ret == [] and ''.join(str(ret)) in lists:
                        lists.append(''.join(ret))
                    continue
    msg = lists
    return msg


# 优化数据格式，单个数据为string，多个为list
def dict_get(dict2, objkey):
    sd = dict_gets(dict2, objkey)
    if len(sd) == 1:
        return sd[0]
    else:
        return sd


def read_file(path, sheetname, ranges, type=None):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(path)
    if type is None:
        value = wb.sheets[sheetname].range(ranges).value
        wb.close()
        app.quit()
        return value
    elif type == 'down':
        value = wb.sheets[sheetname].range(ranges).expand('down').value
        wb.close()
        app.quit()
        return value


def new_file(testdir):
    list = os.listdir(testdir)
    list.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir + '\\' + list[-1]))
    filepath = os.path.join(testdir, list[-1])
    print("最新修改的文件(夹)：" + list[-1])
    print("时间：" + filetime.strftime('%Y-%m-%d %H-%M-%S'))
    return filepath


def createExcel():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\Log')
    path1 = self.new_file(path)
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    wb = app.books.add()
    wb.sheets['Sheet1'].name = 'log'
    wb.sheets['log'].range('A1').value = '运行时间'
    # wb.sheets['log'].range('a1:a5').merge()
    wb.sheets['log'].range('b1').value = '测试页面'
    wb.sheets['log'].range('c1').value = '测试用例'
    wb.sheets['log'].range('d1').value = '调用函数'
    wb.sheets['log'].range('e1').value = '日志等级'
    wb.sheets['log'].range('f1').value = '用例运行信息'
    wb.sheets['log'].autofit()
    wb.sheets['log'].range('f1').column_width = 77
    f = open(path1, encoding='utf-8')
    line = f.readline()
    count = 2
    while line:
        if line.startswith('2020'):
            msg = line.split(' ')
            wb.sheets['log'].range('a' + str(count)).value = msg[0]
            wb.sheets['log'].range('e' + str(count)).value = msg[2]
            if msg[2] == 'INFO':
                wb.sheets['log'].range('e' + str(count)).color = (255, 255, 0)
            if msg[2] == 'ERROR':
                wb.sheets['log'].range('e' + str(count)).color = (255, 0, 0)
            if msg[1].startswith('base'):
                a = msg[3].split('\\')
                # wb.sheets['log'].range('b' + str(count)).value = a[-1]
                string1 = "".join(msg[6:])
                wb.sheets['log'].range('f' + str(count)).value = string1[:-1]
                wb.sheets['log'].range('d' + str(count)).value = a[-1] + ':' + msg[5] + '[line:' + msg[4] + ']'
            else:
                wb.sheets['log'].range('b' + str(count)).value = (msg[1].split('['))[0]
                wb.sheets['log'].range('f' + str(count)).value = msg[3]
                if msg[3].startswith('开始执行:用例') or msg[3].startswith('开始执行 用例'):
                    curstart = count
                    wb.sheets['log'].range('c' + str(count)).value = (msg[3].split('-'))[1:]
                if msg[3].startswith('执行结束:用例') or msg[3].startswith('执行结束 用例'):
                    curend = count
                    wb.sheets['log'].range('c' + str(curstart) + ":" + 'c' + str(curend)).merge()
                if msg[3].endswith('自动化测试') and msg[3].startswith('开始执行'):
                    curstart1 = count
                    # wb.sheets['log'].range('b' + str(count)).value = (msg[3].split('-'))[-1]
                if msg[3].endswith('自动化测试') and msg[3].startswith('执行结束'):
                    curend1 = count
                    wb.sheets['log'].range('b' + str(curstart1) + ":" + 'b' + str(curend1)).merge()
            wb.sheets['log'].autofit()
            # print(line, end='')
            if msg[3].startswith('Finish'):
                break
            line = f.readline()
            count += 1
        else:
            wb.sheets['log'].range('f' + str(count)).value = line
            line = f.readline()

    time.sleep(5)
    wb.save()
    wb.close()
    app.quit()
    f.close()
