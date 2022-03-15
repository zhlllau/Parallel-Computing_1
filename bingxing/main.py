import pyecharts.options as opts
import pandas as pd
from pyecharts.charts import Line

def biao1():
    data1 = pd.read_csv('biao1_normaloo1.csv')
    x = data1['n']
    y1 = data1['o']
    y2= data1['o1']
    line=(
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
        .add_xaxis(xaxis_data= x)
        .add_yaxis(series_name="平凡算法（o）", y_axis=y1, label_opts=False)
        .add_yaxis(series_name="平凡算法（o1优化）", y_axis=y2, label_opts=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="平凡算法o、o1对比", pos_bottom='10', pos_right='150'),
                     xaxis_opts=opts.AxisOpts(name='N',is_show=True),
                     yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True),)

)
    line.render('tu1.html')

def biao2():
    data1 = pd.read_csv('biao2_piple_pandfpo.csv')
    x = data1['n']
    y1 = data1['o']
    y2 = data1['o1']
    line = (
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name="平凡算法（o）", y_axis=y1, label_opts=False)
            .add_yaxis(series_name="优化算法（o）", y_axis=y2, label_opts=False)
            .set_global_opts(title_opts=opts.TitleOpts(title="平凡算法o、优化算法o对比", pos_bottom='10', pos_right='150'),
                             xaxis_opts=opts.AxisOpts(name='N', is_show=True),
                             yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True), )

    )
    line.render('tu2.html')

def biao3():
    data1 = pd.read_csv('biao3.csv')
    x = data1['n']
    y0=data1['o']
    y1 = data1['o1']
    y2 = data1['o2']
    y3 = data1['o3']
    line = (
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name="优化算法（o）", y_axis=y0, label_opts=False)
            .add_yaxis(series_name="优化算法（o1）", y_axis=y1, label_opts=False)
            .add_yaxis(series_name="优化算法（o2）", y_axis=y2, label_opts=False)
            .add_yaxis(series_name="优化算法（o3）", y_axis=y3, label_opts=False)
            .set_global_opts(title_opts=opts.TitleOpts(title="优化算法o、o1、o2、o3对比", pos_bottom='10', pos_right='150'),
                             xaxis_opts=opts.AxisOpts(name='N', is_show=True),
                             yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True,name_gap=8),)

    )
    line.render('tu3.html')


def biao4():
    data1 = pd.read_csv('arm_pipleoandyou.csv')
    x = data1['n']
    y1 = data1['po']
    y2 = data1['youo']
    line = (
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name="平凡算法（o）", y_axis=y1, label_opts=False)
            .add_yaxis(series_name="优化算法（o）", y_axis=y2, label_opts=False)
            .set_global_opts(title_opts=opts.TitleOpts(title="Arm-平凡算法o、优化算法o对比", pos_bottom='10', pos_right='100'),
                             xaxis_opts=opts.AxisOpts(name='N', is_show=True),
                             yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True), )

    )
    line.render('tu4.html')
biao1()
biao2()
biao3()
biao4()
def biao_4():
    data1 = pd.read_csv('biao4.csv')
    x = data1['n']
    y1 = data1['o2']
    y2= data1['youo2']
    line=(
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
        .add_xaxis(xaxis_data= x)
        .add_yaxis(series_name="平凡算法（o2）", y_axis=y1, label_opts=False)
        .add_yaxis(series_name="优化算法（o2）", y_axis=y2, label_opts=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="X86_平凡算法o2、优化算法o2对比", pos_bottom='10', pos_right='70'),
                     xaxis_opts=opts.AxisOpts(name='N',is_show=True),
                     yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True),)

)
    line.render('tu_4.html')
def biao5():
    data1 = pd.read_csv('biao5.csv')
    x = data1['n']
    y0=data1['o']
    y1 = data1['o1']
    y2 = data1['o2']
    y3 = data1['o3']
    line = (
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name="优化算法（o）", y_axis=y0, label_opts=False)
            .add_yaxis(series_name="优化算法（o1）", y_axis=y1, label_opts=False)
            .add_yaxis(series_name="优化算法（o2）", y_axis=y2, label_opts=False)
            .add_yaxis(series_name="优化算法（o3）", y_axis=y3, label_opts=False)
            .set_global_opts(title_opts=opts.TitleOpts(title="X86_优化算法o、o1、o2、o3对比", pos_bottom='10', pos_right='100'),
                             xaxis_opts=opts.AxisOpts(name='N', is_show=True),
                             yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True,name_gap=8),)

    )
    line.render('tu5.html')

def biao6():
    data1 = pd.read_csv('biao6.csv')
    x = data1['n']
    y1 = data1['o']
    y2 = data1['youo']
    line = (
        Line(init_opts=opts.InitOpts(width="500px", height='500px'))
            .add_xaxis(xaxis_data=x)
            .add_yaxis(series_name="平凡算法（o）", y_axis=y1, label_opts=False)
            .add_yaxis(series_name="优化算法（o）", y_axis=y2, label_opts=False)
            .set_global_opts(title_opts=opts.TitleOpts(title="Arm-平凡算法o、优化算法o对比", pos_bottom='10', pos_right='100'),
                             xaxis_opts=opts.AxisOpts(name='N', is_show=True),
                             yaxis_opts=opts.AxisOpts(name='单次执行时间(ms)', is_show=True), )

    )
    line.render('tu6.html')

biao_4()
biao5()
biao6()
# 以下为Cache
