from common.myunit import MyTest
from pages.ClientManage.client_tag_page import ClientTag
from pages.public_page import PublicPage
from common.statics import get_config
import json
admin = get_config('3.1_www')  # 读取注册管理员账号
tag_group = get_config('client_tag_page', 'tag_group')
tags = json.loads(get_config('client_tag_page', 'tag1'))


class TestClientTag(MyTest, ClientTag, PublicPage):
    """测试用户添加标签组和标签"""
    def test_TestClientTag_01(self):
        # 验证用户条件标签组合标签时，可以正确添加
        self.login(admin['username'], admin['password'])
        self.switch_to_current()    # 进入客户管理
        self.switch_to_client_tag() # 进入客户标签
        try:
            self.delete_tag_group(tag_group)    # 预计先删除该标签组
        except:
            print('事先没有标签组%s' % tag_group)
            pass
        self.add_tag_group(tag_group, tags)     # 添加了tag_group和tag
        self.assert_tag(tag_group,tags)   # 验证标签组名和标签是一致的
