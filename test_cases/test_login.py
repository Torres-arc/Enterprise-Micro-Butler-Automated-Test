from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
admin = get_config('3.1_www')  # 读取注册管理员账号


class TestAdminManage(MyTest, LoginPage):
    """测试用户登录时"""
    def test_login_01(self):
        # 验证测试时输入用户名和密码
        self.login(admin['username'], admin['password'])
