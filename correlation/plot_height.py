import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


# 读取Excel文件
data = pd.read_excel('population.xlsx')

high_dict = ("Low_rise", "Multi_storey", "Medium_and_high_rise", "High_rise_v1", "High_rise_v2")

# 获取需要提取的列
columns_to_extract = list(high_dict)

show_label = ("Low", "Multi_storey", "Medium_and_high", "High_v1", "High_v2")

show = list(show_label)

save_path = 'images/height_images'
os.chdir(save_path)

label_item = data['样本']
label_country = data['国家']
label_state = data['大洲']

# 逐行读取数据，仅提取所需列
for i, row in data[columns_to_extract].iterrows():

    plt.figure(figsize=(8, 8), dpi=100)
    variable = np.array(list(row))

    # 对y轴数据进行对数变换
    log_variable = np.log(variable.clip(1.01, None))

    # 设置中文字体
    plt.rcParams["font.family"] = "SimHei"

    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

    # 绘制柱状图，注意这里的y轴数据是处理过后的log_variable
    plt.bar(show, log_variable)

    # 添加文本
    for x, y in zip(show, variable):
        plt.text(x, np.log(y.clip(1.01, None)) + 0.05, '%d' % y, ha='center')

    # 设置y轴刻度为对数值
    ticks = [np.log(i) for i in np.array([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])]
    # plt.xticks(rotation=45, ha='right', va='top', y=0.03)
    plt.yticks(ticks, ['1', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000'])
    plt.xlabel("建筑物高度分类")
    plt.ylabel("log(height)")

    if i < 72:
        title = f"{label_state[i]} - {label_country[i]} - {label_item[i]}"
    else:
        title = f"{label_country[i]}"

    plt.title(title)

    # 保存当前柱状图
    plt.savefig(f'item_{i}.png')


