from selenium.webdriver.common.by import By


class FissionActionLoc:
    # 裂变活动的定位
    # 裂变活动
    _btn_fission_action = (By.XPATH, "//li[contains(text(),'裂变活动')]")
    # 任务裂变
    _btn_mission_fission = (By.XPATH, "//div[text()='任务裂变(任务宝)']")
    # 群裂变
    _btn_group_fission = (By.XPATH, "//div[text()='群裂变']")

    # 任务裂变
    # 新建任务裂变
    _btn_new_mission_fission = (By.XPATH, "//button/span[text()='新建任务裂变']")
    # 任务裂变搜索框
    _input_mission_fission_search = (By.XPATH, "//span[text()='新建任务裂变']/../../..//input")
    # 任务裂变搜索按钮
    _btn_mission_fission_search = (By.XPATH, "//span[text()='新建任务裂变']/../../..//button/span[text()='查询']")
    # 任务裂变的第一条数据
    _text_first_mission_fission = (By.XPATH, "//span[text()='新建任务裂变']/../../..//td/div")
    # 新建任务裂变
    # 活动发起成员,选择成员
    _btn_select_start_staff = (By.XPATH, "//label[@role='radio']//span[text()='选择成员']")
    # 活动发起成员，具体选择成员
    _btn_fission_select_staff = (By.XPATH, "//button/span[text()='选择成员']")
    # 活动发起成员，具体选择成员后的确定
    _btn_fission_select_staff_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[4]/div/div[3]/div/button[2]/span')
    # 客户标签, 选择标签
    _btn_select_start_tag = (By.XPATH, "//label[@role='radio']//span[text()='选择标签']")
    # 客户标签，具体选择标签
    _btn_fission_select_tag = (By.XPATH, "//button/span[text()='选择标签']")
    # 客户标签，具体选择标签后的确定
    _btn_fission_select_tag_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[3]/div/button[2]/span')
    # 添加员工，选择员工
    _btn_fission_add_staff = (By.XPATH, "//label[text()='添加员工']/..//span[text()='选择员工']")
    # 添加员工，具体选择员工后的确定
    _btn_fission_add_staff_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[5]/div/div[3]/div/button[2]/span')
    # 客户欢迎语
    _input_welcome_message = (By.XPATH, "//label[text()='欢迎语']/..//textarea")


    # 群裂变
    # 新建群裂变
    _btn_new_group_fission = (By.XPATH, "//button/span[text()='新建群裂变']")
    # 群裂变搜索框
    _input_group_fission_search = (By.XPATH, "//span[text()='新建群裂变']/../../..//input")
    # 群裂变的搜索按钮
    _btn_group_fission_search = (By.XPATH, "//span[text()='新建群裂变']/../../..//button/span[text()='查询']")
    # 群裂变的第一条数据
    _text_first_group_fission = (By.XPATH, "//span[text()='新建群裂变']/../../..//td/div")
    # 新建群裂变
    # 按群主选择
    _btn_select_start_group = (By.XPATH, "//label[@role='radio']//span[text()='按群主选择']")
    # 按群主选择，具体选择群主
    _btn_select_group = (By.XPATH, "//button/span[text()='选择群主']")
    # 按群主选择，选择群主后确定
    _btn_select_group_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[3]/div/button[2]/span')
    # 选择群活码
    _btn_select_group_code = (By.XPATH, "//label[text()='群活码']/..//span[text()='选择群活码']")
    # 选择群活码的搜索按钮
    _btn_select_group_code_search = (By.XPATH, "//button[@slot='append']")
    # 选择群活码的输入框
    _input_select_group_code = (By.XPATH, "//div[@class='searchContent']//input[@class='el-input__inner']")
    # 选择群活码的选择按钮
    _btn_select_group_code_name = (By.XPATH, "//div[@class='cell el-tooltip']")
    # 选择群活码的搜索确认按钮
    _btn_select_group_code_sure = (By.XPATH, '//*[@id="app"]/section/section/div/div[1]/div/div[1]/div[2]/main/div/div[4]/div/div[3]/div/button[2]/span')


    # 共同点
    # 任务名称
    _input_fission_name = (By.XPATH, "//label[@for='taskName']/..//input")
    # 裂变引导语
    _input_fission_msg = (By.XPATH, "//label[text()='裂变引导语']/..//textarea")
    # 裂变客户数量
    _input_fission_number = (By.XPATH, "//label[@for='fissionCustomerNum']/..//input")
    # 活动时间-开始时间点击
    _btn_submit_time = (By.XPATH, "//label[text()='活动时间']/..//input[@placeholder='开始时间']")
    # 开始时间选择今天之后的一天
    _btn_submit_start_time = (By.XPATH, "//td[@class='available']")
    # 结束时间选择下个月的一天
    _btn_submit_end_time = (By.XPATH, "//div[contains(@class, 'is-right')]//td[@class='available']")
    # 时间选择器的确定
    _btn_time_sure = (By.XPATH, "//button/span[contains(text(),'确定')]")
    # 裂变海报
    _btn_fission_poster = (By.XPATH, "//label[text()='裂变海报']/..//button/span")
    # 海报搜索
    _input_fission_search_poster = (By.XPATH, "//input[@placeholder='搜索素材']")
    # 海报搜索的选择
    _btn_fission_select_poster = (By.XPATH, "//div[@class='filter-material-content']/div[4]//span[@class='el-checkbox__input']")
    # 海报搜索后的确认
    _btn_fission_select_poster_sure = (By.XPATH, "//div[@aria-label='选择海报素材']/div[@class='el-dialog__footer']//span[text()='确 定']")
    # 兑换码
    _input_gift = (By.XPATH, "//label[text()='兑奖码']/..//input[@placeholder]")
    # 活动下发途径-管理员统一群发消息
    _btn_admin_load = (By.XPATH, "//label[text()='活动下发途径']/..//span[text()='管理员统一群发消息']")
    # 阅读《功能说明》
    _btn_read_introduction = (By.XPATH, "//span[text()='阅读《功能说明》']/../../..//span[@class='el-checkbox__inner']")
    # 保存
    _btn_fission_save = (By.XPATH, "//button/span[text()='保存']")

    # 验证信息栏
    # 活动名称的值
    _text_check_fission_name = (By.XPATH, "//div[contains(text(),'活动名称')]/..//div[2]")
    # 裂变引导语的值
    _text_check_fission_guide = (By.XPATH, "//div[contains(text(),'裂变引导语')]/..//div[2]")
    # 裂变人数的值
    _text_check_fission_number = (By.XPATH, "//div[contains(text(),'裂变客户数')]/..//div[2]")
    # 活动发起成员
    _text_check_start_staff = (By.XPATH, "//div[contains(text(),'活动发起成员')]/..//div[2]")
    # 活动发起成员的id
    _text_check_start_staff_id = (By.XPATH, "//div[contains(text(),'活动发起成员')]/..//div[2]//ww-open-data")
    # 活动发起群主
    _text_check_start_group = (By.XPATH, "//div[contains(text(),'活动发起群主')]/..//div[2]")
    # 活动发起群主的id
    _text_check_start_group_id = (By.XPATH, "//div[contains(text(),'活动发起群主')]/..//div[2]//ww-open-data")
    # 客户标签
    _text_check_tag = (By.XPATH, "//div[contains(text(),'客户标签')]/..//div[2]")
    # 客户标签的具体值
    _text_check_tag_name = (By.XPATH, "//div[contains(text(),'客户标签')]/..//div[2]/span")
    # 兑奖码
    _text_check_gift = (By.XPATH, "//div[contains(text(),'兑奖码')]/..//div[2]")
    # 活动下发途径
    _text_check_load = (By.XPATH, "//div[contains(text(),'活动下发途径')]/..//div[2]")

