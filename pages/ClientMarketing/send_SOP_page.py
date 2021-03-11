from selenium.webdriver.common.by import By
from common.base_page import BasePage
from Location.sop_loc import SopLoc
from pages.public_page import PublicPage
from common.statics import get_userid_info
from time import sleep

class SendSopPage(PublicPage, SopLoc):
    def switch_to_person_send(self):
        self.click_element(self.find_Element(self._btn_person_send))    # 点击个人群发

    def switch_to_group_sop(self):
        self.click_element(self.find_Element(self._btn_group_sop_page)) # 点击群SOP

    def switch_to_friends_circle_sop(self):
        self.click_element(self.find_Element(self._btn_friends_circle_page)) # 点击朋友圈SOP

    def new_sop(self, sop_type, sop_name, sop_limit, submit_name, submit_msg, attach_type, attach_name):   # 新建SOP
        """
        :param sop_type: client_group或者 friends_circle
        :param sop_name: sop的名称
        :param sop_limit: sop的范围，可以为人或者群聊
        :param submit_name: 推送名称
        :param submit_msg: 推送内容
        :param attach_type: 添加类型：pic,poster,web
        :param attach_name: 素材名称
        :return:
        """
        if sop_type == 'client_group':  # 判定如果是发送客户群的SOP
            self.click_element(self.find_Element(self._btn_group_sop_create))   # 点击新建任务
            sleep(1)
            self.send_keys(self.find_Element(self._input_act_name), sop_name)   # 填写名称
            sleep(1)
            self.public_select_group(self._btn_select_limit, self._btn_confirm, sop_limit)  # 选择某群组
        elif sop_type == 'friends_circle':   # 判定如果是发送朋友圈的SOP
            self.click_element(self.find_Element(self._btn_friends_circle_sop_create))      # 点击新建任务
            sleep(1)
            self.send_keys(self.find_Element(self._input_act_name), sop_name)   # 填写名称
            sleep(1)
            self.public_select_staff(self._btn_select_friends_circle_limit, self._btn_select_friends_circle_limit_sure, sop_limit)  # 选择某人
        else:
            print('sop_type只能是client_group或者friends_circle')
        self.send_keys(self.find_Element(self._input_submit_name), submit_name) # 填写推送名称
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_time))    # 点击时间选择器
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_start_time))  # 选择开始时间
        sleep(1)
        self.click_element(self.find_Element(self._btn_submit_end_time))    # 选择结束时间
        # sleep(5)
        # element = WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div')))
        self.wait_element_to_be_clickable(self._btn_time_sure)   # 等待元素可点击
        self.click_element(self.find_Element(self._btn_time_sure))  # 点击时间选择器的确认
        sleep(1)
        self.send_keys(self.find_Element(self._input_msg), submit_msg)  # 输入内容
        sleep(1)
        self.click_element(self.find_Element(self._btn_add_attach))     # 点击添加图片/海报/网页
        sleep(1)
        if attach_type == 'pic':
            self.click_element(self.find_Element(self._btn_pic))    # 点击图片
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_attach), attach_name)   # 输入该名称
            sleep(1)
            self.tap_keyboard('enter')
            sleep(1)
            self.click_element(self.find_Element(self._btn_select_attach_pic))  # 选择搜索出来的图片
            sleep(1)
        elif attach_type == 'poster':
            self.click_element(self.find_Element(self._btn_poster)) # 点击海报
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_attach), attach_name)   # 输入该名称
            sleep(1)
            self.tap_keyboard('enter')
            sleep(1)
            self.click_element(self.find_Element(self._btn_select_attach_poster))  # 选择搜索出来的海报
        elif attach_type == 'web':
            self.click_element(self.find_Element(self._btn_web))    # 点击网页
            sleep(1)
            self.send_keys(self.find_Element(self._input_search_attach), attach_name)   # 输入该名称
            sleep(1)
            self.tap_keyboard('enter')
            sleep(1)
            self.click_element(self.find_Element(self._btn_select_attach_web))  # 选择搜索出来的网页
        sleep(1)
        self.click_element(self.find_Element(self._btn_attach_sure))    # 点击确认
        sleep(1)
        target = self.find_Element(self._btn_new_sop)   # 找到新建按钮
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到指定位置
        self.click_element(target)    # 点击新建
        sleep(5)

    def delete_sop(self, sop_name):
        """
        :param sop_name:  需要删除的SOP名称
        :return:
        """
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % sop_name)))
        sleep(1)
        self.click_element(self.find_Element(self._btn_delete_sop)) # 点击删除
        sleep(1)
        self.click_element(self.find_Element(self._btn_delete_sop_sure))    # 确认删除
        sleep(2)

    def assert_sop(self, sop_type, sop_name, group_name, submit_name, submit_msg, assert_type=1):
        """
        :param sop_type:client_group或者 friends_circle
        :param assert_type: 由于编辑过后不会经历点击过程，故，默认为需要点击进去后验证，如果不需要，则=0
        :param sop_name: sop名称
        :param group_name   群名称/人名
        :param submit_name 推送名称
        :param submit_msg 推送内容
        :return:
        """
        sop_content = ''
        assert_group_name = ''
        if assert_type == 1:
            if sop_type == 'client_group':
                sop_content = self.get_element_value(self.find_Element(self._text_first_group_name))      # 获取到第一个的值的任务名称
            elif sop_type == 'friends_circle':
                sop_content = self.get_element_value(self.find_Element(self._text_first_friends_circle_name))      # 获取到第一个的值的任务名称
            self.assert_Equal(sop_name, sop_content)    # 验证是在第一个
            self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % sop_name)))
            sleep(2)
        elif assert_type == 0:
            pass
        assert_sop_name = self.get_element_value(self.find_Element(self._text_sop_name))    # 获取待验证的sop_name
        if sop_type == 'client_group':
            assert_group_name = self.get_element_value(self.find_Element(self._text_group_name))    # 获取待验证的group_name
        elif sop_type == 'friends_circle':
            assert_group_id = self.find_Element(self._text_staff_name).get_attribute('openid')
            assert_group_name=get_userid_info(assert_group_id)
        assert_submit_name = self.get_element_value(self.find_Element(self._text_submit_name))    # 获取待验证的submit_name
        assert_submit_msg = self.get_element_value(self.find_Element(self._text_submit_msg))    # 获取待验证的submit_msg
        assert_sop_name.strip()
        assert_group_name.strip()
        assert_submit_name.strip()
        assert_submit_msg.strip()
        self.assert_Equal(assert_sop_name,sop_name)
        self.assert_Equal(assert_group_name,group_name)
        self.assert_Equal(assert_submit_name,submit_name)
        self.assert_Equal(assert_submit_msg,submit_msg)

    def edit_sop(self, sop_name, edit_sop_name, edit_submit_name, edit_submit_msg):
        """

        :param sop_name: 原来的sop_name
        :param edit_sop_name: 修改后的sop_name
        :param edit_submit_name: 修改后的推送名
        :param edit_submit_msg:修改后的推送内容
        :return:
        """
        self.click_element(self.find_Element((By.XPATH, "//div[text()='%s']" % sop_name)))
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_sop)) # 点击编辑
        sleep(2)
        self.send_keys(self.find_Element(self._input_act_name), edit_sop_name)   # 填写名称
        sleep(1)
        self.send_keys(self.find_Element(self._input_submit_name), edit_submit_name) # 填写推送名称
        sleep(1)
        self.send_keys(self.find_Element(self._input_msg), edit_submit_msg)  # 输入内容
        sleep(1)
        self.click_element(self.find_Element(self._btn_save_sop))   # 点击保存
        sleep(5)
















