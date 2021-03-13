from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.key_group_page import KeyGroup
admin = get_config('3.1_www')  # 读取注册管理员账号
# 快速拉群
quick_group_name = get_config('quick_group','quick_group_name') # 任务名称
quick_group_key = get_config('quick_group','quick_group_key')   # 关键词
quick_group_guide = get_config('quick_group','quick_group_guide')   # 入群引导语
quick_group_code = get_config('quick_group','quick_group_code')     # 群活码
# 编辑快速拉群
edit_quick_group_name = get_config('quick_group','edit_quick_group_name')  # 编辑的名称
edit_quick_group_key = get_config('quick_group', 'edit_quick_group_key')   # 编辑的关键词
edit_quick_group_guide = get_config('quick_group', 'edit_quick_group_guide')   # 编辑的入群引导语


class TestKeyGroup(MyTest, LoginPage, KeyGroup):
    """测试快速拉群"""
    def test_TestAddGroupChat_01(self):
        # 新建快速拉群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_marking_add()    # 点击营销插件
        self.switch_to_quick_group()    # 点击快速拉群
        self.new_key_group(quick_group_name,quick_group_guide,quick_group_key,quick_group_code)
        # 任务名称：quick_group_name
        # 入群引导语：quick_group_guide
        # 关键词：quick_group_key
        # 群活码：quick_group_code
        self.assert_key_group(quick_group_name,quick_group_key)

    def test_TestAddGroupChat_02(self):
        # 新建快速拉群后删除
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_marking_add()    # 点击营销插件
        self.switch_to_quick_group()    # 点击快速拉群
        self.new_key_group('自动化测试删除的',quick_group_guide,quick_group_key,quick_group_code)
        # 任务名称：quick_group_name
        # 入群引导语：quick_group_guide
        # 关键词：quick_group_key
        # 群活码：quick_group_code
        self.delete_key_group('自动化测试删除的')

    def test_TestAddGroupChat_03(self):
        # 新建快速拉群后编辑
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_marking_add()    # 点击营销插件
        self.switch_to_quick_group()    # 点击快速拉群
        self.new_key_group(quick_group_name,quick_group_guide,quick_group_key,quick_group_code)
        # 任务名称：quick_group_name
        # 入群引导语：quick_group_guide
        # 关键词：quick_group_key
        # 群活码：quick_group_code
        self.edit_key_group(quick_group_name,edit_quick_group_name,quick_group_key,edit_quick_group_key,quick_group_guide,edit_quick_group_guide)
        # 老的任务名quick_group_name
        # 新的任务名edit_quick_group_name
        # 老的关键词quick_group_key
        # 新建的关键词edit_quick_group_key
        # 老的入群引导语quick_group_guide
        # 新的入群引导语edit_quick_group_guide
        self.assert_key_group(edit_quick_group_name,edit_quick_group_key)

    def test_TestAddGroupChat_04(self):
        # 新建快速拉群
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_marking_add()    # 点击营销插件
        self.switch_to_quick_group()    # 点击快速拉群
        self.new_key_group(quick_group_name,quick_group_guide,quick_group_key,quick_group_code)
        # 任务名称：quick_group_name
        # 入群引导语：quick_group_guide
        # 关键词：quick_group_key
        # 群活码：quick_group_code
        self.search_key_group(quick_group_name) # 搜索
        self.assert_key_group(quick_group_name,quick_group_key) # 验证