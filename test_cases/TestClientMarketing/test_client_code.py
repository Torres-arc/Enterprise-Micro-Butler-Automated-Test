from time import sleep

from common.myunit import MyTest
from pages.ClientMarketing.client_code_page import ClientCodePage
from pages.public_page import PublicPage
from common.statics import get_config, get_userid_info

admin = get_config('3.1_www')  # 读取注册管理员账号
ccp = get_config('client_code_page')


class TestClient(MyTest, ClientCodePage, PublicPage):
    """测试用户搜索（输入搜索）时，搜索结果是包含搜索关键词的"""

    def test_TestClientCode_01_searchByCreator(self):
        # 验证搜索后，搜索结果与目标创建人一致
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销

        self.public_select_staff(self._btn_creator, self._btn_confirm, ccp['creator'])  # 搜索目标员工
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_staff(self._texts_creator, ccp['creator'])  # 验证搜索结果与搜索员工一致

    def test_TestClientCode_02_searchByActScene(self):
        # 验证搜索后，搜索结果包含目标文本
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销

        self.unfold_market_search_bar()
        sleep(2)
        self.search_by_input(self._input_act_scene, ccp['actscene'], self._btn_search)  # 输入search_input来进行搜索
        self.assert_search_input(self._texts_actscene, ccp['actscene'])  # 验证搜索值是否正确

    def test_TestClientCode_03_searchByUser(self):
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 切换到客户营销

        self.unfold_market_search_bar()
        sleep(2)
        self.public_select_staff(self._btn_user, self._btn_confirm, ccp['creator'])  # 搜索目标员工
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_user(ccp['creator'])  # 验证搜索结果与搜索员工一致

    def test_TestClientCode_04_searchByDate(self):
        # 验证搜索后，搜索结果是符合日期要求的
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.select_date(ccp['stime'], ccp['etime'])  # 搜索目标日期内的数据
        self.click_element(self.find_Element(self._btn_search))
        sleep(2)
        self.assert_search_date(self._texts_ctetime, ccp['stime'], ccp['etime'])  # 验证搜索结果符合日期范围一致

    def test_TestClientCode_05_createSingleWeb(self):
        # 测试创建单人活码-网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面
        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('single')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, ccp['user'])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), ccp['actscene'])  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        globals()['msg'] = self.select_tag(self._btn_add_tags,
                                           [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                                           self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('web', ccp['web_msg'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page(ccp['actscene'])  # 判断活动场景是否存在于页面中

    def test_TestClientCode_06_checkCodeInfo(self):
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_check_detail))  # 进入详情页
        sleep(3)
        msglist = [ccp['actscene'], ccp['user'], ccp['welcome']]
        self.assert_details(msglist)  # 验证详情数据
        self.switch_to_client_marketing_tab()

    def test_TestClientCode_07_editCode(self):
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.edit_code()  # 进入编辑活码页面
        self.send_keys(self.find_Element(self._input_activity_scene), ccp['actscene2'])  # 编辑活动场景
        sleep(1)
        self.send_keys(self.find_Element(self._input_welcomg), ccp['welcome2'])  # 编辑欢迎语
        sleep(2)
        self.click_element(self.find_Element(self._btn_save2))  # 点击保存按钮
        sleep(2)

        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page(ccp['actscene2'])  # 判断活动场景是否存在于页面中

    def test_TestClientCode_08_deleteCode(self):
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.delete_code()  # 删除活码
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_not_exist_in_page(ccp['actscene2'])  # 判断活动场景是否存在于页面中

    def test_TestClientCode_09_createSinglePic(self):
        # 测试创建单人活码-图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('single')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, ccp['user'])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '2'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('pic', ccp['picpath'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '2'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_10_createSingleMini(self):
        # 测试创建单人活码-小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('single')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, ccp['user'])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '3'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('mini', ccp['web_path'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '3'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_11_createMultiPic(self):
        # 测试创建多人活码-图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('multi')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '4'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('pic', ccp['picpath'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '4'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_12_createMultiMini(self):
        # 测试创建多人活码-小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('multi')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '5'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('mini', ccp['web_msg'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '5'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_13_createMultiWeb(self):
        # 测试创建多人活码-网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('multi')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '6'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('web', ccp['web_msg'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '6'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_14_createBatchPic(self):
        # 测试创建批量单人活码-图片
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('batch')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '7'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('pic', ccp['picpath'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '7'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_15_createMultiMini(self):
        # 测试创建批量单人活码-小程序
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('batch')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '8'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('mini', ccp['web_msg'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '8'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_16_createMultiWeb(self):
        # 测试创建批量单人活码-网页
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.click_element(self.find_Element(self._btn_create_employee_code))  # 点击创建活码按钮
        self.select_code_type('batch')  # 选择单人活码
        self.public_select_staff(self._btn_add_employer, self._btn_confirm, [ccp['user'], ccp['user2']])  # 选择使用员工
        self.send_keys(self.find_Element(self._input_activity_scene), (ccp['actscene'] + '9'))  # 输入活动场景
        sleep(2)
        self.click_element(self.find_Element(self._btn_advanced_design))  # 点击高级设置，展开欢迎语
        sleep(2)
        self.select_tag(self._btn_add_tags,
                        [self._btn_tags1, self._btn_tags2, self._btn_tags3],
                        self._btn_tag_confirm)  # 选择三个标签
        self.select_wel('web', ccp['web_msg'], ccp['welcome'])  # 选择欢迎语
        self.switch_to_client_marketing_tab()  # 回到列表页
        self.check_exist_in_page((ccp['actscene'] + '9'))  # 判断活动场景是否存在于页面中

    def test_TestClientCode_17_deleteCodeInBatch(self):
        # 测试批量删除
        self.login(admin['username'], admin['password'])
        self.switch_to_client_marketing_tab()  # 进入客户群页面

        self.unfold_market_search_bar()
        sleep(2)
        self.search_by_input(self._input_act_scene, ccp['actscene'], self._btn_search)  # 搜索目标活码
        self.delete_code_in_batch()  # 批量删除
        self.check_not_exist_in_page(ccp['actscene'])  # 验证目标活码不存在于页面中
