import os
import shutil
import cv2
from tqdm import tqdm

from predict_img import predict_img
from predict_vid import run_vid

img_folder = "../multiview_action_videos"
result_folder = "./result_vid"

for folder in os.listdir(img_folder):
    os.makedirs(os.path.join(result_folder, folder), exist_ok=True)
    for filename in tqdm(os.listdir(os.path.join(img_folder, folder))):
        if filename.endswith(".avi"):
            img_path = os.path.join(img_folder, folder, filename)
            print(img_path)
            re_path = os.path.join(result_folder, folder, filename)
            run_vid(img_path, re_path)