from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 上面两行代码解决matplotlib绘图不能显示中文问题
import matplotlib.pyplot as plt

labels = ['男性', '女性', '其他']
sizes = [57.1, 32.2, 10.7]
explode = (0, 0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# 纵横相等，画成一个圆
ax1.axis('equal')
plt.legend()
plt.show()
