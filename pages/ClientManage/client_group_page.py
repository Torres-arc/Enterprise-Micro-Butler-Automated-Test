from common.base_page import BasePage
from Location.client_group_loc import ClientGroupLoc
from time import sleep
from selenium.webdriver.common.by import By


class ClientTag(BasePage, ClientGroupLoc):
    def switch_to_client_group(self):     # 点击进入客户标签界面
        self.click_element(self.find_Element(self._btn_client_group_page))
        sleep(2)



