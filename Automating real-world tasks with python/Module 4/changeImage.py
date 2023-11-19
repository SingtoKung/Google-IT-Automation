#!/usr/bin/env python3

from PIL import Image
import os

directory = "./supplier-data/images/"

for imagefile in os.listdir("./supplier-data/images"):
    if ".tiff" in imagefile:
        image = Image.open(os.path.join(directory, imagefile))
        image = image.resize((600, 400))
        image = image.convert("RGB")
        image.save(os.path.join(directory, imagefile.replace(".tiff","") + ".jpeg"))