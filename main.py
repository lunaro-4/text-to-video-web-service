#!.venv/bin/python


import cv2
import glob
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw




SIZE = (100,100)
FPS = 20
LENGH_IN_SECONDS = 3


frames_folder = "frames/"

outfile = "image.png"




class BaseTextImage(object):

    def save_image(self,outfile):
        self.img.save(outfile, "png")
    def scale_image(self):
        while self.img.size[0] < self.font.getlength(self.text):
            self.img = Image.new("RGB", (self.img.size[0]+1,self.img.size[1]))
    
    def add_text(self):
        draw = ImageDraw.Draw(self.img)
        draw.text((0,0),self.text,(255,255,255),self.font)

    def __init__(self, text, font):
        img = Image.new("RGB", SIZE)
        self.img = img
        self.font = ImageFont.truetype(font, 90)
        self.text = text
        self.scale_image()
        self.add_text()




class RenderTools(object):
    @staticmethod
    def render_part(base_img : Image.Image, left_coord: float, margin: int = SIZE[0]) -> Image.Image:
        right_coord = left_coord + margin
        croped = base_img.crop((int(left_coord), int(0), int(right_coord), int(SIZE[1]))) 
        return croped

    @staticmethod
    def part_render_loop(base_img : Image.Image, save_folder: str, fps : int = FPS, length : int = LENGH_IN_SECONDS):
        if not os.path.isdir(save_folder):
            os.makedirs(save_folder)
        total_frames = fps * length
        offset = base_img.size[0]/total_frames
        for frame in range(total_frames):
            shot = RenderTools.render_part(base_img,offset*frame) 
            shot.save(f"{frames_folder}{frame}.png","png")

    @staticmethod
    def render_video(frames_folder: str, outp_path:str):
        frames_list = sorted(glob.glob(str(frames_folder + '*.png')), key=lambda x: int(str(x)[:str(x).find('.')][str(x).find('/'):].replace('/','')))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(outp_path, fourcc, FPS, SIZE)

        for frame_path in frames_list:
            frame = cv2.imread(frame_path)
            video_writer.write(frame)
        return video_writer


def cli_arg_handling():
    args = sys.argv
    if len(args) != 3:
        print("Usage: script.py \"text for animation\" output.mp4")
        exit()
    else:
        return (args[1], args[2])
    

if __name__ == "__main__":
    (text, outp) = cli_arg_handling()
    base_img = BaseTextImage(text, "tnr.ttf").img
    #base_img.save("base_img.png", "png")
    RenderTools.part_render_loop(base_img, frames_folder)
    RenderTools.render_video(frames_folder,outp).release()












