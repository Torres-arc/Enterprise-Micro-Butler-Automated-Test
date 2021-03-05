from selenium.webdriver.common.by import By


class LoginLoc:
    # 3.1text登录界面
    _input_username = (By.CSS_SELECTOR, 'input[type="text"]')
    _input_pword = (By.CSS_SELECTOR, 'input[type="password"]')
    _btn_login = (By.XPATH, '//span[text()="登入后台 "]/..')

    # 切换新版后台
    # 立即体验按钮
    _btn_switch = (By.XPATH, '//span[text()="知道了"]/..')