from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_web_page import MaterialWebPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mwp = get_config('material_web_page')


class TestMaterialWeb(MyTest, MaterialWebPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialWeb_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mwp['group'])  # 创建主分类
        self.create_group(mwp['group2'])
        self.assert_group(mwp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mwp['group2'])

    def test_TestMaterialWeb_02_addWeb(self):
        # 添加网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_web(mwp['title1'], mwp['main'], mwp['path1'])  # 开始创建网页
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_text_group.format(mwp['group'])),
                                   (By.XPATH, self._btn_select_text_group.format(mwp['group'])))  # 选择网页分组
        self.click_element(self.find_Element(self._btn_web_save))  # 上传图片并保存网页
        sleep(2)
        self.check_exist_in_page(mwp['title1'])  # 验证网页是否存在于页面内

    def test_TestMaterialWeb_03_searchWeb(self):
        # 搜索网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_web, mwp['title1'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mwp['title1'], self._texts_web_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialWeb_04_moveGroup(self):
        # 将网页移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_web, mwp['title1'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_web_all_select)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mwp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mwp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mwp['group2'])  # 进入分组
        self.check_exist_in_page(mwp['title1'])  # 验证页面内是否存在目标网页

    def test_TestMaterialWeb_05_editWeb(self):
        # 编辑网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mwp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_web_operation, self._btn_edit_web)  # 进入网页编辑页
        self.send_keys(self.find_Element(self._input_web_name), mwp['edited_title'])  # 编辑网页名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_web_save))  # 保存网页
        sleep(2)
        self.check_exist_in_page(mwp['edited_title'])  # 验证页面是否存在修改后的网页

    def test_TestMaterialWeb_06_deleteWeb(self):
        # 删除网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mwp['group2'])  # 进入预定分组
        self.select_all_and_delete_material()  # 选择并删除网页
        self.check_not_exist_in_page(mwp['edited_title'])  # 验证页面不存在目标网页

    def test_TestMaterialWeb_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mwp['group2'])  # 进入预定分组
        self.create_child_group(mwp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mwp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialWeb_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mwp['group2'])  # 进入预定分组
        self.delete_group(mwp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(mwp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialWeb_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mwp['group'])  # 删除分组
        self.assert_not_in_group(mwp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mwp['group2'])
        self.assert_not_in_group(mwp['group2'])

