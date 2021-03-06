from common.base_page import BasePage
from Location.client_manager_loc import ClientManagerLoc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def search_by_tag(self, tag_group, tag):
        # 通过标签进行搜索
        self.click_element(self.find_Element(self._btn_select_tag))     # 点击标签搜索
        sleep(2)
        # target = self.find_Element(self._btn_tag_group.format(tag_group))
        target = self.find_Element((By.XPATH, '//div[@class="tagName" and text()="%s"]' % tag_group))
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滑动到指定位置
        sleep(2)
        # self.click_element(self.find_Element(self._btn_tags.format(tag)))  # 选择指定的标签
        # self.click_element(self.find_Element(self._btn_tags.format(tag)))   # 选择指定的标签
        self.click_element(self.find_Element((By.XPATH, "//li[@class='tag' and contains(text(),'%s')]" % tag)))
        self.click_element(self.find_Element(self._btn_confirm))    # 点击确认
        sleep(1)
        self.click_element(self.find_Element(self._btn_search))     # 点击搜索
        sleep(2)

    def assert_search_tag(self, search_tag):
        # 验证通过搜索标签时的结果，应该都包含本标签
        tags = self.get_elements_values(self.find_Elements(self._texts_full_tags))
        print(tags)
        for tag in tags:
            self.check_exist_in_lists(search_tag, tag)

    def search_by_adder(self, adder):
        # 通过添加人进行筛选
        self.click_element(self.find_Element(self._btn_more_filter))    # 点击更多筛选
        sleep(2)
        self.click_element(self.find_Element(self._btn_select_adder))   # 点击添加人输入框
        sleep(2)
        self.select_people(adder)   # 在组织架构中选择人
        self.click_element(self.find_Element(self._btn_search))     # 点击搜索
        sleep(2)


    def select_people(self, people):
        # 添加人员，进入结构层选择人员
        self.send_keys(self.find_Element(self._input_addname), people)  # 输入对应的人员
        sleep(2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()   # 点击Enter进行搜索
        sleep(1)
        self.click_element(self.find_Element(self._btn_adder))      # 点击选择出来的人
        sleep(1)
        self.click_element(self.find_Element(self._btn_confirm))    # 点击确认
        sleep(1)




