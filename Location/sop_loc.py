from selenium.webdriver.common.by import By


class SopLoc:
    # 个人群发
    _btn_person_send = (By.XPATH, "//li[contains(text(),'个人群发')]")


    # 群SOP页面
    _btn_group_sop_page = (By.XPATH, "//div[contains(text(),'群发客户群任务(群SOP)')]")
    # 客户群新建任务按钮
    _btn_group_sop_create = (By.XPATH, "//p[contains(text(),'客户群')]/..//span[contains(text(),'新建任务')]")
    # 客户群的查询按钮
    _btn_group_sop_search = (By.XPATH, "//p[contains(text(),'客户群')]/../..//button/span[contains(text(),'查 询')]")
    # 客户群的查询输入框
    _input_group_sop_search = (By.XPATH, "//p[contains(text(),'客户群')]/../..//input")


    # 朋友圈SOP页面
    _btn_friends_circle_page = (By.XPATH, "//div[contains(text(),'群发朋友圈任务(朋友圈SOP)')]")
    # 朋友圈新建任务按钮
    _btn_friends_circle_sop_create = (By.XPATH, "//p[contains(text(),'朋友圈')]/..//span[contains(text(),'新建任务')]")
    # 朋友圈的查询按钮
    _btn_friends_circle_sop_search = (By.XPATH, "//p[contains(text(),'朋友圈')]/../..//button/span[contains(text(),'查 询')]")
    # 朋友圈的查询输入框
    _input_friends_circle_sop_search = (By.XPATH, "//p[contains(text(),'朋友圈')]/../..//input")


    # 共同位置
    # 任务名称输入框
    _input_act_name = (By.XPATH, "//label[text()='任务名称']/..//input[@class='el-input__inner']")
    # 执行范围选择框
    _btn_select_limit = (By.XPATH, "//label[text()='执行范围']/..//button/span")
    # 执行范围选择框，选择成员
    _btn_select_friends_circle_limit = (By.XPATH, "//label[text()='执行范围']/..//span")
    # 选择成员的确认
    _btn_select_friends_circle_limit_sure = (By.XPATH, "//div[@class='el-dialog__wrapper']//button/span[text()='确 定']")
    # 设置推送-推送名称
    _input_submit_name = (By.XPATH, "//label[text()='设置推送']/..//input")
    # 设置推送-开始时间点击
    _btn_submit_time = (By.XPATH, "//label[text()='设置推送']/..//input[@placeholder='起始时间']")
    # 开始时间选择今天之后的一天
    _btn_submit_start_time = (By.XPATH, "//td[@class='available']")
    # 结束时间选择下个月的一天
    _btn_submit_end_time = (By.XPATH, "//div[contains(@class, 'is-right')]//td[@class='available']")
    # 时间选择器的确定
    _btn_time_sure = (By.XPATH, "//button/span[contains(text(),'确定')]")
    # 输入框
    _input_msg = (By.XPATH, "//textarea")
    # 新建按钮
    _btn_new_sop = (By.XPATH, "//button/span[contains(text(),'新建')]")


    # 添加附件
    _btn_add_attach = (By.XPATH, "//div[contains(text(),'添加')]")
    # 图片
    _btn_pic = (By.XPATH, "//p[text()='图 片']")
    # 图片选择按钮
    _btn_select_attach_pic = (By.XPATH,"//div[@class='filter-material-content']/div[3]//span[@class='el-checkbox__input']")
    # 海报
    _btn_poster = (By.XPATH, "//p[text()='海 报']")
    # 海报选择按钮
    _btn_select_attach_poster = (By.XPATH, "//div[@class='filter-material-content']/div[4]//span[@class='el-checkbox__input']")
    # 网页
    _btn_web = (By.XPATH, "//p[text()='网 页']")
    # 网页选择按钮
    _btn_select_attach_web = (By.XPATH, "//div[@class='filter-material-content']/div[2]//span[@class='el-radio__input']")
    # 搜索框输入
    _input_search_attach = (By.XPATH, "//input[@placeholder='搜索素材']")
    # 确定按钮
    _btn_attach_sure = (By.XPATH, "//span[@class='dialog-footer']//button/span[text()='确 定']")

    # 添加群聊
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')

    # 删除SOP
    _btn_delete_sop = (By.XPATH, "//span[text()='删 除']")
    # 删除SOP的确认按钮
    _btn_delete_sop_sure = (By.XPATH, "//span[contains(text(),'确定')]")

    # 第一个位置的sop名称
    _text_first_group_name = (By.XPATH, "//p[contains(text(),'客户群')]/../..//div[@class='cell el-tooltip']")
    # 第一个位置的朋友圈sop名称
    _text_first_friends_circle_name = (By.XPATH, "//p[contains(text(),'朋友圈')]/../..//div[@class='cell el-tooltip']")
    # 编辑界面中信息是否正确
    _text_sop_name = (By.XPATH, "//div[contains(text(),'任务名称')]/../div[@class='row-content']")
    _text_group_name = (By.XPATH, "//div[contains(text(),'执行群聊')]/../div[@class='row-content']/span")
    _text_staff_name = (By.XPATH, "//div[contains(text(),'执行成员')]/..//ww-open-data")
    _text_submit_name = (By.XPATH, "//div[contains(text(),'推送名称')]/../div[@class='row-content']")
    _text_submit_msg = (By.XPATH, "//div[contains(text(),'推送内容：')]/../div[@class='row-content']/div")
    # 编辑SOP
    _btn_edit_sop = (By.XPATH, "//span[text()='编 辑']")
    # 编辑时的保存按钮
    _btn_save_sop = (By.XPATH, "//button/span[contains(text(),'保存')]")

























    # # 规则名称列表
    # _texts_rule_names = (By.CSS_SELECTOR, 'tbody tr td:nth-child(1) div')
    # # 创建人列表
    # _texts_key_words = 'tbody tr td:nth-child(2) ww-open-data"]'
    # # 详情
    # _btn_detail = (By.XPATH, '//span[text()="详情"]/..')
    # # 编辑
    # _btn_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # # 删除
    # _btn_delete = (By.XPATH, '//span[text()="删除"]/..')
    # # 删除确认按钮
    # _btn_confirm_delete = (By.CSS_SELECTOR, 'div[aria-hidden="false"] button+button')
    #
    # # 规则名称搜索框
    # _input_search_act_name = (By.CSS_SELECTOR, 'input[placeholder="请输入规则名称"]')
    # # 页码数
    # _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # # 翻页按钮
    # _btn_next_page = (By.CSS_SELECTOR, '.btn-next')
    #
    # # 新建页面
    # # 规则名称输入框
    # _input_act_name = (By.CSS_SELECTOR, 'input.el-input__inner')
    # # 选择群聊按钮
    # _btn_choose_group = (By.XPATH, '//span[text()="选择群聊"]/..')
    # # 删除群聊按钮
    # _btn_delete_group = (By.CSS_SELECTOR, '.choose-group-box>span>i')
    # # 关键词输入框
    # _input_key_words = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # # 群聊查询按钮
    # _btn_search_group = (By.XPATH, '//span[text()="查询"]/..')
    # # 群聊选择框
    # _btn_select_group = (By.CSS_SELECTOR, '.el-checkbox__inner')
    # # 群聊确定按钮
    # _btn_confirm_group = (By.CSS_SELECTOR, 'div[aria-label="添加群聊"] .el-dialog__footer button+button')
    # # 添加推送按钮
    # _btn_add_msg = (By.XPATH, '//span[text()="添加推送"]/..')
    # # 修改推送按钮
    # _btn_edit_msg = (By.XPATH, '//span[text()="修改"]/..')
    # # 推送内容输入框
    # _input_send_name = (By.XPATH, '//label[text()="内容名称"]/following-sibling::div/div/input')
    # # 添加时间选择框
    # _btn_add_time = (By.CSS_SELECTOR, 'input[placeholder="起始时间"]')
    # # 开始日期输入框
    # _input_start_time = (By.CSS_SELECTOR, 'input[placeholder="开始日期"]')
    # # 开始时间输入框
    # _input_start_time_time = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # # 结束日期输入框
    # _input_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束日期"]')
    # # 结束时间输入框
    # _input_end_time_time = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # # 日期确认按钮
    # _btn_confirm_date = (By.CSS_SELECTOR, '.el-picker-panel__footer button+button')
    # # 消息输入框
    # _input_msg = (By.CSS_SELECTOR, 'textarea[placeholder="直接开始输入..."]')
    # # 素材确认按钮
    # _btn_confirm_msg = (By.CSS_SELECTOR, 'div[class="el-form-item el-form-item--small"] button')
    # # 新建确定按钮
    # _btn_confirm = (By.XPATH, '//span[text()=" 确定 "]/..')
    #
    # # 详情页面
    # # 规则名称
    # _text_detail_rule_name = (By.XPATH, '//label[text()="规则名称"]/following-sibling::div/span')
    # # 执行群聊
    # _text_detail_group_name = (By.XPATH, '//label[text()="执行群聊"]/following-sibling::div/span')
    # # 开始时间
    # _text_detail_start_time = (By.XPATH, '//span[text()="至"]/preceding-sibling::span')
    # # 结束时间
    # _text_detail_end_time = (By.XPATH, '//span[text()="至"]/following-sibling::span')
    # # 推送名称
    # _text_detail_msg_name = (By.CSS_SELECTOR, '.left')
    # # 推送内容
    # _text_detail_msg = (By.CSS_SELECTOR, '.text')
