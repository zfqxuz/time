import time
import os
import datetime
import threading
from docx import Document

global namelist
namelist=[]
def body(path):
    os.chdir(path)
    curr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"开始监视路径{path}，开始时间{curr}")
    n=os.listdir()
    while True:
        time.sleep(1)
        m=os.listdir()
        if m==n:
            continue
        else:
            dif1=set(m).difference(set(n))
            dif2=set(n).difference(set(m))
            n=m
            name=""
            curr=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if dif1!=set():
                for item in dif1:
                    name = item
                if name[0]=="~":
                    continue
                namelist.insert(0,name)
                print(f"{curr},新增了{name}")
            if dif2!=set():
                for item in dif2:
                    name=item
                if name[0]=="~":
                    continue
                print(f"{curr},移除了{name}")

def change(k):
    print(k)
    while True:
        try:
            if len(namelist)==0:
                time.sleep(1)
                continue
            else:
                name=namelist.pop()
                if name[-4:]=="docx":
                    doc=Document(u""+name)
                    doc.add_paragraph()
                    doc.save(u""+name)
                else:
                    f= open (name,"a")
                    f.write(" ")
                    f.close()
        except:
            print("转换失败")
            continue

if __name__ == '__main__':
    while True:
        i=input("输入地址")
        try:
            os.chdir(i)
            break
        except:
            print("地址错误")
            continue
    t1 = threading.Thread(target=body, args=(i,))
    t2 = threading.Thread(target=change, args=("转换程序运行了",))
    t2.start()
    t1.start()
