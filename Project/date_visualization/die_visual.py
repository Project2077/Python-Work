from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# 创建一个D6。
d6 = Die()
d10 = Die(10)

# 掷几次骰子并将结果存储在一个列表中。
results = []
for roll_num in range(50_000):
    # result = d6.roll()
    result = d6.roll() + d10.roll()
    results.append(result)

# 分析结果。
frequencies = []
max_result = d6.num_sides + d10.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

print(frequencies)

print(results)
