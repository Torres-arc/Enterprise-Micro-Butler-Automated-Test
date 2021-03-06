from common.base_page import BasePage
from Location.client_tag_loc import ClientTagLoc
from time import sleep
from selenium.webdriver.common.by import By


class ClientTag(BasePage, ClientTagLoc):
    def switch_to_client_tag(self):     # 点击进入客户标签界面
        self.click_element(self.find_Element(self._btn_client_tag_page))
        sleep(2)

    def add_tag_group(self, tag_group, tags):  # 添加标签,注：tag是数组
        self.click_element(self.find_Element(self._btn_create_tag_group))   # 点击“新建标签组”
        sleep(1)
        self.send_keys(self.find_Element(self._input_tag_group_name), tag_group)    # 输入标签组
        sleep(1)
        for tag in tags:    # tags是个数组，需要循环遍历填写进去
            self.click_element(self.find_Element(self._btn_add_tag))    # 点击添加标签
            sleep(1)
            self.send_keys(self.find_Element(self._input_tag), tag)     # 输入tag
            self.tap_keyboard('enter')      # 点击enter
            sleep(1)
        self.click_element(self.find_Element(self._btn_confirm))    # 点击确定按钮完成新建
        sleep(5)

    def assert_tag(self, tag_group, tags_equal):   # 验证显示的tag与添加的tag数组一致,验证tag_group与添加的tag数组一致
        self.check_exist_in_page(tag_group)     # 验证出现tag_group
        self.click_element(self.find_Element(self._btn_get_tags))   # 点击“...”获取所有的标签
        tags_list_preview = self.get_elements_values(self.find_Elements(self._btn_get_tags_text))    # 获取到所有的标签,但是所有的标签都有空格，需要去除
        print(tags_list_preview)
        tags = []
        for tag_preview in tags_list_preview:
            tags.append(tag_preview.strip())    # 去除空格后，再去存储到tags数组中
        print(tags)
        tags.sort()
        tags_equal.sort()
        self.assert_Equal(tags, tags_equal)


    def delete_tag_group(self, tag_group):  # 删除标签组
        sleep(5)
        self.click_element(self.find_Element((By.XPATH, "//div[contains(text(),'%s')]/../..//button/span[text()='删除']" % tag_group))) # 点击删除
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_sure))    # 点击确定删除
        sleep(2)







