from common.myunit import MyTest
from pages.ClientManage.search_page import SearchPage
from pages.public_page import PublicPage
from pages.ClientManage.client_page import ClientPage
from common.statics import get_config
admin = get_config('3.1_www')  # 读取注册管理员账号
search_input = get_config('client_page', 'name')
adder = get_config('client_page', 'adder')


class TestClient(MyTest, SearchPage, ClientPage, PublicPage):
    """测试用户搜索（输入搜索）时，搜索结果是包含搜索关键词的"""

    def test_TestClient_01(self):
        # 验证搜索后，搜索结果是包含搜索关键词的
        self.login(admin['username'], admin['password'])
        self.click_element(self.find_Element(self._btn_client_manage_tab))     # 点击客户管理
        self.click_element(self.find_Element(self._btn_client_page))    # 点击客户
        self.search_by_input(search_input)  # 输入search_input来进行搜索
        self.assert_search_input(search_input)  # 验证搜索值是否正确

    def test_TestClient_02_searchByAdder(self):
        self.login(admin['username'], admin['password'])
        self.switch_to_current()
        self.unfold_search_bar()
        self.puclic_search_by_client(adder)
        self.common_search(self._text_pages_number, self._texts_clients_adders, self._btn_next, adder)
