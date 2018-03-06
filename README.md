## SIL简介
### 学习目的，请勿在任何生产项目中使用

- 依赖Python3.5+
- BMP
  * [x] 24位深度BMP格式解析
  * [ ] 支持其它深度格式解析
- GIF
  * [ ] 支持解析GIF格式
  
```python
import pygame
from sil import bmp
from sys import exit
from pygame.locals import QUIT


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
```

运行效果

![avatar](https://github.com/liqueur/sil/raw/master/sil/img/3.png)
