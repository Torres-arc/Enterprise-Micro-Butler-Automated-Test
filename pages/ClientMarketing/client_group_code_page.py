import os

from common.base_page import BasePage
from Location.client_group_code_loc import ClientGroupCodeLoc
from time import sleep
from selenium.webdriver.common.by import By
from common.statics import get_userid_list, get_userid_info


class ClientGroupCodePage(BasePage, ClientGroupCodeLoc):
    def switch_to_current(self):
        self.click_element(self.find_Element(self._btn_client_group_tab))
        sleep(2)

    def creat_code(self, act_name, act_scene, guide=None, status=0):
        if status == 0:
            self.click_element(self.find_Element(self._btn_activity_picture))
            sleep(1)
            self.upload_file('\\materials\\pic\\photo.png')
            self.send_keys(self.find_Element(self._input_leadding_words), guide)
            sleep(1)
        self.send_keys(self.find_Element(self._input_activity_name), act_name)
        sleep(2)
        sleep(1)
        self.send_keys(self.find_Element(self._input_activity_scene), act_scene)
        sleep(1)

    def delete_code(self):
        self.click_element(self.find_Element(self._btn_edit_delete))
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_delete_confirm))
        sleep(2)

    def add_reality_code(self, group_name, date, status=0):
        if status == 0:
            self.click_element(self.find_Element(self._btn_reality_group_code))
            sleep(2)
            self.upload_file('\\materials\\pic\\groupcode.jpg')
        self.click_element(self.find_Element(self._btn_select_client_group))
        sleep(2)
        self.send_keys(self.find_Element(self._input_group_name), group_name)
        sleep(2)
        self.click_element(self.find_Element(self._btn_search_client_group))
        sleep(2)
        self.click_element(self.find_Element(self._btn_select_specify_group))
        sleep(2)
        self.click_element(self.find_Element(self._btn_client_group_confirm))
        sleep(2)
        self.send_keys(self.find_Element(self._input_expire_date), date)
        sleep(2)
        self.click_element(self.find_Element(self._btn_sure))
        sleep(2)

    def assert_search_by_keys(self, keys):
        actnames = self.get_elements_values(self.find_Elements(self._texts_act_names))
        actscenes = self.get_elements_values(self.find_Elements(self._texts_act_scenes))
        text = []
        for i in range(len(actnames)):
            text.append([])
            text[i].append(actnames[i])
            text[i].append(actscenes[i])
        for i in text:
            st = ','.join(i)
            self.check_exist_in_lists(keys, st)
