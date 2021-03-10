from selenium.webdriver.common.by import By


class SendMessageLoc:
    """"元素定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 企业群发页面
    _btn_addmessage = (By.XPATH, '//li[text()=" 企业群发 "]')
    # 新建群发按钮
    _btn_create_msg = (By.XPATH, '//span[text()="新建企业群发"]/..')
    # 内容消息列表
    _texts_msg = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(1)>div")
    # 创建开始日期搜索
    _input_search_creat_start_time = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    # 创建结束日期搜索
    _input_search_creat_end_time = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 内容搜索
    _input_search_msg = (By.CSS_SELECTOR, 'input[placeholder="请输入"]')
    # 查询
    _btn_search = (By.XPATH, "//span[text()='查询']/..")
    # 创建日期列表
    _texts_create_time = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(4)>div")
    # 页面数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')

    # 新建群发页面
    # 发送范围
    _btn_send_range = (By.XPATH, '//span[text()="发送给客户群"]/preceding-sibling::span')
    # 按群主选择客户群
    _btn_select_client_group = (By.XPATH, '//span[text()="按群主选择客户群"]/..')
    # 按照条件筛选
    _btn_filter = (By.XPATH, '//span[text()="按条件筛选客户"]/preceding-sibling::span')
    # 筛选条件-添加人
    _btn_select_adder = (By.CSS_SELECTOR, '.filter-pop>div button')
    # 添加人输入框
    _input_adder = (By.CSS_SELECTOR, '.el-col .el-input__inner')
    # 选择添加人
    _btn_adder_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 选择添加人窗口的确认按钮
    _btn_sure_adder = (By.CSS_SELECTOR, 'div[aria-label="选择添加人"] .el-dialog__footer button+button')
    # 从素材中心选取按钮
    _btn_select_from_material_center = (By.XPATH, '//span[text()="从素材中心选取"]/..')
    # 文本
    # 搜索
    _input_search_text = (By.CSS_SELECTOR, '#pane-text .filter-left > .el-input > .el-input__inner')
    # 单选框
    _btn_select_text = (By.CSS_SELECTOR, ".radio .el-radio__inner")
    # 确认按钮
    _btn_sure_text = (By.CSS_SELECTOR, ".material-dialog .el-button--primary")
    # 网页
    _btn_web_tab = (By.CSS_SELECTOR, '#tab-web')
    _input_search_web = (By.CSS_SELECTOR, '#pane-web .filter-left > .el-input > .el-input__inner')
    # _btn_select_web = (By.CSS_SELECTOR, 'div[aria-label="选取网页素材"] #pane-web .water-fall-item')
    _btn_select_web = (By.XPATH, '//*[@id="pane-web"]/div/div[2]/div[2]/div/div/div[1]/div/label/span[1]/span')
    _btn_sure_web = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 图片
    _btn_pic_tab = (By.CSS_SELECTOR, "#tab-picture")
    _input_search_pic = (By.CSS_SELECTOR, '#pane-picture .filter-left > .el-input > .el-input__inner')
    # _btn_select_pic = (By.CSS_SELECTOR, 'div[aria-label="选取图片素材"] #pane-picture div[class*="picture"] .water-fall-item')
    _btn_select_pic = (By.XPATH, "//div[@id='pane-picture']//span[@class='el-checkbox__input']")
    _btn_sure_pic = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 海报
    _btn_poster_tab = (By.CSS_SELECTOR, "#tab-poster")
    _input_search_poster = (By.CSS_SELECTOR, '#pane-poster .filter-left > .el-input > .el-input__inner')
    # _btn_select_poster = (By.CSS_SELECTOR, 'div[aria-label="选取海报素材"] #pane-poster div[class*="picture-c"]:nth-child(4) .el-checkbox')
    _btn_select_poster = (By.XPATH, '//*[@id="pane-poster"]/div/div[2]/div[4]/div/div/div[1]/div/div/label/span[1]')
    _btn_sure_poster = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 小程序
    _btn_mini_tab = (By.CSS_SELECTOR, "#tab-miniprogram")
    _input_search_mini = (By.CSS_SELECTOR, '#pane-miniprogram .filter-left > .el-input > .el-input__inner')
    # _btn_select_mini = (By.CSS_SELECTOR, 'div[aria-label="选取小程序素材"] #pane-miniprogram div[class*="picture-c"]:nth-child(5) .water-fall-item')
    _btn_select_mini = (By.XPATH, '//*[@id="pane-miniprogram"]/div/div[2]/div[5]/div/div/div[1]/div/label/span[1]/span')
    _btn_sure_mini = (By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary")
    # 发送
    _btn_send = (By.XPATH, '//span[text()="通知成员发送"]/..')
    # 时间
    _btn_time = (By.XPATH, "//input[@placeholder]")
    _btn_select_time = (By.XPATH, "//td[@class='available']")
    _btn_select_time_sure = (By.XPATH, "//button/span[contains(text(),'确定')]")
    # 第一个的值
    # 第一个的值的消息内容
    _text_enterprise_message_content = (By.XPATH, "//table//span[@class='content']")
    # 第一个的值的群发类型
    _text_enterprise_message_type = (By.XPATH, "//tbody/tr/td[2]/div")