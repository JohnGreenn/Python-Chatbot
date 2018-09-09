from wxpy import *
# 初始化一个机器人对象
bot = Bot(cache_path=r'C:\Users\aa892\Desktop\Python项目\wxpy.pkl')

# 查找聊天对象
my_friend = bot.friends().search('韩代小王子')[0]
my_friend.send('hello how are you?')


# 自动回复
# 如果想对所有好友机器人回复把参数 my_friend 改成 chats = [Friend]
@bot.register(my_friend)
def my_friend_message(msg):
    print('[接收]' + str(msg))
    if msg.type !='Text':  # 除了文字外其他消息回复内容
        ret = '小可爱你给我发了什么鸭，我目前还看不懂'
    elif "你来自哪里" in str(msg): #特定问题回答
        ret = "我来自女娲诞生之时。。。嘿嘿"
    else:       # 文字消息自动回答
        ret = 'I love you baby'
    print('[发送]' + str(ret))
    return ret
# 进入交互式的Python 命令行界面，并且堵塞当前线程
embed()



