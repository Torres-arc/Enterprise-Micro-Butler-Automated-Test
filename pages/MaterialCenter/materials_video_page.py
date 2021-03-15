from common.base_page import BasePage
from Location.materials_video_loc import MaterialVideoLoc
from time import sleep


class MaterialVideoPage(BasePage, MaterialVideoLoc):
    def switch_to_current(self):
        # 切换至网页素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_video_page))
        sleep(2)

    def create_video(self, path1, path2):
        # 创建网页
        self.click_element(self.find_Element(self._btn_add_video))
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_video))
        sleep(2)
        self.upload_file(path1)
        self.click_element(self.find_Element(self._btn_upload_video_cover))
        sleep(2)
        self.upload_file(path2)
