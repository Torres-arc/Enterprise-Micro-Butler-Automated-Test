from selenium.webdriver.common.by import By


class AddGroupChatLoc:
    # 拉群工具
    _btn_add_group_chat = (By.XPATH, "//li[contains(text(),'拉群工具')]")
    # 老客标签建群
    _btn_old_client_tag_group = (By.XPATH, "//div[@id='tab-1']")

    # 自动拉群
    # 新建自动拉群
    _btn_new_add_group = (By.XPATH, "//span[text()='新建自动拉群']")
    # 自动拉群的搜索框
    _input_add_group_chat = (By.XPATH, "//span[text()='新建自动拉群']/../../..//input")
    # 自动拉群的搜索按钮
    _btn_group_chat_search = (By.XPATH, "//span[text()='新建自动拉群']/../../..//button/span[text()='查 询']")
    # 第一行数据
    _text_first_add_group = (By.XPATH, "//span[text()='新建自动拉群']/../../../..//div[@class='cell el-tooltip']")
    # 添加使用员工
    _btn_add_group_staff = (By.XPATH, "//span[text()=' 添加']")
    # 添加使用员工的确认按钮
    _btn_add_group_staff_sure = (By.XPATH, "//span[text()='选择添加人']/../..//span[@class='dialog-footer']//span[text()='确 定']")
    # 添加标签
    _btn_add_group_tag = (By.XPATH, "//span[text()='选择标签']")
    # 添加标签确认按钮
    _btn_add_group_tag_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[2]/div/div/div/div[1]/form/div[4]/div/div/div/div/div[3]/div/button[2]/span')



    # 老客标签建群
    # 新建标签建群
    _btn_new_tag_group = (By.XPATH, "//span[text()='新建标签建群']")
    # 标签建群搜索框
    _input_tag_group = (By.XPATH, "//span[text()='新建标签建群']/../../..//input")
    # 标签建群搜索按钮
    _btn_tag_group_search = (By.XPATH, "//span[text()='新建标签建群']/../../..//button/span[text()='查 询']")
    # 第一行数据任务名
    _text_first_tag_group = (By.XPATH, "//span[text()='新建标签建群']/../../../..//div[@class='cell el-tooltip']")
    # 第一行数据发送方式
    _text_first_tag_send = (By.XPATH,"//span[text()='新建标签建群']/../../../..//tr[@class='el-table__row']//div[@class='cell']")
    # 按条件筛选客户
    _btn_group_select_client = (By.XPATH, "//span[text()='按照条件筛选客户']")
    # 选择添加人
    _btn_add_tag_group_staff = (By.XPATH, "//span[text()=' 选择添加人']")
    # 选择添加人后的确定
    _btn_add_tag_group_staff_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[2]/div/div/div[1]/form/div[2]/div/div/div[2]/div/div[3]/span/button[2]/span')
    # 个人群发
    _btn_tag_group_person = (By.XPATH, "//span[text()='个人群发']")


    # 共同点
    # 任务名称
    _input_mission_name = (By.XPATH, "//label[contains(text(),'任务名称')]/..//input")
    # 入群引导语
    _input_into_group_guide = (By.XPATH, "//label[contains(text(),'入群引导语')]/..//textarea")
    # 选择群活码
    _btn_add_group_code = (By.XPATH, "//label[text()='选择群活码']/..//i[@class='el-icon-plus']")
    # 选择群活码的输入框
    _input_add_group_code = (By.XPATH, "//span[text()='选择群活码']/../..//input")
    # 选择群活码的查询按钮
    _btn_add_group_code_search = (By.XPATH, "//span[text()='选择群活码']/../..//button/span[text()='查询']")
    # 选择群活码的选择按钮
    _btn_add_group_code_select = (By.XPATH, "//span[text()='选择群活码']/../..//span[@class='el-radio__input']")
    # 选择群活码的确定按钮
    _btn_add_group_code_sure = (By.XPATH, "//span[text()='选择群活码']/../..//button/span[text()='确 定']")
    # 发送
    _btn_add_group_send = (By.XPATH, "//span[text()='通知成员，向选中客户发送以上消息']/..//button/span")

    # 验证
    # 任务名称
    _text_add_group_name = (By.XPATH, "//div[@class='title']")
    # 使用成员
    _text_add_group_staff_id = (By.XPATH, "//label[contains(text(),'使用成员')]/..//ww-open-data")
    # 客户标签
    _text_add_group_tag = (By.XPATH, "//label[contains(text(),'客户标签')]/..//span")
    # 入群引导语
    _text_add_group_guide = (By.XPATH, "//label[contains(text(),'入群引导语')]/..//div")
    # 删除按钮
    _btn_delete_add_group = (By.XPATH, "//span[text()='删 除']")
    # 删除按钮-确定
    _btn_delete_add_group_sure = (By.XPATH, "//button/span[contains(text(),'确定')]")
    # 添加人
    _text_add_tag_group_staff_id = (By.XPATH, "//label[contains(text(),'添加人')]/..//ww-open-data")