#! /usr/bin/env python3
import os
import requests

fruits = {}
keys = ["name", "weight", "description", "image_name"]
index = 0
current_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_path,"descriptions")
img_path = os.path.join(current_path,"images_new")
for file in os.listdir(path):
    with open(path + file) as f:
        for ln in f:
            line = ln.strip()
            if "lbs" in line:
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except:
                    fruits[keys[2]] = line
        index = 0
        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        for fle in os.listdir("./supplier-data/images"):
            if fle == name:
                fruits["image_name"] = name
        response = requests.post("http://<External_IP>/fruits/", json=fruits)
        fruits.clear()
