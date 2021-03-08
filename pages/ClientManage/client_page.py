from common.base_page import BasePage
from Location.client_loc import ClientLoc
from common.statics import get_config
from time import sleep


class ClientPage(BasePage, ClientLoc):
    def switch_to_client(self):
        self.click_element(self.find_Element(self._btn_client_page))    # 点击客户
        sleep(2)

    def assert_search_tag(self, search_tag):
        # 验证通过搜索标签时的结果，应该都包含本标签
        tags = self.get_elements_values(self.find_Elements(self._texts_full_tags))
        print(tags)
        for tag in tags:
            self.check_exist_in_lists(search_tag, tag)

    def go_through_list_to_get_msg(self, details_loc, msg_loc):
        """
        遍历列表每个客户的详情页，获取目标数据
        :param details_loc: 客户信息定位（为了计数及点击进入详情页）
        :param msg_loc: 需要获取信息的元素定位
        :return:
        """
        data_list = []
        for i in range(len(self.find_Elements(details_loc))):
            self.click_element(self.find_Element(details_loc))
            sleep(2)
            data_list.append(self.get_elements_values(self.find_Elements(msg_loc)))
            self.click_element(self.find_Element(self._btn_back))  # 返回列表页
        return data_list
