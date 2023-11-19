#!/usr/bin/env/ python3

from PIL import Image
import os

for imagefile in os.listdir("images/"):
    if imagefile != "DS_Store":
        image = Image.open(os.path.join("images/", imagefile))
        image = image.rotate(-90)
        image = image.resize((128, 128))
        image = image.convert("RGB")
        image.save(os.path.join("/opt/icons/", imagefile + ".jpeg"))