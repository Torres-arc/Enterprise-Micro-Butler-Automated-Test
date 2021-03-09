from selenium.webdriver.common.by import By
from common.base_page import BasePage
# from Location.welcome_message_loc import WelcomeMessageLoc
from common.statics import get_userid_list
from pages.public_page import PublicPage
from time import sleep
from common.statics import get_userid_info

class DepartStaffWelcome(PublicPage):
    def switch_to_welcome_message(self):
        sleep(1)
        self.click_element(self.find_Element(self._btn_welcome_page))   # 进入欢迎语

    def switch_to_department_staff_welcome_message(self):
        sleep(2)
        self.click_element(self.find_Element(self._btn_department_client_tab))  # 进入部门员工欢迎语tab

    def new_department_welcome_message(self, welcome_message, staff): # 新建欢迎语
        self.click_element(self.find_Element(self._btn_create_department_client_welcome))  # 点击新建部门员工欢迎语
        sleep(1)
        self.public_select_staff(self._btn_select_staff, self._btn_confirm, staff)      # 选择staff员工
        sleep(1)
        self.send_keys(self.find_Element(self._input_welcome), welcome_message)     # 输入欢迎语
        sleep(1)
        self.click_element(self.find_Element(self._btn_insert_client_nickname))     # 点击插入客户昵称
        sleep(1)
        self.click_element(self.find_Element(self._btn_create))     # 点击新建
        sleep(2)

    def assert_welcome_message(self, welcome_message):  # 验证欢迎语出现在第一个位置
        first_message = self.get_element_value(self.find_Element(self._texts_department_client_welcome))      # 获取到第一个的值
        print(first_message)
        first_message.strip()   # 去掉前后空格
        self.assert_Equal(welcome_message+'#客户昵称#', first_message)   # 验证是一致的

    def delete_welcome_message(self, welcome_message):  # 删除欢迎语
        sleep(2)
        self.click_element(self.find_Element((By.XPATH, "//div[contains(text(),'%s')]/../../..//span[text()='删除']" % welcome_message)))   # 点击该欢迎语后续的删除按钮
        sleep(2)
        self.click_element(self.find_Element(self._btn_client_delete_confirm))  # 删除后的确认按钮
        sleep(2)

    def edit_department_welcome_message(self, old_welcome_message, new_welcome_message, staff_name):   # 编辑欢迎语，分老的和更改后的,新增验证出现了该员工人名
        sleep(2)
        self.click_element(self.find_Element((By.XPATH, "//div[contains(text(),'%s')]/../../..//span[text()='编辑']" % old_welcome_message)))   # 点击该欢迎语后续的编辑按钮
        sleep(2)
        staff_id = self.find_Element(self._text_user_open_id).get_attribute('openid')
        print(staff_id)
        staff_name_assert=get_userid_info(staff_id)
        print(staff_name_assert)
        self.assert_Equal(staff_name, staff_name_assert)    # 验证名字一样
        self.send_keys(self.find_Element(self._input_welcome), new_welcome_message)     # 输入欢迎语
        sleep(1)
        self.click_element(self.find_Element(self._btn_insert_client_nickname))     # 点击插入客户昵称
        sleep(1)
        self.click_element(self.find_Element(self._btn_save))     # 点击保存
        sleep(2)

