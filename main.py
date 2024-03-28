#!.venv/bin/python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os, sys


SIZE = (100,100)


text = "Supertext"

outfile = "image.png"




class BaseTextImage(object):

    def save_image(self,outfile):
        self.img.save(outfile, "png")
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



def render_part(base_img : Image.Image, left_coord: float) -> Image.Image:
    right_coord = left_coord + SIZE[0]
    croped = base_img.crop((int(left_coord), int(0), int(right_coord), int(SIZE[1]))) 
    return croped




if __name__ == "__main__":
    base_img = BaseTextImage(text, "tnr.ttf")
    base_img.save_image(outfile)
    cords = (0,0,100,100)
    with Image.open(outfile) as base_img:
        im_crop=base_img.crop(cords)
        render_part(base_img, 5).save("func_crop.png","png")
        im_crop.save("croped.png", "png")

