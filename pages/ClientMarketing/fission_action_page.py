from selenium.webdriver.common.by import By
from common.base_page import BasePage
from Location.fission_action_loc import FissionActionLoc
from pages.public_page import PublicPage
from common.statics import get_userid_info
from time import sleep

class FissionActionPage(PublicPage, FissionActionLoc):
    def switch_to_fission_action(self):
        self.click_element(self.find_Element(self._btn_fission_action))     # 点击裂变活动

    def switch_to_group_fission(self):
        self.click_element(self.find_Element(self._btn_group_fission))      # 点击群裂变

    def new_fission(self, fission_type, fission_name, fission_guide, fission_number, fission_poster, gift, fission_load, fission_start_member=None, fission_tag=None,
                    fission_group=None, add_code=None):    # 创建裂变
        """
        :param fission_type:mission_fission和group_fission裂变类型
        :param fission_name:裂变名称
        :param fission_guide:裂变引导语
        :param fission_number:裂变人数
        :param  fission_start_member:发起成员
        :param fission_tag: 客户标签
        :param fission_group: 客户群
        :param fission_poster: 裂变海报
        :param add_code: 添加活码
        :param gift: 兑奖码
        :param fission_load:活动下发途径:group_helper, admin_helper
        :return:
        """
        """
        mission_fission(任务裂变):fission_type,fission_name,fission_guide,fission_number,fission_start_member,fission_tag,fission_poster,gift.fission_load
        group_fission(群裂变):fission_type,fission_name,fission_guide,fission_number,fission_group,fission_poster，add_code,gift,fission_load
        """
        if fission_type == 'mission_fission':   # 如果是任务裂变
            self.click_element(self.find_Element(self._btn_new_mission_fission))    # 点击新建任务裂变
        elif fission_type == 'group_fission':   # 如果是群裂变
            self.click_element(self.find_Element(self._btn_new_group_fission))      # 点击新建群裂变
        else:
            print('fission_type只能是mission_fission或者group_fission')
        self.send_keys(self.find_Element(self._input_fission_name), fission_name)   # 输入裂变名称
        self.send_keys(self.find_Element(self._input_fission_msg), fission_guide)  # 输入裂变引导语
        self.send_keys(self.find_Element(self._input_fission_number), fission_number)   # 输入裂变人数
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_time))    # 点击时间
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_start_time))  # 点击明天为开始时间
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_end_time))    # 点击下个月1号为结束时间
        sleep(1)
        self.wait_element_to_be_clickable(self._btn_time_sure)  # 等待按钮可以点击
        self.click_element(self.find_Element(self._btn_time_sure))  # 点击按钮
        sleep(1)
        if fission_type == 'mission_fission':   # 如果是任务裂变
            if fission_start_member == 'all':   # 发起成员如果是all，则pass
                pass
            else:
                self.click_element(self.find_Element(self._btn_select_start_staff)) # 点击选择成员
                self.public_select_staff(self._btn_fission_select_staff, self._btn_fission_select_staff_sure, fission_start_member) # 具体选择成员
            if fission_tag == 'all':    # 如果客户标签是all，则pass
                pass
            else:
                self.click_element(self.find_Element(self._btn_select_start_tag))   # 点击选择标签
                self.select_tag_by_name(self._btn_fission_select_tag, self._btn_fission_select_tag_sure, fission_tag)   # 具体选择标签
        elif fission_type == 'group_fission':   # 如果是群裂变
            if fission_group == 'all':  # 群裂变客户群如果是all，则pass
                pass
            else:
                self.click_element(self.find_Element(self._btn_select_start_group)) # 点击选择群主
                self.public_select_staff(self._btn_select_group, self._btn_select_group_sure, fission_group) # 具体选择群主
        self.click_element(self.find_Element(self._btn_fission_poster))     # 点击裂变海报
        sleep(1)
        self.send_keys(self.find_Element(self._input_fission_search_poster), fission_poster)    # 添加裂变海报
        sleep(1)
        self.tap_keyboard('enter')
        self.click_element(self.find_Element(self._btn_fission_select_poster))  # 选择海报
        self.click_element(self.find_Element(self._btn_fission_select_poster_sure))     # 点击确定
        if fission_type == 'mission_fission':   # 如果是任务裂变
            # self.public_select_staff(self._btn_fission_add_staff, self._btn_fission_add_staff_sure, add_staff) # 具体选择成员
            pass
        elif fission_type == 'group_fission':   # 如果是群裂变
            self.select_group_code(self._btn_select_group_code,self._input_select_group_code, self._btn_select_group_code_search, self._btn_select_group_code_name,
                                   self._btn_select_group_code_sure, add_code)  # 具体选择群活码
        gift_loc = self.find_Element(self._input_gift)
        self.driver.execute_script("arguments[0].scrollIntoView();", gift_loc)  # 滑动到指定位置
        self.send_keys(self.find_Element(self._input_gift), gift)   # 输入兑奖码
        if fission_load == 'group_helper':
            pass
        elif fission_load == 'admin_helper':
            self.click_element(self.find_Element(self._btn_admin_load))     # 点击管理员统一群发
        save_loc = self.find_Element(self._btn_fission_save)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_loc)  # 滑动到指定位置
        self.click_element(self.find_Element(self._btn_read_introduction))  # 勾选已阅读
        self.click_element(self.find_Element(self._btn_fission_save))   # 点击保存
        sleep(5)
        self.wait_element_to_be_clickable(self._btn_fission_action)     # 出现裂变活动（意味着新建后已经跳转了）

    def assert_fission(self, fission_type, fission_name, fission_guide, fission_number, fission_gift, fission_load,
                       fission_start_member=None,fission_tag=None, fission_group=None):
        """
        :param fission_type:mission_fission和group_fission裂变类型
        :param fission_name: 验证的裂变名称
        :param fission_guide: 验证的裂变引导语
        :param fission_number: 裂变客户数量
        :param fission_gift: 兑奖码
        :param fission_load: 活动下发途径
        :param fission_start_member:活动发起成员
        :param fission_tag: 客户标签
        :param fission_group：活动发起群主
        :return:
        """
        assert_fission_name = ''
        if fission_type == 'mission_fission':
            assert_fission_name = self.get_element_value(self.find_Element(self._text_first_mission_fission))     # 获取到第一条信息的裂变名称
        elif fission_type == 'group_fission':
            assert_fission_name = self.get_element_value(self.find_Element(self._text_first_group_fission))     # 获取到第一条信息的裂变名称
        self.assert_Equal(assert_fission_name, fission_name)    # 验证名称一致
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % fission_name)))  # 点进去后查看
        sleep(2)
        assert_fission_name_page = self.get_element_value(self.find_Element(self._text_check_fission_name))    # 获取裂变名称值
        assert_fission_guide = self.get_element_value(self.find_Element(self._text_check_fission_guide))    # 获取裂变引导语
        assert_fission_number = self.get_element_value(self.find_Element(self._text_check_fission_number))  # 获取裂变客户数
        assert_fission_gift = self.get_element_value(self.find_Element(self._text_check_gift))  # 获取兑奖码
        assert_fission_load = self.get_element_value(self.find_Element(self._text_check_load))  # 获取活动下发途径
        self.assert_Equal(assert_fission_name_page.strip(), fission_name)   # 验证页面名称一致
        self.assert_Equal(assert_fission_guide.strip(), fission_guide)  # 验证引导语一致
        self.assert_Equal(assert_fission_number.strip(), fission_number+'人')    # 验证裂变客户数一致
        self.assert_Equal(assert_fission_gift.strip(), fission_gift)    # 验证兑换码一致
        if fission_load == 'group_helper':
            self.assert_Equal(assert_fission_load.strip(), '客户群群发助手')   # 验证下发途径一致，都是：客户群群发助手
        elif fission_load == 'admin_helper':
            self.assert_Equal(assert_fission_load.strip(), '管理员统一群发消息') # 验证下发途径一致，都是：管理员统一群发消息
        if fission_type == 'mission_fission':
            if fission_start_member == 'all':   # 如果是任务裂变，活动发起成员选择全部
                assert_fission_start_member = self.get_element_value(self.find_Element(self._text_check_start_staff))   # 获取活动发起成员
                self.assert_Equal(assert_fission_start_member.strip(), '全部')    # 验证活动发起成员显示全部
            else:   # 否则就是具体人名
                assert_fission_start_member_id = self.find_Element(self._text_check_start_staff_id).get_attribute('openid') # 获取活动发起人成员
                assert_fission_start_member=get_userid_info(assert_fission_start_member_id)
                self.assert_Equal(assert_fission_start_member, fission_start_member)    # 验证人名一致
            if fission_tag == 'all':    # 如果是任务裂变，客户标签选择全部
                assert_fission_tag = self.get_element_value(self.find_Element(self._text_check_tag))    # 获取客户标签
                self.assert_Equal(assert_fission_tag.strip(), '全部') # 验证客户标签选的是全部
            else:   # 否则就是具体的标签名
                assert_fission_tag = self.get_element_value(self.find_Element(self._text_check_tag_name))   # 获取客户标签的具体值
                self.assert_Equal(assert_fission_tag.strip(), fission_tag)  # 验证标签名一致
        elif fission_type == 'group_fission':
            if fission_group == 'all':  # 如果是群裂变，活动发起群主选择全部
                assert_fission_group = self.get_element_value(self.find_Element(self._text_check_start_group))  # 获取活动发起群主
                self.assert_Equal(assert_fission_group.strip(), '全部')   # 验证活动发起群显示全部
            else:   # 如果是群裂变，活动发起群主具体选择了
                assert_fission_start_group_id = self.find_Element(self._text_check_start_group_id).get_attribute('openid') # 获取群主的id
                assert_fission_start_group=get_userid_info(assert_fission_start_group_id)
                self.assert_Equal(assert_fission_start_group, fission_group)    # 验证活动发起群主人名一致


    def search_fission(self,fission_type,fission_name):
        """
        :param fission_type:mission_fission和group_fission裂变类型
        :param fission_name:    裂变名称
        :return:
        """
        if fission_type == 'mission_fission':
            self.search_by_input(self._input_mission_fission_search,fission_name, self._btn_mission_fission_search)
        elif fission_type == 'group_fission':
            self.search_by_input(self._input_group_fission_search, fission_name, self._btn_group_fission_search)
        # 验证搜索结果
        assert_fission_name = ''
        if fission_type == 'mission_fission':
            assert_fission_name = self.get_element_value(self.find_Element(self._text_first_mission_fission))     # 获取到第一条信息的裂变名称
        elif fission_type == 'group_fission':
            assert_fission_name = self.get_element_value(self.find_Element(self._text_first_group_fission))     # 获取到第一条信息的裂变名称
        self.assert_Equal(assert_fission_name, fission_name)    # 验证名称一致

























