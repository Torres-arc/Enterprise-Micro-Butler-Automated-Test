from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.myunit import MyTest
from pages.MaterialCenter.materials_pic_page import MaterialPicPage
from pages.public_page import PublicPage
from pages.MaterialCenter.public_material_page import PublicMaterialPage
from common.statics import get_config

admin = get_config('3.1_www')  # 读取注册管理员账号
mpp = get_config('material_pic_page')


class TestMaterialPic(MyTest, MaterialPicPage, PublicPage, PublicMaterialPage):
    def test_TestMaterialPic_01_createGroup(self):
        # 创建主分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_group(mpp['group'])  # 创建主分类
        self.create_group(mpp['group2'])
        self.assert_group(mpp['group'])  # 验证分类存在于主分类列表内
        self.assert_group(mpp['group2'])

    def test_TestMaterialPic_02_addPic(self):
        # 添加图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.create_pic(mpp['path'])  # 开始创建图片
        self.material_select_group(self._btn_select_group,
                                   (By.XPATH, self._text_select_text_group.format(mpp['group'])),
                                   (By.XPATH, self._btn_select_text_group.format(mpp['group'])))  # 选择图片分组
        self.click_element(self.find_Element(self._btn_save))  # 点击保存
        sleep(2)
        self.check_exist_in_page(mpp['msg'])  # 验证图片是否存在于页面内

    def test_TestMaterialPic_03_searchPic(self):
        # 搜索图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_pic, mpp['msg'], self._btn_search)  # 输入关键词并搜索
        self.assert_materials(mpp['msg'], self._texts_pic_name)  # 验证搜索结果是否包含关键词

    def test_TestMaterialPic_04_moveGroup(self):
        # 将图片移动分组
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.search_by_input(self._input_search_pic, mpp['msg'], self._btn_search)  # 输入关键词并搜索
        self.select_all_and_move_group(self._btn_pic_all_select)  # 选择并点击移动分组
        self.material_select_group(self._btn_input_move_group,
                                   (By.XPATH, self._text_select_move_group.format(mpp['group2'])),
                                   (By.XPATH, self._btn_select_move_group.format(mpp['group2'])))  # 选择分组
        self.move_group_confirm()  # 移动分组确认
        self.enter_specify_group(mpp['group2'])  # 进入分组
        self.check_exist_in_page(mpp['msg'])  # 验证页面内是否存在目标图片

    def test_TestMaterialPic_05_editPic(self):
        # 编辑图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分类
        self.enter_edit_page(self._btn_pic_div, self._btn_edit_pic)  # 进入图片编辑页
        self.send_keys(self.find_Element(self._input_pic_name), mpp['msg2'])  # 编辑图片名称
        sleep(2)
        self.click_element(self.find_Element(self._btn_pic_save))  # 保存图片
        sleep(2)
        self.check_exist_in_page(mpp['msg2'])  # 验证页面是否存在修改后的图片

    def test_TestMaterialPic_06_deletePic(self):
        # 删除图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.select_all_and_delete_material()  # 选择并删除图片
        self.check_not_exist_in_page(mpp['msg2'])  # 验证页面不存在目标图片

    def test_TestMaterialPic_07_createChildGroup(self):
        # 创建子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.create_child_group(mpp['child_group'])  # 创建子分组
        namelist = self.get_elements_values(self.find_Elements(self._texts_child_groups))  # 获取子分组名称列表
        self.check_exist_in_lists(mpp['child_group'], namelist)  # 验证是否创建成功

    def test_TestMaterialPic_08_deleteChildGroup(self):
        # 删除子分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.enter_specify_group(mpp['group2'])  # 进入预定分组
        self.delete_group(mpp['child_group'])  # 删除子分组

        # 验证目标子分组是否还存在
        try:
            self.check_not_exist_in_page(mpp['child_group'])
        except Exception as e:
            raise e

    def test_TestMaterialPic_09_deleteGroup(self):
        # 删除分类
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销
        self.switch_to_current()

        self.delete_group(mpp['group'])  # 删除分组
        self.assert_not_in_group(mpp['group'])  # 验证分组是否存在于页面内
        self.delete_group(mpp['group2'])
        self.assert_not_in_group(mpp['group2'])
