from common.myunit import MyTest
from pages.login_page import LoginPage
# from Page.AdminManage.admin import Admin
from common.statics import get_config
import time
admin = get_config('3.1_www')  # 读取注册管理员账号
# wdgly = get_config('3.1_www')  # 读取文档管理员账号
# ptgly = get_config('3.1_www')  # 读取普通管理员账号


class TestAdminManage(MyTest, LoginPage):

    def test_TestAdminManage_01(self):
        pass
    #     """登录并且创建各种管理员"""
    #     self.login(admin['username'], admin['password'])  # 登录
    #     self.wait_element(self.my_file_loc)
    #     self.into_console()  # 进入控制台
    #     self.element_click(self.admin_manage_loc)   # 点击管理员管理
    #     self.element_click(self.admin_manage_inner_loc)  # 点击管理员管理里的管理员管理
    #     try:
    #         self.delete_admin(ptgly['name'])  # 删除普通管理员
    #         self.delete_admin(wdgly['name'])  # 删除文档管理员
    #     except:
    #         pass
    #     self.new_admin('普通管理员', ptgly['name'])      # 添加普通管理员
    #     self.new_admin('文档管理员', wdgly['name'])  # 添加普通管理员