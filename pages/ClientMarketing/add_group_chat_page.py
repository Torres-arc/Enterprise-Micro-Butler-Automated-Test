from selenium.webdriver.common.by import By
from common.base_page import BasePage
from Location.add_group_chat_loc import AddGroupChatLoc
from pages.public_page import PublicPage
from common.statics import get_userid_info
from time import sleep

class AddGroupChat(PublicPage, AddGroupChatLoc):
    def switch_to_add_group(self):
        self.click_element(self.find_Element(self._btn_add_group_chat))     # 点击拉群工具

    def switch_to_old_client_tag_group(self):
        self.click_element(self.find_Element(self._btn_old_client_tag_group))   # 点击老客标签建群

    def new_add_group(self, add_type, mission_name, group_guide, add_code,add_group_staff=None, add_group_tag=None, send_limit=None, send_type=None):
        """
        :param add_type: 创建拉群类型add_group_chat和add_tag_group
        :param mission_name: 任务名称
        :param group_guide :  入群引导语
        :param add_code :选择群活码
        :param add_group_staff:添加使用员工名称
        :param add_group_tag: 选择标签
        :param send_limit: 发送范围，可以选择人
        :param send_type: 发送方式：企业群发enterprise/个人群发person
        :return:
        """
        if add_type == 'add_group_chat':    # 如果是自动拉群
            self.click_element(self.find_Element(self._btn_new_add_group))  # 点击新建自动拉群
        elif add_type == 'add_tag_group':   # 如果是标签拉群
            self.click_element(self.find_Element(self._btn_new_tag_group))  # 点击新建标签进群
        self.send_keys(self.find_Element(self._input_mission_name), mission_name)   # 输入任务名称
        self.send_keys(self.find_Element(self._input_into_group_guide), group_guide)    # 输入入群引导语
        if add_type == 'add_group_chat':    # 如果是自动拉群
            self.public_select_staff(self._btn_add_group_staff, self._btn_add_group_staff_sure, add_group_staff)  # 添加员工
            if add_group_tag == 'all':  # 如果新客户标签不选择
                pass
            else:
                self.select_tag_by_name(self._btn_add_group_tag, self._btn_add_group_tag_sure, add_group_tag)   # 否则就需要寻找标签了
        elif add_type == 'add_tag_group':   # 如果是标签拉群
            if send_limit == 'all':
                pass
            else:
                self.click_element(self.find_Element(self._btn_group_select_client))    # 点击按照条件筛选客户
                self.public_select_staff(self._btn_add_tag_group_staff, self._btn_add_tag_group_staff_sure, send_limit) # 发送范围选择了人
            if send_type == 'enterprise':   # 如果是企业群发
                pass
            elif send_type == 'person':     # 如果是个人群发
                self.click_element(self.find_Element(self._btn_tag_group_person))   # 点击个人群发
        self.select_group_code(self._btn_add_group_code, self._input_add_group_code, self._btn_add_group_code_search, self._btn_add_group_code_select,
                               self._btn_add_group_code_sure, add_code)     # 选择群活码
        self.click_element(self.find_Element(self._btn_add_group_send))     # 点击发送
        self.wait_element_to_be_clickable(self._btn_add_group_chat)     # 等待出现了页面了
        sleep(5)

    def assert_group_chat(self,add_type, mission_name,group_guide,add_group_staff=None, add_group_tag=None, send_limit=None, send_type=None):
        """
        :param add_type: 创建拉群类型add_group_chat和add_tag_group
        :param mission_name: 任务名称
        :param group_guide :  入群引导语
        :param add_group_staff:添加使用员工名称
        :param add_group_tag: 选择标签
        :param send_limit: 发送范围，可以选择人
        :param send_type: 发送方式：企业群发enterprise/个人群发person
        :return:
        """
        assert_mission_name = ''
        if add_type == 'add_group_chat':    # 如果是自动拉群
            assert_mission_name = self.get_element_value(self.find_Element(self._text_first_add_group))     # 获取到第一行的任务名
        elif add_type == 'add_tag_group':   # 如果是标签拉群
            assert_mission_name = self.get_element_value(self.find_Element(self._text_first_tag_group))     # 获取到第一行的任务名
            assert_send_type =  self.get_element_value(self.find_Element(self._text_first_tag_send))    # 获取到第一行的发送方式
            if send_type == 'enterprise':
                self.assert_Equal(assert_send_type.strip(), '企业群发')        # 验证发送方式是一样的
            elif send_type == 'person':
                self.assert_Equal(assert_send_type.strip(), '个人群发')        # 验证发送方式是一样的
        self.assert_Equal(assert_mission_name, mission_name)    # 验证与第一条的名称一致
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % mission_name)))  # 点进去后查看
        sleep(2)
        if add_type == 'add_group_chat':    # 如果是自动拉群
            assert_mission_name_page = self.get_element_value(self.find_Element(self._text_add_group_name))     # 获取页面里的任务名称
            self.assert_Equal(assert_mission_name_page.strip(), mission_name)   # 验证任务名称一致
            assert_staff_id = self.find_Element(self._text_add_group_staff_id).get_attribute('openid')  # 获取页面里使用成员id
            assert_staff=get_userid_info(assert_staff_id)
            self.assert_Equal(assert_staff, add_group_staff)    # 验证使用成员一致
            assert_group_guide = self.get_element_value(self.find_Element(self._text_add_group_guide))  # 获取页面里的引导语
            self.assert_Equal(assert_group_guide.strip(), group_guide)  # 验证引导语一致
            if add_group_tag == 'all':  # 如果tag没有选择，则不验证
                pass
            else:
                assert_group_tag = self.get_element_value(self.find_Element(self._text_add_group_tag))  # 获取客户标签
                self.assert_Equal(assert_group_tag, add_group_tag)  # 验证标签一致
        elif add_type == 'add_tag_group':   # 如果是标签拉群
            if send_limit == 'all':  # 如果发送给全部群，没人名就不验证
                pass
            else:
                assert_send_limit_id = self.find_Element(self._text_add_tag_group_staff_id).get_attribute('openid')  # 获取页面里添加人员id
                assert_send_limit=get_userid_info(assert_send_limit_id) # 获取到添加人员
                self.assert_Equal(assert_send_limit, send_limit)    # 验证添加人一致

    def search_group_chat(self, add_type, mission_name):
        assert_mission_name = ''
        if add_type == 'add_group_chat':
            self.search_by_input(self._input_add_group_chat, mission_name, self._btn_group_chat_search)
            assert_mission_name = self.get_element_value(self.find_Element(self._text_first_add_group))     # 获取到第一行的任务名
        elif add_type == 'add_tag_group':
            self.search_by_input(self._input_tag_group, mission_name, self._btn_tag_group_search)
            assert_mission_name = self.get_element_value(self.find_Element(self._text_first_tag_group))     # 获取到第一行的任务名
        self.assert_Equal(assert_mission_name, mission_name)    # 验证与第一条的名称一致


    def delete_group_chat(self, mission_name):
        # 删除 新客自动拉群
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % mission_name)))  # 点进去后查看
        # 点击删除
        self.click_element(self.find_Element(self._btn_delete_add_group))   # 点击删除
        sleep(1)
        self.click_element(self.find_Element(self._btn_delete_add_group_sure))  # 确定
        sleep(5)


