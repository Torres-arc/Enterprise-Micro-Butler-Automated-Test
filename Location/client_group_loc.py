from selenium.webdriver.common.by import By


class ClientGroupLoc:
    # 本页面元素
    # 客户群页面
    _btn_client_group_page = (By.XPATH, '//li[text()=" 客户群 "]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 客户群名输入框
    _input_group_name = (By.XPATH, '//input[@placeholder="请输入"]')
    # 群主输入框
    _btn_select_group_master = (By.XPATH, '//span[text()="请选择"]/..')
    # 创建日期输入框（起始）
    _input_create_start_time = (By.XPATH, '//input[@placeholder="开始时间"]')
    # 更多筛选按钮
    _btn_more_filter = (By.CSS_SELECTOR, '.more_btn')
    # 创建日期输入框（结束）
    _input_create_end_time = (By.XPATH, '//input[@placeholder="结束时间"]')
    # 客户群名列表
    _texts_client_groups_names = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(2) .cell span')
    # 页面数
    _text_pages_number = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 下一页按钮
    _btn_next = (By.CLASS_NAME, 'btn-next')
    # 群主名列表
    _texts_master_name = (By.CSS_SELECTOR, 'td ww-open-data')
    # 创建日期列表
    _texts_create_time = (By.CSS_SELECTOR, 'tbody>tr>td:last-child .cell')
    # 导出列表
    _btn_export_groups_list = (By.XPATH, '//span[text()="导出列表"]/..')

    # 点击群主输入框后显示的元素
    # 群主搜索输入框
    _input_client = (By.XPATH, '//input[@placeholder="请输入关键词"]')
    # 员工节点
    _btn_client_node = (By.CLASS_NAME, 'custom-tree-node')
    # 群主选择确认按钮
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')