from selenium.webdriver.common.by import By
from common.base_page import BasePage
from Location.send_message_loc import SendMessageLoc
from common.statics import get_userid_list
from pages.public_page import PublicPage
from time import sleep
from common.statics import get_userid_info

class SendEnterpriseMessage(SendMessageLoc, PublicPage):

    def switch_to_enterprise_send_message(self):
        sleep(1)
        self.click_element(self.find_Element(self._btn_addmessage))     # 进入企业群发
        sleep(1)

    def send_enterprise_message(self, send_type, send_limit, send_attach, msg):
        """
        :param send_type:发送类型：发送给客户，发送给客户群
        :param send_limit:发送范围：全部客户，按条件筛选客户，按群主筛选
        :param send_attach:附件：文本，图片，海报，网页，小程序
        :param msg:搜索素材时的关键字
        """
        self.click_element(self.find_Element(self._btn_create_msg))    # 点击新建企业群发
        if send_type == 'client':
            pass    # 默认选中“发送给客户”
            if send_limit == 'all':
                pass    # 默认选中“发送给全部客户”
            else:
                self.click_element(self.find_Element(self._btn_filter))    # 点击按条件筛选
                sleep(1)
                # self.click_element(self._btn_select_adder)  # 点击添加人
                self.public_select_staff(self._btn_select_adder, self._btn_sure_adder, send_limit)   # 添加人
        elif send_type == 'client_group':
            self.click_element(self.find_Element(self._btn_send_range)) # 选择发送给客户群
            self.public_select_staff(self._btn_select_client_group, self._btn_sure_adder, send_limit)    # 按群主选择客户群
        else:
            print('send_type只能是client或者client_group')
        # 添加时间问题
        self.click_element(self.find_Element(self._btn_time))  # 点击时间选择器
        sleep(1)
        self.click_element(self.find_Element(self._btn_select_time))   # 选择今天的后一天
        sleep(1)
        self.click_element(self.find_Element(self._btn_select_time_sure))  # 确定
        sleep(1)
        self.click_element(self.find_Element(self._btn_select_from_material_center))   # 点击添加素材
        if send_attach == 'text':
            self.send_keys(self.find_Element(self._input_search_text),msg)     # 输入搜索文本
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_text))   # 点击选中
            sleep(1)
            self.click_element(self.find_Element(self._btn_sure_text))     # 点击确认
        elif send_attach == 'pic':
            self.click_element(self.find_Element(self._btn_pic_tab))   # 点击图片tab
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_pic),msg)      # 输入搜索图片
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_pic))   # 点击选中
            sleep(1)
            self.click_element(self.find_Element(self._btn_sure_pic))     # 点击确认
        elif send_attach == 'web':
            self.click_element(self.find_Element(self._btn_web_tab))   # 点击网页tab
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_web),msg)     # 输入搜索网页
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_web))   # 点击选中
            sleep(1)
            self.click_element(self.find_Element(self._btn_sure_web))     # 点击确认
        elif send_attach == 'poster':
            self.click_element(self.find_Element(self._btn_poster_tab))   # 点击海报tab
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_poster),msg)      # 输入搜索海报
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_poster))   # 点击选中
            sleep(1)
            self.click_element(self.find_Element(self._btn_sure_poster))     # 点击确认
        elif send_attach == 'mini':
            self.click_element(self.find_Element(self._btn_mini_tab))   # 点击小程序tab
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_mini),msg)      # 输入搜索小程序
            sleep(1)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_mini))   # 点击选中
            sleep(1)
            self.click_element(self.find_Element(self._btn_sure_mini))     # 点击确认
        else:
            print('send_attach只能是text,pic,web,poster,mini')
        sleep(2)
        self.click_element(self.find_Element(self._btn_send))  # 点击发送

    def assert_enterprise_message(self, send_type, send_attach, msg):
        sleep(5)
        message_content = self.get_element_value(self.find_Element(self._text_enterprise_message_content))      # 获取到第一个的值的消息内容
        message_type = self.get_element_value(self.find_Element(self._text_enterprise_message_type))      # 第一个的值的群发类型
        message_content.strip() # 去掉前后空格
        message_type.strip()    # 去掉前后空格
        if send_type == 'client':
            self.assert_Equal(message_type, '发送客户')
        elif send_type == 'client_group':
            self.assert_Equal(message_type, '发送客户群')
        if send_attach == 'text':
            self.assert_Equal(message_content, msg)
        elif send_attach == 'pic':
            self.assert_Equal(message_content, '【图片】'+msg)
        elif send_attach == 'poster':
            self.assert_Equal(message_content, '【海报】'+msg)
        elif send_attach == 'web':
            self.assert_Equal(message_content, '【网页】'+msg)
        elif send_attach == 'mini':
            self.assert_Equal(message_content, '【小程序】'+msg)

    def search_enterprise_message(self, send_attach, msg):
        search_message = ''
        if send_attach == 'text':
            search_message = msg
        elif send_attach == 'pic':
            search_message = '【图片】'+msg
        elif send_attach == 'poster':
            search_message = '【海报】'+msg
        elif send_attach == 'web':
            search_message = '【网页】'+msg
        elif send_attach == 'mini':
            search_message = '【小程序】'+msg
        self.search_by_input(self._input_search_msg, search_message, self._btn_search)