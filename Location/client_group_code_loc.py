from selenium.webdriver.common.by import By


class ClientGroupCodeLoc:
    # 元素定位信息
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 员工活码页面
    _btn_employee_code_page = (By.XPATH, '//li[text()="创建活码"]')
    # 客户群活码tab
    _btn_client_group_tab = (By.XPATH, '//div[text()="客户群活码"]')
    # 关键词输入框
    _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 查询按钮
    _btn_search = (By.XPATH, '(//span[text()="查 询"]/..)[2]')
    # 管理群聊
    _btn_manage_client_group = (By.XPATH, '//span[text()="管理群聊"]/..')
    # 进入详情页
    _btn_enter_details = (By.CSS_SELECTOR, '#pane-2 tbody tr')
    # 活动名称列表
    _texts_act_names = (By.CSS_SELECTOR, '#pane-2 tbody tr td:nth-child(2)')
    # 活动场景列表
    _texts_act_scenes = (By.CSS_SELECTOR, '#pane-2 tbody tr td:nth-child(3)')

    # 添加
    # 新建客户群活码
    _btn_add_client_group_code = (By.XPATH, '//span[text()=" 新建客户群活码 "]/..')
    # 开始创建按钮
    _btn_create = (By.XPATH, '//span[text()="开始新建"]')
    # 添加活动头像按钮
    _btn_activity_picture = (By.CSS_SELECTOR, 'div[class="el-upload el-upload--text"]')
    # 活动名称
    _input_activity_name = (By.XPATH, '//input[@placeholder="给客户群起个名字"]')
    # 活动场景
    _input_activity_scene = (By.XPATH, '//input[@placeholder="给客户群使用的活动场景做个备注"]')
    # 引导语
    _input_leadding_words = (By.XPATH, '//input[@placeholder="可在二维码跳转页面展示社群介绍、入群引导等内容"]')
    # 无法进群提示
    _btn_prompt = (By.CSS_SELECTOR, '.el-switch__core')
    # 下一步
    _btn_next_step1 = (By.XPATH, '//span[text()="下一步 "]/..')
    # 修改确认按钮
    _btn_edit_confirm = (By.XPATH, '//span[text()="确认"]/..')
    # 添加实际群码
    _btn_add_reality_group_code = (By.XPATH, '//span[text()="添加群二维码"]/..')
    # 实际群码
    _btn_reality_group_code = (By.CSS_SELECTOR, 'div[aria-label="添加群聊"] i[class*="el-icon-p"]')
    # 选择客户群按钮
    _btn_select_client_group = (By.XPATH, '//span[text()="选择客户群"]/..')
    # 群名称
    _input_group_name = (By.CSS_SELECTOR, 'input[placeholder="请输入群名"]')
    # 查询按钮
    _btn_search_client_group = (By.XPATH, '//span[text()="查询"]/..')
    # 选择具体客户群
    _btn_select_specify_group = (By.CSS_SELECTOR, 'div[aria-label="选择客户群"] .el-table__row')
    # 客户群确定按钮
    _btn_client_group_confirm = (By.CSS_SELECTOR, 'div[aria-label="选择客户群"] .el-dialog__footer button+button')
    # 有效期
    _input_expire_date = (By.CSS_SELECTOR, 'input[placeholder="选择日期"]')
    # 下一天
    _btn_next_day = (By.CSS_SELECTOR, 'td.available')
    # 确定按钮
    _btn_sure = (By.XPATH, '//span[text()="确 定"]')
    # 下一步
    _btn_next_step2 = (By.XPATH, '//span[text()="下一步"]/..')
    # 点击完成
    _btn_finish = (By.CSS_SELECTOR, '.create-code-success button')

    # 详情页面
    # 编辑按钮
    _btn_edit_code = (By.XPATH, '//span[text()="编 辑"]/..')
    # 删除按钮
    _btn_edit_delete = (By.XPATH, '//span[text()="删 除"]/..')
    # 删除确认按钮
    _btn_edit_delete_confirm = (By.CSS_SELECTOR, 'div[class$="btns"] button+button')
    # 群名称文本
    _text_group_name = (By.CSS_SELECTOR, 'tbody td:nth-child(1)>div')
    # 有效期
    _text_effect_date = (By.CSS_SELECTOR, 'tbody td:nth-child(3)>div')
    # 引导语
    _text_guide = (By.XPATH, '//div[text()="引导语："]/following-sibling::div')
    # 活动名称
    _text_act_name = (By.CSS_SELECTOR, 'div.title')
    # 活动内容
    _text_act_info = (By.XPATH, '//div[text()="活动内容："]/following-sibling::div')

    # 管理群聊页面
    # 编辑按钮
    _btn_manage_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # 群名称
    _text_manage_group_name = (By.CSS_SELECTOR, 'tr td:nth-child(2) div')
    # 有效期
    _text_active_date = (By.CSS_SELECTOR, 'tr td:nth-child(4) div span')
