little crawler
---
## OATable 
### 公司需要统计加班数据来计算加班费，由于个人加班较多，就做了考勤的小工具
### TODO : 
*1、完整的写入excel
*2、密码加密显示

## lastMovies
### 用urllib来爬时光网，查看最近有什么电影
### TODO: 
*1、将影片名字作为图片名字
*2、将影片简介添加到一个文本里面

## cx_freeze 介绍
* 安装 install cx_freeze
* 切换到Python安装目录的Scripts目录，比如我的为c:\Python34\Scripts
* 运行 python cxfreeze-postinstall
* 测试是否安装成功 cxfreeze -h
## 使用
* cxfreeze  OATable.py  --target-dir dist  
* 去掉黑框
* cxfreeze  Devation.py  --target-dir dist  --base-name=win32gui
------------------
------------------
其他打包工具都太low了， 有的还要专门写个setup.py 指定import了哪些外部依赖，非常不方便！
cxfreeze 之前使用也可以 ，但是好像不怎么兼容python3. So low ， 还是推荐流行的 pyinstaller 吧，很方便 兼容也可以

举例：
···
pyinstaller -F xxx.py
···

>> 
pyinstaller相关参数

-F：打包后只生成单个exe格式文件；
-D：默认选项，创建一个目录，包含exe文件以及大量依赖文件；
-c：默认选项，使用控制台(就是类似cmd的黑框)；
-w：不使用控制台；
-p：添加搜索路径，让其找到对应的库；
-i：改变生成程序的icon图标。

[完整参数参考](https://cloud.tencent.com/developer/news/299957)
