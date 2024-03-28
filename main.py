#!.venv/bin/python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os, sys


SIZE = (100,100)
FPS = 20
LENGH_IN_SECONDS = 1


frames_folder = "frames/"
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


class RenderTools(object):
    @staticmethod
    def render_part(base_img : Image.Image, left_coord: float) -> Image.Image:
        right_coord = left_coord + SIZE[0]
        croped = base_img.crop((int(left_coord), int(0), int(right_coord), int(SIZE[1]))) 
        return croped

    @staticmethod
    def part_render_loop(base_img : Image.Image, save_folder: str):
        if not os.path.isdir(save_folder):
            os.makedirs(save_folder)
        total_frames = FPS * LENGH_IN_SECONDS
        offset = base_img.size[0]/total_frames
        for frame in range(total_frames):
            shot = RenderTools.render_part(base_img,offset*frame) 
            shot.save(f"{frames_folder}{frame}.png","png")
        pass



if __name__ == "__main__":
    base_img = BaseTextImage(text, "tnr.ttf").img
    base_img.save("base_img.png", "png")
    RenderTools.render_part(base_img, 5).save("func_crop.png","png")
    RenderTools.part_render_loop(base_img, frames_folder)

