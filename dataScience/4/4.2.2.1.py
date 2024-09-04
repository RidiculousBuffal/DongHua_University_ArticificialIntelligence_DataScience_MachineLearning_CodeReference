# -*- coding: utf-8 -*-
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION
import matplotlib.figure
import pandas
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 从high-speed rail.csv中读入文件
high_speed_rail = pd.read_csv("High-speed rail.csv", encoding='utf-8', index_col='Country')
Countries = high_speed_rail.index.tolist()
Operations = high_speed_rail['Operation'].tolist()
CO_zip = list(zip(Countries, Operations))
c = (
    MapGlobe(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add_schema()
    .add(
        maptype="world",
        series_name="high_speedrail operation",
        data_pair=CO_zip[:],
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(
            is_show=True,
            position="bottom",
            color="#000",
        ),
    )
    .render("map_globe.html")
)
