from selenium.webdriver.common.by import By


class MaterialWebLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_others_page = (By.XPATH, '//li[text()=" 其他素材 "]')
    # 网页页面按钮
    _btn_web_page = (By.XPATH, '//p[text()="网页"]/..')

    # 添加网页按钮
    _btn_add_web = (By.XPATH, '//span[text()="添加网页"]/..')
    # 搜索网页输入框
    _input_search_web = (By.CSS_SELECTOR, 'input[placeholder="搜索网页素材"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_web = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_web_all_select = (By.CSS_SELECTOR, '.action-part span')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组网页组块
    _btn_move_group_text_groups = (By.XPATH, '(//div[@class="el-cascader-menu__wrap el-scrollbar__wrap"])[2]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # 网页操作面板展开元素
    _btn_web_operation = (By.CSS_SELECTOR, 'i[class*="more-operation"]')
    # 网页编辑按钮
    _btn_edit_web = (By.CSS_SELECTOR, 'div#fatkun-drop-panel+ul li')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 网页内容列表
    _texts_web_name = (By.CSS_SELECTOR, '.text-limit')

    # 新建页面
    # 网页分类选择框
    _btn_select_group = (By.CSS_SELECTOR, 'div[aria-label] input[placeholder="请选择"]')
    # 网页名称输入框
    _input_web_name = (By.CSS_SELECTOR, 'input[placeholder="请输入标题"]')
    # 网页组块
    _btn_text_groups = (By.CSS_SELECTOR, 'div[class="el-cascader-panel"] ul li')
    # 网页分类选择
    _btn_select_text_group = '(//span[text()="{}"]/../label)[2]'
    # 网页分组div块
    _text_select_text_group = '(//span[text()="{}"]/../label/..)[2]'
    # 上传网页按钮
    _btn_upload_pic = (By.CSS_SELECTOR, '.el-upload__text')
    # 保存按钮
    _btn_web_save = (By.XPATH, '(//span[text()="确 定"]/..)[2]')