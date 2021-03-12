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
# 群裂变
group_fission_name = get_config('fission_action', 'group_fission_name')     # 群裂变名称
group_fission_guide = get_config('fission_action', 'group_fission_guide')   # 群裂变引导语
group_fission_number = get_config('fission_action', 'group_fission_number') # 群裂变客户数量
group_fission_group = get_config('fission_action', 'group_fission_group')   # 群裂变客户群
group_fission_add_code = get_config('fission_action', 'group_fission_add_code') # 群裂变群活码
group_fission_gift = get_config('fission_action', 'group_fission_gift') # 群裂变兑奖码

class TestFissionAction(MyTest, LoginPage, FissionActionPage):
    """测试裂变活动"""
    def test_TestFissionAction_01(self):
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

    def test_TestFissionAction_02(self):
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

    def test_TestFissionAction_03(self):
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

    def test_TestFissionAction_04(self):
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

    def test_TestFissionAction_05(self):
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

    def test_TestFissionAction_06(self):
        # 验证员工新建群裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        self.switch_to_group_fission()      # 点击群裂变
        # 新建任务裂变
        self.new_fission('group_fission',group_fission_name, group_fission_guide,group_fission_number, attach_msg,group_fission_gift,'group_helper',
                         fission_group='all',add_code=group_fission_add_code)
        # 裂变类型: group_fission
        # 任务名称：group_fission_name
        # 裂变引导语：group_fission_guide
        # 裂变人数：group_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：group_fission_gift
        # 下发途径：group_helper
        # 选择客户群：fission_group='all'
        # 群活码：add_code=group_fission_add_code
        self.switch_to_group_fission()  # 点击群裂变
        self.assert_fission('group_fission',group_fission_name,group_fission_guide,group_fission_number,group_fission_gift,'group_helper',
                            fission_group='all')

    def test_TestFissionAction_07(self):
        # 验证员工新建群裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        self.switch_to_group_fission()      # 点击群裂变
        # 新建任务裂变
        self.new_fission('group_fission',group_fission_name, group_fission_guide,group_fission_number, attach_msg,group_fission_gift,'group_helper',
                         fission_group=group_fission_group,add_code=group_fission_add_code)
        # 裂变类型: group_fission
        # 任务名称：group_fission_name
        # 裂变引导语：group_fission_guide
        # 裂变人数：group_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：group_fission_gift
        # 下发途径：group_helper
        # 选择客户群：fission_group=group_fission_group
        # 群活码：add_code=group_fission_add_code
        self.switch_to_group_fission()  # 点击群裂变
        self.assert_fission('group_fission',group_fission_name,group_fission_guide,group_fission_number,group_fission_gift,'group_helper',
                            fission_group=group_fission_group)

    def test_TestFissionAction_08(self):
        # 验证员工新建群裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        self.switch_to_group_fission()      # 点击群裂变
        # 新建任务裂变
        self.new_fission('group_fission',group_fission_name, group_fission_guide,group_fission_number, attach_msg,group_fission_gift,'admin_helper',
                         fission_group=group_fission_group,add_code=group_fission_add_code)
        # 裂变类型: group_fission
        # 任务名称：group_fission_name
        # 裂变引导语：group_fission_guide
        # 裂变人数：group_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：group_fission_gift
        # 下发途径：admin_helper
        # 选择客户群：fission_group=group_fission_group
        # 群活码：add_code=group_fission_add_code
        self.switch_to_group_fission()  # 点击群裂变
        self.assert_fission('group_fission',group_fission_name,group_fission_guide,group_fission_number,group_fission_gift,'admin_helper',
                            fission_group=group_fission_group)

    def test_TestFissionAction_09(self):
        # 验证员工新建群裂变
        self.login(admin['username'], admin['password'])    # 登录
        self.switch_to_client_marketing_tab()   # 点击客户营销
        self.switch_to_fission_action()      # 点击裂变活动
        self.switch_to_group_fission()      # 点击群裂变
        # 新建任务裂变
        self.new_fission('group_fission',group_fission_name, group_fission_guide,group_fission_number, attach_msg,group_fission_gift,'admin_helper',
                         fission_group='all',add_code=group_fission_add_code)
        # 裂变类型: group_fission
        # 任务名称：group_fission_name
        # 裂变引导语：group_fission_guide
        # 裂变人数：group_fission_number
        # 裂变海报：attach_msg
        # 兑奖码：group_fission_gift
        # 下发途径：admin_helper
        # 选择客户群：fission_group='all'
        # 群活码：add_code=group_fission_add_code
        self.switch_to_group_fission()  # 点击群裂变
        # self.assert_fission('group_fission',group_fission_name,group_fission_guide,group_fission_number,group_fission_gift,'admin_helper',
        #                     fission_group='all')
        self.search_fission('group_fission', group_fission_name)