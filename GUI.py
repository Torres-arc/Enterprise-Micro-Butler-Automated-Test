# coding=utf-8
import unittest

import os
from tkinter import *
import tkinter.messagebox
from runner import start

os.chdir(sys.path[0])


class MainPage:
    paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_cases'
    lists = []
    for dirpath, dirnames, filenames in os.walk(paths):
        for file in filenames:
            if os.path.splitext(file)[0].startswith('test_') and os.path.splitext(file)[1] == '.py':
                lists.append(file)

    v = []
    w = []
    origin_dict = {}
    example_dict = {}
    current_dict = {}
    root = Tk()
    version = ""
    env = ""
    var = IntVar()
    var2 = IntVar()
    var4 = IntVar()
    var3 = IntVar()
    btn = []

    def suitsget(self):
        dict = {}
        paths = os.path.dirname(os.path.abspath(__file__)) + '\\test_cases'
        discover = unittest.defaultTestLoader.discover(paths, pattern="test*", top_level_dir=None)
        for test_cases in discover:
            for cases in test_cases:
                name = re.findall(r'<Test[\S]+', str(cases))
                casea = re.findall(r'=[a-z][\S]+?>', str(cases))
                for i in casea:
                    namess = (name[0])[1:]
                    # print('name', namess)
                    dict.setdefault((namess.split('.'))[1], []).append(i[1:-1])
        self.origin_dict = dict
        self.example_dict = dict
        print(dict)
        return dict

    def select_version(self):
        if self.var.get() == 1:
            self.version = "3.0"
        elif self.var.get() == 2:
            self.version = "3.1"

    def select_env(self):
        if self.var2.get() == 1:
            self.env = "www"
        elif self.var2.get() == 2:
            self.env = "test"

    def getselect(self, test):
        index = self.lists.index(test)
        if test[:-3] in self.current_dict:
            del self.current_dict[test[:-3]]
            # print(self.current_dict)
        else:
            # print(self.current_dict)
            self.current_dict[test[:-3]] = self.example_dict[test[:-3]]
            # print(self.current_dict)
        if self.btn[index]['state'] == 'normal':
            self.btn[index]['state'] = 'disabled'
        if self.btn[index]['state'] == 'disabled':
            self.btn[index]['state'] = 'normal'

    def unselectall(self):
        for index, item in enumerate((self.lists[:-1])):
            self.v[index].set('')
            self.btn[index]['state'] = 'disabled'
        self.current_dict = {}
        # print(self.example_dict)

    def selectall(self):
        for index, item in enumerate((self.lists[:-1])):
            self.v[index].set(item)
            self.btn[index]['state'] = 'normal'
        self.current_dict = self.example_dict
        # print(self.example_dict)

    def unselectall1(self, lists):
        for index, item in enumerate(lists):
            self.w[index].set('')

    def selectall1(self, lists):
        for index, item in enumerate(lists):
            self.w[index].set(item)

    def showselect(self):
        # print(self.version)
        # print(self.env)
        self.version = '3.1'
        # if self.version == "3.1" and self.env == "test":
        #     tkinter.messagebox.showerror('错误', '目前3.1不支持测试环境运行自动化！')
        #     return
        self.root.destroy()
        start(self.current_dict, 0)

    def getcases(self, page, ttk):
        selected = [i.get() for i in self.w if i.get()]
        # print(selected)
        if selected:
            self.example_dict[page] = selected
            self.current_dict[page] = selected
            # print(self.current_dict)
        if not selected:
            index = self.lists.index((page + '.py'))
            # print(index)
            self.v[index].set('')
            self.btn[index]['state'] = 'disabled'
        ttk.destroy()

    def creat(self):
        self.root.title('客户运营自动化测试')
        Label(self.root, text="请选择测试版本:").grid(row=0, column=0)
        self.current_dict = self.suitsget()
        self.example_dict = self.suitsget()
        Radiobutton(self.root, text='企微3.0',
                    variable=self.var, value=1, command=self.select_version, state=DISABLED).grid(row=0, column=1)
        Radiobutton(self.root, text='企微3.1',
                    variable=self.var, value=2, command=self.select_version, state=DISABLED).grid(row=0, column=2)
        self.var.set(2)
        Label(self.root, text="请选择测试环境:").grid(row=1, column=0)
        Radiobutton(self.root, text='正式环境',
                    variable=self.var2, value=1, command=self.select_env, state=DISABLED).grid(row=1, column=1)
        Radiobutton(self.root, text='测试环境',
                    variable=self.var2, value=2, command=self.select_env, state=DISABLED).grid(row=1, column=2)
        self.var2.set(1)
        Label(self.root, text="请选择需要进行测试的页面:").grid(row=2, column=0)
        Radiobutton(self.root, text='全选',
                    variable=self.var4, value=1, command=self.selectall).grid(row=2, column=1)
        Radiobutton(self.root, text='清空',
                    variable=self.var4, value=2, command=self.unselectall).grid(row=2, column=2)
        for i, item in enumerate(self.lists[:-1]):
            self.v.append(StringVar())
            Checkbutton(self.root, variable=self.v[-1], text=item, onvalue=item, offvalue='',
                        command=lambda a=item: self.getselect(a)).grid(row=i // 2 + 3, column=((i % 2) * 2), sticky=W)
            asa = Button(self.root, text='详细', command=lambda items=item: self.create_son(items))
            asa.grid(row=i // 2 + 3, column=(((i % 2) * 2) + 1))
            self.v[-1].set(item)
            self.btn.append(asa)
        Button(self.root, text="开始测试", command=self.showselect).grid(row=len(self.lists) - 5, column=1)
        self.root.mainloop()

    def create_son(self, page):
        ttk = Toplevel()
        ttk.title('客户运营自动化测试')
        lists = (self.suitsget())[page[:-3]]
        Label(ttk, text="请选择具体测试用例:").grid(row=1, column=2, sticky=W)
        Radiobutton(ttk, text='全选', variable=self.var3,
                    value=2, command=lambda lis=lists: self.selectall1(lis)).grid(row=2, column=1)
        Radiobutton(ttk, text='反选', variable=self.var3,
                    value=1, command=lambda lis=lists: self.unselectall1(lis)).grid(row=2, column=2)
        self.w.clear()
        # print(self.current_dict[page[:-3]])
        for i, info in enumerate(lists):
            self.w.append(StringVar())
            Checkbutton(ttk, variable=self.w[-1], text=info, onvalue=info,
                        offvalue='').grid(row=(i // 3) + 3, column=(i % 3) + 1, sticky=W)

            if info in self.current_dict[page[:-3]]:
                self.w[-1].set(info)
        Button(ttk, text="选择完成", command=lambda curpage=page[:-3]: self.getcases(curpage, ttk)) \
            .grid(row=len(lists) // 3 + 4, column=2)

if __name__ == "__main__":
    MainPage().creat()