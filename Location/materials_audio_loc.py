from selenium.webdriver.common.by import By


class MaterialAudioLoc:
    # 客户营销tab
    _btn_client_marketing_tab = (By.XPATH, '//span[text()="客户营销"]/..')
    # 海报素材页面
    _btn_material_others_page = (By.XPATH, '//li[text()=" 其他素材 "]')
    # 语音页面按钮
    _btn_audio_page = (By.XPATH, '//p[text()="语音"]/..')

    # 添加语音按钮
    _btn_add_audio = (By.XPATH, '//span[text()="添加语音"]/..')
    # 搜索语音输入框
    _input_search_text = (By.CSS_SELECTOR, 'input[placeholder="搜索语音素材"]')
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
    _btn_delete_audio = (By.XPATH, '//span[text()="删除"]/..')
    # 点击具体分类
    _btn_select_specify_group = '//span[text()="{}"]/..'
    # 全选勾选框
    _btn_all_select_audio = (By.CSS_SELECTOR, '.header_sel_wrap span')
    # 分类删除按钮
    _btn_delete_group = '//span[text()="{}"]/following-sibling::i'
    # 编辑完成按钮
    _btn_edit_complete = (By.XPATH, '//span[text()="完成"]/..')
    # 删除确认按钮
    _btn_delete_confirm = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
    # 移动分组输入框按钮
    _btn_input_move_group = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 移动分组语音组块
    _btn_move_group_audio_groups = (By.XPATH, '(//div[@class="el-cascader-menu__wrap el-scrollbar__wrap"])[2]')
    # 移动分组选择框
    _audio_select_move_group = '//span[text()="{}"]/../label/..'
    # 移动分组选择框
    _btn_select_move_group = '//span[text()="{}"]/../label'
    # 移动分组选择按钮
    _btn_move_group_confirm = (By.XPATH, '//span[text()="确定"]/..')
    # 语音编辑按钮
    _btn_edit_audio = (By.XPATH, '//span[text()="编辑"]/..')
    # 语音分类名称输入框
    _input_text_group_name = (By.CSS_SELECTOR, '.catagory__list input')
    # 主分类名称列表
    _texts_main_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap"] .catagory__list>span span')
    # 子分类名称列表
    _texts_child_groups = (By.CSS_SELECTOR, 'div[class="main-catagory__wrap sub__wrap"] .catagory__list>span span')
    # 语音内容列表
    _texts_audio_name = (By.CSS_SELECTOR, 'table tr td:nth-child(2) div')

    # 新建页面
    # 语音分类选择框
    _btn_select_group = (By.CSS_SELECTOR, 'div[aria-label] input[placeholder="请选择"]')
    # 语音组块
    _btn_audio_groups = (By.CSS_SELECTOR, 'div[class="el-cascader-panel"] ul li')
    # 语音分类选择
    _btn_select_audio_group = '(//span[text()="{}"]/../label)[2]'
    # 语音分组div块
    _text_select_audio_group = '(//span[text()="{}"]/../label/..)[2]'
    # 语音内容输入框
    _input_audio_msg = (By.CSS_SELECTOR, 'input[placeholder="请输入素材名称"]')
    # 语音上传按钮
    _btn_upload_audio = (By.CSS_SELECTOR, '.img-upload-before')
    # 保存按钮
    _btn_save = (By.XPATH, '(//span[text()="确 定"]/..)[2]')
    # 保存确认按钮
    _btn_confirm_audio = (By.CSS_SELECTOR, '.el-message-box__btns button+button')
