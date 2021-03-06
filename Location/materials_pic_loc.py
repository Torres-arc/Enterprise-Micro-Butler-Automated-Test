from selenium.webdriver.common.by import By


class MaterialPicLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_others_page = (By.XPATH, '//li[text()=" 其他素材 "]')
    # 图片页面按钮
    _btn_pic_page = (By.XPATH, '//p[text()="图片"]/..')

    # 添加图片按钮
    _btn_add_pic = (By.XPATH, '//span[text()="添加图片"]/..')
    # 搜索图片输入框
    _input_search_pic = (By.CSS_SELECTOR, 'input[placeholder="搜索图片素材"]')
    # 查询按钮
    _btn_search = (By.XPATH, '//span[text()="查询"]/..')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_pic = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_pic_all_select = (By.CSS_SELECTOR, '.action-part span')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组图片组块
    _btn_move_group_text_groups = (By.XPATH, '(//div[@class="el-cascader-menu__wrap el-scrollbar__wrap"])[2]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # 图片块元素
    _btn_pic_div = (By.CSS_SELECTOR, 'div[class*="el-image"]')
    # 图片编辑按钮
    _btn_edit_pic = (By.CSS_SELECTOR, 'i[class*="el-icon-edit"]')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 图片内容列表
    _texts_pic_name = (By.CSS_SELECTOR, '.bottom-name span+span')

    # 新建页面
    # 图片分类选择框
    _btn_select_group = (By.CSS_SELECTOR, 'div[aria-label] input[placeholder="请选择"]')
    # 图片名称输入框
    _input_pic_name = (By.XPATH, '//label[text()="图片名称"]/following-sibling::div/div/input')
    # 图片组块
    _btn_text_groups = (By.CSS_SELECTOR, 'div[class="el-cascader-panel"] ul li')
    # 图片分类选择
    _btn_select_text_group = '(//span[text()="{}"]/../label)[2]'
    # 图片分组div块
    _text_select_text_group = '(//span[text()="{}"]/../label/..)[2]'
    # 上传图片按钮
    _btn_upload_pic = (By.CSS_SELECTOR, '.img-upload-before')
    # 保存按钮
    _btn_pic_save = (By.XPATH, '(//span[text()="确 定"]/..)[3]')