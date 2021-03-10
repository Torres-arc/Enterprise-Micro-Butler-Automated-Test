from selenium.webdriver.common.by import By


class ClientCodeLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 员工活码页面
    _btn_employee_code_page = (By.XPATH, '//li[text()="创建活码"]')
    # 新建员工活码
    _btn_create_employee_code = (By.XPATH, '//span[text()=" 新建员工活码 "]/..')
    # 删除
    _btn_delete = (By.XPATH, '//span[text()="删 除"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, 'div[class*="btns"] button+button')
    # 更多筛选按钮
    _btn_search_more_filter = (By.XPATH, '//span[text()="更多筛选"]')
    # 使用员工输入框
    _btn_user = (By.XPATH, '//label[text()="使用员工"]/following-sibling::div')
    # 活动场景输入框
    _input_act_scene = (By.XPATH, '//label[text()="活动场景"]/following-sibling::div/div/input')
    # 创建人输入框
    _btn_creator = (By.XPATH, '//label[text()="创建人"]/following-sibling::div/div')
    # 创建时间输入框
    _input_creat_time1 = (By.CSS_SELECTOR, 'input[placeholder="开始时间"]')
    _input_creat_time2 = (By.CSS_SELECTOR, 'input[placeholder="结束时间"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 查看详情按钮
    _btn_check_detail = (By.CSS_SELECTOR, 'table tbody tr')
    # 使用员工文本
    _texts_user = 'tbody tr:nth-child({}) td:nth-child(2) ww-open-data'
    # 活动场景文本
    _texts_actscene = (By.CSS_SELECTOR, '#pane-1 tbody td:nth-child(3) div')
    # 创建时间文本
    _texts_ctetime = (By.CSS_SELECTOR, '#pane-1 tbody td:nth-child(5) div span')
    # 创建人文本
    _texts_creator = (By.CSS_SELECTOR, 'tbody td:nth-child(4) ww-open-data')
    # 页数
    _text_page_num = (By.CSS_SELECTOR, '.el-pager>li:last-child')
    # 翻页按钮
    _btn_next_page = (By.CSS_SELECTOR, '.btn-next')
    # 全选框
    _btn_check_box = (By.CSS_SELECTOR, '.el-checkbox>span>span')

    # 新建界面
    # 批量单人活码
    _btn_type_batch_single = (By.XPATH, '//span[text()="批量单人"]/../span')
    # 单人活码
    _btn_type_single = (By.XPATH, '//span[text()="单人"]/../span')
    # 多人活码
    _btn_type_multi = (By.XPATH, '//span[text()="多人"]/../span')
    # 使用员工
    _btn_add_employer = (By.XPATH, '//span[text()=" 添加 "]')
    # 活动场景输入框
    _input_activity_scene = (By.XPATH, '//*[@placeholder="输入活动场景"]')
    # 高级设置
    _btn_advanced_design = (By.XPATH, '//span[text()="高级设置"]/..')
    # 添加标签
    _btn_add_tags = (By.XPATH, '//span[text()="添加标签"]/..')
    # 选择前三个标签
    _btn_tags1 = (By.XPATH, '(//*[@class="tag"])[1]')
    _btn_tags2 = (By.XPATH, '(//*[@class="tag"])[2]')
    _btn_tags3 = (By.XPATH, '(//*[@class="tag"])[3]')
    # 确定标签按钮
    _btn_tag_confirm = (By.CSS_SELECTOR, 'div[aria-label="选择标签"]>.el-dialog__footer button+button')
    # 添加欢迎语
    _btn_welcoming_speech_button = (By.XPATH, '//div[text()=" 添加图片/网页/小程序消息 "]')
    # 欢迎语图片按钮
    _btn_wel_pic = (By.XPATH, '//p[text()="图 片"]/../..')
    # 欢迎语网页按钮
    _btn_wel_web = (By.XPATH, '//p[text()="网 页"]/../..')
    # 欢迎语小程序按钮
    _btn_wel_mini = (By.XPATH, '//p[text()="小程序"]/../..')
    # 网页搜索输入框
    _input_search_web = (By.CSS_SELECTOR, '[placeholder="搜索素材"]')
    # 网页选择按钮
    _btn_select_web = (By.CSS_SELECTOR, '.waterFall .water-fall-item')
    # 网页选择按钮
    _btn_select_mini = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] div[class*="pic"] .waterFall>.water-fall-item')
    # 网页选择确定按钮
    _btn_web_sure = (By.CSS_SELECTOR, 'div[aria-label="添加网页消息"] div[class$="footer"] button:last-child')
    # 网页选择确定按钮
    _btn_mini_sure = (By.CSS_SELECTOR, 'div[aria-label="添加小程序消息"] div[class$="footer"] button:last-child')
    # 欢迎语输入框
    _input_welcomg = (By.CSS_SELECTOR, 'textarea')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="新建"]/..')
    # 保存按钮
    _btn_save2 = (By.XPATH, '//span[text()="保存"]/..')

    # 组织架构
    # 输入框
    _input_client = (By.CSS_SELECTOR, 'input[placeholder$="关键词"]')
    # 结点
    _btn_client_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 外部使用员工确定
    _btn_confirm_outer = (By.CSS_SELECTOR, 'div[aria-label="选择使用员工"] .el-dialog__footer button+button')
    # 外部创建人确定
    _btn_confirm_outer2 = (By.CSS_SELECTOR, 'div[aria-label="选择创建人"] .el-dialog__footer button+button')
    # 创建选择员工确定
    _btn_confirm = (By.CSS_SELECTOR, 'div[aria-label="组织架构"] .el-dialog__footer button+button')

    # 活码详情页面
    # 使用员工文本
    _text_user = (By.CSS_SELECTOR, 'svg+div ww-open-data')
    # 活动场景
    _text_act_scene = (By.CSS_SELECTOR, '.content .row:nth-child(4)>div+div')
    # 标签文本
    _texts_tag_list = (By.CSS_SELECTOR, 'div[class="tag"]')
    # 欢迎语文本
    _text_wel_speech = (By.CSS_SELECTOR, 'div[class^="wel"] .text')
    # 编辑按钮
    _btn_edit = (By.XPATH, '//span[text()="编辑"]/..')
    # 删除按钮
    _btn_single_delete = (By.XPATH, '//span[text()="删除"]/..')
    # 删除确认按钮
    _btn_single_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
