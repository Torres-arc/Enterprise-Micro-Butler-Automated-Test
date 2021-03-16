# -*- coding: UTF-8 -*-
# @Time    : 2021/1/8 17:18 
# @Author  : Torres 
# @File    : generate.py
import os
import re
import time

from lxml import etree
from bs4 import BeautifulSoup
import xlwings as xw
# from runner import MainPage

dicts = {'test_01_clients': ['test_01_searchByClientName', 'test_02_searchByAdder', 'test_03_searchByTag'], 'test_02_client_groups': ['test_01_searchByGroupName', 'test_02_searchByMasterName', 'test_03_searchByCreateTime'], 'test_03_client_tags': ['test_01_addNewTagGroup', 'test_02_editTagGroup', 'test_03_deleteTagGroup'], 'test_04_add_message': ['test_01_addmessage_wb', 'test_02_addmessage_web', 'test_03_addmessage_pic', 'test_04_addmessage_pos', 'test_05_addmessage_mini', 'test_06_addmessage_text_group', 'test_07_addmessage_web_group', 'test_08_addmessage_pic_group', 'test_09_addmessage_pos_group', 'test_10_addmessage_mini_group', 'test_11_searchByMsg', 'test_12_searchByTime'], 'test_05_send_record': ['test_02_serachBytext', 'test_03_serachBytype', 'test_04_serachBytime', 'test_05_reset'], 'test_06_employee_code': ['test_01_searchByUser', 'test_02_searchByActScene', 'test_03_searchByCreator', 'test_04_searchByCreateTime', 'test_05_addSingleClientWebCode', 'test_06_checkCodeInfo', 'test_07_editCode', 'test_08_integratedTest', 'test_09_deleteCode', 'test_10_addSingleClientPicCode', 'test_11_addSingleClientMiniCode', 'test_12_addBatchSingleClientMiniCode', 'test_13_addBatchSingleClientPicCode', 'test_14_addBatchSingleClientWebCode', 'test_15_addMultiClientWebCode', 'test_16_addMultiClientMiniCode', 'test_17_addMultiClientPicCode', 'test_18_deleteCodeInBatch'], 'test_07_client_group_code': ['test_01_addClientgroupcode', 'test_02_manageClientgroupcode', 'test_03_editClientgroupcode', 'test_04_deleteClientgroupcode', 'test_05_selectClientgroupcode'], 'test_08_welcoming_message': ['test_01_addEmwelcomingmessage', 'test_02_searchClientWel', 'test_03_editEmwelcomingmessage', 'test_04_deleteEmwelcomingmessage', 'test_05_addDeptemwelcomingmessage', 'test_05_editDeptemwelcomingmessage', 'test_06_deleteDeptemwelcomingmessage', 'test_06_searchDepClientWel'], 'test_09_material_poster': ['test_01_add_group', 'test_02_add_poster', 'test_03_search_poster', 'test_04_move_group', 'test_05_edit_poster', 'test_06_del_poster', 'test_07_creatChildGroup', 'test_08_deleteChildGroup', 'test_09_deleteGroup'], 'test_100_red_record': ['test_01_btn_search'], 'test_10_material_text': ['test_01_add_group', 'test_02_add_text', 'test_03_search_text', 'test_04_move_group', 'test_05_edit_text', 'test_06_del_text', 'test_07_new_group_add_child', 'test_08_del_new_group'], 'test_11_material_picture': ['test_01_add_group', 'test_02_add_pic', 'test_03_search_pic', 'test_04_move_group', 'test_05_edit_pic', 'test_06_del_pic', 'test_07_new_group_add_child', 'test_08_del_new_group'], 'test_12_material_web': ['test_01_addGroup', 'test_02_addCustomizeWeb', 'test_03_addExternalLinkWeb', 'test_04_editWeb', 'test_05_searchWeb', 'test_06_deleteWeb', 'test_07_addChildGroup', 'test_08_deleteGroup'], 'test_13_material_audio': ['test_01_AddGroup', 'test_02_addAudio', 'test_03_editAudio', 'test_04_deleteAudio', 'test_05_deleteGroup'], 'test_14_material_video': ['test_01_AddGroup', 'test_02_addvideo', 'test_03_editVideo', 'test_04_deleteVideo', 'test_05_deleteGroup'], 'test_15_material_document': ['test_01_addDocumentmaterial', 'test_02_editDocumentmaterial', 'test_03_deleteDocumentmaterial'], 'test_16_material_small_routine': ['test_01_addSmallroutinematerial', 'test_02_editSmallroutinematerial', 'test_03_deleteSmallroutinematerial'], 'test_17_chat_toolbar': ['test_01_getnum', 'test_02_check_button'], 'test_18_circle_of_friends': ['test_01_searchByKeys', 'test_02_searchByTime', 'test_03_addReleaseNews', 'test_04_editReleaseNews', 'test_05_deleteReleaseNews'], 'test_19_organization': ['test_01_searchStaff'], 'test_20_mission_treasure': ['test_01_searchByName', 'test_02_searchByDate', 'test_03_resetSearch', 'test_04_addMission'], 'test_21_group_fission': ['test_01_searchByName', 'test_02_searchByDate', 'test_03_resetSearch', 'test_04_addMission'], 'test_22_pull_new_client_into_group': ['test_01_searchByName', 'test_02_createAct', 'test_03_checkDetails', 'test_04_editAct', 'test_05_deleteAct'], 'test_23_create_group_by_tags': ['test_01_searchByWayOfSending', 'test_02_searchByTaskName', 'test_03_reset', 'test_04_creatTask', 'test_05_checkDetails'], 'test_24_keys_to_group': ['test_01_searchByName', 'test_02_createAct', 'test_03_editAct', 'test_04_deleteAct'], 'test_25_group_sop': ['test_01_searchByGroupName', 'test_02_createRule', 'test_03_checkDetailInfo', 'test_04_editRule'], 'test_50_loss_remind': ['test_01_searchByClientName', 'test_03_searchByTag', 'test_04_buttonReset']}


def generate():
    soup = BeautifulSoup(open('企微测试报告.html', encoding='utf-8'), features='html.parser')
    asaa = soup.select('div[style="float: left"] p:first-child')
    curtime = (re.findall(r'\S*\s\S*(?=</p>)', str(asaa)))[0]
    failclasslist = soup.select('tr[id*="ft"]>td>div.testcase')
    fail_list = []
    err_list = []
    for i in failclasslist:
        fail_list.append((i.text.split(':'))[0])
    errclasslist = soup.select('tr[id*="et"]>td>div.testcase')
    for i in errclasslist:
        err_list.append((i.text.split(':'))[0])
    classs = soup.select('tr[class*="Class"]>td:first-child')
    lsits = []
    for i in classs:
        lsits.append((i.text.split('.'))[0])

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('D:/tst/工作簿1.xlsx')
    curs = wb.sheets['测试情况']
    count = 1
    while curs.range(1, count).value is not None:
        print(count, curs.range(1, count).value)
        count += 1
    print(curtime)
    print(count)
    curs.range(1, count).value = curtime
    for i in err_list:
        row = 1
        while True:
            if curs.range(row, 2).value == i:
                curs.range(row, count).color = (255, 255, 0)
                break
            row += 1
    for i in fail_list:
        row = 1
        while True:
            if curs.range(row, 2).value == i:
                curs.range(row, count).color = (255, 0, 0)
                break
            row += 1
    curs.autofit()
    time.sleep(3)
    wb.save()
    wb.close()
    app.kill()

def init_excel():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    try:
        path = os.path.abspath(os.path.dirname(__file__))+'/generate.xlsx'
        if not os.path.exists(path):
            wb=app.books.add()
            wb.save(path)
        wb=app.books.open(path)
        if wb.sheets[0].name != '测试情况':
            wb.sheets[0].name = '测试情况'
        curs = wb.sheets['测试情况']
        curs.range('A1').value = '测试页面'
        curs.range('b1').value = '测试用例'
        curs.range('c1').value = '测试时间'
        curs.autofit()
        count = 2
        for i in dicts.keys():
            a_count = str(count)
            curs.range('a' + str(count)).value = i
            for x in dicts[i]:
                curs.range('b' + str(count)).value = x
                count += 1
            b_count = str(count-1)
            curs.range('a'+str(a_count)+":"+'a'+str(b_count)).merge()
        time.sleep(3)
        wb.save()
        wb.close()
        app.kill()
    except:
        app.kill()


if __name__ == '__main__':
    # init_excel()
    generate()
