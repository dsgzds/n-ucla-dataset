<<<<<<< HEAD
=======
# import os
# import shutil
# import cv2

# # 设置视频文件夹路径
# video_folder = "result_vid"

# # 设置输出文件夹路径
# output_folder = "../d_outputs1"

# # 设置视频命名相关参数
# C_count = 2  # C的数量
# P_count = 4  # P的数量
# R_count = 2  # R的数量
# A_count = 12 # A的数量

# # 获取视频文件列表
# A_int = 1
# for folder in os.listdir(video_folder):
#     video_list = []
#     folder_path = os.path.join(video_folder, folder)
#     if os.path.isdir(folder_path):
#         video_txt = os.path.join(folder_path, "videos.txt")
#         if os.path.isfile(video_txt):
#             with open(video_txt, "r") as file:
#                 lines = file.readlines()
#                 video_list.extend([os.path.join(folder_path, line.strip()) for line in lines])

# # 计算视频数量和每个类别的视频数量
#     total_videos = len(video_list)
#     print("视频数量:", total_videos)
#     C1_count = int(total_videos * 4 // 5)
#     C1_count += C1_count % 2
#     C2_count = total_videos - C1_count


#     # 创建输出文件夹
#     os.makedirs(output_folder, exist_ok=True)
    
#     # 遍历视频文件列表，进行转换
#     for i in range(total_videos):
#         video = video_list[i]
#         print("正在转换:", video)
#         # 确定C和P的索引
#         if i < C1_count:
#             C_index = "001"
#             P_index = i // 2 + 1
#             P_index = "{:03d}".format(P_index)
#         else:
#             C_index = "002"
#             P_index = (i-C1_count) // 2 + 1
#             P_index = "{:03d}".format(P_index)
        
#         R_index = i % 2 + 1

#         # 确定A的索引
#         A_index = "{:03d}".format(A_int)
#         folder_name1 = "a" + A_index
#         output_subfolder1 = os.path.join(output_folder, folder_name1)
#         # 构建输出文件夹名称
#         folder_name = "S001C{}P{}R00{}A{}".format(C_index, P_index, R_index, A_index)
#         output_subfolder = os.path.join(output_subfolder1, folder_name)
#         print("输出文件夹:", output_subfolder)
#         os.makedirs(output_subfolder, exist_ok=True)

#         # 使用OpenCV读取视频
#         cap = cv2.VideoCapture(video)
#         frame_count = 0

#         # 逐帧保存为PNG格式
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             # 构建输出文件路径
#             frame_output_path = os.path.join(output_subfolder, f"MDepth-{frame_count:08d}.png")

#             # 保存帧为PNG格式
#             cv2.imwrite(frame_output_path, frame)
#             print("转换完成:", frame_output_path)

#             frame_count += 1

#         cap.release()
#         shutil.copy(video, frame_output_path)
        
#         print("转换完成:", frame_output_path)
#     A_int += 1

>>>>>>> 153c4cf (.)
import os
import shutil
import cv2

# 设置视频文件夹路径
<<<<<<< HEAD
video_folder = "../multiview_action_videos"

# 设置输出文件夹路径
output_folder = "../d_outputs"

# 设置视频命名相关参数
C_count = 2  # C的数量
P_count = 4  # P的数量
R_count = 2  # R的数量
A_count = 12 # A的数量

# 获取视频文件列表
A_int = 1
=======
video_folder = "/data1/jilinfei/mxc/rgb2depth/DE_resnet_unet_hyb/result_vid"

# 设置输出文件夹路径
output_folder = "/data1/jilinfei/mxc/rgb2depth/d_outputs1"

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)
    
# 获取视频文件列表
>>>>>>> 153c4cf (.)
for folder in os.listdir(video_folder):
    video_list = []
    folder_path = os.path.join(video_folder, folder)
    if os.path.isdir(folder_path):
        video_txt = os.path.join(folder_path, "videos.txt")
        if os.path.isfile(video_txt):
            with open(video_txt, "r") as file:
                lines = file.readlines()
<<<<<<< HEAD
                video_list.extend([os.path.join(folder_path, line.strip()) for line in lines])

# 计算视频数量和每个类别的视频数量
    total_videos = len(video_list)
    print("视频数量:", total_videos)
    C1_count = int(total_videos * 4 // 5)
    C1_count += C1_count % 2
    C2_count = total_videos - C1_count


    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历视频文件列表，进行转换
    for i in range(total_videos):
        video = video_list[i]
        print("正在转换:", video)
        # 确定C和P的索引
        if i < C1_count:
            C_index = "001"
            P_index = i // 2 + 1
            P_index = "{:03d}".format(P_index)
        else:
            C_index = "002"
            P_index = (i-C1_count) // 2 + 1
            P_index = "{:03d}".format(P_index)
        
        R_index = i % 2 + 1

        # 确定A的索引
        A_index = "{:03d}".format(A_int)
        folder_name1 = "a" + A_index
        output_subfolder1 = os.path.join(output_folder, folder_name1)
        # 构建输出文件夹名称
        folder_name = "S001C{}P{}R00{}A{}".format(C_index, P_index, R_index, A_index)
        output_subfolder = os.path.join(output_subfolder1, folder_name)
=======
                video_list.extend([line.strip() for line in lines])

    total_videos = len(video_list)
    print("视频数量:", total_videos)
    output_folder1 = os.path.join(output_folder, folder)
    os.makedirs(output_folder1, exist_ok=True)
    # 遍历视频文件列表，进行转换
    for i in range(total_videos):
        video = video_list[i]
        # 构建输出文件夹名称
        folder_name = folder+'_'+video[:-4]
        output_subfolder = os.path.join(output_folder1, folder_name)
>>>>>>> 153c4cf (.)
        print("输出文件夹:", output_subfolder)
        os.makedirs(output_subfolder, exist_ok=True)

        # 使用OpenCV读取视频
<<<<<<< HEAD
        cap = cv2.VideoCapture(video)
=======
        cap = cv2.VideoCapture(os.path.join(video_folder, folder, video))
>>>>>>> 153c4cf (.)
        frame_count = 0

        # 逐帧保存为PNG格式
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 构建输出文件路径
            frame_output_path = os.path.join(output_subfolder, f"MDepth-{frame_count:08d}.png")

            # 保存帧为PNG格式
            cv2.imwrite(frame_output_path, frame)
            print("转换完成:", frame_output_path)

            frame_count += 1

        cap.release()
<<<<<<< HEAD
        shutil.copy(video, frame_output_path)
        
        print("转换完成:", frame_output_path)
    A_int += 1
=======
        # shutil.copy(video, frame_output_path)
        
        print("转换完成:", frame_output_path)
>>>>>>> 153c4cf (.)
