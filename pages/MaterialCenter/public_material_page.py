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
        self.click_element(self.find_Element(self._btn_all_select))  # 勾选全选框
        sleep(2)
        self.click_element(self.find_Element(self._btn_move_group))  # 点击移动分组
        sleep(2)

    def select_all_and_delete_material(self):
        # 全选并删除海报
        self.click_element(self.find_Element(self._btn_all_select))  # 勾选全选框
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_poster))  # 点击删除海报
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))  # 二次确认
        sleep(2)

    def create_group(self, group):
        # 创建分组
        self.click_element(self.find_Element(self._btn_edit_group))  # 点击编辑分类
        sleep(2)
        self.click_element(self.find_Element(self._btn_add_main_group))  # 点击添加主分类
        sleep(2)
        self.send_keys(self.find_Element(self._input_poster_group_name), group)  # 输入分类名
        sleep(2)
        self.tap_keyboard('enter')
        sleep(1)
        self.click_element(self.find_Element(self._btn_edit_complete))  # 点击编辑完成
        sleep(2)

    def create_child_group(self, child_group):
        # 创建子分类
        self.click_element(self.find_Element(self._btn_edit_group))  # 点击编辑分类
        sleep(2)
        self.click_element(self.find_Element(self._btn_add_child_group))  # 点击添加子分类
        sleep(2)
        self.send_keys(self.find_Element(self._input_poster_group_name), child_group)  # 输入分类名
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_complete))  # 点击编辑完成
        sleep(2)

    def delete_group(self, child_group):
        # 删除分类
        self.click_element(self.find_Element(self._btn_edit_group))  # 点击编辑分类
        sleep(2)
        self.click_element(self.find_Element((By.XPATH, self._btn_delete_group.format(child_group))))  # 点击删除分类
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))  # 二次确认
        sleep(2)
        self.click_element(self.find_Element(self._btn_edit_complete))  # 点击编辑完成
        sleep(2)

    def move_group_confirm(self):
        # 移动分组确认
        self.click_element(self.find_Element(self._btn_move_group_confirm))  # 点击移动分组确认
        sleep(2)
        self.click_element(self.find_Element(self._btn_delete_confirm))  # 二次确认
        sleep(2)

    def enter_specify_group(self, group):
        # 点击进入对应的分类
        self.click_element(self.find_Element((By.XPATH, self._btn_select_specify_group.format(group))))
        sleep(2)

    def enter_edit_page(self, material_loc, edit_loc):
        # 进入编辑页面
        self.move_to_element(self.find_Element(material_loc))  # 移动至对应海报
        sleep(2)
        self.click_element(self.find_Element(edit_loc))  # 点击编辑按钮
        sleep(2)

    def assert_group(self, group):
        # 验证分类存在于主分类列表
        group_list = self.get_elements_values(self.find_Elements(self._texts_main_groups))
        self.check_exist_in_lists(group, group_list)

    def assert_not_in_group(self, group):
        # 验证分类不存在于主分类列表
        group_list = self.get_elements_values(self.find_Elements(self._texts_main_groups))
        self.check_exist_not_in_lists(group, group_list)

    def assert_materials(self, material, material_loc):
        # 验证素材搜索结果
        name_list = self.get_elements_values(self.find_Elements(material_loc))  # 获取素材名称列表
        for i in name_list:
            self.check_exist_in_lists(material, i)  # 验证搜索关键词是否存在于素材名称内