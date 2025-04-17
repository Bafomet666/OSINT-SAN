#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmind.core.markerref
"""
from . import const
from .mixin import WorkbookMixinElement


class MarkerId:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<MarkerId: %s>" % self

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

    def getFamily(self):
        return self.name.split('-')[0]


# star(星星)
MarkerId.starRed = 'star-red'
MarkerId.starOrange = 'star-orange'
MarkerId.starYellow = 'star-yellow'
MarkerId.starBlue = 'star-blue'
MarkerId.starGreen = 'star-green'
MarkerId.starPurple = 'star-purple'
# priority(优先级)
MarkerId.priority1 = 'priority-1'
MarkerId.priority2 = 'priority-2'
MarkerId.priority3 = 'priority-3'
MarkerId.priority4 = 'priority-4'
MarkerId.priority5 = 'priority-5'
MarkerId.priority6 = 'priority-6'
MarkerId.priority7 = 'priority-7'
MarkerId.priority8 = 'priority-8'
MarkerId.priority9 = 'priority-9'
# smiley(表情)
MarkerId.smileySmile = 'smiley-smile'
MarkerId.smileyLaugh = 'smiley-laugh'
MarkerId.smileyAngry = 'smiley-angry'
MarkerId.smileyCry = 'smiley-cry'
MarkerId.smileySurprise = 'smiley-surprise'
MarkerId.smileyBoring = 'smiley-boring'
# task(任务进度)
MarkerId.task0_8 = 'task-start'
MarkerId.task1_8 = 'task-oct'
MarkerId.task2_8 = 'task-quarter'
MarkerId.task3_8 = 'task-3oct'
MarkerId.task4_8 = 'task-half'
MarkerId.task5_8 = 'task-5oct'
MarkerId.task6_8 = 'task-3quar'
MarkerId.task7_8 = 'task-7oct'
MarkerId.task8_8 = 'task-done'
# flag(旗子)
MarkerId.flagRed = 'flag-red'
MarkerId.flagOrange = 'flag-orange'
MarkerId.flagYellow = 'flag-yellow'
MarkerId.flagBlue = 'flag-blue'
MarkerId.flagGreen = 'flag-green'
MarkerId.flagPurple = 'flag-purple'
# people(人像)
MarkerId.peopleRed = 'people-red'
MarkerId.peopleOrange = 'people-orange'
MarkerId.peopleYellow = 'people-yellow'
MarkerId.peopleBlue = 'people-blue'
MarkerId.peopleGreen = 'people-green'
MarkerId.peoplePurple = 'people-purple'
# arrow(箭头)
MarkerId.arrowUp = 'arrow-up'
MarkerId.arrowUpRight = 'arrow-up-right'
MarkerId.arrowRight = 'arrow-right'
MarkerId.arrowDownRight = 'arrow-down-right'
MarkerId.arrowDown = 'arrow-down'
MarkerId.arrowDownLeft = 'arrow-down-left'
MarkerId.arrowLeft = 'arrow-left'
MarkerId.arrowUpLeft = 'arrow-up-left'
MarkerId.arrowRefresh = 'arrow-refresh'
# symbol(符号)
MarkerId.symbolPlus = 'symbol-plus'  # 加号
MarkerId.symbolMinus = 'symbol-minus'  # 减号
MarkerId.symbolQuestion = 'symbol-question'  # 问号
MarkerId.symbolInfo = 'symbol-info'  # 信息
MarkerId.symbolAttention = 'symbol-attention'  # 注意
MarkerId.symbolWrong = 'symbol-wrong'  # 错误
MarkerId.symbolRight = 'symbol-right'  # 对号
MarkerId.symbolPause = 'symbol-pause'  # 暂停
MarkerId.symbolBarChart = 'c_symbol_bar_chart'  # 条形图
MarkerId.symbolFlight = 'c_symbol_flight'  # 航班
MarkerId.symbolExercise = 'c_symbol_exercise'  # 锻炼
MarkerId.symbolDrink = 'c_symbol_drink'  # 引用
MarkerId.symbolDislike = 'c_symbol_dislike'  # 嫌恶
MarkerId.symbolContact = 'c_symbol_contact'  # 联系
MarkerId.symbolTrophy = 'c_symbol_trophy'  # 奖牌
MarkerId.symbolThermometer = 'c_symbol_thermometer'  # 温度计
MarkerId.symbolTelephone = 'c_symbol_telephone'  # 电话
MarkerId.symbolShoppingCart = 'c_symbol_shopping_cart'  # 购物车
MarkerId.symbolPieChart = 'c_symbol_pie_chart'  # 扇形图
MarkerId.symbolPen = 'c_symbol_pen'  # 钢笔
MarkerId.symbolMusic = 'c_symbol_music'  # 音乐
MarkerId.symbolMoney = 'c_symbol_money'  # 金钱
MarkerId.symbolMedals = 'c_symbol_medals'  # 奖杯
MarkerId.symbolLineGraph = 'c_symbol_line_graph'  # 折线图
MarkerId.symbolLike = 'c_symbol_like'  # 喜欢
MarkerId.symbolHeart = 'c_symbol_heart'  # 爱心

# month(月份)
MarkerId.monthJan = 'month-jan'
MarkerId.monthFeb = 'month-feb'
MarkerId.monthMar = 'month-mar'
MarkerId.monthApr = 'month-apr'
MarkerId.monthMay = 'month-may'
MarkerId.monthJun = 'month-jun'
MarkerId.monthJul = 'month-jul'
MarkerId.monthAug = 'month-aug'
MarkerId.monthSep = 'month-sep'
MarkerId.monthOct = 'month-oct'
MarkerId.monthNov = 'month-nov'
MarkerId.monthDec = 'month-dec'
# week(星期)
MarkerId.weekSun = 'week-sun'
MarkerId.weekMon = 'week-mon'
MarkerId.weekTue = 'week-tue'
MarkerId.weekWed = 'week-wed'
MarkerId.weekThu = 'week-thu'
MarkerId.weekFri = 'week-fri'
MarkerId.weekSat = 'week-sat'


class MarkerRefsElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_MARKERREFS

    def __init__(self, node=None, ownerWorkbook=None):
        super(MarkerRefsElement, self).__init__(node, ownerWorkbook)


class MarkerRefElement(WorkbookMixinElement):
    TAG_NAME = const.TAG_MARKERREF

    def __init__(self, node=None, ownerWorkbook=None):
        super(MarkerRefElement, self).__init__(node, ownerWorkbook)

    def getMarkerId(self):
        return MarkerId(self.getAttribute(const.ATTR_MARKERID))

    def setMarkerId(self, val):
        self.setAttribute(const.ATTR_MARKERID, str(val))

