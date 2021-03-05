from common.base_page import BasePage
from Location.client_manager_loc import ClientManagerLoc
from time import sleep

class SearchPage(BasePage,ClientManagerLoc):
    def search_by_input(self, search_input):
        # 通过输入方式来搜索
        self.send_keys(self.find_Element(self._input_name), search_input)  # 输入
        sleep(1)
        self.click_element(self.find_Element(self._btn_search))     # 点击搜索
        sleep(1)

    def assert_search_input(self, search_input):
        # 通过输入方式来搜索后，验证里面的值都是包含输入的值
        clients = self.get_elements_values(self.find_Elements(self._texts_clients_name))
        print(clients)
        for client in clients:
            self.check_exist_in_lists(search_input, client)
