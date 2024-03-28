from PIL import Image
import os, sys


SIZE = (100,100)


text = ""



outfile = "image.png"

im = Image.new("RGB", SIZE)
im.save(outfile, "png")
