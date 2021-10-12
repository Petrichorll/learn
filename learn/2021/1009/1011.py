from moviepy.editor import *

fp="C://Users/19144/Desktop/666.mkv"

video1=VideoFileClip(fp).subclip(t_start=0,t_end=52)

video1.write_videofile("C://Users/19144/Desktop/667.mp4")

'''
别人博客：
from moviepy.editor import VideoFileClip, concatenate_videoclips

clipOri = VideoFileClip("E:/2020-03-29 19-31-39.mkv")


#截取两个subclip再拼接
#time_length = int(clipOri.duration) 这句可以获取片子的时
#超过时长会报错，时长默认用秒，也可以写得更细，(00:03:50.54)->3分50秒

cut1 = clipOri.subclip(0, 7053)
cut2 = clipOri.subclip(7059, 8941)

finalClip = concatenate_videoclips([cut1,cut2])

finalClip.write_videofile("E:/acut.mp4")
'''