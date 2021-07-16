#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import bitarray
from bitarray import bitarray
import getopt
import sys
import re
import numpy as np
import random
truetypefile = './STFangsong.ttf'
def random_perm(imgs):
    while True:
        yield random.choice(imgs)
def order_perm(imgs):
    while True:
        for v in imgs:
            yield v


def build_image(unit_images,charactors,size=32,generator_type='o'):
    # zi_mask is 2D bool array
    zi_mask = get_zi_image(charactors,size)   
    zi_h,zi_w = zi_mask.shape[:2] 
    imgs = []
    for unit_image in unit_images:
        rimg =Image.open(unit_image)
        img = np.array(rimg)
        h,w = img.shape[:2]
        img = np.array(rimg.resize((20,20),Image.BICUBIC))
        imgs.append(img)
    
    tmp = np.zeros((zi_h,zi_w,20,20,3),dtype=np.uint8)
    if generator_type=='r':
        generator = random_perm(imgs)
    elif generator_type=='o':
        generator = order_perm(imgs)
    else:
        generator = random_perm(imgs)
    for i in range(zi_h):
        for j in range(zi_w):
            tmp[i,j]=next(generator)
    #tmp = tmp * ~zi_mask.reshape((zi_h,zi_w)+(1,)*len(img.shape)) 
    tmp[zi_mask] = [150,236,111]
    tmp = np.transpose(tmp,(0,2,1,3,4))
    out_img = Image.fromarray(tmp.reshape((zi_h*20,zi_w*20,3)))
    out_img.save('images/final.png')


def textlen(string):
    """english char is 0.4 and 中文 is 1"""
    l = 0
    for _char in string:
        if '\u4e00' <= _char <= '\u9fa5':
            l+=1
        elif _char.isalpha():
            l+=0.42
        else:
            l+=1
    return l

def get_zi_image(charactors, size=20):
    c_splits = charactors.split('\n')
    row_num = len(c_splits)
    col_num = max([textlen(v) for v in c_splits])
    w, h = int(size*col_num),int(size*row_num)
    # image = Image.new("RGB", (w, h), (255, 255, 255))
    usr_font = ImageFont.truetype(truetypefile, size-size//10)
    image = Image.new("1", (w, h), (1))
    d_usr = ImageDraw.Draw(image)
    unicode_code = charactors
    d_usr.text((0,-size//10), unicode_code, (0),spacing=0,font=usr_font)
    np_img = np.array(image)
    return np_img

if __name__=="__main__":
    chars = '我爱你\n你也爱我\n是不是！'
    build_image(['images/0.png','images/1.png','images/108.png'],chars,generator_type='o')

    


