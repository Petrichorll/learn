import requests
import uuid
import json
import random
import time
import re

type_choice = {
    1: "营销",
    2: "全局",
    3: "行业",
    4: "宏劲专用"
}

type_choice = {
    1: "营销",
    2: "营销",
    3: "营销",
    4: "营销"
}


message_choice = {
    1: "你好我哈士奇大家566好1",
    2: "你好我哈士奇大555家好1",
    3: "你好我哈士奇大666家好1",
    4: "你好我哈士奇大666家好1"
}

account_choice = {
    1: "中国银行",
    2: "建设银行",
    3: "工商银行",
    4: "农业银行"
}

headers = {
    "content-type": "application/json",
    "user-id": "c96b30d1-f2eb-44d7-adf2-f1efb49286f9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ5QjVoZC01WDlZX0ZrRlgtQlBwRTBtREU2Y3k0QnVCb0tBWjd3V0NQbWRJIn0.eyJleHAiOjE2MzE1NTM2MDQsImlhdCI6MTYzMTUzOTIwNCwianRpIjoiOTlkMDIzNmUtMTEyNy00MWQ4LTg5ZDUtMWQ1OGJkMzliN2M2IiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMC44Njo4MDExL2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6ImM5NmIzMGQxLWYyZWItNDRkNy1hZGYyLWYxZWZiNDkyODZmOSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJyb2tlciIsInNlc3Npb25fc3RhdGUiOiI3ZGFmNGMzZC04ZTE0LTRkOTMtYjRiZC1mZmY0ZGUzNzU4MTYiLCJhY3IiOiIxIiwicmVzb3VyY2VfYWNjZXNzIjp7ImJyb2tlciI6eyJyb2xlcyI6WyIvYXBpL3YxL29yZGVycy9zdWJ0YWcvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHJlY29yZC9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL3JvbGUvZWRpdCIsIi9hcGkvdjEvdXNlcnMvcm9sZS9jcmVhdGUiLCIvYXBpL3YxL29yZGVycy9teW9yZGVyL2F1ZGl0IiwiL2FwaS92MS9vcmRlcnMvdXBsb2FkcmVjb3JkL2xpc3QiLCIvYXBpL3YxL29yZGVycy90YWcvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL2JvdHRvbWxpYnJhcnkvZGVsZXRlIiwiL2FwaS92MS91c2Vycy9vcmcvZGVsZXRlIiwiL2FwaS92MS9vcmRlcnMvbXlvcmRlci9hc3NpZ25vcmRlciIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9saXN0IiwiL2FwaS92MS9vcmRlcnMvb3JkZXJxdWVyeS9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy93b3JkL2RlbGV0ZSIsIi9hcGkvdjEvdXNlcnMvdXNlci9lZGl0IiwiL2FwaS92MS9vcmRlcnMvdXBsb2FkcmVjb3JkL2luZm8iLCIvYXBpL3YxL29yZGVycy90YWcvaW5mbyIsIi9hcGkvdjEvb3JkZXJzL3RhZy9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL3VzZXIvZXhwb3J0dXNlciIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9jcmVhdGUiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvaW1wb3J0IiwiL2FwaS92MS91c2Vycy9wZXJtaXNzaW9ucy9pbmZvIiwiL2FwaS92MS9tZXNzYWdlcy90ZW1wbGF0ZS9jcmVhdGUiLCIvYXBpL3YxL21lc3NhZ2VzL2xpYnJhcnkvbGlzdCIsIi9hcGkvdjEvZmlsZS92aWRlbyIsIi9hcGkvdjEvb3JkZXJzL3N0cmF0ZWd5L3VwZGF0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdHlwZS9jcmVhdGUiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvdGVtcGxhdGVkb3dubG9hZCIsIi9hcGkvdjEvb3JkZXJzL21odHVwbG9hZHZvcmRlci9jcmVhdGUiLCIvYXBpL3YxL3VzZXJzL3VzZXIvaW1wb3J0IiwiL2FwaS92MS91c2Vycy9wZXJtaXNzaW9ucy9tZW51dHJlZSIsIi9hcGkvdjEvbWVzc2FnZXMvYXVkaXRyZXBvcnQvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9pbmZvIiwiL2FwaS92MS9vcmRlcnMvb3JkZXIvcmVjZWl2ZSIsIi9hcGkvdjEvb3JkZXJzL3Jlc3VsdC9kZXRhaWxzIiwiL2FwaS92MS9vcmRlcnMvYm90dG9tbGlicmFyeS9saXN0IiwiL2FwaS92MS9maWxlL2V4dHJhY3QiLCIvYXBpL3YxL3VzZXJzL3VzZXJyb2xlL2xpc3QiLCIvYXBpL3YxL3VzZXJzL3Blcm1pc3Npb25zL29yZ3JvbGVsaXN0IiwiL2FwaS92MS9vcmRlcnMvYWlyZXN1bHQvZGV0YWlscyIsIi9hcGkvdjEvb3JkZXJzL29yZGVyL2RlbGV0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdGVtcGxhdGUvdGVtcGxhdGVkb3dubG9hZCIsIi9hcGkvdjEvb3JkZXJzL3Jlc3VsdC9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy9hdWRpdHJlcG9ydC9leHBvcnQiLCIvYXBpL3YxL21lc3NhZ2VzL2xpYnJhcnkvY3JlYXRlIiwiL2FwaS92MS9maWxlL3VwbG9hZCIsIi9hcGkvdjEvdXNlcnMvcGVybWlzc2lvbnMvZWRpdCIsIi9hcGkvdjEvdXNlcnMvb3JnL2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvc2luZ2xlc2VhcmNoIiwiL2FwaS92MS9vcmRlcnMvbXlvcmRlci9saXN0IiwiL2FwaS92MS91c2Vycy91c2VyL3RlbXBsYXRlZG93bmxvYWQiLCIvYXBpL3YxL29yZGVycy9zdWJ0YWcvZGVsZXRlIiwiL2FwaS92MS91c2Vycy9sb2cvbGlzdCIsIi9hcGkvdjEvbWVzc2FnZXMvbGlicmFyeS9kZWxldGUiLCIvYXBpL3YxL29yZGVycy9vcmRlcmluZm8vcmVjZWl2ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdHlwZS9lZGl0IiwiL2FwaS92MS91c2Vycy9yb2xlL2RlbGV0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvbGlicmFyeS9lZGl0IiwiL2FwaS92MS91c2Vycy9vcmcvaW5mbyIsIi9hcGkvdjEvdXNlcnMvdXNlci9jcmVhdGUiLCIvYXBpL3YxL3VzZXJzL3VzZXIvZGVsZXRlIiwiL2FwaS92MS9vcmRlcnMvbXlvcmRlci9pbmZvIiwiL2FwaS92MS9vcmRlcnMvb3JkZXJxdWVyeS9yZWNlaXZlIiwiL2FwaS92MS91c2Vycy9vcmcvY3JlYXRlIiwiL2FwaS92MS91c2Vycy91c2Vyb3JnL2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvY3JlYXRlIiwiL2FwaS92MS91c2Vycy9yb2xlL2luZm8iLCIvYXBpL3YxL29yZGVycy9vcmRlcnF1ZXJ5L2luZm8iLCIvYXBpL3YxL29yZGVycy91cGxvYWR2b3JkZXIvY3JlYXRlIiwiL2FwaS92MS9vcmRlcnMvdGFnL2NyZWF0ZSIsIi9hcGkvdjEvZmlsZS9nZXRmaWxlIiwiL2FwaS92MS9vcmRlcnMvc3RyYXRlZ3kvaW5mbyIsIi9hcGkvdjEvdXNlcnMvdXNlci9saXN0IiwiL2FwaS92MS91c2Vycy9vcmcvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL29yZGVyL2xpc3QiLCIvYXBpL3YxL21lc3NhZ2UvdGVtcGxhdGUvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9jaGVjayIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvYXNzaWdudXNlcmxpc3QiLCIvYXBpL3YxL29yZGVycy9hbGx0YWcvbGlzdCIsIi9hcGkvdjEvdXNlcnMvcm9sZS9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy90ZW1wbGF0ZS9kZWxldGUiLCIvYXBpL3YxL21lc3NhZ2VzL21hbnVhbG9yZGVyL2F1ZGl0IiwiL2FwaS92MS9tZXNzYWdlcy90eXBlL2RlbGV0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdGVtcGxhdGUvbGlzdCIsIi9hcGkvdjEvbWVzc2FnZXMvbWFudWFsb3JkZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3RhZy9lZGl0IiwiL2FwaS92MS91c2Vycy9yb2xlb3JnL2xpc3QiLCIvYXBpL3YxL29yZGVycy9ib3R0b21saWJyYXJ5L3JlbmFtZSIsIi9hcGkvdjEvbWVzc2FnZXMvdGVtcGxhdGUvaW1wb3J0IiwiL2FwaS92MS9tZXNzYWdlcy90eXBlbGlicmFyeS9saXN0IiwiL2FwaS92MS9vcmRlcnMvYWlyZXN1bHQvbGlzdCIsIi9hcGkvdjEvbWVzc2FnZXMvdHlwZS9saXN0IiwiL2FwaS92MS9maWxlL21odC91cGxvYWQiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6InRlc3QwMDAzQHFxLmNvbSIsImVtYWlsIjoidGVzdDAwMDNAcXEuY29tIn0.VE7fyZjdPptesbu6dOU7ZPzlRfOUXbANL1rLX0Jtwcg3PdDNZmSSLGp154jXXxxxhOHZ6e87zk8I0ICU-dQ6FntU5P5TjvK4dGZG8HevkeROaSI95L2dHDo6wxyIRDv6VGDf64WL3nfhcRUQJraBww_oiDqHeGVhUuGJDBoiFObnvLS08afaT9M4Ygk7LLiGFsHWp0QL80ssf4kqQ5fsA5S9b9L7M4WCVygt_ti-5tM8kkOt4Q0F0fW23v_QaAUJIzxQvsnUTXurjHbGCfc6x7Cugd_VYV84YE2MDFCf4xZxoUJSDrmV73R_qDO_pp4qtP2KpQyC9nzC35utS_yUJA"
}

def getid():
    hh = str(time.time())
    ret = re.sub("\.", "", hh)
    return ret

# def set_message(message, type_name, account):
#     return {'msg': message, 'id': str(uuid.uuid4()), 'type': type_name, 'from': '壹通道',
#             'patt': '短信模板', 'account': account}

def set_message(message, type_name, account,i):
    return {'msg': message, 'id': str(getid())+"{0:02d}".format(i), 'type': type_name, 'from': '壹通道',
            'patt': '短信模板', 'account': account}


def create_messages():
    messages = []
    for i in range(20):
        random_int = random.randint(1, 4)
        type_name = type_choice[random_int]
        message = message_choice[random_int]
        account = account_choice[random_int]
        messages.append(set_message(message, type_name, account,i))
    return messages


def fas():
    messages = create_messages()
    t = str(int(time.time()))
    payload = {"requestId": t, "data": messages}
    print(payload)
    r = requests.post(
        "http://192.168.0.86:8203/api/v1/messages/upload", json=payload, headers=headers)
    print(r.text)

def jie():
    r1 = requests.get("http://192.168.0.86:8203/api/v1/messages/results", headers=headers)
    print(r1.text)

if __name__ == "__main__":
    #print(getid())
    #fas()
    jie()
    # i=1
    # while(i<10):
    #     jie()
    #     i=i+1

    # pstr="{\"requestId\":\"${__time(,)}\",\"data\":\"[{'msg': '${mmsg}', 'id': '${__time(,)}00${iid}', 'type': '${ttp}', 'patt': '短信模板', 'account': '${acc}', 'from': '壹通道'}"
    # zstr=",{'msg': '${mmsg}', 'id': '${__time(,)}"
    # estr="${iid}', 'type': '${ttp}', 'patt': '短信模板', 'account': '${acc}', 'from': '壹通道'}"
    # ii=""
    # i=1
    # while(i<100):
    #     ss="{0:03d}".format(i)
    #     y=zstr+ss+estr
    #     ii=ii+y
    #     i=i+1

    # wstr="]\"}"

    # h = open(r"C:\Users\19144\Desktop\887.txt", "w", encoding="utf-8")
    # h.writelines(pstr+ii+wstr)
    

    
