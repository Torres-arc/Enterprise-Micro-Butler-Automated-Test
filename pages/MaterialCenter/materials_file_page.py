from common.base_page import BasePage
from Location.materials_file_loc import MaterialFileLoc
from time import sleep


class MaterialFilePage(BasePage, MaterialFileLoc):
    def switch_to_current(self):
        # 切换至文件素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_file_page))
        sleep(2)

    def create_file(self, path):
        # 创建文件
        self.click_element(self.find_Element(self._btn_add_file))
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_file))
        sleep(2)
        self.upload_file(path)

