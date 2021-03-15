from common.base_page import BasePage
from Location.materials_text_loc import MaterialTextLoc
from time import sleep


class MaterialTextPage(BasePage, MaterialTextLoc):
    def switch_to_current(self):
        # 切换至文本素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_text_page))
        sleep(2)

    def create_text(self, msg):
        # 创建文本
        self.click_element(self.find_Element(self._btn_add_text))
        sleep(2)
        self.send_keys(self.find_Element(self._input_text_msg), msg)
        sleep(2)

