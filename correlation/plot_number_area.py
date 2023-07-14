import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


# 读取Excel文件
data = pd.read_excel('population.xlsx')

class_dict = ("类别flat_roof", "类别gable_roof", "类别gambrel_roof", "类别row_roof", "类别multiple_eave_roof",
              "类别hipped_roof_v1", "类别hipped_roof_v2", "类别mansard_roof", "类别pyramid_roof", "类别arched_roof",
              "类别revolved", "类别other")

area_dict = ("flat_roof面积", "gable_roof面积", "gambrel_roof面积", "row_roof面积", "multiple_eave_roof面积",
             "hipped_roof_v1面积", "hipped_roof_v2面积", "mansard_roof面积", "pyramid_roof面积", "arched_roof面积",
             "revolved面积", "other面积")


# 获取需要提取的列
columns_to_extract = list(area_dict)

show_label = ("flat", "gable", "gambrel", "row", "multiple", "hipped_v1",
              "hipped_v2", "mansard", "pyramid", "arched", "revolved", "other")

show = list(show_label)

save_path = 'images/area_images'
os.chdir(save_path)

label_item = data['样本']
label_country = data['国家']
label_state = data['大洲']


# 逐行读取数据，仅提取所需列
for i, row in data[columns_to_extract].iterrows():

    plt.figure(figsize=(8, 8), dpi=100)
    variable = np.array(list(row))

    # 对y轴数据进行对数变换
    log_variable = np.log(variable)

    # 设置中文字体
    plt.rcParams["font.family"] = "SimHei"

    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

    # 绘制柱状图，注意这里的y轴数据是处理过后的log_variable
    plt.bar(show, log_variable)

    # 添加文本
    for x, y in zip(show, variable):
        plt.text(x, np.log(y) + 0.05, '%d' % y, ha='center')

    # 设置y轴刻度为对数值
    ticks = [np.log(i) for i in np.array([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000])]
    plt.xticks(rotation=45, ha='right', va='top', y=0.01)
    plt.yticks(ticks, ['1', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000', '1000000000'])
    plt.xlabel("建筑物类别")
    plt.ylabel("log(number)")
    if i < 72:
        title = f"{label_state[i]} - {label_country[i]} - {label_item[i]}"
    else:
        title = f"{label_country[i]}"

    plt.title(title)

    # 保存当前柱状图
    plt.savefig(f'item_{i}.png')


