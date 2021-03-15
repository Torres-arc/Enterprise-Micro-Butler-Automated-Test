from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_audio_page import MaterialAudioPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
map = get_config('material_audio_page')


class TestMaterialAudio(MyTest, MaterialAudioPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialAudio_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(map['group'])  # 创建主分类
        self.create_group(map['group2'])
        self.assert_group(map['group'])  # 验证分类存在于主分类列表内
        self.assert_group(map['group2'])

    def test_TestMaterialAudio_02_addAudio(self):
        # 添加语音
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_audio(map['path'])  # 开始创建语音
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_audio_group.format(map['group'])),
                                   (By.XPATH, self._btn_select_audio_group.format(map['group'])))  # 选择语音分组
        self.click_element(self.find_Element(self._btn_save))  # 点击保存
        sleep(2)
        self.click_element(self.find_Element(self._btn_confirm_audio))
        sleep(2)
        self.check_exist_in_page(map['name1'])  # 验证语音是否存在于页面内

    def test_TestMaterialAudio_03_searchAudio(self):
        # 搜索语音
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_text, map['name1'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(map['name1'], self._texts_audio_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialAudio_04_moveGroup(self):
        # 将语音移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_text, map['name1'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_all_select_audio)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(map['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(map['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(map['group2'])  # 进入分组
        self.check_exist_in_page(map['name1'])  # 验证页面内是否存在目标语音

    def test_TestMaterialAudio_05_editAudio(self):
        # 编辑语音
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(map['group2'])  # 进入预定分类
        self.click_element(self.find_Element(self._btn_edit_audio))  # 进入语音编辑页
        self.send_keys(self.find_Element(self._input_audio_msg), map['name2'])  # 编辑语音名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_confirm_audio))  # 保存语音
        sleep(2)
        self.check_exist_in_page(map['name2'])  # 验证页面是否存在修改后的语音

    def test_TestMaterialAudio_06_deleteAudio(self):
        # 删除语音
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(map['group2'])  # 进入预定分组
        self.select_all_and_delete_material(self._btn_all_select_audio)  # 选择并删除语音
        self.check_not_exist_in_page(map['name2'])  # 验证页面不存在目标语音

    def test_TestMaterialAudio_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(map['group2'])  # 进入预定分组
        self.create_child_group(map['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(map['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialAudio_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(map['group2'])  # 进入预定分组
        self.delete_group(map['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(map['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialAudio_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(map['group'])  # 删除分组
        self.assert_not_in_group(map['group'])  # 验证分组是否存在于页面内
        self.delete_group(map['group2'])
        self.assert_not_in_group(map['group2'])
