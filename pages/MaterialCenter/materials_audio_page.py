from common.base_page import BasePage
from Location.materials_audio_loc import MaterialAudioLoc
from time import sleep


class MaterialAudioPage(BasePage, MaterialAudioLoc):
    def switch_to_current(self):
        # 切换至语音素材页面
        self.click_element(self.find_Element(self._btn_material_others_page))
        sleep(2)
        self.click_element(self.find_Element(self._btn_audio_page))
        sleep(2)

    def create_audio(self, path):
        # 创建语音
        self.click_element(self.find_Element(self._btn_add_audio))
        sleep(2)
        self.click_element(self.find_Element(self._btn_upload_audio))
        sleep(2)
        self.upload_file(path)

