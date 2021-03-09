from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.staff_welcome_page import StaffWelcome
admin = get_config('3.1_www')  # 读取注册管理员账号
welcome_message = get_config('welcoming_msg_page', 'msg')       # 读取欢迎语
welcome_message_edit = get_config('welcoming_msg_page', 'edited_msg')  # 读取修改的欢迎语


class TestStaffWelcome(MyTest, LoginPage, PublicPage, StaffWelcome):
    """测试员工欢迎语"""
    def test_TestStaffWelcome_01(self):
        # 验证员工新建欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        try:
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        self.new_welcome_message(welcome_message)   # 新建欢迎语
        self.assert_welcome_message(welcome_message)    # 验证第一条是该欢迎语

    def test_TestStaffWelcome_02(self):
        # 验证员工编辑欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        try:
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        self.new_welcome_message(welcome_message)   # 新建欢迎语
        self.edit_welcome_message(welcome_message, welcome_message_edit)    # 编辑，把老的改成新的
        self.assert_welcome_message(welcome_message_edit)   # 验证第一条欢迎语变成了最新的

    def test_TestStaffWelcome_03(self):
        # 验证搜索员工欢迎语
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_welcome_message()      # 点击欢迎语tab
        try:
            self.delete_welcome_message(welcome_message)    # 再尝试删除掉
        except:
            pass
        try:
            self.delete_welcome_message(welcome_message_edit)    # 再尝试删除掉
        except:
            pass
        self.new_welcome_message(welcome_message)   # 新建欢迎语
        self.search_by_input(self._input_client_search,welcome_message, self._btn_search)     # 搜索
        self.assert_welcome_message(welcome_message)   # 验证第一条欢迎语就是这条




