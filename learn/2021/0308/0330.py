# -*- coding: utf-8 -*-

import re, requests, time, threading


# headers = {"Connection": "keep-alive"
#     , "Upgrade-Insecure-Requests": "1"
#     ,
#            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
#
# mstr = "<video data-v-b2582c8a='' class='wbpv-tech' playsinline='playsinline' webkit-playsinline='true' x5-playsinline='true' x5-video-player-type='h5' x5-video-player-fullscreen='false' id='wbpv_video_467_html5_api' tabindex='-1' role='application' preload='meta' src='//f.video.weibocdn.com/uxg3IBDJlx07LIXJtBaE0104120c0Q410E050.mp4?label=mp4_1080p&amp;template=1920x1080.25.0&amp;trans_finger=0bde055d9aa01b9f6bc04ccac8f0b471&amp;media_id=4623706614595631&amp;tp=8x8A3El:YTkl0eM8&amp;us=0&amp;ori=1&amp;bf=2&amp;ot=h&amp;ps=3lckmu&amp;uid=5JGzqu&amp;ab=3915-g1,966-g1,3370-g1,1493-g0,1192-g0,1191-g0,1258-g0&amp;Expires=1618203591&amp;ssig=GECI2pf9h5&amp;KID=unistore,video'></video>"
#
# rebstr = re.findall("src=.+><", mstr)
#
# hstr = re.sub("src='", '', rebstr[0])
# hstr = re.sub("'><", '', hstr)
# hstr = re.sub("&amp;", '&', hstr)
# hstr = "https:" + hstr
# print(hstr)
#
# reb = requests.get(hstr)
# with open("333.mp4", 'ab') as file:
#     file.write(reb.content)
#     file.flush()


def run(i,j):
    print('task', i+j)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)


if __name__ == '__main__':
    j = 9
    for i in range(0, 10):
        t1 = threading.Thread(target=run, args=(i, j,))  # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
        t1.start()
