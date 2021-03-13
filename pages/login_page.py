from common.base_page import BasePage
from Location.login_loc import LoginLoc
from time import sleep


class LoginPage(BasePage, LoginLoc):
    def login(self, name, password):
        # 登录操作
        sleep(2)
        self.send_keys(self.find_Element(self._input_username), name)   # 输入用户名
        sleep(2)
        self.send_keys(self.find_Element(self._input_pword), password)  # 输入密码
        sleep(2)
        self.click_element(self.find_Element(self._btn_login))  # 点击登录
        sleep(3)
        try:
            self.wait_element_to_be_clickable(self._btn_switch)     # 一直等到出现了“知道了”
            self.check_exist_in_page('旧版本下线通知')
            self.click_element(self.find_Element(self._btn_switch))  # 点击“知道了”，进入新版
        except:
            pass
        # else:
        #     print('122')
        #     # self.click_element(self.find_Element(self._btn_switch))  # 点击“知道了”，进入新版
        #     sleep(2)