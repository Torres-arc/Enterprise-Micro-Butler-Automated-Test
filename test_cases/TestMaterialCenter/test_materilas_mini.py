from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_mini_page import MaterialMiniPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mmp = get_config('material_mini_page')


class TestMaterialMini(MyTest, MaterialMiniPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialMini_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mmp['group'])  # 创建主分类
        self.create_group(mmp['group2'])
        self.assert_group(mmp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mmp['group2'])

    def test_TestMaterialMini_02_addMini(self):
        # 添加小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_mini(mmp['title1'], mmp['appid'], mmp['url'], mmp['path'])  # 开始创建小程序
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_text_group.format(mmp['group'])),
                                   (By.XPATH, self._btn_select_text_group.format(mmp['group'])))  # 选择小程序分组
        self.click_element(self.find_Element(self._btn_mini_save))  # 上传图片并保存小程序
        sleep(2)
        self.click_element(self.find_Element(self._btn_mini_save_confirm))
        sleep(2)
        self.check_exist_in_page(mmp['title1'])  # 验证小程序是否存在于页面内

    def test_TestMaterialMini_03_searchMini(self):
        # 搜索小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_mini, mmp['title1'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mmp['title1'], self._texts_mini_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialMini_04_moveGroup(self):
        # 将小程序移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_mini, mmp['title1'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_mini_all_select)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mmp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mmp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mmp['group2'])  # 进入分组
        self.check_exist_in_page(mmp['title1'])  # 验证页面内是否存在目标小程序

    def test_TestMaterialMini_05_editMini(self):
        # 编辑小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mmp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_mini_operation, self._btn_edit_mini)  # 进入小程序编辑页
        self.send_keys(self.find_Element(self._input_mini_name), mmp['title2'])  # 编辑小程序名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_mini_save))  # 保存小程序
        sleep(2)
        self.click_element(self.find_Element(self._btn_mini_save_confirm))
        sleep(2)
        self.check_exist_in_page(mmp['title2'])  # 验证页面是否存在修改后的小程序

    def test_TestMaterialMini_06_deleteMini(self):
        # 删除小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mmp['group2'])  # 进入预定分组
        self.select_all_and_delete_material(self._btn_all_select)  # 选择并删除小程序
        self.check_not_exist_in_page(mmp['title2'])  # 验证页面不存在目标小程序

    def test_TestMaterialMini_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mmp['group2'])  # 进入预定分组
        self.create_child_group(mmp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mmp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialMini_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mmp['group2'])  # 进入预定分组
        self.delete_group(mmp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(mmp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialMini_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mmp['group'])  # 删除分组
        self.assert_not_in_group(mmp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mmp['group2'])
        self.assert_not_in_group(mmp['group2'])

