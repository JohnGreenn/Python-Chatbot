'''
author : 蜡笔小强
data : 2018.9.9
goal : 获取微信好友性别、分布、微信昵称，可视化分析
'''

from wxpy import *

# 初始化一个机器人对象
# cache_path缓存路径，给定值为第一次登录生成的缓存文件路径
bot = Bot(cache_path=r"C:\Users\aa892\Desktop\Python项目\wxpy.pkl")
#获取好友列表(包括自己)
my_friends = bot.friends(update=False)
'''
stats_text 函数：帮助我们简单统计微信好友基本信息
简单的统计结果的文本
    :param total: 总体数量
    :param sex: 性别分布
    :param top_provinces: 省份分布
    :param top_cities: 城市分布
    :return: 统计结果文本
'''
print(my_friends.stats_text())
