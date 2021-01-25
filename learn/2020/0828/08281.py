# -*- coding: utf-8 -*-

import requests
import re
import json
import time
import pymongo
import psutil
from hashlib import md5
from moviepy.editor import *
from multiprocessing import Pool

#基本配置
config = {
    'UID':'gKpdxKRWXwaW',#用户ID
    'CID':104,#栏目ID
    'TYPE':1, #1=>按用户id采集列表，2=>按栏目ID采集列表
    'TIME_START':1,#起始时间
    'TIME_ENT':500,#结束时间
    'PAGE_START':1,#起始页
    'PAGE_END':10,#结束页
    'TIME_GE':0,#每个下载间隔时间
    'POOL':False,#是否开启线程池
    'CHECKID':True, #True 过滤已经下载过的视频 False 不过滤
    'FILE_PATH':'F:/ceshi/',#下载目录，【会自动创建文件夹】
    'TS_PATH':'F:/ceshi/download/',#缓存文件目录，【会自动创建文件夹】
    'DB_URL':'localhost',#数据库地址
    'DB_NAME':'douyu',#数据库名称'
    'DB_TABLE':'douyu'#数据库表
}

#MongoDB初始化
client = pymongo.MongoClient(config['DB_URL'])
mango_db = client[config['DB_NAME']]

#MongoDB存储
def save_to_mango(result):
    if mango_db[config['DB_TABLE']].insert_one({'vid':result}):
        print('成功存储到MangoDB')
        return True
    return False
#MongoDB验证重复
def check_to_mongo(vid):
    count = mango_db[config['DB_TABLE']].find({'vid':vid}).count()
    if count==0:
        return False
    return True

#删除文件
def del_file(page):
    if os.path.exists(page):
        # 删除文件，可使用以下两种方法。
        os.remove(page)
        # os.unlink(my_file)
    else:
        print('no such file:%s' % page)

#循环列表删除文件
def loop_del_file(arr):
    for item in arr:
        del_file(item)

#请求器
def get_content_requests(url):
    headers = {}
    headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers['cookie'] = 'dy_did=07f83a57d1d2e22942e0883200001501; acf_did=07f83a57d1d2e22942e0883200001501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1556514266,1557050422,1557208315; acf_auth=; acf_auth_wl=; acf_uid=; acf_nickname=; acf_username=; acf_own_room=; acf_groupid=; acf_notification=; acf_phonestatus=; _dys_lastPageCode=page_video,page_video; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1557209469; _dys_refer_action_code=click_author_video_cate2'
    try:
        req_content = requests.get(url,headers = headers)
        if req_content.status_code == 200:
            return req_content
        print('请求失败：',url)
        return None
    except:
        print('请求失败：', url)
        return None

#把时间换算成秒
def str_to_int(time):
    try:
        time_array = time.split(':')
        time_int = (int(time_array[0])*60)+int(time_array[1])
        return time_int
    except:
        print('~~~~~计算视频时间失败~~~~~')
        return None

#提取需要采集的数据
def get_list(html,type = 1):
    data = []
    try:
        list_json = json.loads(str(html))
        for om in list_json['data']['list']:
            gtime = str_to_int(om['video_str_duration'])
            if gtime > config['TIME_START'] and gtime < config['TIME_ENT']:
                if type == 2:
                    data.append({'title': om['title'], 'vid': om['url'].split('show/')[1]})
                else:
                    data.append({'title': om['title'], 'vid': om['hash_id']})
        return data
    except:
        print('~~~~~数据提取失败~~~~~')
        return None

#解析playlist.m3u8
def get_ts_list(m3u8):
    data = []
    try:
        html_m3u8_json = json.loads(m3u8)
        m3u8_text = get_content_requests(html_m3u8_json['data']['video_url'])
        m3u8_vurl =html_m3u8_json['data']['video_url'].split('playlist.m3u8?')[0]
        if m3u8_text:
            get_text = re.findall(',\n(.*?).ts(.*?)\n#',m3u8_text.text,re.S)
            for item in get_text:
                data.append(m3u8_vurl+item[0]+'.ts'+item[1])
            return data
        return None
    except:
        print('~~~~~解析playlist.m3u8失败~~~~~')
        return None

# 杀死moviepy产生的特定进程
def killProcess():
    # 处理python程序在运行中出现的异常和错误
    try:
        # pids方法查看系统全部进程
        pids = psutil.pids()
        for pid in pids:
            # Process方法查看单个进程
            p = psutil.Process(pid)
            # print('pid-%s,pname-%s' % (pid, p.name()))
            # 进程名
            if p.name() == 'ffmpeg-win64-v4.1.exe':
                # 关闭任务 /f是强制执行，/im对应程序名
                cmd = 'taskkill /f /im ffmpeg-win64-v4.1.exe  2>nul 1>null'
                # python调用Shell脚本执行cmd命令
                os.system(cmd)
    except:
        pass

#下载.ts文件
def download_ts(m3u8_list,name):
    try:
        if not os.path.exists(config['FILE_PATH']):
            os.makedirs(config['FILE_PATH'])
        if not os.path.exists(config['TS_PATH']):
            os.makedirs(config['TS_PATH'])
        if os.path.exists(config['FILE_PATH']+name+'.mp4'):
            name = name+'_'+str(int(time.time()))
        print('开始下载：',name)
        L = []
        R = []
        for p in m3u8_list:
            ts_find = get_content_requests(p)
            file_ts = '{0}{1}.ts'.format(config['TS_PATH'],md5(ts_find.content).hexdigest())
            with open(file_ts,'wb') as f:
                f.write(ts_find.content)
            R.append(file_ts)
            hebing = VideoFileClip(file_ts)
            L.append(hebing)
            killProcess()
            print('下载完成：',file_ts)
        mp4file = '{0}{1}.mp4'.format(config['FILE_PATH'],name)
        final_clip = concatenate_videoclips(L)
        final_clip.to_videofile(mp4file, fps=24, remove_temp=True)
        killProcess()
        loop_del_file(R)
        print('\n下载完成：',name)
        print('')
        return True
    except:
        print('~~~~~合成.ts文件失败~~~~~')
        return None

#下载视频列表
def list_get_kong(list_json):
    for item in list_json:
        y = True
        if config['CHECKID']:
            if check_to_mongo(item['vid']):
                print('~~~~~检测到重复项~~~~~')
                y = False
        if y:
            get_show_html = get_content_requests('https://vmobile.douyu.com/video/getInfo?vid=' + item['vid'])
            if get_show_html:
                m3u8_list = get_ts_list(get_show_html.text)
                if m3u8_list:
                    download = download_ts(m3u8_list, item['title'])
                    if download: save_to_mango(item['vid'])
        time.sleep(config['TIME_GE'])

#控制器
def main(page):
    if config['TYPE']==1:
        print('~~~~~按用户ID采集~~~~~')
        listurl = 'https://v.douyu.com/video/author/getAuthorVideoListByNew?up_id={0}&cate2_id=0&limit=30&page={1}'.format(config['UID'],page)
        get_list_html = get_content_requests(listurl)
        if get_list_html:
            list_json = get_list(get_list_html.text,1)
            if list_json:
                list_get_kong(list_json)
    else:
        print('~~~~~按列表ID采集~~~~~')
        listurl = 'https://v.douyu.com/video/video/listData?page={1}&cate2Id={0}&action=new'.format(config['CID'],page)
        get_list_html = get_content_requests(listurl)
        if get_list_html:
            list_json = get_list(get_list_html.text,2)
            if list_json:
                list_get_kong(list_json)

#初始化
if __name__=='__main__':
    if config['POOL']:
        groups = [x for x in range(config['PAGE_START'],config['PAGE_END']+1)]
        pool = Pool()
        pool.map(main, groups)
    else:
        for item in range(config['PAGE_START'],config['PAGE_END']+1):
            main(item)
    print('~~~~~已经完成【所有操作】~~~~~')
