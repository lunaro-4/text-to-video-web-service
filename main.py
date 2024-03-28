#!.venv/bin/python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os, sys


SIZE = (100,100)


text = "Supertext"

outfile = "image.png"




class BaseTextImage(object):
    def scale_image(self):
        while self.img.size[0] < self.font.getlength(text):
            self.img = Image.new("RGB", (self.img.size[0]+1,self.img.size[1]))
    
    def add_text(self):
        draw = ImageDraw.Draw(self.img)
        draw.text((0,0),text,(255,255,255),self.font)

    def __init__(self, text, font):
        img = Image.new("RGB", SIZE)
        self.img = img
        self.font = ImageFont.truetype(font, 90)
        self.text = text
        self.scale_image()
        self.add_text()
        self.img.save(outfile, "png")


base_img = BaseTextImage(text, "tnr.ttf")


