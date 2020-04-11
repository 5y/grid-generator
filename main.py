from PIL import Image, ImageDraw
import os
import sys
import subprocess
from subprocess import Popen, PIPE
if __name__ == '__main__':
    step_count = 71 #pixel width/pixelstep
    height = 2116 #41 1550 #pixel
    width = 1511#57 #pixel
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=8)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=8)

#    del draw
    store = image.save("output.png")
    subprocess.call("convert output.png output-coverted.pdf", shell=True)
    subprocess.call("pdfposter -p 4x2letter output-coverted.pdf output.pdf", shell= True)
    print("Saved to output.pdf")
