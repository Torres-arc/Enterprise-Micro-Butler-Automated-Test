from common.base_page import BasePage
from Location.login import LoginLoc
from common.statics import get_config
from time import sleep


class LoginPage(BasePage, LoginLoc):
    # 登录操作
    def login(self, url, name, password):
        self._open(url)
        sleep(2)
        self.send_keys(self.find_Element(LoginLoc._input_username), name)
        sleep(2)
        self.send_keys(self.find_Element(LoginLoc._input_pword), password)
        sleep(2)
        self.click_element(self.find_Element(LoginLoc._btn_login))
        sleep(3)
        try:
            self.check_exist_in_page('旧版本下线通知')
        except:
            pass
        else:
            print('122')
            self.click_element(self.find_Element(LoginLoc._btn_switch))  # 点击“知道了”，进入新版
            sleep(2)