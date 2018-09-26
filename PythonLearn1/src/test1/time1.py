# coding=utf-8
import time
 
 
class GetTime(object):
 
    def get_system_time(self):
        print (time.time()) # time.time()获取的是从1970年到现在的间隔，单位是秒
        print (time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
        print (new_time)
        new_time1 = time.strftime('%Y-%m-%d', time.localtime()) # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
        print (new_time1)
 
gettime = GetTime()
gettime.get_system_time()
