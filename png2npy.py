import numpy as np
import os
from PIL import Image
 
dir="../d_outputs/a001"
 
def getFileArr(dir):
    result_arr=[]
    label_list=[]
    map={}
    map_file_result={}
    map_file_label={}
    map_new={}
    count_label=0
    count=0
 
    file_list=os.listdir(dir)
    for file in file_list:
        file_path=os.path.join(dir,file)
 
        label=file.split(".")[0].split("_")[0]
        map[file]=label
        if label not in label_list:
            label_list.append(label)
            map_new[label]=count_label
            count_label=count_label+1
        img=Image.open(file_path)
        result=np.array([])
        r,g,b=img.split()
 
        r_arr=np.array(r).reshape(4096)
        g_arr=np.array(g).reshape(4096)
        b_arr=np.array(b).reshape(4096)
        img_arr=np.concatenate((r_arr,g_arr,b_arr))
        result=np.concatenate((result,img_arr))
        result=result.reshape((64,64,3))
        result=result/255.0
        map_file_result[file]=result
        result_arr.append(result)
        count=count+1
    for file in file_list:
        map_file_label[file]=map_new[map[file]]
        #map[file]=map_new[map[file]]
 
    ret_arr=[]
    for file in file_list:
        each_list=[]
        label_one_zero=np.zeros(count_label)
        result=map_file_result[file]
        label=map_file_label[file]
        label_one_zero[label]=1.0
        #print(label_one_zero)
        each_list.append(result)
        each_list.append(label_one_zero)
        ret_arr.append(each_list)
    os.makedirs("../np_outputs")
    np.save('../np_outputs/test_data.npy', ret_arr)
    return ret_arr
if __name__=="__main__":
    ret_arr=getFileArr(dir)