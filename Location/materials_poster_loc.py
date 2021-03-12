from selenium.webdriver.common.by import By


class MaterialPosterLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_poster_page = (By.XPATH, '//li[text()=" 海报素材 "]')

    # 编辑分类按钮
    _btn_edit_group = (By.CSS_SELECTOR, '.edit_btn')
    # 添加主分类
    _btn_add_main_group = (By.XPATH, '//span[text()="+ 添加分类"]/..')
    # 添加子分类按钮
    _btn_add_child_group = (By.XPATH, '(//span[text()="+ 添加分类"]/..)[2]')
    # 添加海报按钮
    _btn_add_poster = (By.XPATH, '//span[text()="添加海报"]/..')
    # 移动分组按钮
    _btn_move_group = (By.XPATH, '//span[text()="移动分组"]/..')
    # 删除按钮
    _btn_delete_poster = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_all_select = (By.CSS_SELECTOR, '.action-part span')
    # 海报选择勾选框
    _btn_check_poster = (By.CSS_SELECTOR, '.post-des .el-checkbox__inner')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 海报搜索输入框
    _input_poster_search = (By.CSS_SELECTOR, 'input[placeholder="搜索海报素材"]')
    # 海报查询按钮
    _btn_search = (By.XPATH, '//span[text()="查 询"]/..')
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组选择框
    _text_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # # 移动分组二次确认按钮
    # _btn_move_group_twice_confirm = ()
    # 海报块
    _btn_poster = (By.CSS_SELECTOR, 'div[role="group"]')
    # 海报编辑按钮
    _btn_edit_poster = (By.CSS_SELECTOR, 'i[class="el-tooltip el-icon-edit item"]')
    # 海报分类名称输入框
    _input_poster_group_name = (By.CSS_SELECTOR, '.catagory__list input')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 海报名称列表
    _texts_poster_name = (By.CSS_SELECTOR, '.text-limit')

    # 新建页面
    # 海报名称输入框
    _input_poster_name = (By.CSS_SELECTOR, 'input[placeholder="请输入海报名称"]')
    # 海报分类输入框
    _btn_poster_groups = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 海报分类选择
    _btn_select_poster_group = '//span[text()="{}"]/../label'
    # 背景图片选择
    _btn_upload_pic = (By.XPATH, '//div[text()="上传图片"]')
    # 分类选择面板第一项
    _text_first_group = (By.CSS_SELECTOR, 'div[role="menu"]')
    # 保存按钮
    _btn_save = (By.XPATH, '//span[text()="保存"]/..')
    # 标题元素
    _btn_title = (By.CSS_SELECTOR, '.page_title')
