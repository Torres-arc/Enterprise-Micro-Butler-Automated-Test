from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_video_page import MaterialVideoPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mvp = get_config('material_video_page')


class TestMaterialWeb(MyTest, MaterialVideoPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialWeb_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mvp['group'])  # 创建主分类
        self.create_group(mvp['group2'])
        self.assert_group(mvp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mvp['group2'])

    def test_TestMaterialWeb_02_addWeb(self):
        # 添加视频
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_video(mvp['path1'], mvp['path2'])  # 开始创建网页
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_text_group.format(mvp['group'])),
                                   (By.XPATH, self._btn_select_text_group.format(mvp['group'])))  # 选择网页分组
        self.click_element(self.find_Element(self._btn_video_save))  # 上传图片并保存网页
        sleep(2)
        self.check_exist_in_page(mvp['name'])  # 验证网页是否存在于页面内

    def test_TestMaterialWeb_03_searchVideo(self):
        # 搜索视频
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_video, mvp['name'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mvp['name'], self._texts_video_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialWeb_04_moveGroup(self):
        # 将视频移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_video, mvp['name'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_video_all_select)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mvp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mvp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mvp['group2'])  # 进入分组
        self.check_exist_in_page(mvp['name'])  # 验证页面内是否存在目标网页

    def test_TestMaterialWeb_05_editVideo(self):
        # 编辑视频
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mvp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_video_operation, self._btn_edit_video)  # 进入网页编辑页
        self.send_keys(self.find_Element(self._input_video_name), mvp['name2'])  # 编辑网页名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_video_save))  # 保存网页
        sleep(2)
        self.click_element(self.find_Element(self._btn_video_save_confirm))
        sleep(2)
        self.check_exist_in_page(mvp['name2'])  # 验证页面是否存在修改后的网页

    def test_TestMaterialWeb_06_deleteVideo(self):
        # 删除视频
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mvp['group2'])  # 进入预定分组
        self.select_all_and_delete_material(self._btn_all_select)  # 选择并删除网页
        self.check_not_exist_in_page(mvp['name2'])  # 验证页面不存在目标网页

    def test_TestMaterialWeb_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mvp['group2'])  # 进入预定分组
        self.create_child_group(mvp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mvp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialWeb_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mvp['group2'])  # 进入预定分组
        self.delete_group(mvp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.find_Elements(self._texts_child_groups)
        except TimeoutException:
            self.check_not_exist_in_page(mvp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialWeb_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mvp['group'])  # 删除分组
        self.assert_not_in_group(mvp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mvp['group2'])
        self.assert_not_in_group(mvp['group2'])

