from selenium.webdriver.common.by import By
from common.base_page import BasePage
from Location.key_group_loc import KeyGroupLoc
from pages.public_page import PublicPage
from common.statics import get_userid_info
from time import sleep

class KeyGroup(PublicPage, KeyGroupLoc):
    def switch_to_marking_add(self):
        self.click_element(self.find_Element(self._btn_marking_add))    # 点击营销插件
        sleep(1)

    def switch_to_quick_group(self):
        self.click_element(self.find_Element(self._btn_quick_group))    # 点击快速拉群
        sleep(1)

    def new_key_group(self, mission_name, mission_guide, key_word, key_code):
        """

        :param mission_name:任务名称
        :param mission_guide:入群引导语
        :param key_word:关键词
        :param key_code:群活码
        :return:
        """
        self.click_element(self.find_Element(self._btn_new_key_group))  # 点击关键词拉群
        self.send_keys(self.find_Element(self._input_key_group), mission_name)  # 输入活动名称
        self.send_keys(self.find_Element(self._input_key_group_guide), mission_guide)   # 输入入群引导语
        # 添加关键词
        self.click_element(self.find_Element(self._btn_add_key))    # 点击添加关键词
        sleep(1)
        self.send_keys(self.find_Element(self._input_add_key), key_word)    # 输入关键词
        self.click_element(self.find_Element(self._btn_add_key_sure))   # 点击确定
        sleep(1)
        # 选择群活码
        self.select_group_code(self._btn_add_key_code, self._input_key_code_search, self._btn_key_code_search, self._btn_key_group_select_code,
                               self._btn_key_group_select_code_sure, key_code)     # 选择群活码
        sleep(2)
        self.click_element(self.find_Element(self._btn_key_group_sure)) # 点击确定
        self.wait_element_to_be_clickable(self._btn_marking_add)    # 等待营销插件可点击，即为跳转了
        sleep(5)

    def assert_key_group(self, mission_name, key_word):
        """

        :param mission_name: 任务名称
        :param key_word:关键词
        :return:
        """
        assert_mission_name = self.get_element_value(self.find_Element(self._text_first_key_group_name))    # 获取第一行的任务名称
        assert_key_word = self.get_element_value(self.find_Element(self._text_first_key_name))  # 获取第一行的关键词
        self.assert_Equal(assert_mission_name.strip(), mission_name)   # 验证任务名称一致
        self.assert_Equal(assert_key_word.strip(), key_word)    # 验证关键词一致

    def edit_key_group(self, old_mission_name, new_mission_name, old_key_word, new_key_word, old_mission_guide, new_mission_guide):
        """

        :param old_mission_name: 老的任务名
        :param new_mission_name: 编辑后的任务名
        :param old_key_word: 老的关键词
        :param new_key_word: 编辑后的关键词
        :param old_mission_guide: 老的入群引导语
        :param new_mission_guide: 新的入群引导语
        :return:
        """
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']/../..//li[text()=' 编辑 ']" % old_mission_name)))     # 点击进入
        sleep(5)
        assert_old_mission_name = self.find_Element(self._input_key_group).get_attribute('value')   # 获取到任务名称输入框的值
        assert_old_key_word = self.get_element_value(self.find_Element(self._text_key_code_page))   # 获取到关键词
        assert_old_mission_guide = self.find_Element(self._input_key_group_guide).get_attribute('value')   # 获取到入群引导语输入框的值
        print(assert_old_mission_name)
        print(assert_old_key_word)
        print(assert_old_mission_guide)
        self.assert_Equal(assert_old_mission_name, old_mission_name)    # 验证老的任务名称是对的
        self.assert_Equal(assert_old_key_word, old_key_word)    # 验证老的关键词是对的
        self.assert_Equal(assert_old_mission_guide, old_mission_guide)  # 验证老的入群引导语是对的
        # 验证完老数据后，开始填写新数据
        self.send_keys(self.find_Element(self._input_key_group), new_mission_name)  # 输入新的活动名称
        self.send_keys(self.find_Element(self._input_key_group_guide), new_mission_guide)   # 输入入群引导语
        # 更换关键词
        self.click_element(self.find_Element((By.XPATH, "//span[text()='%s']/i" % old_key_word)))   # 点击老的关键词的x按钮
        self.click_element(self.find_Element(self._btn_add_key))    # 点击添加关键词
        sleep(1)
        self.send_keys(self.find_Element(self._input_add_key), new_key_word)    # 输入关键词
        self.click_element(self.find_Element(self._btn_add_key_sure))   # 点击确定
        sleep(1)
        self.click_element(self.find_Element(self._btn_key_group_sure)) # 点击确定
        self.wait_element_to_be_clickable(self._btn_marking_add)    # 等待营销插件可点击，即为跳转了
        sleep(5)


    def delete_key_group(self, mission_name):
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']/../..//span[text()='删除']" % mission_name)))
        sleep(2)
        self.click_element(self.find_Element(self._delete_sure_button))     # 点击确认删除
        sleep(5)
        assert_mission_name = self.get_element_value(self.find_Element(self._text_first_key_group_name))    # 获取第一行的任务名称
        self.assert_Not_Equal(assert_mission_name, mission_name)    # 不一致了

    def search_key_group(self, mission_name):
        self.send_keys(self.find_Element(self._input_key_group_search), mission_name)
        sleep(1)
        self.click_element(self.find_Element(self._btn_key_group_search))
        sleep(5)