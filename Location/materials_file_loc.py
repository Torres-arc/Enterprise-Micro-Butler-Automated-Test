from selenium.webdriver.common.by import By


class MaterialFileLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_others_page = (By.XPATH, '//li[text()=" 其他素材 "]')
    # 文本页面按钮
    _btn_file_page = (By.XPATH, '//p[text()="文件"]/..')

    # 添加文本按钮
    _btn_add_file = (By.XPATH, '//span[text()="添加文件"]/..')
    # 搜索文本输入框
    _input_search_file = (By.CSS_SELECTOR, 'input[placeholder="搜索文件素材"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 编辑分类按钮
    _btn_edit_group = (By.CSS_SELECTOR, '.edit_btn')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_file = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_all_select_file = (By.CSS_SELECTOR, '.header_sel_wrap span')
    # 文件选择勾选框
    _btn_check_file = (By.CSS_SELECTOR, 'div[role="group"] label')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组文本组块
    _btn_move_group_text_groups = (By.XPATH, '(//div[@class="el-cascader-menu__wrap el-scrollbar__wrap"])[2]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # 文件编辑按钮
    _btn_edit_file = (By.XPATH, '//span[text()="编辑"]/..')
    # 文件分类名称输入框
    _input_file_group_name = (By.CSS_SELECTOR, '.catagory__list input')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 文件内容列表
    _texts_file_name = (By.CSS_SELECTOR, 'table tr td:nth-child(2) div')

    # 新建页面
    # 文件分类选择框
    _btn_select_group = (By.CSS_SELECTOR, 'div[aria-label] input[placeholder="请选择"]')
    # 文件组块
    _btn_file_groups = (By.CSS_SELECTOR, 'div[class="el-cascader-panel"] ul li')
    # 文件分类选择
    _btn_select_file_group = '(//span[text()="{}"]/../label)[2]'
    # 文件分组div块
    _text_select_file_group = '(//span[text()="{}"]/../label/..)[2]'
    # 文件上传按钮
    _btn_upload_file = (By.CSS_SELECTOR, '.img-upload-before')
    # 文件内容输入框
    _input_file_msg = (By.CSS_SELECTOR, '.el-message-box__input input')
    # 保存按钮
    _btn_save = (By.XPATH, '(//span[text()="确 定"]/..)[2]')
    # 保存确认按钮
    _btn_save_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
