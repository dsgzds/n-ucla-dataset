import os
import shutil
import cv2
from tqdm import tqdm

from predict_img import predict_img

img_folder = "../outputs"
result_folder = "./result"

for folder in os.listdir(img_folder):
    os.makedirs(os.path.join(result_folder, folder), exist_ok=True)
    for filename in tqdm(os.listdir(os.path.join(img_folder, folder))):
        os.makedirs(os.path.join(result_folder, folder, filename), exist_ok=True)
        for frame in os.listdir(os.path.join(img_folder, folder, filename)):
            if frame.endswith(".png"):
                # 只转换偶数帧 
                # print(int(frame[3:5]))
                if int(frame[3:5]) % 2 == 1:
                    continue
                # 将偶数帧的文件名除以2
                frame = "{:05d}.png".format(int(frame[3:5]) // 2)
                img_path = os.path.join(img_folder, folder, filename, frame)
                #print(img_path)
                re_frame = "MDepth-000" + frame
                re_path = os.path.join(result_folder, folder, filename, re_frame)
                predict_img(img_path=img_path, output_path=re_path)