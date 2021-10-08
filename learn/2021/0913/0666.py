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
    "user-id": "370573ca-8b28-49dc-95e9-0e8fd3bc6bdf",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ5QjVoZC01WDlZX0ZrRlgtQlBwRTBtREU2Y3k0QnVCb0tBWjd3V0NQbWRJIn0.eyJleHAiOjE2MzIzNzY5MTksImlhdCI6MTYzMjM2MjUxOSwianRpIjoiMDZlYjYwMjctODMyNy00YzUwLTg4YWEtMDhkOTU5NmVmMmUzIiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMC44Njo4MDExL2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6IjM3MDU3M2NhLThiMjgtNDlkYy05NWU5LTBlOGZkM2JjNmJkZiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJyb2tlciIsInNlc3Npb25fc3RhdGUiOiI3ZDJiMDFmMy1jMmYzLTQwOWEtOTY5OC1jZGRlYWY4ZjJjY2IiLCJhY3IiOiIxIiwicmVzb3VyY2VfYWNjZXNzIjp7ImJyb2tlciI6eyJyb2xlcyI6WyIvYXBpL3YxL29yZGVycy9zdWJ0YWcvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHJlY29yZC9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL3JvbGUvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvYXVkaXQiLCIvYXBpL3YxL3VzZXJzL3JvbGUvY3JlYXRlIiwiL2FwaS92MS9vcmRlcnMvdXBsb2FkcmVjb3JkL2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL3VwbG9hZCIsIi9hcGkvdjEvb3JkZXJzL3RhZy9saXN0IiwiL2FwaS92MS9vcmRlcnMvYm90dG9tbGlicmFyeS9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL29yZy9kZWxldGUiLCIvYXBpL3YxL29yZGVycy9zdWJ0YWcvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvYXNzaWdub3JkZXIiLCIvYXBpL3YxL29yZGVycy9vcmRlcnF1ZXJ5L2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvZGVsZXRlIiwiL2FwaS92MS91c2Vycy91c2VyL2VkaXQiLCIvYXBpL3YxL29yZGVycy91cGxvYWRyZWNvcmQvaW5mbyIsIi9hcGkvdjEvb3JkZXJzL3RhZy9pbmZvIiwiL2FwaS92MS9vcmRlcnMvdGFnL2RlbGV0ZSIsIi9hcGkvdjEvdXNlcnMvdXNlci9leHBvcnR1c2VyIiwiL2FwaS92MS9vcmRlcnMvc3VidGFnL2NyZWF0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvd29yZC9pbXBvcnQiLCIvYXBpL3YxL3VzZXJzL3Blcm1pc3Npb25zL2luZm8iLCIvYXBpL3YxL21lc3NhZ2VzL3RlbXBsYXRlL2NyZWF0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvbGlicmFyeS9saXN0IiwiL2FwaS92MS9maWxlL3ZpZGVvIiwiL2FwaS92MS9vcmRlcnMvc3RyYXRlZ3kvdXBkYXRlIiwiL2FwaS92MS9tZXNzYWdlcy93b3JkL3RlbXBsYXRlZG93bmxvYWQiLCIvYXBpL3YxL3VzZXJzL3VzZXIvaW1wb3J0IiwiL2FwaS92MS9vcmRlcnMvbWh0dXBsb2Fkdm9yZGVyL2NyZWF0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdHlwZS9jcmVhdGUiLCIvYXBpL3YxL3VzZXJzL3Blcm1pc3Npb25zL21lbnV0cmVlIiwiL2FwaS92MS9tZXNzYWdlcy9hdWRpdHJlcG9ydC9saXN0IiwiL2FwaS92MS9vcmRlcnMvc3VidGFnL2luZm8iLCIvYXBpL3YxL29yZGVycy9vcmRlci9yZWNlaXZlIiwiL2FwaS92MS9vcmRlcnMvcmVzdWx0L2RldGFpbHMiLCIvYXBpL3YxL29yZGVycy9ib3R0b21saWJyYXJ5L2xpc3QiLCIvYXBpL3YxL2ZpbGUvZXh0cmFjdCIsIi9hcGkvdjEvdXNlcnMvdXNlcnJvbGUvbGlzdCIsIi9hcGkvdjEvdXNlcnMvcGVybWlzc2lvbnMvb3Jncm9sZWxpc3QiLCIvYXBpL3YxL29yZGVycy9haXJlc3VsdC9kZXRhaWxzIiwiL2FwaS92MS9vcmRlcnMvb3JkZXIvZGVsZXRlIiwiL2FwaS92MS9tZXNzYWdlcy90ZW1wbGF0ZS90ZW1wbGF0ZWRvd25sb2FkIiwiL2FwaS92MS9vcmRlcnMvcmVzdWx0L2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL2F1ZGl0cmVwb3J0L2V4cG9ydCIsIi9hcGkvdjEvbWVzc2FnZXMvbGlicmFyeS9jcmVhdGUiLCIvYXBpL3YxL2ZpbGUvdXBsb2FkIiwiL2FwaS92MS91c2Vycy9wZXJtaXNzaW9ucy9lZGl0IiwiL2FwaS92MS91c2Vycy9vcmcvbGlzdCIsIi9hcGkvdjEvbWVzc2FnZXMvd29yZC9zaW5nbGVzZWFyY2giLCIvYXBpL3YxL3VzZXJzL3VzZXIvdGVtcGxhdGVkb3dubG9hZCIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL2xvZy9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy9saWJyYXJ5L2RlbGV0ZSIsIi9hcGkvdjEvbWVzc2FnZXMvdHlwZS9lZGl0IiwiL2FwaS92MS9vcmRlcnMvb3JkZXJpbmZvL3JlY2VpdmUiLCIvYXBpL3YxL3VzZXJzL3JvbGUvZGVsZXRlIiwiL2FwaS92MS9tZXNzYWdlcy9saWJyYXJ5L2VkaXQiLCIvYXBpL3YxL3VzZXJzL29yZy9pbmZvIiwiL2FwaS92MS91c2Vycy91c2VyL2NyZWF0ZSIsIi9hcGkvdjEvdXNlcnMvdXNlci9kZWxldGUiLCIvYXBpL3YxL29yZGVycy9teW9yZGVyL2luZm8iLCIvYXBpL3YxL29yZGVycy9vcmRlcnF1ZXJ5L3JlY2VpdmUiLCIvYXBpL3YxL3VzZXJzL29yZy9jcmVhdGUiLCIvYXBpL3YxL21lc3NhZ2VzL3dvcmQvY3JlYXRlIiwiL2FwaS92MS91c2Vycy91c2Vyb3JnL2xpc3QiLCIvYXBpL3YxL29yZGVycy9vcmRlcnF1ZXJ5L2luZm8iLCIvYXBpL3YxL3VzZXJzL3JvbGUvaW5mbyIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHZvcmRlci9jcmVhdGUiLCIvYXBpL3YxL21lc3NhZ2VzL3Jlc3VsdHMiLCIvYXBpL3YxL29yZGVycy90YWcvY3JlYXRlIiwiL2FwaS92MS9maWxlL2dldGZpbGUiLCIvYXBpL3YxL3VzZXJzL3VzZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3N0cmF0ZWd5L2luZm8iLCIvYXBpL3YxL3VzZXJzL29yZy9lZGl0IiwiL2FwaS92MS9vcmRlcnMvb3JkZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvYXNzaWdudXNlcmxpc3QiLCIvYXBpL3YxL21lc3NhZ2UvdGVtcGxhdGUvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9jaGVjayIsIi9hcGkvdjEvb3JkZXJzL2FsbHRhZy9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy90ZW1wbGF0ZS9kZWxldGUiLCIvYXBpL3YxL3VzZXJzL3JvbGUvbGlzdCIsIi9hcGkvdjEvbWVzc2FnZXMvbWFudWFsb3JkZXIvYXVkaXQiLCIvYXBpL3YxL21lc3NhZ2VzL3RlbXBsYXRlL2xpc3QiLCIvYXBpL3YxL21lc3NhZ2VzL3R5cGUvZGVsZXRlIiwiL2FwaS92MS9tZXNzYWdlcy9tYW51YWxvcmRlci9saXN0IiwiL2FwaS92MS91c2Vycy9yb2xlb3JnL2xpc3QiLCIvYXBpL3YxL29yZGVycy90YWcvZWRpdCIsIi9hcGkvdjEvb3JkZXJzL2JvdHRvbWxpYnJhcnkvcmVuYW1lIiwiL2FwaS92MS9tZXNzYWdlcy90ZW1wbGF0ZS9pbXBvcnQiLCIvYXBpL3YxL29yZGVycy9haXJlc3VsdC9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy90eXBlbGlicmFyeS9saXN0IiwiL2FwaS92MS9tZXNzYWdlcy90eXBlL2xpc3QiLCIvYXBpL3YxL2ZpbGUvbWh0L3VwbG9hZCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdDAwMDFAcXEuY29tIiwiZW1haWwiOiJ0ZXN0MDAwMUBxcS5jb20ifQ.X0iHnnriiN2mxy0PE0GZ6x_CMI6T8wtpB_Co8F8HETEduQebJY-n2iumOyjL2INXvw7S5PbDDCKFI-_L1Ed6eJgZ6iA7TqYQmpUxGdm-xnyAr6hF1gvNFyIvLlnC253_8V8iJmb5TqcdsI9pK-FSFINAOtGml7aTFkZ79dIUsBDK8z5GDv4gf80yyR6BNyITFLNvzEeReUAwzqfTPCvwEOssD2OjcMNwWbHzRZ462XWhJM_YWDVQAK-RqpPtzDc-C79_a_WKAckq6ElpM8KeH-HzEHtj-6XeeM_ttHYXXX2xBNe4ufad-5ceTieslQIlgbn515PezfsS1GEKzwSxVg"
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
    

    
