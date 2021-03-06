from common.base_page import BasePage
from Location.client_loc import ClientLoc
from common.statics import get_config
from time import sleep


class ClientPage(BasePage, ClientLoc):
    # def switch_to_current(self):
    #     self.click_element(self.find_Element(self._btn_client_manage_tab))  # 进入客户管理tab
    #     sleep(2)

    # def unfold_search_bar(self):
    #     self.click_element(self.find_Element(self._btn_more_filter))    # 展现隐藏搜索栏
    #     sleep(2)

    def switch_to_client(self):
        self.click_element(self.find_Element(self._btn_client_page))    # 点击客户
        sleep(2)