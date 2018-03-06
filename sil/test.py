import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))


import pygame
from sil import bmp
from sys import exit
from pygame.locals import QUIT


'''
测试代码，需要安装pygame库
'''


def test_bmp(path):
    pygame.init()

    bf, bi, img_data, fd = bmp.parse(path)
    screen = pygame.display.set_mode((bi.biWidth, bi.biHeight), 0, bi.biBitCount)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        for y, line in enumerate(img_data):
            for x, (b, g, r) in enumerate(line):
                pygame.draw.rect(screen, (r, g, b), (x, y, 1, 1))

        pygame.display.update()


if __name__ == '__main__':
    test_bmp('img/1.bmp')