# -*-coding:utf-8 -*-
import json
import os
import sys
import time

from pathlib import Path
from time import sleep
from unittest import TestCase

from BeautifulReport import BeautifulReport
from BeautifulReport.BeautifulReport import HTML_IMG_TEMPLATE
from PIL import ImageDraw, Image
from pymouse import PyMouse
from pykeyboard.windows import PyKeyboard
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.log import log


class BasePage(object):
    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    #####################################################################################################
    # 页面操作方法
    # 打开网址并最大化
    # def _open(self, url):
    #     self.driver.get(url)
    #     self.driver.maximize_window()

    # 定位i至最新打开的窗口
    def switch_to_window(self):
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])

    # 网页回退的方法
    def _back(self):
        self.driver.back()

    # 获取当前URL的方法
    def get_cur_url(self):
        return self.driver.current_url

    # 跳转回默认页面焦点
    def switchtodefault(self):
        return self.driver.switch_to.default_content()

    # 获取浏览器宽
    def get_window_width(self):
        return self.driver.get_window_size()['width']

    # 获取浏览器高
    def get_window_height(self):
        return self.driver.get_window_size()['height']

    # 进行截图并输入测试报告，可对元素进行框选
    # def GetScreen(self, action, startTime=time.time(), rect=None):
    #     # 定义截图存放目录的路径
    #     screenpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\img')
    #     # 生成图片
    #     png = time.strftime('%Y%m%d_%H%M%S', time.localtime(startTime)) + "_" + "_" + action + ".png"
    #     self.driver.get_screenshot_as_file(screenpath + '\\' + png)
    #     if rect is not None:
    #         img = Image.open(screenpath + '\\' + png)
    #         draw = ImageDraw.Draw(img)
    #         draw.rectangle(rect, outline=(255, 0, 0))
    #         img.save(screenpath + '\\' + png)
    #     data = BeautifulReport.img2base(screenpath, png)
    #     print("<p style='font-weight: bold; font-size: x-large; color: #0000CD; text-align: center'>"
    #           "{}</p>".format(action))
    #     print(HTML_IMG_TEMPLATE.format(data, data))
    #     # print("<img src='" + data + "' width=600 />")
    #     return png

    # 获取元素的位置信息
    def locate_element(self, ele, zoom=1.25):
        ele_x = ele.location_once_scrolled_into_view.get('x')
        ele_y = ele.location_once_scrolled_into_view.get('y')
        ele_wid = ele.size.get('width')
        ele_hei = ele.size.get('height')
        xoffset_min = ele_x * zoom
        xoffset_max = (ele_x + ele_wid) * zoom
        yoffset_min = ele_y * zoom
        yoffset_max = (ele_y + ele_hei) * zoom
        return [xoffset_min, yoffset_min, xoffset_max, yoffset_max]

    #####################################################################################################
    # 返回接口数据
    def get_response_data(self, api):
        """
        参数：
            api:传入 Request URL
        用法:
            self.get_response_data('https://qw.wshoto.com/v3/api-qrcode/guide_qr_code/staff/list')
        :return:
            回调一个字典，内容为接口返回数据 dict
        """
        request_log = self.driver.get_log('performance')
        # print(request_log)
        # 逐行读取请求数据
        for i in range(len(request_log)):
            message = json.loads(request_log[len(request_log) - i - 1]['message'])
            message = message['message']['params']
            # .get() 方式获取是了避免字段不存在时报错
            request = message.get('request')
            if request is None:
                continue
            url = request.get('url')
            # 如果该请求为目标请求,则返回对应的接口数据
            if url.startswith(api):
                # 通过requestId获取接口内容
                content = self.driver.execute_cdp_cmd('Network.getResponseBody',
                                                      {'requestId': message['requestId']})
                # 将接口的主体数据以json格式输出
                dict1 = json.loads(content['body'])
                return dict1

    #####################################################################################################
    # 查找单个元素
    def find_Element(self, *args):
        """
        :param args:元素定位地址 (By.XPATH, '//div[@id="1"]')
        :return:网页元素 webelement
        """
        # 用于日志输出的调用函数名、行号、模块名
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(*args))
        except Exception as e:
            log().error('{}-{}-{},未找到元素:{}'.format(str(module), str(lineno), name, str(args)), exc_info=True)
            raise e
        else:
            log().debug('{}-{}-{},成功找到元素:{}'.format(str(module), str(lineno), name, str(args)))
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(*args))

    # 查找多个元素
    def find_Elements(self, *loc):
        """
        :param loc: 元素定位地址 (By.XPATH, '//div[@id="1"]')
        :return: 网页元素列表 list：webelements
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(*loc))
        except TimeoutException as e:
            log().error('{}-{}-{},未找到多元素:{}'.format(str(module), str(lineno), name, str(loc)), exc_info=True)
            raise e
        else:
            log().debug('{}-{}-{},成功找到多元素:{}'.format(str(module), str(lineno), name, str(loc)))
            return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(*loc))

    # 重写输入方法
    def send_keys(self, element, value):
        """
        :param element: 网页元素
        :param value: 输入的值 'test'
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            element.clear()
            element.send_keys(value)
        except:
            log().error('{}-{}-{},输入字符:{},有误'.format(str(module), str(lineno), name, str(value)), exc_info=True)
        else:
            log().debug('{}-{}-{},成功输入字符:{}'.format(str(module), str(lineno), name, str(value)))

    # 点击元素
    # 重写点击元素方法
    def click_element(self, element):
        """
        :param element: 网页元素
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]

        try:
            element.click()
        except:
            log().error('{}-{}-{},未点击到元素'.format(str(module), str(lineno), name), exc_info=True)
        else:
            log().debug('{}-{}-{},成功点击元素'.format(str(module), str(lineno), name))

    # 鼠标移动至某一点并强制点击
    def move_click_element(self, element):
        """
        :param element: 网页元素
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            ActionChains(self.driver).move_to_element(element).click().perform()
        except:
            log().error('{}-{}-{},未点击到元素'.format(str(module), str(lineno), name), exc_info=True)
        else:
            log().debug('{}-{}-{},成功点击元素'.format(str(module), str(lineno), name))

    # 鼠标移动至某一点
    def move_to_element(self, element):
        """
        :param element: 网页元素
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            log().error('{}-{}-{},鼠标无法移至元素'.format(str(module), str(lineno), name), exc_info=True)
        else:
            log().debug('{}-{}-{},鼠标成功移至元素'.format(str(module), str(lineno), name))

    # 获取元素的值
    def get_element_value(self, element):
        """
        :param element: 网页元素
        :return: 元素文本值 string
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            text = element.text
        except:
            log().error('{}-{}-{},未获取到元素文本'.format(str(module), str(lineno), name), exc_info=True)
        else:
            log().debug('{}-{}-{},获取元素文本:{}'.format(str(module), str(lineno), name, str(element.text)))
            return text

    # 获取多个元素的值
    def get_elements_values(self, elements):
        """
        :param elements: 网页元素列表 list:webelements
        :return: 文本值列表 list:strings
        """
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            texts = []
            for i in elements:
                texts.append(i.text)
        except:
            log().error('{}-{}-{},未获取到多元素文本'.format(str(module), str(lineno), name), exc_info=True)
        else:
            log().debug('{}-{}-{},获取多元素文本:{}'.format(str(module), str(lineno), name, str(texts)))
            return texts

    # 操作键盘的方法
    def control_keyboard(self, string):
        """
        :param string:需要输入的字符串
        """
        k = PyKeyboard()
        k.type_string(string)

    def tap_keyboard(self, type):
        """
        :param type: 按键类型 enter/shift
        """
        k = PyKeyboard()
        if type == 'enter':
            k.tap_key(k.enter_key)
        if type == 'shift':
            k.tap_key(k.shift_key)

    # # 滚动屏幕方法
    # def scroll_screen(self, element, vertical=-10, ele=None, zoom=1):
    #     """
    #     :param element: 目标元素，即想要看到的元素
    #     :param vertical: 每一步垂直滚动的距离， +向上，-向下
    #     """
    #     m = PyMouse()
    #     while not element.is_displayed():
    #         x_dim, y_dim = m.screen_size()
    #         sleep(3)
    #         if ele is None:
    #             # m.move(x_dim // 2, y_dim // 2)
    #             pass
    #         else:
    #             m.move(ele.location_once_scrolled_into_view.get('x') * zoom,
    #                    ele.location_once_scrolled_into_view.get('y') * zoom)
    #         m.scroll(vertical=vertical)
    #         sleep(3)
    #
    # def force_scroll_screen(self, vertical=-10, ele=None, zoom=1):
    #     """
    #     :param element: 目标元素，即想要看到的元素
    #     :param vertical: 每一步垂直滚动的距离， +向上，-向下
    #     """
    #     m = PyMouse()
    #     if ele is None:
    #         pass
    #     else:
    #         m.move(ele.location_once_scrolled_into_view.get('x') * zoom,
    #                ele.location_once_scrolled_into_view.get('y') * zoom)
    #     m.scroll(vertical=vertical)
    #     sleep(3)

    # 重写js执行方法
    def execute_JS(self, js):
        """
        :param js: 需要执行的js语句
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            raise e

    #####################################################################################################
    # 断言方法封装
    # 校验是否为真
    def assert_True(self, key, msg=None):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertTrue(key, msg=msg)
        except AssertionError as e:
            log().error('{}-{}-{},{}:校验为错误，与预期不符'.format(str(module), str(lineno), name, msg))
            raise e
        else:
            log().info('{}-{}-{},{}:校验为正确，与预期相符'.format(str(module), str(lineno), name, msg))

    # 校验是否为假
    def assert_False(self, key, msg=None):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = ((sys._getframe(1).f_code.co_filename).split('pages'))[-1]
        try:
            TestCase().assertFalse(key, msg=msg)
        except AssertionError as e:
            log().error('{}-{}-{},{}:校验为正确，与预期不符'.format(str(module), str(lineno), name, msg))
            raise e
        else:
            log().info('{}-{}-{},{}:校验为错误，与预期相符'.format(str(module), str(lineno), name, msg))

    # 校验是否相等
    def assert_Equal(self, key1, key2, msg=None):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertEqual(key1, key2, msg)
        except AssertionError as e:
            log().error('{}-{}-{},{} 与 {} 不相等,验证错误'.format(str(module), str(lineno), name, str(key1), str(key2)))
            raise e
        else:
            log().info('{}-{}-{},{} 与 {} 相等,验证正确'.format(str(module), str(lineno), name, str(key1), str(key2)))

    # 校验是否不相等
    def assert_Not_Equal(self, key1, key2):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertNotEqual(key1, key2)
        except AssertionError as e:
            log().error('{}-{}-{},{} 与 {} 相等,验证错误'.format(str(module), str(lineno), name, str(key1), str(key2)))
            raise e
        else:
            log().info('{}-{}-{},{} 与 {} 不相等,验证正确'.format(str(module), str(lineno), name, str(key1), str(key2)))

    # 校验页面是否存在某字符串
    def check_exist_in_page(self, string):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertTrue(string in self.driver.page_source)
        except AssertionError as e:
            log().error('{}-{}-{},经验证,{} 不存在于页面内，与预期不符'.format(str(module), str(lineno), name, string))
            raise e
        else:
            log().info('{}-{}-{},经验证,{} 存在于页面内，与预期相符'.format(str(module), str(lineno), name, string))

    # 校验页面是否存在某字符串
    def check_not_exist_in_page(self, string):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertTrue(string not in self.driver.page_source)
        except AssertionError as e:
            log().error('{}-{}-{},经验证,{} 存在于页面内，与预期不符'.format(str(module), str(lineno), name, string))
            raise e
        else:
            log().info('{}-{}-{},经验证,{} 不存在于页面内，与预期相符'.format(str(module), str(lineno), name, string))

    # 校验某字符串是否在列表内
    def check_exist_in_lists(self, string1, string2):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertIn(string1, string2)
        except AssertionError as e:
            log().error(
                '{}-{}-{},经验证,{} 不存在于字符串{}内，与预期不符'.format(str(module), str(lineno), name, string1, str(string2)))
            raise e
        else:
            log().info('{}-{}-{},经验证,{} 存在于字符串"{}内，与预期相符'.format(str(module), str(lineno), name, string1, str(string2)))

    # 校验某字符串是否在列表内
    def check_exist_not_in_lists(self, string1, string2):
        name = sys._getframe(1).f_code.co_name
        lineno = sys._getframe(1).f_back.f_lineno
        module = (sys._getframe(1).f_code.co_filename.split('\\'))[-1]
        try:
            TestCase().assertNotIn(string1, string2)
        except AssertionError as e:
            log().error('{}-{}-{},经验证,{} 存在于字符串{}内，与预期不符'.format(str(module), str(lineno), name, string1, str(string2)))
            raise e
        else:
            log().info('{}-{}-{},经验证,{} 不存在于字符串{}内，与预期相符'.format(str(module), str(lineno), name, string1, str(string2)))
