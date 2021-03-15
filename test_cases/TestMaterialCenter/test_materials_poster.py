from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materias_poster_page import MaterialPosterPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mpp = get_config('material_poster_page')


class TestMaterialPoster(MyTest, MaterialPosterPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialPoster_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mpp['group'])  # 创建主分类
        self.create_group(mpp['group2'])
        self.assert_group(mpp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mpp['group2'])

    def test_TestMaterialPoster_02_addPoster(self):
        # 添加海报
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_poster(mpp['poster'])  # 开始创建海报
        self.material_select_group(self._btn_poster_groups,
                                   (By.XPATH, self._text_select_move_group.format(mpp['group'])),
                                   (By.XPATH, self._btn_select_poster_group.format(mpp['group'])))  # 选择海报分组
        self.save_poster()  # 上传图片并保存海报
        self.check_exist_in_page(mpp['poster'])  # 验证海报是否存在于页面内

    def test_TestMaterialPoster_03_searchPoster(self):
        # 搜索海报
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_poster_search, mpp['poster'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mpp['poster'], self._texts_poster_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialPoster_04_moveGroup(self):
        # 将海报移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_poster_search, mpp['poster'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_all_select)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mpp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mpp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mpp['group2'])  # 进入分组
        self.check_exist_in_page(mpp['poster'])  # 验证页面内是否存在目标海报

    def test_TestMaterialPoster_05_editPoster(self):
        # 编辑海报
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_poster, self._btn_edit_poster)  # 进入海报编辑页
        self.send_keys(self.find_Element(self._input_poster_name), mpp['poster2'])  # 编辑海报名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_save))  # 保存海报
        sleep(2)
        self.check_exist_in_page(mpp['poster2'])  # 验证页面是否存在修改后的海报

    def test_TestMaterialPoster_06_deletePoster(self):
        # 删除海报
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.select_all_and_delete_material()  # 选择并删除海报
        self.check_not_exist_in_page(mpp['group2'])  # 验证页面不存在目标海报

    def test_TestMaterialPoster_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.create_child_group(mpp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mpp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialPoster_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.delete_group(mpp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(mpp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialPoster_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mpp['group'])  # 删除分组
        self.check_not_exist_in_page(mpp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mpp['group2'])
        self.check_not_exist_in_page(mpp['group2'])

