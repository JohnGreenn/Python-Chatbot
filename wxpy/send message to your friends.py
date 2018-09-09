from wxpy import *
# 初始化一个机器人对象
bot = Bot(cache_path =r"C:\Users\aa892\Desktop\Python项目\wxpy.pkl")

'''
# 查找朋友"小王子"
my_friend = bot.friends().search('小王子')[0]
# 发送消息
my_friend.send('hello world')
'''
# 获取所有好友【返回列表包含chats对象（你的所有好友包括你自己）】
t0 = bot.friends(update=False)
# 查看自己的好友数(除开自己)
print("我的好友数: "+str(len(t0)-1))

#获取所有微信群[返回列表包含Groups对象]
t1 = bot.groups(update=False)
# 查看微信群数（活跃的）
print("我的微信群聊数: "+str(len(t1)))

# 获取所有关注的微信公众号[返回列表包含chats对象]
t2 = bot.mps(update=False)

# 查看关注的微信公众号数
print("我关注逇微信公众号数: "+str(len(t2)))
