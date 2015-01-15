# coding: utf-8


import Image
import ImageDraw


def showHist(im, w=512, h=512):
    hist = im.convert('L').histogram()
    print hist
    hist = map(lambda i : h - h * i / max(hist), hist) # 归一化, 之后会有误差
    w = w % 256 and 256 * (w / 256 + 1) or w # 保证宽是256的倍数
    im2 = Image.new('L', (w, h), 255)
    draw = ImageDraw.Draw(im2)
    step = w / 256 # 每个矩形的宽度
    [draw.rectangle([i * step, hist[i], (i+1) * step, h], fill=0) for i in range(256)]
    im.show()
    im2.show()

if __name__ == '__main__':
    image = Image.open('Hydrangeas.png')
    showHist(image, 512, 512)
