from common.base_page import BasePage
from Location.materials_pic_loc import MaterialPicLoc
from time import sleep


class MaterialPicPage(BasePage, MaterialPicLoc):
    def switch_to_current(self):
        # 切换至图片素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_pic_page))
        sleep(2)

    def create_pic(self):
        # 创建图片
        self.click_element(self.find_Element(self._btn_add_pic))
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_pic))
        sleep(2)
        self.upload_file('\\materials\\pic\\photo.png')
