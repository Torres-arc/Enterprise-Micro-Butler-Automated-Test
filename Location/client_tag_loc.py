from selenium.webdriver.common.by import By


class ClientTagLoc:
     # 本页面元素
    # 客户管理tab
    _btn_client_manage_tab = (By.XPATH, '//span[text()="客户管理"]/..')
    # 客户页面
    _btn_client_tag_page = (By.XPATH, '//li[text()=" 客户标签 "]')
    # 新建标签组按钮
    _btn_create_tag_group = (By.XPATH, '//span[text()="新建标签组"]/..')
    # 标签组名称列表
    _texts_list_tag_group = (By.CSS_SELECTOR, 'tbody>tr>td:first-child div')
    # 特定标签组的编辑按钮
    _btn_spcecify_edit = 'tbody>tr:nth-child({})>td:last-child button:first-child'
    # 特定标签组的删除按钮
    _btn_specify_delete = 'tbody>tr:nth-child({})>td:last-child button+button'
    # ...点击后获取所有的标签
    _btn_get_tags = (By.XPATH, "//table//span[@class='el-popover__reference-wrapper']")
    # 标签的位置
    _btn_get_tags_text = (By.XPATH, "//div[contains(@id, 'el-popover') and contains(@style,'center')]/span")
    # 标签窗口
    # 标签组名称输入框
    _input_tag_group_name = (By.XPATH, '//form[@class="el-form"]/div[1]/div[2]/div/input')
    # 添加标签按钮
    _btn_add_tag = (By.XPATH, '//span[text()="+ 添加标签"]/..')
    # 标签输入框
    _input_tag = (By.XPATH, '//form[@class="el-form"]/div[2]/div[2]/div/input')
    # 确定按钮
    _btn_confirm = (By.XPATH, '//div[@class="el-dialog__footer"]/div/button[2]')
    # 现有标签列表
    _texts_list_tags_exist = (By.XPATH, '//div[@class="el-form-item__content"]/span/span')
    # 标签删除按钮
    _btn_delete_tag = '//div[@class="el-form-item__content"]/span/span[{}]/i'

    # 删除提示窗口
    # 确定按钮
    _btn_delete_sure = (By.XPATH, '//div[@class="el-message-box__btns"]/button[2]')