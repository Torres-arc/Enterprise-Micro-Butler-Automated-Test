from common.base_page import BasePage
from Location.materials_mini_loc import MaterialMiniLoc
from time import sleep


class MaterialMiniPage(BasePage, MaterialMiniLoc):
    def switch_to_current(self):
        # 切换至小程序素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_mini_page))
        sleep(2)

    def create_mini(self, title, appid, url, path):
        # 创建小程序
        self.click_element(self.find_Element(self._btn_add_mini))
        sleep(2)
        self.send_keys(self.find_Element(self._input_mini_name), title)
        sleep(2)
        self.send_keys(self.find_Element(self._input_mini_appid), appid)
        sleep(2)
        self.send_keys(self.find_Element(self._input_mini_url), url)
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_pic))
        sleep(2)
        self.upload_file(path)
