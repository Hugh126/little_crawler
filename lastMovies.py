#!/usr/bin/python
#-*-coding:utf-8-*-
import re
import time
import urllib2
import urllib

__author__ = "hongzm" 

#UTF-8编码
reload(sys)
# sys.setdefaultencoding('utf8')


#get html
def getHtml(url):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
    req=urllib2.Request(url)
    req.add_header('User-Agent', user_agent)
    try:
        urlOpen=urllib2.urlopen(req, timeout=5)
        html=urlOpen.read().decode('utf-8')
        return html
    except Exception,e:
        print url+" read failed. ",str(e)
    return None

def getImage(url):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
    req=urllib2.Request(url)
    req.add_header('User-Agent', user_agent)
    try:
        urlOpen=urllib2.urlopen(req, timeout=5)
        html=urlOpen.read()
        return html
    except Exception,e:
        print url+" read failed. ",str(e)
    return None

#get urlList
def reUrl(data):
#       reJpeg = r'"thumbURL":"(http://.+?\.jpg)"'
#       reJpeg = r'src="(.+?\.jpg)" pic_ext'
    reJpeg = r'src="(.+?\.jpg)" alt'
    re_compile = re.compile(reJpeg)
    urlList = re.findall(re_compile, data)
    return urlList

#show loadProcess
def callbackfunc(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

#load jpgs
def loadJpgs(urlList):
    loadPath = "D:\\Python27\\files\\downLoad\\"
    dateFormateDay = "%Y%m%d"
    loadDate = time.strftime(dateFormateDay, time.localtime(time.time()))
    for i,jpgUrl in enumerate(urlList, start=1):
        content = getImage(jpgUrl)
        with open(loadPath + str(i) + ".jpg", "wb") as fw:
            fw.write(content)
    schedule = 1
    for jpg in urlList:
        print "download the %d pic." % schedule 
        urllib.urlretrieve(jpg, loadPath+("%s_"+str(schedule)+".jpg")%loadDate, callbackfunc)
        schedule += 1

if __name__ == '__main__':
    html = getHtml("http://theater.mtime.com/China_Guangdong_Province_Guangzhou/")
    urlList = reUrl(html)
    loadJpgs(urlList)

