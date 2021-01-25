# -*- coding: utf-8 -*-
import re, requests

str7 = "C:\\Users\\19144\\Desktop\\"

str1 = "https://v.douyu.com/api/stream/getStreamUrl?v=220320201030&did=ab7003ae17ec9f15dc4a3dc800081501&tt=1604046415&sign=a99b7892083db3661a3a692e6b6ec0d5&vid=jNBdvnZDZlJvE2yw"

str2 = "https://vmobile.douyu.com/video/getInfo?vid=jNBdvnZDZlJvE2yw"

head = {
    # ':authority': 'v.douyu.com',
    # ':method': 'POST',
    # ':path': '/api/stream/getStreamUrl',
    # ':scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'content-length': '124',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'acf_did=ab7003ae17ec9f15dc4a3dc800081501; dy_did=ab7003ae17ec9f15dc4a3dc800081501; dy_auth=8b96Ql%2BaOByNWnFHP6vO71qeUlVXjrdQqn4byt4%2BZoLGoyHG7vgnWF4FxuGM9UjqI5Rhyb9xGvua6tSbfRTw%2FjArwR7o%2BS7%2BIedu5VQRxS3obPj9SHHaviqk; wan_auth37wan=beeaaa07219cAIF0Qk09C1cNMQE5E04Xw74kAnL%2FEzY2MoC0jtbyjVe77fpxY%2FR3%2F4G1pO4Oe%2F%2F8rhaqrgSxvkVeu%2F%2Bt4lHlhWULldYf36P4zIS0Gw; acf_auth_wl=; acf_notification=; PHPSESSID=ltl7s1llbt0fhbnm72krh6nvl5; acf_auth=7632XVv%2Fw5W016ILZfuaMdxYPhZEccF%2FXPXOoOMP%2FX%2BXFz%2FJX8UAjUQunF0kZY6%2Bi0VVb3L1sn7ze9I9xPsrFpsSv3RbsIjVqm9%2BU%2BJ%2BCM%2BIrflDfq3Z7TDg; acf_uid=22276458; acf_username=qq_SY5LROgf; acf_nickname=Petrichorll; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=26098545; acf_biz=6; acf_stk=d760fa1baea679df; acf_avatar=%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2Fface%2F201604%2Ff84c2c33ee6ed648015ec61136cd272b_; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1603963341,1604019907,1604039784,1604046116; _dys_lastPageCode=page_home,page_video; _dys_refer_action_code=init_page_home; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1604046330',
    'origin': 'https://v.douyu.com',
    'referer': 'https://v.douyu.com/show/jNBdvnZDZlJvE2yw',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56',
    'x-requested-with': 'XMLHttpRequest'
}


head2={
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36 Edg/86.0.622.56'
}

reb = requests.get(str2, headers=head2)

print(reb.content.decode())
