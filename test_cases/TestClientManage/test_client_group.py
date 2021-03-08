from time import sleep

from common.myunit import MyTest
from pages.ClientManage.client_group_page import ClientGroup
from pages.public_page import PublicPage
from common.statics import get_config
admin = get_config('3.1_www')  # 读取注册管理员账号
search_adder = get_config('client_group_page', 'master_name')
search_input = get_config('client_group_page', 'name')
search_start_time = get_config('client_group_page', 'start_time')
search_end_time = get_config('client_group_page', 'end_time')


class TestClient(MyTest, ClientGroup, PublicPage):
    """测试用户搜索（输入搜索）时，搜索结果是包含搜索关键词的"""
    def test_TestClientGroup_01_searchByName(self):
        # 验证搜索后，搜索结果是包含搜索关键词的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理
        self.switch_to_client_group()  # 进入客户群页面

        self.search_by_input(self._input_group_name, search_input)  # 输入search_input来进行搜索
        self.assert_search_input(self._texts_client_groups_names, search_input)  # 验证搜索值是否正确

    def test_TestClientGroup_02_searchByMasterName(self):
        # 验证搜索后，搜索结果与员工一致的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理
        self.switch_to_client_group()  # 进入客户群页面

        self.unfold_search_bar()
        self.public_select_staff(self._btn_select_group_master, self._btn_confirm, search_adder)  # 搜索目标员工
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_staff(self._texts_master_name, search_adder)  # 验证搜索结果与搜索员工一致

    def test_TestClientGroup_03_searchByDate(self):
        # 验证搜索后，搜索结果是符合日期要求的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理
        self.switch_to_client_group()  # 进入客户群页面

        self.select_date(search_start_time, search_end_time)  # 搜索目标日期内的数据
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_date(self._texts_create_time, search_start_time, search_end_time)  # 验证搜索结果符合日期范围一致

