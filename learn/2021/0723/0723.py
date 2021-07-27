# -*- coding: utf-8 -*-

import requests
import time
base_url = 'https://weibo.com/ajax/statuses/mymblog?uid=7482127087&page={}&feature=0'

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": "SINAGLOBAL=4969063250520.609.1596608342424; UOR=book.ifeng.com,widget.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWajG0bhyxLVj1CGW0_D_Pk5JpX5KMhUgL.Fo-ESK-NSh-Ee0n2dJLoI0qLxKMLB.zL1hnLxKqL1KnLB-qLxK-L1KzLBo2LxKBLB.zLB-eLxKqL1KnLB-qLxK-L1KzLBo2t; ALF=1658560269; SSOLoginState=1627024270; SCF=ArMdAoVI1BDufDxJ5UXhXJ70e80NVdHiSzVy74e1oZpxkkmN8vRChPwAwFmGeVK6hA4-AAjBgQjc5DmJAplASgE.; SUB=_2A25N_hvfDeRhGeNM7lcW9CvOyDSIHXVuigoXrDV8PUNbmtAKLXbDkW9NThsGCwgT6K6T3J3clETVeFUX8b7c-rf9; XSRF-TOKEN=N1abiXn_Z0ZuaLB_eIkMClbZ; WBPSESS=OCD2UOU-T5P-nSRkbMIU-MOiKiNswZyk0D3XH-oWQehRLgQJzo64ozHscpwAiR7ODroeZ6Z8nS80f1IOcc_upuT8qqmMVowrMoBZw4uPxIdgkoVMFCUaGKgE4EtINXxD; YF-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; _s_tentry=-; Apache=3570077540838.703.1627025004916; ULV=1627025005220:88:12:5:3570077540838.703.1627025004916:1627003275482",
    "dnt": "1",
    "referer": "https://weibo.com/n/%E7%9C%9F%E8%AF%9A%E5%BD%95%E5%88%B6?tabtype=feed",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-45aa7493f5f7c456c2c316a32fbaaa0f-e34b11355a11ac40-00",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "N1abiXn_Z0ZuaLB_eIkMClbZ"
}


# 获取网页的json
def get_page(page):
    url =page
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error:", e.args)


# 分析JSON格式的数据，抓取目标信息
def parse_json(data):
    if data:
        items = data.get('data').get('list')
        for item in items:
            awr=item.get('text_raw')
            print(awr)
            filename = 'result' + '.txt'
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(awr + '\n')

if __name__ == '__main__':

    i=1
    while(i):
        data = get_page(base_url.format(i))
        results = parse_json(data)
        print("第{}页".format(i))
        i=i+1
        time.sleep(1)
