from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.send_SOP_page import SendSopPage
admin = get_config('3.1_www')  # 读取注册管理员账号
attach_msg = get_config('sop', 'attach_msg')    # 搜索附件

group_sop_name = get_config('sop', 'group_sop_name')    # 客户群的sop名称
edit_group_sop_name = get_config('sop', 'edit_group_sop_name')  # 客户群的sop名称修改
group_sop_limit = get_config('sop', 'group')    # 客户群的sop群组
group_submit_name = get_config('sop', 'group_submit_name')  # 客户群的推送名称
edit_group_submit_name = get_config('sop', 'edit_group_submit_name')    # 客户群的推送名称修改
group_msg = get_config('sop', 'group_msg')  # 客户群推送内容
edit_group_msg = get_config('sop', 'edit_group_msg')    # 客户群的推送内容修改

friends_circle_sop_name = get_config('sop', 'friends_circle_sop_name')     # 朋友圈的sop名称
edit_friends_circle_sop_name = get_config('sop', 'edit_friends_circle_sop_name')    # 朋友圈的sop名称修改
staff = get_config('sop', 'staff')  # 朋友圈的职工姓名
friends_circle_submit_name = get_config('sop', 'friends_circle_submit_name') # 朋友圈的推送名称
edit_friends_circle_submit_name = get_config('sop', 'edit_friends_circle_submit_name') # 朋友圈的推送名称修改
friends_circle_msg = get_config('sop', 'friends_circle_msg')    # 朋友圈推送内容
edit_friends_circle_msg = get_config('sop', 'edit_friends_circle_msg')  # 朋友圈的推送内容修改

class TestSendSop(MyTest, LoginPage, SendSopPage):
    """测试个人群发"""
    def test_TestSendSop_01(self):
        # 验证员工群发客户群任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        try:
            self.delete_sop(group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('client_group', group_sop_name, group_sop_limit, group_submit_name, group_msg, 'pic', attach_msg)
        # SOP类型：client_group客户群
        # SOP任务名称：group_sop_name
        # SOP执行范围：group_sop_limit
        # 推送名称：group_submit_name
        # 推送内容： group_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.assert_sop('client_group',group_sop_name, group_sop_limit, group_submit_name, group_msg)

    def test_TestSendSop_02(self):
        # 验证员工群发客户群任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        try:
            self.delete_sop(group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('client_group', group_sop_name, group_sop_limit, group_submit_name, group_msg, 'poster', attach_msg)
        # SOP类型：client_group客户群
        # SOP任务名称：group_sop_name
        # SOP执行范围：group_sop_limit
        # 推送名称：group_submit_name
        # 推送内容： group_msg
        # 附件类型： poster
        # 附件名称： attach_msg
        self.assert_sop('client_group',group_sop_name, group_sop_limit, group_submit_name, group_msg)

    def test_TestSendSop_03(self):
        # 验证员工群发客户群任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        try:
            self.delete_sop(group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('client_group', group_sop_name, group_sop_limit, group_submit_name, group_msg, 'web', attach_msg)
        # SOP类型：client_group客户群
        # SOP任务名称：group_sop_name
        # SOP执行范围：group_sop_limit
        # 推送名称：group_submit_name
        # 推送内容： group_msg
        # 附件类型： web
        # 附件名称： attach_msg
        self.assert_sop('client_group',group_sop_name, group_sop_limit, group_submit_name, group_msg)

    def test_TestSendSop_04(self):
        # 验证员工群发客户群任务后编辑
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        try:
            self.delete_sop(group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('client_group', group_sop_name, group_sop_limit, group_submit_name, group_msg, 'web', attach_msg)
        # SOP类型：client_group客户群
        # SOP任务名称：group_sop_name
        # SOP执行范围：group_sop_limit
        # 推送名称：group_submit_name
        # 推送内容： group_msg
        # 附件类型： web
        # 附件名称： attach_msg
        # self.assert_sop(group_sop_name, group_sop_limit, group_submit_name, group_msg)
        self.edit_sop(group_sop_name, edit_group_sop_name,edit_group_submit_name, edit_group_msg)
        # 修改SOP名称：edit_group_sop_name
        # 修改推送名称：edit_group_submit_name
        # 修改推送内容：edit_group_msg
        self.assert_sop('client_group',edit_group_sop_name, group_sop_limit, edit_group_submit_name, edit_group_msg, assert_type=0)

    def test_TestSendSop_05(self):
        # 验证员工群发客户群任务,进行搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        try:
            self.delete_sop(group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_group_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('client_group', group_sop_name, group_sop_limit, group_submit_name, group_msg, 'pic', attach_msg)
        # SOP类型：client_group客户群
        # SOP任务名称：group_sop_name
        # SOP执行范围：group_sop_limit
        # 推送名称：group_submit_name
        # 推送内容： group_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.search_by_input(self._input_group_sop_search, group_sop_name, self._btn_group_sop_search)  # 查询
        self.assert_sop('client_group',group_sop_name, group_sop_limit, group_submit_name, group_msg)

    def test_TestSendSop_06(self):
        # 验证员工群发朋友圈任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        self.switch_to_friends_circle_sop()     # 点击群发朋友圈任务
        try:
            self.delete_sop(friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('friends_circle', friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg, 'pic', attach_msg)
        # SOP类型：friends_circle客户群
        # SOP任务名称：friends_circle_sop_name
        # SOP执行范围：staff
        # 推送名称：friends_circle_submit_name
        # 推送内容： friends_circle_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.assert_sop('friends_circle',friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg)

    def test_TestSendSop_07(self):
        # 验证员工群发朋友圈任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        self.switch_to_friends_circle_sop()     # 点击群发朋友圈任务
        try:
            self.delete_sop(friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('friends_circle', friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg, 'poster', attach_msg)
        # SOP类型：friends_circle客户群
        # SOP任务名称：friends_circle_sop_name
        # SOP执行范围：staff
        # 推送名称：friends_circle_submit_name
        # 推送内容： friends_circle_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.assert_sop('friends_circle',friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg)

    def test_TestSendSop_08(self):
        # 验证员工群发朋友圈任务
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        self.switch_to_friends_circle_sop()     # 点击群发朋友圈任务
        try:
            self.delete_sop(friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('friends_circle', friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg, 'web', attach_msg)
        # SOP类型：friends_circle客户群
        # SOP任务名称：friends_circle_sop_name
        # SOP执行范围：staff
        # 推送名称：friends_circle_submit_name
        # 推送内容： friends_circle_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.assert_sop('friends_circle',friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg)

    def test_TestSendSop_09(self):
        # 验证员工群发朋友圈任务后进行编辑
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        self.switch_to_friends_circle_sop()     # 点击群发朋友圈任务
        try:
            self.delete_sop(friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('friends_circle', friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg, 'pic', attach_msg)
        # SOP类型：friends_circle客户群
        # SOP任务名称：friends_circle_sop_name
        # SOP执行范围：staff
        # 推送名称：friends_circle_submit_name
        # 推送内容： friends_circle_msg
        # 附件类型： pic
        # 附件名称： attach_msg
        self.edit_sop(friends_circle_sop_name, edit_friends_circle_sop_name,edit_friends_circle_submit_name, edit_friends_circle_msg)
        # 修改SOP名称：edit_friends_circle_sop_name
        # 修改推送名称：edit_friends_circle_submit_name
        # 修改推送内容：edit_friends_circle_msg
        self.assert_sop('friends_circle',edit_friends_circle_sop_name, staff, edit_friends_circle_submit_name, edit_friends_circle_msg, assert_type=0)

    def test_TestSendSop_10(self):
        # 验证员工群发朋友圈任务后进行搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_person_send()      # 点击个人群发
        self.switch_to_friends_circle_sop()     # 点击群发朋友圈任务
        try:
            self.delete_sop(friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        try:
            self.delete_sop(edit_friends_circle_sop_name)     # 尝试删除SOP后再去新建
        except:
            pass
        # 新建群发客户群任务
        self.new_sop('friends_circle', friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg, 'web', attach_msg)
        # SOP类型：friends_circle客户群
        # SOP任务名称：friends_circle_sop_name
        # SOP执行范围：staff
        # 推送名称：friends_circle_submit_name
        # 推送内容： friends_circle_msg
        # 附件类型： web
        # 附件名称： attach_msg
        self.search_by_input(self._input_friends_circle_sop_search, friends_circle_sop_name, self._btn_friends_circle_sop_search)  # 查询
        self.assert_sop('friends_circle',friends_circle_sop_name, staff, friends_circle_submit_name, friends_circle_msg)