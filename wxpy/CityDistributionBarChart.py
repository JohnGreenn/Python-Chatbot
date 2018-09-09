import numpy as np
import matplotlib.pyplot as plt

n_groups = 10
# 
city_weight = (10.2,8.98,8.57,2.04,2.04,1.63,1.63,1.22,1.22,1.22)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = ax.bar(index, city_weight, bar_width,alpha=opacity, color='b', error_kw=error_config,label='城市')
ax.set_xlabel('城市名称')
ax.set_ylabel('数据占比(%)')
ax.set_title('好友城市Top10')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('荆州', '武汉', '黄石', '海淀', '广州','深圳', '黄冈', '杭州', '长沙', '昌平'))
ax.legend()
fig.tight_layout()
plt.show()
