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

    def save_poster(self):
        # 提交添加海报
        self.click_element(self.find_Element(self._btn_title))  # 关闭分组弹窗
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_pic))  # 点击上传图片
        sleep(1)
        self.upload_file('\\materials\\pic\\photo.png')  # 上传本地素材
        self.click_element(self.find_Element(self._btn_save))  # 点击保存
        sleep(2)



