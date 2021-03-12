from common.base_page import BasePage
from Location.materials_poster_loc import MaterialPosterLoc
from time import sleep


class MaterialPosterPage(BasePage, MaterialPosterLoc):
    def switch_to_current(self):
        # 切换至海报素材页面
        self.click_element(self.find_Element(self._btn_material_poster_page))
        sleep(2)

    def create_poster(self, poster):
        # 创建海报
        self.click_element(self.find_Element(self._btn_add_poster))  # 点击创建海报
        sleep(2)
        self.send_keys(self.find_Element(self._input_poster_name), poster)  # 输入海报名称
        sleep(2)

    def save_poster(self, poster):
        # 提交添加海报
        self.click_element(self.find_Element(self._btn_title))  # 关闭分组弹窗
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_pic))  # 点击上传图片
        sleep(1)
        self.upload_file('\\materials\\pic\\photo.png')  # 上传本地素材
        self.click_element(self.find_Element(self._btn_save))  # 点击保存
        sleep(2)

    def assert_poster(self, poster):
        # 验证海报搜索结果
        name_list = self.get_elements_values(self.find_Elements(self._texts_poster_name))  # 获取海报名称列表
        for i in name_list:
            self.check_exist_in_lists(poster, i)  # 验证搜索关键词是否存在于海报名称内

    def assert_group(self, group):
        # 验证主分类列表
        group_list = self.get_elements_values(self.find_Elements(self._texts_main_groups))
        self.check_exist_in_lists(group, group_list)
