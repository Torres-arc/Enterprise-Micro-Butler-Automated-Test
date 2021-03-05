import logging
import time


def log():
    # 创建一个日志器
    logger = logging.getLogger('logger')
    # 设置日志输出最低等级
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # 创建处理器
        # 控制台日志输出
        sh = logging.StreamHandler()
        # 文件日志输出
        # fh = logging.FileHandler(filename='Log/{}.log'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())),
        #                          encoding='utf-8')
        # mfh = logging.FileHandler(
        #     filename='Log/outer-{}.log'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())),
        #     encoding='utf-8')
        # mfh.setLevel(logging.INFO)
        # 创建格式器
        # fh_formator = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                                  datefmt='%Y/%m/%d/%X')
        sh_formator = logging.Formatter(fmt='%(levelname)s %(message)s')

        sh.setFormatter(sh_formator)
        # fh.setFormatter(fh_formator)
        # mfh.setFormatter(fh_formator)

        logger.addHandler(sh)
        # logger.addHandler(fh)
        # logger.addHandler(mfh)

    return logger
