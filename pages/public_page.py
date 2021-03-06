from common.base_page import BasePage
from Location.client_loc import ClientLoc
from common.statics import get_config
from time import sleep


class PublicPage(BasePage, ClientLoc):

    def switch_to_current(self):
        self.click_element(self.find_Element(self._btn_client_manage_tab))  # 进入客户管理tab
        sleep(2)

    def unfold_search_bar(self):
        self.click_element(self.find_Element(self._btn_more_filter))    # 展现隐藏搜索栏
        sleep(2)

    def public_search_by_adder(self, adder):
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

    def common_search(self, page_num_loc, target_loc, next_page_loc, msg):
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
