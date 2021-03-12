from selenium.webdriver.common.by import By

from common.base_page import BasePage
from Location.materials_poster_loc import MaterialPosterLoc
from time import sleep


class PublicMaterialPage(BasePage, MaterialPosterLoc):
    def material_select_group(self, open_window_loc, text_loc, select_loc):
        """
        素材中心，选择分组
        :param open_window_loc: 打开选择分组弹窗的定位
        :param text_loc:  需要选择的分组的文本定位
        :param select_loc:  需要选择的分组的按钮定位
        :return:
        """
        self.click_element(self.find_Element(open_window_loc))  # 打开选择分组弹窗
        sleep(2)
        self.scroll_screen(self.find_Element(text_loc))  # 滚动至目标分组
        sleep(1)
        self.click_element(self.find_Element(text_loc))  # 使分组完全可见、可点击
        sleep(1)
        self.click_element(self.find_Element(select_loc))  # 选择分组
        sleep(2)

    def select_all_and_move_group(self):
        # 全选并移动分组
        self.click_element(self.find_Element(self._btn_all_select))
        sleep(2)
        self.click_element(self.find_Element(self._btn_move_group))
        sleep(2)

    def select_all_and_delete_poster(self):
        # 全选并删除海报
        self.click_element(self.find_Element(self._btn_all_select))
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_poster))
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))
        sleep(2)

    def create_group(self, group):
        # 创建分组
        self.click_element(self.find_Element(self._btn_edit_group))
        sleep(2)
        self.click_element(self.find_Element(self._btn_add_main_group))
        sleep(2)
        self.send_keys(self.find_Element(self._input_poster_group_name), group)
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_complete))
        sleep(2)

    def create_child_group(self, child_group):
        self.click_element(self.find_Element(self._btn_edit_group))
        sleep(2)
        self.click_element(self.find_Element(self._btn_add_child_group))
        sleep(2)
        self.send_keys(self.find_Element(self._input_poster_group_name), child_group)
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_complete))
        sleep(2)

    def delete_group(self, child_group):
        self.click_element(self.find_Element(self._btn_edit_group))
        sleep(2)
        self.click_element(self.find_Element((By.XPATH, self._btn_delete_group.format(child_group))))
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_complete))
        sleep(2)

    def move_group_confirm(self):
        self.click_element(self.find_Element(self._btn_move_group_confirm))
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))
        sleep(2)

    def enter_specify_group(self, group):
        self.click_element(self.find_Element((By.XPATH, self._btn_select_specify_group.format(group))))
        sleep(2)

    def enter_edit_page(self, material_loc, edit_loc):
        self.move_to_element(self.find_Element(material_loc))
        sleep(2)
        self.click_element(self.find_Element(edit_loc))
        sleep(2)