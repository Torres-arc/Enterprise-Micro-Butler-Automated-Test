from common.myunit import MyTest
from pages.login_page import LoginPage
from common.statics import get_config
from pages.public_page import PublicPage
from pages.ClientMarketing.fission_action_page import FissionActionPage
admin = get_config('3.1_www')  # 读取注册管理员账号
attach_msg = get_config('fission_action', 'fission_poster')    # 海报信息
# 任务裂变
mission_fission_name = get_config('fission_action', 'mission_fission_name')    # 任务裂变名称
mission_fission_guide = get_config('fission_action', 'mission_fission_guide')   # 任务裂变引导语
mission_fission_number = get_config('fission_action', 'mission_fission_number')     # 任务裂变客户数量
mission_fission_start_member = get_config('fission_action', 'mission_fission_start_member')     # 任务裂变发起人
mission_fission_tag = get_config('fission_action', 'mission_fission_tag')       # 任务裂变标签
mission_fission_gift = get_config('fission_action', 'mission_fission_gift')     # 兑奖码



# edit_group_sop_name = get_config('sop', 'edit_group_sop_name')  # 客户群的sop名称修改
# group_sop_limit = get_config('sop', 'group')    # 客户群的sop群组
# group_submit_name = get_config('sop', 'group_submit_name')  # 客户群的推送名称
# edit_group_submit_name = get_config('sop', 'edit_group_submit_name')    # 客户群的推送名称修改
# group_msg = get_config('sop', 'group_msg')  # 客户群推送内容
# edit_group_msg = get_config('sop', 'edit_group_msg')    # 客户群的推送内容修改
# # 群裂变
# friends_circle_sop_name = get_config('sop', 'friends_circle_sop_name')     # 朋友圈的sop名称
# edit_friends_circle_sop_name = get_config('sop', 'edit_friends_circle_sop_name')    # 朋友圈的sop名称修改
# staff = get_config('sop', 'staff')  # 朋友圈的职工姓名
# friends_circle_submit_name = get_config('sop', 'friends_circle_submit_name') # 朋友圈的推送名称
# edit_friends_circle_submit_name = get_config('sop', 'edit_friends_circle_submit_name') # 朋友圈的推送名称修改
# friends_circle_msg = get_config('sop', 'friends_circle_msg')    # 朋友圈推送内容
# edit_friends_circle_msg = get_config('sop', 'edit_friends_circle_msg')  # 朋友圈的推送内容修改

class TestSendSop(MyTest, LoginPage, FissionActionPage):
    """测试裂变活动"""
    def test_TestSendSop_01(self):
        # 验证员工新建任务裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        # 新建任务裂变
        self.new_fission('mission_fission',mission_fission_name, mission_fission_guide,mission_fission_number, attach_msg,mission_fission_gift,'group_helper',
                         fission_start_member='all',fission_tag='all')
        # 裂变类型: mission_fission
        # 任务名称：mission_fission_name
        # 裂变引导语：mission_fission_guide
        # 裂变人数：mission_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：mission_fission_gift
        # 下发途径：group_helper
        # 活动发起成员：fission_start_member='all'
        # 客户标签：fission_tag='all'
        self.assert_fission('mission_fission',mission_fission_name,mission_fission_guide,mission_fission_number,mission_fission_gift,'group_helper',
                            fission_start_member='all', fission_tag='all')

    def test_TestSendSop_02(self):
        # 验证员工新建任务裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        # 新建任务裂变
        self.new_fission('mission_fission',mission_fission_name, mission_fission_guide,mission_fission_number, attach_msg,mission_fission_gift,'group_helper',
                         fission_start_member=mission_fission_start_member,fission_tag='all')
        # 裂变类型: mission_fission
        # 任务名称：mission_fission_name
        # 裂变引导语：mission_fission_guide
        # 裂变人数：mission_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：mission_fission_gift
        # 下发途径：group_helper
        # 活动发起成员：fission_start_member=mission_fission_start_member
        # 客户标签：fission_tag='all'
        self.assert_fission('mission_fission',mission_fission_name,mission_fission_guide,mission_fission_number,mission_fission_gift,'group_helper',
                            fission_start_member=mission_fission_start_member,fission_tag='all')

    def test_TestSendSop_03(self):
        # 验证员工新建任务裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        # 新建任务裂变
        self.new_fission('mission_fission',mission_fission_name, mission_fission_guide,mission_fission_number, attach_msg,mission_fission_gift,'group_helper',
                         fission_start_member=mission_fission_start_member,fission_tag=mission_fission_tag)
        # 裂变类型: mission_fission
        # 任务名称：mission_fission_name
        # 裂变引导语：mission_fission_guide
        # 裂变人数：mission_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：mission_fission_gift
        # 下发途径：group_helper
        # 活动发起成员：fission_start_member=mission_fission_start_member
        # 客户标签：fission_tag=mission_fission_tag
        self.assert_fission('mission_fission',mission_fission_name,mission_fission_guide,mission_fission_number,mission_fission_gift,'group_helper',
                            fission_start_member=mission_fission_start_member,fission_tag=mission_fission_tag)

    def test_TestSendSop_04(self):
        # 验证员工新建任务裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        # 新建任务裂变
        self.new_fission('mission_fission',mission_fission_name, mission_fission_guide,mission_fission_number, attach_msg,mission_fission_gift,'admin_helper',
                         fission_start_member='all',fission_tag=mission_fission_tag)
        # 裂变类型: mission_fission
        # 任务名称：mission_fission_name
        # 裂变引导语：mission_fission_guide
        # 裂变人数：mission_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：mission_fission_gift
        # 下发途径：admin_helper
        # 活动发起成员：fission_start_member='all'
        # 客户标签：fission_tag=mission_fission_tag
        self.assert_fission('mission_fission',mission_fission_name,mission_fission_guide,mission_fission_number,mission_fission_gift,'admin_helper',
                            fission_start_member='all',fission_tag=mission_fission_tag)

    def test_TestSendSop_05(self):
        # 验证员工新建任务裂变后，进行搜索
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        # 新建任务裂变
        self.new_fission('mission_fission',mission_fission_name, mission_fission_guide,mission_fission_number, attach_msg,mission_fission_gift,'admin_helper',
                         fission_start_member='all',fission_tag=mission_fission_tag)
        # 裂变类型: mission_fission
        # 任务名称：mission_fission_name
        # 裂变引导语：mission_fission_guide
        # 裂变人数：mission_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：mission_fission_gift
        # 下发途径：admin_helper
        # 活动发起成员：fission_start_member='all'
        # 客户标签：fission_tag=mission_fission_tag
        self.search_fission('mission_fission',mission_fission_name)