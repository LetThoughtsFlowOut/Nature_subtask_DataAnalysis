import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


# 读取Excel文件
data = pd.read_excel('population.xlsx')


dense_dict = ("flat_roof密度", "gable_roof密度", "gambrel_roof密度", "row_roof密度", "multiple_eave_roof密度",
              "hipped_roof_v1密度", "hipped_roof_v2密度", "mansard_roof密度", "pyramid_roof密度", "arched_roof密度",
              "revolved密度", "other密度")

proportion_dict = ("flat_roof占比", "gable_roof占比", "gambrel_roof占比", "row_roof占比", "multiple_eave_roof占比",
                   "hipped_roof_v1占比", "hipped_roof_v2占比", "mansard_roof占比", "pyramid_roof占比", "arched_roof占比",
                   "revolved占比", "other占比")


# 获取需要提取的列
columns_to_extract = list(proportion_dict)

show_label = ("flat", "gable", "gambrel", "row", "multiple", "hipped_v1",
              "hipped_v2", "mansard", "pyramid", "arched", "revolved", "other")

show = list(show_label)

save_path = 'images/proportion_images'
os.chdir(save_path)

label_item = data['样本']
label_country = data['国家']
label_state = data['大洲']

# 逐行读取数据，仅提取所需列
for i, row in data[columns_to_extract].iterrows():

    plt.figure(figsize=(8, 8), dpi=100)
    variable = np.array(list(row))

    variable[variable < 0.05] = 0
    # 对y轴数据进行对数变换
    log_variable = np.log(variable * 20)

    # 设置中文字体
    plt.rcParams["font.family"] = "SimHei"

    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

    # 绘制柱状图，注意这里的y轴数据是处理过后的log_variable
    plt.bar(show, variable)

    # 添加文本
    for x, y in zip(show, variable):
        plt.text(x, y + 0.05, '%.2f' % y, ha='center')

    # 设置y轴刻度为对数值
    # ticks = [np.log(i*20) for i in np.array([1, 5, 10, 15, 20, 25, 30])]
    plt.xticks(rotation=45, ha='right', va='top', y=0.01)
    # plt.yticks(ticks, ['1', '5', '10', '15', '20', '25', '30'])
    plt.xlabel("建筑物类别")
    plt.ylabel("建筑物占比（百分制）")

    if i < 72:
        title = f"{label_state[i]} - {label_country[i]} - {label_item[i]}"
    else:
        title = f"{label_country[i]}"

    plt.title(title)

    # 保存当前柱状图
    plt.savefig(f'item_{i}.png')


