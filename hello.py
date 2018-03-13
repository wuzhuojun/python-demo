#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def test():
    print('test')


test()


# str = input('请输入：')
# print("你输入的内容是：", str)

class Parent:
    def prt(self):
        print(self.count)


class Child(Parent):
    count = 0

    def prt(self):
        print(self.count)


p = Parent()
p.count = 1
p.prt()

c = Child()
c.count = 2
c.prt()
