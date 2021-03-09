from selenium.webdriver.common.by import By


class WelcomeMessageLoc:
    """欢迎语定位信息"""
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 欢迎语页面
    _btn_welcome_page = (By.XPATH, '//li[text()=" 欢迎语 "]')
    # 部门员工tab
    _btn_department_client_tab = (By.XPATH, '//div[text()="部门员工欢迎语"]')

    # 员工欢迎语页面
    # 新建员工欢迎语按钮
    _btn_create_client_welcome = (By.XPATH, '//span[text()="新建员工欢迎语"]/..')
    # 员工欢迎语列表
    _texts_clients_welcome = (By.CSS_SELECTOR, '#pane-0 tbody tr td:first-child div')
    # 员工页面编辑按钮
    _btn_client_edit = (By.CSS_SELECTOR, '#pane-0 tbody tr td:nth-child(4) button')
    # 员工页面删除按钮
    _btn_client_delete = (By.CSS_SELECTOR, '#pane-0 tbody tr td:nth-child(4) button+button')
    # 员工页面删除确认按钮
    _btn_client_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns  button+button')
    # 员工页面搜索输入框
    _input_client_search = (By.CSS_SELECTOR, '#pane-0 input[placeholder$="关键词"]')
    # 员工页面查询按钮
    _btn_client_search = (By.CSS_SELECTOR, '#pane-0 .search button')
    # 员工欢迎语第一条数据的值
    _texts_client_welcome = (By.XPATH, "//tbody//div[@class='cell']//div")

    # 部门员工欢迎语页面
    # 员工的openid位置
    _text_user_open_id = (By.XPATH, "//label[text()='使用员工']/..//ww-open-data")
    # 新建部门员工欢迎语按钮
    _btn_create_department_client_welcome = (By.XPATH, '//span[text()="新建部门员工欢迎语"]/..')
    # 部门员工欢迎语列表
    _texts_department_clients_welcome = (By.CSS_SELECTOR, '#pane-1 tbody tr td:first-child div')
    # 部门员工页面编辑按钮
    _btn_department_client_edit = (By.CSS_SELECTOR, '#pane-1 tbody tr td:nth-child(4) button')
    # 部门员工页面删除按钮
    _btn_department_client_delete = (By.CSS_SELECTOR, '#pane-1 tbody tr td:nth-child(4) button+button')
    # 部门员工页面搜索输入框
    _input_department_client_search = (By.CSS_SELECTOR, '#pane-1 input[placeholder$="关键词"]')
    # 部门员工页面查询按钮
    _btn_department_client_search = (By.CSS_SELECTOR, '#pane-1 .search button')
    # 部门员工欢迎语第一条数据的值
    _texts_department_client_welcome = (By.XPATH, "//div[@class='el-table__body-wrapper is-scrolling-none']//div[@class='cell']/div")

    # 添加素材按钮
    _btn_add_materials = (By.XPATH, '//div[text()="添加图片/网页/小程序消息"]')
    # 添加图片按钮
    _btn_add_pic = (By.CSS_SELECTOR, '.material-type-list>div')
    # 欢迎语输入框
    _input_welcome = (By.CSS_SELECTOR, 'textarea')
    # 新建按钮
    _btn_create = (By.XPATH, '//span[text()="新建"]/..')
    # 插入客户昵称按钮
    _btn_insert_client_nickname = (By.XPATH, '//span[text()="插入客户昵称"]/..')
    # 添加员工按钮
    _btn_select_staff = (By.XPATH, '//span[text()="添加"]/..')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')

    # 组织架构
    # 员工搜索输入框
    _input_select_staff = (By.CSS_SELECTOR, 'input[placeholder="请输入关键词"]')
    # 员工节点
    _btn_staff_node = (By.CSS_SELECTOR, '.custom-tree-node')
    # 选择确认按钮
    _btn_confirm = (By.CSS_SELECTOR, 'div[aria-label="组织架构"] div[class$="footer"] button+button')