import os
import cv2
import numpy as np
import operator
from functools import cmp_to_key
from config import Config
def img2mp4(param):
    path = './result/'
    filelist = os.listdir(path)
    if param.dataset == "ETH":
        fps = 12 #视频每秒12帧
        getId = lambda imgName:int(imgName[-14:-6])
    elif param.dataset == "MOT":
        fps = 24 #视频每秒24帧
        getId = lambda imgName:int(imgName[:-4])
    size = (param.imgsize[1],param.imgsize[0]) #需要转为视频的图片的尺寸
    #可以使用cv2.resize()进行修改
    video = cv2.VideoWriter("TrackResult.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
    #视频保存在当前目录下
    imgList  = [img for img in filelist]
    imgList = sorted(imgList,key=cmp_to_key(lambda x,y:getId(x) - getId(y)))
    for item in imgList:
        if item.endswith(param.imgtype): 
        #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = path + item
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
if __name__=="__main__":

    param = Config()
    img2mp4(param)
