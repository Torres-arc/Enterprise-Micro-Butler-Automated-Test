from time import sleep

from common.myunit import MyTest
from pages.ClientMarketing.client_group_code_page import ClientGroupCodePage
from pages.public_page import PublicPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
cgcp = get_config('client_group_code_page')


class TestClientGroupCode(MyTest, ClientGroupCodePage, PublicPage):
    def test_TestClientGroupCode_01_createCode(self):
        # 创建活码
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.click_element(self.find_Element(self._btn_add_client_group_code))  # 点击新建活码
        sleep(2)
        self.click_element(self.find_Element(self._btn_create))  # 点击创建
        sleep(2)
        self.creat_code(cgcp['actname'], cgcp['actscene'], cgcp['guide'])  # 输入信息
        self.click_element(self.find_Element(self._btn_next_step1))  # 进入下一步
        sleep(2)
        self.click_element(self.find_Element(self._btn_add_reality_group_code))
        sleep(2)
        self.add_reality_code(cgcp['groupname'], cgcp['date'])  # 添加实际群码
        sleep(2)
        self.click_element(self.find_Element(self._btn_next_step2))  # 进入下一步
        sleep(2)
        self.force_scroll_screen()
        self.click_element(self.find_Element(self._btn_finish))  # 滚动屏幕并点击完成
        sleep(3)
        self.check_exist_in_page(cgcp['actname'])
        self.check_exist_in_page(cgcp['actscene'])  # 验证页面是否存在数据

    def test_TestClientGroupCode_02_manageCode(self):
        # 管理实际群码
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.click_element(self.find_Element(self._btn_manage_client_group))  # 进入管理群聊页面
        sleep(2)
        self.click_element(self.find_Element(self._btn_manage_edit))  # 编辑群聊
        sleep(2)
        self.add_reality_code(cgcp['groupname2'], cgcp['date2'], 1)  # 编辑实际群码
        self.check_exist_in_page(cgcp['groupname2'])
        self.check_exist_in_page(cgcp['date2'])  # 验证页面是否存在数据

    def test_TestClientGroupCode_03_editCode(self):
        # 编辑群活码
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.click_element(self.find_Element(self._btn_enter_details))  # 进入详情页
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_code))  # 点击编辑按钮
        sleep(2)
        self.creat_code(cgcp['actname1'], cgcp['actscene1'], status=1)  # 输入信息
        self.click_element(self.find_Element(self._btn_edit_confirm))  # 点击编辑完成
        sleep(2)
        self.assert_reality_code(cgcp['actname1'], cgcp['actscene1'])  # 验证数据正确

    def test_TestClientGroupCode_04_deleteCode(self):
        # 删除活码
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.click_element(self.find_Element(self._btn_enter_details))  # 进入详情页
        sleep(2)
        self.delete_code()  # 删除活码
        self.check_not_exist_in_page(cgcp['actname1'])  # 验证数据正确

    def test_TestClientGroupCode_05_searchByKeys(self):
        # 搜索关键词
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_key_words, cgcp['search_key'], self._btn_search)  # 搜索关键词
        self.assert_search_by_keys(cgcp['search_key'])  # 验证数据正确


