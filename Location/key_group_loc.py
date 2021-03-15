from selenium.webdriver.common.by import By


class KeyGroupLoc:
    # 营销插件
    _btn_marking_add = (By.XPATH, "//li[contains(text(),'营销插件')]")
    # 快速拉群
    _btn_quick_group = (By.XPATH, "//div[@id='tab-1']")
    # 新建关键词拉群
    _btn_new_key_group = (By.XPATH, "//span[text()='新建关键词拉群']")
    # 关键词搜索框
    _input_key_group_search = (By.XPATH, "//span[text()='新建关键词拉群']/../..//input")
    # 关键词查询按钮
    _btn_key_group_search = (By.XPATH, "//span[text()='新建关键词拉群']/../..//button/span[text()='查询 ']")

    # 新建界面
    # 任务名称
    _input_key_group = (By.XPATH, "//label[text()='活动名称']/..//input")
    # 添加关键词
    _btn_add_key = (By.XPATH, "//span[text()='添加关键词']")
    # 输入关键词
    _input_add_key = (By.XPATH, "//input[@placeholder='请输入关键词']")
    # 输入关键词后的确认
    _btn_add_key_sure = (By.XPATH, "//span[text()='关键词']/../..//span[text()='确 定']")
    # 入群引导语
    _input_key_group_guide = (By.XPATH, "//textarea")
    # 确定新建
    _btn_key_group_sure = (By.XPATH, "//p[contains(text(),'关键词拉群')]/../..//button/span[text()='确定']")

    # 群活码
    # 点击添加群活码
    _btn_add_key_code = (By.XPATH, "//label[text()='选择群活码']/..//i[@class='el-icon-plus']")
    # 搜索群活码位置
    _input_key_code_search = (By.XPATH, "//span[text()='选择群活码']/../..//input[@class='el-input__inner']")
    # 搜索群活码的查询
    _btn_key_code_search = (By.XPATH, "//span[text()='选择群活码']/../..//span[text()='查询']")
    # 搜索群活码后的选择
    _btn_key_group_select_code = (By.XPATH, "//span[text()='选择群活码']/../..//span[@class='el-radio__inner']")
    # 搜索群活码后的选择确定
    _btn_key_group_select_code_sure = (By.XPATH, "//span[text()='选择群活码']/../..//button/span[text()='确 定']")

    # 验证
    # 验证活动名称
    _text_first_key_group_name = (By.XPATH, "//div[@class='cell el-tooltip']")
    # 验证关键词
    _text_first_key_name = (By.XPATH, "//div[@class='cell']/span[contains(@class,'tag')]")

    # 验证点击编辑进入界面
    # 验证关键词的内容
    _text_key_code_page = (By.XPATH, "//span[contains(@class,'tag')]")

    # 删除
    _delete_sure_button = (By.XPATH, "//div[@x-placement='bottom']//span[contains(text(),'确定')]")
