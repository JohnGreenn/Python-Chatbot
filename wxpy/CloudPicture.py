# 5.获取好友微信名称，词云分析
from wxpy import *
from os import path
import re, jieba
import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm

# 清洗数据，生成词云图
#获取当前的项目文件加的路径
d=path.dirname(__file__)
#读取停用词表
stopwords_path=d + '/static/stopwords.txt'

#定义个函数式用于分词
def jiebaclearText(text):
    #定义一个空的列表，将去除的停用词的分词保存
    mywordList=[]
    #进行分词
    seg_list=jieba.cut(text,cut_all=False)
    #将一个generator的内容用/连接
    listStr='/'.join(seg_list)
    listStr = listStr.replace("class","")
    listStr = listStr.replace("span", "")
    listStr = listStr.replace("emoji", "")
    #打开停用词表
    f_stop=open(stopwords_path,encoding="utf8")
    #读取
    try:
        f_stop_text=f_stop.read()
    finally:
        f_stop.close()#关闭资源
    #将停用词格式化，用\n分开，返回一个列表
    f_stop_seg_list=f_stop_text.split("\n")
    #对默认模式分词的进行遍历，去除停用词
    for myword in listStr.split('/'):
        #去除停用词
        if not(myword.split()) in f_stop_seg_list and len(myword.strip())>1:
            mywordList.append(myword)
    return ' '.join(mywordList)

# 生成词云图
def make_wordcloud(text1,i):
	bg = plt.imread(d+r"/image/爱心01.jpg")
	# 生成
	wc = WordCloud(# FFFAE3
		background_color="#FFFFFF",  # 设置背景为白色，默认为黑色
		width=990,  # 设置图片的宽度
		height=440,  # 设置图片的高度
		mask=bg,
		margin=10,  # 设置图片的边缘
		max_font_size=70,  # 显示的最大的字体大小
		random_state=20,  # 为每个单词返回一个PIL颜色
		font_path=d+'/static/simkai.ttf'  # 中文处理，用系统自带的字体
	).generate(text1)
	# 为图片设置字体
	my_font = fm.FontProperties(fname=d+'/static/simkai.ttf')
	# 图片背景
	bg_color = ImageColorGenerator(bg)
	# 开始画图
	plt.imshow(wc.recolor(color_func=bg_color))
	# 为云图去掉坐标轴
	plt.axis("off")
	# 画云图，显示
	# 保存云图
	wc.to_file(d+r"/image/render_0%d.png"%i)


# bot = Bot(cache_path=d + "/wxpy.pkl")
bot = Bot(cache_path=r'C:\Users\aa892\Desktop\Python项目\wxpy.pkl')
#获取好友列表(包括自己)
my_friends = bot.friends(update=False)
# 微信昵称
nick_name = ''
# 微信个性签名
wx_signature = ''
for friend in my_friends:
	# 微信昵称：NickName
	nick_name = nick_name + friend.raw['NickName']
	# 个性签名：Signature
	wx_signature = wx_signature + friend.raw['Signature']

nick_name = jiebaclearText(nick_name)
wx_signature = jiebaclearText(wx_signature)
make_wordcloud(nick_name,1)
make_wordcloud(wx_signature,2)

