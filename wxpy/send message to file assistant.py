from wxpy import *
# 初始化一个机器人对象
bot = Bot(cache_path=True)
# 向文件传输助手发送消息
bot.file_helper.send("hi,I love you!")
