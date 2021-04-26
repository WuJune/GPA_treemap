import pandas as pd
import plotly.express as px

def func(x):
    if isinstance(x, str):
        return -1.0
    else :
        if x < 60:
            x = 60
        return float(x)



print('开始处理 data.xlsx')

try:
    data = pd.read_excel('data.xlsx')
except FileNotFoundError:
    print('文件 data.xlsx 未找到，请放在和 main.py 同一目录下')

data["Semester"] = data["Semester"].apply(lambda x : 'Semester' + str(x))

data = data.drop(data[data.Credit  == 0].index)

if data['Score'].dtype == 'object':
    print("成绩栏不能含有符号和文字等非纯数字, 成绩为非纯数字科目将不会参与最后结果")
    data["Score"] = data["Score"].apply(func)
    data = data.drop(data[data.Score == -1.0].index)

data['Sum'] = 'Sum'

fig = px.treemap(data, height = 1080, width = 1920,path=['Sum', 'Semester', 'Course'], values='Credit', color='Score', range_color = [100, 60], color_continuous_scale='Geyser', color_continuous_midpoint=80)
fig.update_traces(textinfo='label+value',textfont = dict(size = 24))
fig.show()