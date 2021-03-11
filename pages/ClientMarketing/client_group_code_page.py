from common.base_page import BasePage
from Location.client_group_code_loc import ClientGroupCodeLoc
from pages.public_page import PublicPage
from time import sleep


class ClientGroupCodePage(BasePage, ClientGroupCodeLoc, PublicPage):
    def switch_to_current(self):
        self.click_element(self.find_Element(self._btn_client_group_tab))
        sleep(2)

    def creat_code(self, act_name, act_scene, guide=None, status=0):
        """
        群活码信息输入
        :param act_name:  活动名称文本
        :param act_scene:  活动场景文本
        :param guide:   引导语文本
        :param status:  状态：0 or 其他（0的话，才会上传图片及输入引导语，适用于初次创建，若是编辑的话，status不要为0）
        :return:
        """
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
        self.click_element(self.find_Element(self._btn_edit_delete))  # 点击删除
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_delete_confirm))  # 二次删除
        sleep(2)

    def add_reality_code(self, group_name, date, status=0):
        """
        添加实际群码
        :param group_name:  群名文本
        :param date:  日期文本
        :param status: 状态：0 or 其他（0的话，才会上传图片，适用于初次创建，若是编辑的话，status不要为0）
        :return:
        """
        if status == 0:
            self.click_element(self.find_Element(self._btn_reality_group_code))
            sleep(2)
            self.upload_file('\\materials\\pic\\groupcode.jpg')
        self.select_group_code(self._btn_select_client_group, self._input_group_name,
                               self._btn_search_client_group, self._btn_select_specify_group,
                               self._btn_client_group_confirm, group_name)
        self.send_keys(self.find_Element(self._input_expire_date), date)
        sleep(2)
        self.click_element(self.find_Element(self._btn_sure))
        sleep(2)

    def assert_reality_code(self, act_name, act_scene):
        # 判断实际群码的群名及有效期
        acn = self.get_element_value(self.find_Element(self._text_act_name))
        acs = self.get_element_value(self.find_Element(self._text_act_info))
        self.assert_Equal(acn, act_name)
        self.assert_Equal(acs, act_scene)

    def assert_search_by_keys(self, keys):
        # 验证搜索关键词是否存在于 活动姓名与活动场景 中
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
