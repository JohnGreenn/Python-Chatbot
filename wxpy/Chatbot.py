from wxpy import *
# 初始化一个机器人对象
bot = Bot(cache_path=r'C:\Users\aa892\Desktop\Python项目\wxpy.pkl')

#来自图灵官网api 去注册可以获得
tuling = Tuling(api_key='6eaa0643cbf649b88521aaa184b8447c')
print('蜡笔小强机器人已经启动')
# 查找聊天对象
my_friend = bot.friends().search('韩代小王子')[0]



# 自动回复
# 如果想对所有好友机器人回复把参数 my_friend 改成 chats = [Friend]
@bot.register(my_friend)
def my_friend_message(msg):
    tuling.do_reply(msg)
    
# 进入交互式的Python 命令行界面，并且堵塞当前线程
embed()



