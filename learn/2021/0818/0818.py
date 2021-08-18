# from moviepy.editor import *

# video = VideoFileClip("test1.mp4")
# audio = video.audio
# audio.write_audiofile('test.mp3')


from moviepy.editor import AudioFileClip

audioc= AudioFileClip("C:\\Users\\19144\\PycharmProjects\\learn\\learn\\2021\\0818\\test1.mp4")

audioc.write_audiofile(".\\test.mp3")