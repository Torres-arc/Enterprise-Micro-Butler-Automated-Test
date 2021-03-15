from common.base_page import BasePage
from Location.materials_web_loc import MaterialWebLoc
from time import sleep


class MaterialWebPage(BasePage, MaterialWebLoc):
    def switch_to_current(self):
        # 切换至网页素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_web_page))
        sleep(2)

    def create_web(self, title, msg, path):
        # 创建网页
        self.click_element(self.find_Element(self._btn_add_web))
        sleep(2)

        self.send_keys(self.find_Element(self._input_web_name), title)
        sleep(2)
        self.force_scroll_screen()
        sleep(2)
        self.send_keys(self.find_Element(self._input_web_main_text), msg)
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_pic))
        sleep(2)
        self.upload_file(path)
