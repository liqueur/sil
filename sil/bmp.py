import struct
from collections import namedtuple
from contextlib import closing


BitmapFileHeader = namedtuple('BitmapFileHeader', 'bfType, bfSize, bfReserved1 bfReserved2 bfOffBits')
BitmapInformation = namedtuple('BitmapInformation', 'biSize biWidth biHeight biPlanes biBitCount biCompression '
                                                    'biSizeImage biXPelsPerMeter biYPelsPerMeter biClrUsed biClrImportant')


def parse(path):
    '''
    24位深度BMP文件解析
    返回头信息和像素信息(b, g, r)，像素从左上往右下以行为主序返回
    :param path:
    :ret bitmapfileheader, bitmapinformation, [[(b, g, r), ...], ...], fd
    :return:
    '''
    f = open(path, 'rb')
    # 解析bmp文件头
    bf_fmt = '<2sihhi'
    content = f.read(struct.calcsize(bf_fmt))
    bf = BitmapFileHeader._make(struct.unpack(bf_fmt, content))
    # 解析位图文件头
    bi_fmt = '<iiihhiiiiii'
    f.seek(struct.calcsize(bf_fmt))
    content = f.read(struct.calcsize(bi_fmt))
    bi = BitmapInformation._make(struct.unpack(bi_fmt, content))

    def gen():
        with closing(f):
            off = struct.calcsize(bf_fmt) + struct.calcsize(bi_fmt)
            f.seek(off)
            data_num = bi.biWidth * 3
            # 补齐0
            zero_num = bi.biWidth * 3 % 4
            off += (bi.biHeight - 1) * (data_num + zero_num)
            for i in range(bi.biHeight):
                f.seek(off)
                content = f.read(data_num + zero_num)
                if zero_num:
                    data = list(content)[:-zero_num]
                else:
                    data = list(content)
                item = []
                while data:
                    item.append(data[:3])
                    data = data[3:]
                off -= data_num + zero_num
                yield item

    f.seek(0)

    return bf, bi, gen(), f
