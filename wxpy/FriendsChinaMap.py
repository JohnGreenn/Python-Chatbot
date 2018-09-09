from pyecharts import Map
# matplotlib的方法比较麻烦，显示起来还没pyecharts 好，就用了pyecharts 
value = [359.2, 65.3, 49.0, 20.4, 20.4, 16.3, 16.3, 12.2, 12.2,12.2]
attr = [
    "湖北", "广东", "北京", "湖南", "上海", "浙江", "河南", "安徽", "山东","福建"
    ]
map = Map("好友分布省份Top10", width=600, height=400)
map.add(
    "",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
)
map.render()
