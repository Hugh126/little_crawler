#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time

goalTime = "20:00:00"
weekend_noon = "12:30"
weekend_night = "17:30"

def getCookie(cook):
    cook = re.findall(r"JSESSIONID=(.*?)\s", cook)[0]
    cookie = "UAI=a.1280x800; ezofficeUserName=hongzm@corp.21cn.com; ezofficeDomainAccount=whir; JSESSIONID=%s; username=hongzm"%cook
    print cookie   
    return cookie

# %m-%d to %m月%d日
def changeDate(date1_str):
    return date1_str.replace("-", "月")
#     date1 = datetime.datetime.strptime(date1_str, "%m-%d")
#     date2 = date1.strftime("%m月%d日")
#     return str(date2)

def loginOA(uname, passwd):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'Host':'oaServer',
        'Connection':'keep-alive',
        'Origin':'http://oaServer',
        'Content-Type':'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':1,
        'Referer':'http://oaServer/attendance/login/login.jsp'}
    
    data = {'username':uname, 
            'password':passwd, 
            'verifycookie':1,
            'style':34,
            'product':'mail163',
            'savelogin':0,
            'selType':-1
            }
    s = requests.session()
    s.post("http://oaServer/servlet/LoginServlet", data, headers = headers)
    html = s.get("http://oaServer/attendance/workdayCompletion/list.do?menu=emp_mon", headers = headers, timeout=5)
    text = html.text
    return text

# 从页面初步过滤数据
def filterText(text):
    soup = BeautifulSoup(text, "html.parser", from_encoding="gb18030")
    # print soup.prettify()
    result = []
    for tr in soup.find_all('tr', attrs={"style":"cursor: pointer"}):
        title =  tr['title']
        if ("年假" in title.encode('utf8')):
            continue
        row = []
        for td in tr.stripped_strings:
            row.append(td)
        if(cmp(row[2], goalTime)==1 and re.match(r'\d{2}:\d{2}:\d{2}', row[2])):
            result.append([row[0].encode('utf8'), row[1].encode('utf8'), row[2].encode('utf8')])
    return result

# 加工处理数据
def processData(result):
    data_txt = ""
    for line in result:
            ori_date = line[0]
            print ori_date
            weekN = ori_date[5:]
            # print out values
            end_date = changeDate(ori_date[:5])
            beginTime = line[1]
            startTime = "17:30" # 加班起算时间
            endTime = line[2]
            isWork = "是"
            money = 20
            if(weekN in ("星期六","星期日")):
                if(is_count in ('F', 'N', 'n', '不计', 'False')):
                    continue
                isWork = "否"
                if(cmp(beginTime, weekend_noon)== -1 and cmp(endTime, weekend_night)== 1):
                    startTime = "12:30"
                    money = 40
                elif(cmp(beginTime, weekend_noon) == -1 and cmp(endTime, weekend_night)== -1):
                    startTime = "12:30"
                    money = 20
                elif(cmp(beginTime, weekend_noon) == 1 and cmp(endTime, weekend_night)== 1):
                    startTime = "17:30"
                    money = 20
            data_txt += ('%s,%s,%s,%s,%d\n'%(end_date, startTime, endTime, isWork, money))
    return data_txt

# 写入文本
def writeTxt(data_txt, outFile):
    try:
        with open(outFile, 'w') as fw:
            fw.write(data_txt)
    except IOError,e:
        print "your path can't find :",e
    else:
        print "your "+ outFile + " product success ."

if __name__ == '__main__':
    username = ""
    passwd = ""
    while(True):
        if(not username.strip()):
            username = raw_input("input your OA userName:").strip()
        if(not passwd.strip()):
            passwd = raw_input("input your OA password:").strip()
        if(username.strip() and passwd.strip()):
            break
    result_path = raw_input("input your file path,press Enter to pass(origin D:/):").strip()
    is_count = raw_input("is count weekend(N for no count), press ENTER to pass:").strip()
    if(not result_path.strip()):
        result_path = "D:/"
    outFile = result_path + username + ".csv"
 
    text = loginOA(username, passwd)
    result = filterText(text)
    data_txt = processData(result)
    writeTxt(data_txt, outFile)
    time.sleep(5)