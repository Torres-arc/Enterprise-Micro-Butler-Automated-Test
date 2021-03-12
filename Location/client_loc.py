from selenium.webdriver.common.by import By


class ClientLoc:
    # 本页面元素
    # 客户管理tab
    _btn_client_manage_tab = (By.XPATH, '//span[text()="客户管理"]/..')
    # 客户页面
    _btn_client_page = (By.XPATH, '//li[text()=" 客户 "]')
    # 暂无数据显示
    _text_ele_empty_data = (By.CSS_SELECTOR, '.el-table__empty-text')
    # 姓名输入框
    _input_name = (By.CSS_SELECTOR, 'input[placeholder="请输入"]')
    # 更多筛选按钮
    _btn_more_filter = (By.CSS_SELECTOR, '.more_btn')
    # 添加人输入框
    _btn_select_adder = (By.XPATH, '//p[text()="添加人"]/following-sibling::div')
    # 标签输入框
    _btn_select_tag = (By.XPATH, '//p[text()="标签"]/following-sibling::div')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 提醒打标签按钮
    _btn_remind = (By.XPATH, '//span[text()="批量提醒打标签"]')
    # 指定客户
    _btn_specify_custom = 'tbody tr:nth-child({}) td:first-child div'
    # 客户姓名表
    _texts_clients_name = (By.CSS_SELECTOR, 'tbody tr td:first-child div')
    # 客户添加人表
    _texts_clients_adders = (By.CSS_SELECTOR, 'td ww-open-data')
    # 下一页按钮
    _btn_next = (By.CLASS_NAME, 'btn-next')
    # 页面数
    _text_pages_number = (By.CSS_SELECTOR, '.el-pager li:last-child')
    # 客户标签组
    _texts_customs_tags = 'tbody tr:nth-child({}) td:nth-child(3) div span[class*="tag"]'

    # 标签页元素
    _btn_tag_group = '//div[@class="tagName" and text()="{}"]'
    _btn_tags = '//li[@class="tag" and text()=" {} "]'

    # 组织架构弹窗
    _input_addname = (By.CSS_SELECTOR, '.el-col input')
    _btn_adder = (By.CLASS_NAME, 'custom-tree-node')
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog"]/div[3]/div/button[2]')
    _btn_group_search = (By.XPATH, '//input[@placeholder="请输入关键词"]/../../../..//span[text()="查询"]')
    # 客户详情页面
    # 所有标签
    _texts_full_tags = (By.XPATH, '//span[@class="el-tag el-tag--info el-tag--light"]')
    # 所有添加人
    _texts_full_adders = (By.CSS_SELECTOR, '.t-row ww-open-data[type="userName"]')
    # 返回按钮
    _btn_back = (By.XPATH, '//span[text()="返回"]/..')
