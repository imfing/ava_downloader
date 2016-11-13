# coding= UTF-8

# Take a look at README first
#
# Author: Fing @EI, WHU
# Finish on 2016-11-13
#
# Usage:
#    $python ava_downloader.py beginIndex endIndex
#  
#  Also you can download in multi-process.
#
# Make sure AVA.txt and folder 'image' is under the directory 
# Note: few images may be deleted from the website
#



import urllib
import re
import sys
import os


# 得到HTML文档,路径为url
def getHtml(url):
    """Get HTML data from url"""
    page = urllib.urlopen(url)  # 打开一个URL地址
    html = page.read()
    return html


# 回调函数 显示下载进度
def schedule(a, b, c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per


# 正则匹配图片并用URLRetrieve下载
def getImg(html, imageID, imageIndex):
    reg = r'http.*?' + imageID + r'\.jpg'
    print reg
    imgre = re.compile(reg)  # 编译成正则表达式变量
    imglist = re.findall(imgre, html)
    for imgurl in imglist:
        print(imgurl)
        urllib.urlretrieve(imgurl, os.path.join(savePath, imageIndex + '.jpg'), schedule)


URLprefix = r'http://www.dpchallenge.com/image.php?IMAGE_ID='
AVAtxt = r'AVA.txt'
savePath = r'image'


# 检查参数个数
if len(sys.argv) < 3:
    print 'arg error # python xxx.py beginIndex endIndex'
    exit()


# 必须>=1
beginIndex = int(sys.argv[1])
# 必须<= 255530
endIndex = int(sys.argv[2])


# 打开AVA.txt 获取图片路径
f = open(AVAtxt)
for line in f:
    line = line.strip().split(' ')
    imageIndex = line[0]  # 得到图片序号

    if int(imageIndex) < 1:
        continue
    elif int(imageIndex) > 5:
        break

    # 跳过已存在的图片
    if os.path.isfile(os.path.join(savePath, imageIndex + '.jpg')) == True:
        continue

    # 得到图片网址
    imageID = line[1]
    URL = URLprefix + imageID
    html = getHtml(URL)
    getImg(html, imageID, imageIndex)
    print('image%s success' % imageIndex)
