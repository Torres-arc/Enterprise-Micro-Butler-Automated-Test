import datetime

from selenium.webdriver.common.by import By

from common.base_page import BasePage
from Location.client_loc import ClientLoc
from Location.client_group_loc import ClientGroupLoc
from Location.client_code_loc import ClientCodeLoc
from Location.welcome_message_loc import WelcomeMessageLoc
from common.statics import get_userid_list
from time import sleep


class PublicPage(BasePage, ClientLoc, ClientGroupLoc, ClientCodeLoc, WelcomeMessageLoc):
    def switch_to_client_manage_tab(self):
        self.click_element(self.find_Element(self._btn_client_manage_tab))  # 进入客户管理tab
        sleep(2)

    def switch_to_client_marketing_tab(self):
        self.click_element(self.find_Element(self._btn_client_marketing_tab))   # 进入客户营销tab
        sleep(2)

    def unfold_search_bar(self):
        # 客户管理模块的展开
        self.click_element(self.find_Element(self._btn_more_filter))    # 展现隐藏搜索栏
        sleep(2)

    def unfold_market_search_bar(self):
        # 客户营销模块的展开
        self.click_element(self.find_Element(self._btn_search_more_filter))    # 展现隐藏搜索栏
        sleep(2)

    def public_select_staff(self, open_window_loc, confirm_loc, adder):
        """
        打开组织架构弹窗，并选择员工
        :param confirm_loc: 确认选择按钮的元素定位
        :param open_window_loc: 打开弹窗的元素定位
        :param adder: 需要搜索选择的员工姓名(支持string及list)
        :return:
        """
        self.click_element(self.find_Element(open_window_loc))  # 点击添加人输入框，进入组织架构
        sleep(2)
        if isinstance(adder, str):
            self.send_keys(self.find_Element(self._input_addname), adder)  # 输入添加人姓名
            sleep(1)
            self.tap_keyboard('enter')  # 按下回车，进行搜索
            sleep(2)
            self.click_element(self.find_Element(self._btn_adder))  # 选择搜索结果
            sleep(2)
        elif isinstance(adder, list):
            for i in adder:
                self.send_keys(self.find_Element(self._input_addname), i)  # 输入添加人姓名
                sleep(1)
                self.tap_keyboard('enter')  # 按下回车，进行搜索
                sleep(2)
                self.click_element(self.find_Element(self._btn_adder))  # 选择搜索结果
                sleep(2)
        else:
            raise TypeError
        self.click_element(self.find_Element(confirm_loc))  # 点击确认
        sleep(2)

    def search_by_input(self, input_loc, search_input, search_loc):
        """
        通过输入方式来搜索
        :param search_loc: 查询按钮定位
        :param input_loc: 输入框定位
        :param search_input: 输入文本
        :return:
        """
        self.send_keys(self.find_Element(input_loc), search_input)  # 输入
        sleep(2)
        self.click_element(self.find_Element(search_loc))     # 点击搜索
        sleep(1)

    def select_tag_by_name(self, open_window_loc, confirm_loc, tag):
        """
        打开弹窗并选择标签
        :param open_window_loc: 打开标签弹窗的按钮定位
        :param confirm_loc: 标签确认的按钮定位
        :param tag: 目标标签
        :return:
        """
        self.click_element(self.find_Element(open_window_loc))  # 点击打开标签弹窗
        sleep(2)
        self.click_element(self.find_Element((By.XPATH, self._btn_tags.format(tag))))  # 选择指定的标签
        sleep(1)
        self.click_element(self.find_Element(confirm_loc))  # 点击确认
        sleep(1)

    def select_tag(self, open_window_loc, tag_loc, confirm_loc):
        """
        打开弹窗并选择标签
        :param open_window_loc: 打开标签弹窗的按钮定位
        :param tag_loc: 标签选择定位(list)
        :param confirm_loc: 标签确认的按钮定位
        :return: list标签列表
        """
        self.click_element(self.find_Element(open_window_loc))  # 点击打开标签弹窗
        sleep(2)
        tag_list = []
        for i in tag_loc:
            tag_list.append(self.get_element_value(self.find_Element(i)))
            self.click_element(self.find_Element(i))  # 选择指定的标签
            sleep(1)
        self.click_element(self.find_Element(confirm_loc))  # 点击确认
        sleep(1)
        return tag_list

    def select_group_code(self, open_window_loc, input_loc, search_loc, select_loc, confirm_loc, group_name):
        """
        弹窗选择群活码
        :param input_loc: 搜索输入框定位
        :param open_window_loc:  打开选择群活码窗口的定位
        :param search_loc: 查询按钮定位
        :param select_loc:  选择群活码定位
        :param confirm_loc:  确定按钮定位
        :param group_name:   群名称文本
        :return:
        """
        self.click_element(self.find_Element(open_window_loc))  # 打开选择活码的弹窗
        sleep(2)
        self.send_keys(self.find_Element(input_loc), group_name)  # 输入群名
        sleep(2)
        self.click_element(self.find_Element(search_loc))  # 点击查询按钮
        sleep(2)
        self.click_element(self.find_Element(select_loc))  # 选择群活码
        sleep(2)
        self.click_element(self.find_Element(confirm_loc))  # 确认选择
        sleep(2)

    def select_date(self, start_time, end_time):
        # 输入开始及结束时间
        self.send_keys(self.find_Element(self._input_create_start_time), start_time)
        sleep(1)
        self.send_keys(self.find_Element(self._input_create_end_time), end_time)
        sleep(1)

    def assert_search_input(self, texts_loc, search_input):
        """
        通过输入方式来搜索后，验证里面的值都是包含输入的值
        :param texts_loc: 文本元素定位
        :param search_input: 目标查找文本
        :return:
        """
        clients = self.get_elements_values(self.find_Elements(texts_loc))
        print(clients)
        for client in clients:
            self.check_exist_in_lists(search_input, client)

    def assert_search_staff(self, texts_loc, staff):
        """
        验证按组织架构搜索，员工数据符合预期
        :param texts_loc: 员工元素定位
        :param staff: 目标员工文本
        :return:
        """
        ele_list = self.find_Elements(texts_loc)
        id_list = []
        for i in ele_list:
            id_list.append(i.get_attribute('openid'))  # 先获取员工的openid列表
        staff_list = get_userid_list(id_list)  # 通过企微接口，将id转化为员工姓名
        for i in staff_list:
            self.assert_Equal(staff, i)

    def assert_search_date(self, time_loc, start_time, end_time):
        """
        验证日期处于筛选区间内
        :param time_loc: 日期文本定位
        :param start_time: 开始时间 YYYY-MM-DD
        :param end_time: 结束时间
        :return:
        """
        time_list = self.get_elements_values(self.find_Elements(time_loc))
        splited_list = []
        for i in time_list:
            splited_list.append((i.split(' '))[0])
        for date in splited_list:
            st = datetime.datetime.strptime(start_time, '%Y-%m-%d')
            et = datetime.datetime.strptime(end_time, '%Y-%m-%d')
            nt = datetime.datetime.strptime(date, '%Y-%m-%d')
            self.assert_True(st <= nt <= et, '验证，{} <= {} <= {}'.format(st, nt, et))

    def public_select_group(self, open_window_loc, confirm_loc, group):
        """
        打开群聊弹窗，并选择群聊
        :param confirm_loc: 确认选择按钮的元素定位
        :param open_window_loc: 打开弹窗的元素定位
        :param group: 需要搜索选择的群组(支持string及list)
        :return:
        """
        self.click_element(self.find_Element(open_window_loc))  # 点击群聊输入框，进入群聊选择框
        sleep(2)
        if isinstance(group, str):
            self.send_keys(self.find_Element(self._input_addname), group)  # 输入群聊名称
            sleep(1)
            self.click_element(self.find_Element(self._btn_group_search))   # 点击查询
            sleep(2)
            # self.click_element(self.find_Element(self._btn_adder))  # 选择搜索结果
            self.click_element(self.find_Element((By.XPATH, "//div[@class='cell' and text()='%s']" % group)))
            sleep(2)
        elif isinstance(group, list):
            for i in group:
                self.send_keys(self.find_Element(self._input_addname), i)  # 输入添加人姓名
                sleep(1)
                self.click_element(self.find_Element(self._btn_group_search))   # 点击查询
                sleep(2)
                # self.click_element(self.find_Element(self._btn_adder))  # 选择搜索结果
                self.click_element(self.find_Element((By.XPATH, "//div[@class='cell' and text()='%s']" % i)))
                sleep(2)
        else:
            raise TypeError
        self.click_element(self.find_Element(confirm_loc))  # 点击确认
        sleep(2)


