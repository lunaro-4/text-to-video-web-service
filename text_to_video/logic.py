

import cv2
import glob
import os, sys
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw




SIZE = (int(100),int(100))
FPS = int(20)
LENGH_IN_SECONDS = int(3)


frames_folder = "frames/"
#text = "Supertext"





class BaseTextImage(object):

    def save_image(self,outfile):
        self.img.save(outfile, "png")
    def scale_image(self):
        while self.img.size[0] < self.font.getlength(self.text):
            self.img = Image.new("RGB", (self.img.size[0]+1,self.img.size[1]))
    
    def add_text(self):
        draw = ImageDraw.Draw(self.img)
        draw.text((0,0),self.text,(255,255,255),self.font)

    def __init__(self, text, font, size = SIZE):
        img = Image.new("RGB", size)
        self.img = img
        self.font = ImageFont.truetype(font, 90)
        self.text = text
        self.scale_image()
        self.add_text()




class RenderTools(object):
    @staticmethod
    def render_part(base_img : Image.Image, left_coord: float,
                    margin: int = SIZE[0], down_margin : int = SIZE[1]) -> Image.Image:
        right_coord = left_coord + margin
        croped = base_img.crop((int(left_coord), int(0), int(right_coord), int(down_margin))) 
        return croped

    @staticmethod
    def part_render_loop(base_img : Image.Image, save_folder: str, size, fps: int , length : int = LENGH_IN_SECONDS):
        if not os.path.isdir(save_folder):
            os.makedirs(save_folder)
        total_frames = fps * length
        offset = base_img.size[0]/total_frames
        for frame in range(total_frames):
            shot = RenderTools.render_part(base_img,offset*frame, size[0], size[1]) 
            shot.save(f"{frames_folder}{frame}.png","png")

    @staticmethod
    def render_video(frames_folder: str, outp_path:str, size, fps):
        frames_list = sorted(glob.glob(str(frames_folder + '*.png')), key=lambda x: int(str(x)[:str(x).find('.')][str(x).find('/'):].replace('/','')))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(outp_path, fourcc, fps, size)

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
    

def main(text, outp = "outp.mp4", size = SIZE, fps = FPS, length = LENGH_IN_SECONDS):
    if size == None:
        size = SIZE
    if fps == None:
        fps = FPS
    if length == None:
        length = LENGH_IN_SECONDS
    base_img = BaseTextImage(text, "tnr.ttf").img
    if os.path.isdir(frames_folder):
        shutil.rmtree(frames_folder) 
    RenderTools.part_render_loop(base_img, frames_folder, size, fps, length)
    return RenderTools.render_video(frames_folder,outp, size, fps)



if __name__ == "__main__":
    (text, outp) = cli_arg_handling()
    main(text,outp).release()











