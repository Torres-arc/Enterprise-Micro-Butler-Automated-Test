import os

from common.base_page import BasePage
from Location.client_code_loc import ClientCodeLoc
from time import sleep
from selenium.webdriver.common.by import By
from common.statics import get_userid_list, get_userid_info


class ClientCodePage(BasePage, ClientCodeLoc):
    def select_code_type(self, type):
        """
        根据type值，决定创建什么类型活码
        :param type:  'single':单人;'batch':批量单人;'multi':多人;
        :return:
        """
        if type == 'single':
            self.click_element(self.find_Element(self._btn_type_single))
        elif type == 'batch':
            self.click_element(self.find_Element(self._btn_type_batch_single))
        else:
            self.click_element(self.find_Element(self._btn_type_multi))
        sleep(2)

    def edit_code(self):
        self.click_element(self.find_Element(self._btn_check_detail))  # 进入详情页
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit))  # 进入编辑页
        sleep(2)

    def delete_code(self):
        self.click_element(self.find_Element(self._btn_check_detail))  # 进入详情页
        sleep(2)
        self.click_element(self.find_Element(self._btn_single_delete))  # 点击删除
        sleep(2)
        self.click_element(self.find_Element(self._btn_single_delete_confirm))  # 删除二次确认
        sleep(2)

    def delete_code_in_batch(self):
        self.click_element(self.find_Element(self._btn_check_box))
        sleep(1)
        self.click_element(self.find_Element(self._btn_delete))
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))
        sleep(2)

    def select_wel(self, msg_type, msg, wel):
        """
        根据类型，决定发送什么类型的欢迎语
        :param msg_type:  'web':网页;'poster':海报;'mini':小程序;
        :param msg:  网页、小程序的搜索条件
        :param wel:   欢迎语文本
        :return:
        """
        self.send_keys(self.find_Element(self._input_welcomg), wel)  # 输入欢迎语
        sleep(1)
        self.click_element(self.find_Element(self._btn_welcoming_speech_button))  # 展开欢迎语类型选择框
        sleep(2)
        if msg_type == 'pic':  # 选择图片
            self.click_element(self.find_Element(self._btn_wel_pic))
            sleep(2)
            mte_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + msg)
            self.tap_keyboard('shift')
            self.control_keyboard(mte_path)
            sleep(1)
            self.tap_keyboard('enter')
        elif msg_type == 'web':
            self.click_element(self.find_Element(self._btn_wel_web))
            sleep(2)
            self.send_keys(self.find_Element(self._input_search_web), msg)
            sleep(2)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_web))
            sleep(1)
            self.click_element(self.find_Element(self._btn_web_sure))
        elif msg_type == 'mini':
            self.click_element(self.find_Element(self._btn_wel_mini))
            sleep(2)
            self.send_keys(self.find_Element(self._input_search_web), msg)
            sleep(2)
            self.tap_keyboard('enter')
            sleep(2)
            self.click_element(self.find_Element(self._btn_select_mini))
            sleep(1)
            self.click_element(self.find_Element(self._btn_mini_sure))
        sleep(2)
        self.click_element(self.find_Element(self._btn_save))  # 点击新建按钮
        sleep(2)

    def assert_search_user(self, staff):
        # 验证使用员工查询
        a_list = self.find_Elements(self._texts_creator)
        for i in range(len(a_list)):

            # 由于使用员工可能有多个，需要逐行读取
            id_list = self.find_Elements((By.CSS_SELECTOR, self._texts_user.format(i + 1)))
            # 使用员工为多个
            if isinstance(id_list, list):
                cell = []
                for x in id_list:
                    cell.append(x.get_attribute('openid'))
                self.check_exist_in_lists(staff, get_userid_list(cell))
            # 使用员工为单个
            else:
                cell = get_userid_info(id_list.get_attribute('openid'))
                self.assert_Equal(staff, cell)

    def assert_details(self, msglist):
        lists = [self.get_element_value(self.find_Element(self._text_act_scene)),
                 get_userid_info((self.find_Element(self._text_user)).get_attribute('openid')),
                 self.get_element_value(self.find_Element(self._text_wel_speech))]
        tag_list = self.get_elements_values(self.find_Elements(self._texts_tag_list))  # 获取详情页内信息
        for i, x in enumerate(lists):
            self.assert_Equal(x, msglist[i])  # 与预设值比较验证

        cur_list = globals()['msg']
        tag_list.sort()
        cur_list.sort()
        self.assert_Equal(cur_list, tag_list)  # 验证标签列表是否一致
