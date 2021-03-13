from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.add_group_chat_page import AddGroupChat
admin = get_config('3.1_www')  # 读取注册管理员账号
group_code = get_config('add_group', 'group_code')  # 群活码
# 自动拉群
auto_group_name = get_config('add_group', 'auto_group_name')    # 任务名称
auto_group_staff = get_config('add_group', 'auto_group_staff')  # 使用员工
auto_group_tag = get_config('add_group', 'auto_group_tag')  # 新客户标签
auto_group_guide = get_config('add_group', 'auto_group_guide')  # 入群引导语
default_auto_group_name = get_config('add_group', 'default_auto_group_name')    # 任务名称
# 老客标签拉群
tag_group_name = get_config('add_group', 'tag_group_name')  # 任务名称
tag_group_guide = get_config('add_group', 'tag_group_guide')    # 入群引导语
tag_group_staff = get_config('add_group','tag_group_staff')     # 条件筛选用户


class TestAddGroupChat(MyTest, LoginPage, AddGroupChat):
    """测试拉群工具"""
    def test_TestAddGroupChat_01(self):
        # 验证员工新建自动拉群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        try:
            self.search_group_chat('add_group_chat', auto_group_name)
            self.delete_group_chat(auto_group_name)     # 尝试删除
        except:
            pass
        try:
            self.search_group_chat('add_group_chat', default_auto_group_name)
            self.delete_group_chat(default_auto_group_name)     # 尝试删除
        except:
            pass
        self.driver.refresh()   # 刷新
        # 新建拉群
        self.new_add_group('add_group_chat',auto_group_name, auto_group_guide,group_code, add_group_staff=auto_group_staff, add_group_tag=auto_group_tag)
        # 拉群类型: add_group_chat
        # 任务名称：auto_group_name
        # 入群引导语：auto_group_guide
        # 选择群活码：group_code
        # 使用员工：add_group_staff=auto_group_staff
        # 新客户标签：add_group_tag=auto_group_tag
        self.assert_group_chat('add_group_chat',auto_group_name,auto_group_guide,add_group_staff=auto_group_staff, add_group_tag=auto_group_tag)

    def test_TestAddGroupChat_02(self):
        # 验证员工新建自动拉群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        try:
            self.search_group_chat('add_group_chat', auto_group_name)
            self.delete_group_chat(auto_group_name)     # 尝试删除
        except:
            pass
        try:
            self.search_group_chat('add_group_chat', default_auto_group_name)
            self.delete_group_chat(default_auto_group_name)     # 尝试删除
        except:
            pass
        self.driver.refresh()   # 刷新
        # 新建拉群
        self.new_add_group('add_group_chat',auto_group_name, auto_group_guide,group_code, add_group_staff=auto_group_staff, add_group_tag='all')
        # 拉群类型: add_group_chat
        # 任务名称：auto_group_name
        # 入群引导语：auto_group_guide
        # 选择群活码：group_code
        # 使用员工：add_group_staff=auto_group_staff
        # 新客户标签：add_group_tag='all'
        self.assert_group_chat('add_group_chat',auto_group_name,auto_group_guide,add_group_staff=auto_group_staff, add_group_tag='all')

    def test_TestAddGroupChat_03(self):
        # 验证员工新建自动拉群，搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        try:
            self.search_group_chat('add_group_chat', auto_group_name)
            self.delete_group_chat(auto_group_name)     # 尝试删除
        except:
            pass
        try:
            self.search_group_chat('add_group_chat', default_auto_group_name)
            self.delete_group_chat(default_auto_group_name)     # 尝试删除
        except:
            pass
        self.driver.refresh()   # 刷新
        # 新建拉群
        self.new_add_group('add_group_chat',auto_group_name, auto_group_guide,group_code, add_group_staff=auto_group_staff, add_group_tag='all')
        # 拉群类型: add_group_chat
        # 任务名称：auto_group_name
        # 入群引导语：auto_group_guide
        # 选择群活码：group_code
        # 使用员工：add_group_staff=auto_group_staff
        # 新客户标签：add_group_tag='all'
        # self.assert_group_chat('add_group_chat',auto_group_name,auto_group_guide,add_group_staff=auto_group_staff, add_group_tag='all')
        self.search_group_chat('add_group_chat', auto_group_name)

    def test_TestAddGroupChat_04(self):
        # 验证员工新建自动拉群,需要占用云书的账号，防止自动化时重复
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        try:
            self.search_group_chat('add_group_chat', auto_group_name)
            self.delete_group_chat(auto_group_name)     # 尝试删除
        except:
            pass
        try:
            self.search_group_chat('add_group_chat', default_auto_group_name)
            self.delete_group_chat(default_auto_group_name)     # 尝试删除
        except:
            pass
        self.driver.refresh()   # 刷新
        # 新建拉群
        self.new_add_group('add_group_chat',default_auto_group_name, auto_group_guide,group_code, add_group_staff=auto_group_staff, add_group_tag='all')
        # 拉群类型: add_group_chat
        # 任务名称：auto_group_name
        # 入群引导语：auto_group_guide
        # 选择群活码：group_code
        # 使用员工：add_group_staff=auto_group_staff
        # 新客户标签：add_group_tag='all'
        self.assert_group_chat('add_group_chat',default_auto_group_name,auto_group_guide,add_group_staff=auto_group_staff, add_group_tag='all')

    def test_TestAddGroupChat_05(self):
        # 验证员工新建老客标签建群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        self.switch_to_old_client_tag_group()   # 点击老客标签拉群
        # 新建拉群
        self.new_add_group('add_tag_group',tag_group_name, tag_group_guide,group_code, send_limit='all', send_type='enterprise')
        # 拉群类型: add_group_chat
        # 任务名称：tag_group_name
        # 入群引导语：tag_group_guide
        # 选择群活码：group_code
        # 发送范围：send_limit='all'：发送给全部客户
        # 发送方式：send_type='enterprise'：企业群发
        self.assert_group_chat('add_tag_group',tag_group_name,tag_group_guide,send_limit='all', send_type='enterprise')

    def test_TestAddGroupChat_06(self):
        # 验证员工新建老客标签建群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        self.switch_to_old_client_tag_group()   # 点击老客标签拉群
        # 新建拉群
        self.new_add_group('add_tag_group',tag_group_name, tag_group_guide,group_code, send_limit='all', send_type='person')
        # 拉群类型: add_group_chat
        # 任务名称：tag_group_name
        # 入群引导语：tag_group_guide
        # 选择群活码：group_code
        # 发送范围：send_limit='all'：发送给全部客户
        # 发送方式：send_type='person'：个人群发
        self.assert_group_chat('add_tag_group',tag_group_name,tag_group_guide,send_limit='all', send_type='person')

    def test_TestAddGroupChat_07(self):
        # 验证员工新建老客标签建群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        self.switch_to_old_client_tag_group()   # 点击老客标签拉群
        # 新建拉群
        self.new_add_group('add_tag_group',tag_group_name, tag_group_guide,group_code, send_limit=tag_group_staff, send_type='person')
        # 拉群类型: add_group_chat
        # 任务名称：tag_group_name
        # 入群引导语：tag_group_guide
        # 选择群活码：group_code
        # 发送范围：send_limit=tag_group_staff：发送给tag_group_staff
        # 发送方式：send_type='person'：个人群发
        self.assert_group_chat('add_tag_group',tag_group_name,tag_group_guide,send_limit=tag_group_staff, send_type='person')

    def test_TestAddGroupChat_08(self):
        # 验证员工新建老客标签建群，后搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_add_group()   # 点击拉群工具
        self.switch_to_old_client_tag_group()   # 点击老客标签拉群
        # 新建拉群
        self.new_add_group('add_tag_group',tag_group_name, tag_group_guide,group_code, send_limit=tag_group_staff, send_type='enterprise')
        # 拉群类型: add_group_chat
        # 任务名称：tag_group_name
        # 入群引导语：tag_group_guide
        # 选择群活码：group_code
        # 发送范围：send_limit=tag_group_staff：发送给tag_group_staff
        # 发送方式：send_type='person'：个人群发
        # self.assert_group_chat('add_tag_group',tag_group_name,tag_group_guide,send_limit=tag_group_staff, send_type='enterprise')
        self.search_group_chat('add_tag_group', tag_group_name)