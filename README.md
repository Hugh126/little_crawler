##little crawler
===
### 公司需要统计加班数据来计算加班费，由于个人加班较多，就做了考勤的小工具
### TODO : 
*1、完整的写入excel
*2、密码加密显示


## cx_freeze 介绍
* 安装 install cx_freeze
* 切换到Python安装目录的Scripts目录，比如我的为c:\Python34\Scripts
* 运行 python cxfreeze-postinstall
* 测试是否安装成功 cxfreeze -h
## 使用
* cxfreeze  OATable.py  --target-dir dist  
* 去掉黑框
* cxfreeze  Devation.py  --target-dir dist  --base-name=win32gui