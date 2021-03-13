from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_text_page import MaterialTextPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mtp = get_config('material_text_page')


class TestMaterialText(MyTest, MaterialTextPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialText_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mtp['group'])  # 创建主分类
        self.create_group(mtp['group2'])
        self.assert_group(mtp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mtp['group2'])

    def test_TestMaterialText_02_addText(self):
        # 添加文本
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_text(mtp['msg'])  # 开始创建文本
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_text_group.format(mtp['group'])),
                                   (By.XPATH, self._btn_select_text_group.format(mtp['group'])))  # 选择文本分组
        self.click_element(self.find_Element(self._btn_save))  # 点击保存
        sleep(2)
        self.check_exist_in_page(mtp['msg'])  # 验证文本是否存在于页面内

    def test_TestMaterialText_03_searchText(self):
        # 搜索文本
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_text, mtp['msg'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mtp['msg'], self._texts_text_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialText_04_moveGroup(self):
        # 将文本移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_text, mtp['msg'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group()  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mtp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mtp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mtp['group2'])  # 进入分组
        self.check_exist_in_page(mtp['msg'])  # 验证页面内是否存在目标文本

    def test_TestMaterialText_05_editText(self):
        # 编辑文本
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mtp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_poster, self._btn_edit_text)  # 进入文本编辑页
        self.send_keys(self.find_Element(self._input_text_msg), mtp['msg2'])  # 编辑文本名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_save))  # 保存文本
        sleep(2)
        self.check_exist_in_page(mtp['msg2'])  # 验证页面是否存在修改后的文本

    def test_TestMaterialText_06_deleteText(self):
        # 删除文本
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mtp['group2'])  # 进入预定分组
        self.select_all_and_delete_material()  # 选择并删除文本
        self.check_not_exist_in_page(mtp['msg2'])  # 验证页面不存在目标文本

    def test_TestMaterialText_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mtp['group2'])  # 进入预定分组
        self.create_child_group(mtp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mtp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialText_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mtp['group2'])  # 进入预定分组
        self.delete_group(mtp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(mtp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialText_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mtp['group'])  # 删除分组
        self.assert_not_in_group(mtp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mtp['group2'])
        self.assert_not_in_group(mtp['group2'])
