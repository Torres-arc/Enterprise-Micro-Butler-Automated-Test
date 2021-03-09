from time import sleep

from common.myunit import MyTest
# from pages.ClientManage.search_page import SearchPage
from pages.ClientManage.client_page import ClientPage
from pages.public_page import PublicPage
from common.statics import get_config
admin = get_config('3.1_www')  # 读取注册管理员账号
search_adder = get_config('client_page', 'adder')
search_input = get_config('client_page', 'name')
search_tag_group = get_config('client_page', 'tag_group31')
search_tag = get_config('client_page', 'tag31')


class TestClient(MyTest, ClientPage, PublicPage):
    """测试用户搜索（输入搜索）时，搜索结果是包含搜索关键词的"""
    def test_TestClient_01_searchByName(self):
        # 验证搜索后，搜索结果是包含搜索关键词的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理

        self.search_by_input(self._input_name, search_input, self._btn_search)  # 输入search_input来进行搜索
        self.assert_search_input(self._texts_clients_name, search_input)  # 验证搜索值是否正确

    def test_TestClient_02_searchByTag(self):
        # 验证搜索后，搜索结果是包含搜索标签的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理
        self.select_tag(self._btn_select_tag, self._btn_confirm, search_tag)    # 按照标签来进行搜索
        self.click_element(self.find_Element(self._btn_search))
        self.go_through_list_to_get_msg(self._texts_clients_name, self._texts_full_tags)  # 遍历所有详情页，获取完整标签信息
        self.assert_search_tag(search_tag)      # 验证搜索结果是包含标签的

    def test_TestClient_03_searchByAdder(self):
        # 验证搜索后，搜索结果是包含添加人的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_manage_tab()    # 切换到客户管理
        self.unfold_search_bar()
        self.public_select_staff(self._btn_select_adder, self._btn_confirm, search_adder)  # 搜索目标员工
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_staff(self._texts_clients_adders, search_adder)  # 验证搜索结果与搜索员工一致
