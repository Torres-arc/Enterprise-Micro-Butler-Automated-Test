from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.ClientMarketing.department_staff_welcome_page import DepartStaffWelcome
admin = get_config('3.1_www')  # 读取注册管理员账号
welcome_message = get_config('welcoming_msg_page', 'msg')       # 读取欢迎语
welcome_message_edit = get_config('welcoming_msg_page', 'edited_msg')  # 读取修改的欢迎语
staff_name = get_config('welcoming_msg_page','staff')       # 读取该人员
preview_message = get_config('welcoming_msg_page', 'preview_msg')   # 预留云书的部门员工欢迎语，防止出现被占用的情况

class TestDepartmentStaffWelcome(MyTest, LoginPage, DepartStaffWelcome):
    """测试部门员工欢迎语"""
    def test_TestDepartmentStaffWelcome_01(self):
        # 验证部门员工新建欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语
        try:
            self.search_by_input(self._input_department_client_search, welcome_message, self._btn_department_client_search)
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, welcome_message_edit,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, preview_message,self._btn_department_client_search)
            self.delete_welcome_message(preview_message)    # 再尝试删除掉
        except:
            pass
        self.driver.refresh()
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语,为了展示所有数据
        self.new_department_welcome_message(welcome_message, staff_name)   # 新建欢迎语
        self.assert_welcome_message(welcome_message)    # 验证第一条是该欢迎语

    def test_TestStaffWelcome_02(self):
        # 验证员工编辑欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语
        try:
            self.search_by_input(self._input_department_client_search, welcome_message,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, welcome_message_edit,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, preview_message,self._btn_department_client_search)
            self.delete_welcome_message(preview_message)    # 再尝试删除掉
        except:
            pass
        self.driver.refresh()
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语,为了展示所有数据
        self.new_department_welcome_message(welcome_message, staff_name)   # 新建欢迎语
        self.edit_department_welcome_message(welcome_message, welcome_message_edit, staff_name)    # 编辑，把老的改成新的
        self.assert_welcome_message(welcome_message_edit)   # 验证第一条欢迎语变成了最新的

    def test_TestStaffWelcome_03(self):
        # 验证搜索员工欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语
        try:
            self.search_by_input(self._input_department_client_search, welcome_message,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, welcome_message_edit,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, preview_message,self._btn_department_client_search)
            self.delete_welcome_message(preview_message)    # 再尝试删除掉
        except:
            pass
        self.driver.refresh()
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语,为了展示所有数据
        self.new_department_welcome_message(welcome_message, staff_name)   # 新建欢迎语
        self.search_by_input(self._input_department_client_search, welcome_message,self._btn_department_client_search)     # 搜索
        self.assert_welcome_message(welcome_message)   # 验证第一条欢迎语就是这条

    def test_TestStaffWelcome_04(self):
        # 由于存在唯一性，所有不论如何都要创建一条云书的数据占有该名称
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语
        try:
            self.search_by_input(self._input_department_client_search, welcome_message,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, welcome_message_edit,self._btn_department_client_search)
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        try:
            self.search_by_input(self._input_department_client_search, preview_message,self._btn_department_client_search)
            self.delete_welcome_message(preview_message)    # 再尝试删除掉
        except:
            pass
        self.driver.refresh()
        self.switch_to_department_staff_welcome_message()   # 点击部门员工欢迎语,为了展示所有数据
        self.new_department_welcome_message(preview_message, staff_name)   # 新建欢迎语
        self.assert_welcome_message(preview_message)    # 验证第一条是该欢迎语




