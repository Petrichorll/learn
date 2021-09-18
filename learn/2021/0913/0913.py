import random


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

typee = ["营销", "行业", "宏劲专用", "全局"]

f = open(r"C:\Users\19144\Desktop\889.txt", "w", encoding="utf-8")
i = 1
while(i < 5001):
    msg="你好你好22Hi"
    '''
    t = random.randint(250, 450)
    j = 0
    msg = ""
    while(j < t):
        msg = msg+Unicode()
        j = j+1
    '''
    tstr = random.choice(typee)
    hstr = msg+",2021{0:04d}".format(i)+","+tstr+"\n"
    f.writelines(hstr)
    i = i+1
    print(i)
