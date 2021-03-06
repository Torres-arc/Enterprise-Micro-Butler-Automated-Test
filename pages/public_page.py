from common.base_page import BasePage
from Location.client_loc import ClientLoc
from common.statics import get_config
from time import sleep


class PublicPage(BasePage, ClientLoc):
    def puclic_search_by_staff(self, adder):
        self.click_element(self.find_Element(self._btn_select_adder))  # 点击添加人输入框，进入组织架构
        sleep(2)
        self.send_keys(self.find_Element(self._input_addname), adder)  # 输入添加人姓名
        sleep(1)
        self.tap_keyboard('enter')
        sleep(2)
        self.click_element(self.find_Element(self._btn_adder))
        sleep(2)
        self.click_element(self.find_Element(self._btn_confirm))
        sleep(2)

    def assert_data(self, data, target):
        for i in data:
            try:
                self.check_exist_in_lists(data, i)
            except AssertionError as e:
                print('搜索条件与数据不匹配')
                raise e

    def common_search(self, page_num_loc, target_loc, next_page_loc, msg):
        """
        :param page_num_loc: 页面数量的定位
        :param target_loc: 需要进行验证的页面文本定位
        :param next_page_loc: 翻页按钮的定位
        :param msg: 目标搜索数据
        :return:
        """
        pages = int(self.get_element_value(self.find_Elements(page_num_loc)))  # 获取搜索结果页数
        count = 1
        while pages > 0 and count <= 3:
            try:
                msglist = self.get_elements_values(self.find_Elements(target_loc))  # 搜索目标

            except TimeoutError:
                try:
                    self.check_exist_in_page('暂无数据')  # 无数据时的页面信息
                except Exception as e:
                    raise e
                else:
                    print('搜索条件下无数据')
            except Exception as e:
                raise e
            else:  # 存在数据，进行验证
                for i in msglist:
                    try:
                        self.check_exist_in_lists(msg, i)
                    except AssertionError as e:
                        print('搜索条件与数据不匹配')
                        raise e
            self.click_element(self.find_Element(next_page_loc))  # 翻页
            sleep(2)
            pages -= 1
            count += 1
