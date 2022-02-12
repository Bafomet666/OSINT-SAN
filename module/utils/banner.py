from module.utils import COLORS

import random
import os

# -*- coding: utf-8 -*-
# dev by bafomet

BANNER1 = fr"""
 {COLORS.GNSL}Тайна это безопасность, а безопасность это победа
 """

BANNER2 = fr"""
 {COLORS.GNSL}Каждое новое открытие в OSINT углубляет ваши знания, согласитесь
"""

BANNER3 = fr"""
 {COLORS.GNSL}Любопытство — это ключ к совершенству. Увлеченный человек готов прилагать усилия, 
 чтобы снова и снова находить ответы и удовлетворять свою тягу к познанию.
"""

BANNER4 = fr"""
 {COLORS.GNSL}Знать о чем то хорошо, но знать обо всем гораздо лучше.
"""


def show_banner(*, clear=False):
    if clear:
        os.system("clear")
    banner = random.SystemRandom().choice([BANNER1, BANNER2, BANNER3, BANNER4])
    print(banner)


if __name__ == "__main__":
    show_banner()
