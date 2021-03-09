from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.send_enterprise_message_page import SendEnterpriseMessage
admin = get_config('3.1_www')  # 读取注册管理员账号
staff = get_config('add_message_page', 'sender')
msg = get_config('add_message_page', 'msg')

class TestSendEnterpriseMessage(MyTest, LoginPage, SendEnterpriseMessage):
    """测试企业群发"""
    def test_TestSendEnterpriseMessage_01(self):
        # 验证员工新建欢迎语，测试发送给客户，发送给全部客户,text
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', 'all', 'text', msg)  # 发送给客户，全部客户，text类型
        self.assert_enterprise_message('client', 'text', msg)   # 验证

    def test_TestSendEnterpriseMessage_02(self):
        # 验证员工新建欢迎语，测试发送给客户，发送给全部客户,pic
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', 'all', 'pic', msg)  # 发送给客户，全部客户，pic类型
        self.assert_enterprise_message('client', 'pic', msg)   # 验证

    def test_TestSendEnterpriseMessage_03(self):
        # 验证员工新建欢迎语，测试发送给客户，发送给全部客户,poster
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', 'all', 'poster', msg)  # 发送给客户，全部客户，poster类型
        self.assert_enterprise_message('client', 'poster', msg)   # 验证

    def test_TestSendEnterpriseMessage_04(self):
        # 验证员工新建欢迎语，测试发送给客户，发送给全部客户,web
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', 'all', 'web', msg)  # 发送给客户，全部客户，web类型
        self.assert_enterprise_message('client', 'web', msg)   # 验证

    def test_TestSendEnterpriseMessage_05(self):
        # 验证员工新建欢迎语，测试发送给客户，发送给全部客户,mini
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', 'all', 'mini', msg)  # 发送给客户，全部客户，mini类型
        self.assert_enterprise_message('client', 'mini', msg)   # 验证

    def test_TestSendEnterpriseMessage_06(self):
        # 验证员工新建欢迎语，测试发送给客户，按条件筛选客户,text
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', staff, 'text', msg)  # 发送给客户，按staff筛选， text类型
        self.assert_enterprise_message('client', 'text', msg)    # 验证

    def test_TestSendEnterpriseMessage_07(self):
        # 验证员工新建欢迎语，测试发送给客户，按条件筛选客户,pic
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', staff, 'pic', msg)  # 发送给客户，按staff筛选， pic类型
        self.assert_enterprise_message('client', 'pic', msg)    # 验证

    def test_TestSendEnterpriseMessage_08(self):
        # 验证员工新建欢迎语，测试发送给客户，按条件筛选客户,poster
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', staff, 'poster', msg)  # 发送给客户，按staff筛选， poster类型
        self.assert_enterprise_message('client', 'poster', msg)    # 验证

    def test_TestSendEnterpriseMessage_09(self):
        # 验证员工新建欢迎语，测试发送给客户，按条件筛选客户,web
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', staff, 'web', msg)  # 发送给客户，按staff筛选， web类型
        self.assert_enterprise_message('client', 'web', msg)    # 验证

    def test_TestSendEnterpriseMessage_10(self):
        # 验证员工新建欢迎语，测试发送给客户，按条件筛选客户,mini
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client', staff, 'mini', msg)  # 发送给客户，按staff筛选， mini类型
        self.assert_enterprise_message('client', 'mini', msg)    # 验证

    def test_TestSendEnterpriseMessage_11(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,text
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'text', msg)  # 发送给客户群，按群主选择客户群,text
        self.assert_enterprise_message('client_group', 'text', msg)    # 验证

    def test_TestSendEnterpriseMessage_12(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,pic
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'pic', msg)  # 发送给客户群，按群主选择客户群,pic
        self.assert_enterprise_message('client_group', 'pic', msg)    # 验证

    def test_TestSendEnterpriseMessage_13(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,poster
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'poster', msg)  # 发送给客户群，按群主选择客户群,poster
        self.assert_enterprise_message('client_group', 'poster', msg)    # 验证

    def test_TestSendEnterpriseMessage_14(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,web
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'web', msg)  # 发送给客户群，按群主选择客户群,web
        self.assert_enterprise_message('client_group', 'web', msg)    # 验证

    def test_TestSendEnterpriseMessage_15(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,mini
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'mini', msg)  # 发送给客户群，按群主选择客户群,mini
        self.assert_enterprise_message('client_group', 'mini', msg)    # 验证

    def test_TestSendEnterpriseMessage_16(self):
        # 验证员工新建欢迎语，测试发送给客户群，按群主选择客户群,web，后搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_enterprise_send_message()      # 点击企业群发
        self.send_enterprise_message('client_group', staff, 'web', msg)  # 发送给客户群，按群主选择客户群,poster
        self.assert_enterprise_message('client_group', 'web', msg)    # 验证
        self.search_enterprise_message('web', msg)
        self.assert_enterprise_message('client_group', 'web', msg)    # 验证


