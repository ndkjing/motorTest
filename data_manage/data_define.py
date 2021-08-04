import threading
import time
import random
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import collections

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

    def test(self):
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [2, 1, 3, 5, 6, 4, 3]
        self.ax.plot(x, y)


class DataDefine:
    def __init__(self):
        # 停止pwm波值
        self.stop_pwm = None
        self.start_pwm = None  # 起始pwm
        self.end_pwm = None  # 结束pwm
        self.step_pwm = None  # pwm步距
        self.step_time = None  # 步距测试时间
        self.is_save_data = None  # 本地保存数据
        self.is_a = None  # 显示pwm与电流关系
        self.is_g = None  # 显示pwm与压力关系
        # 当前pwm波值
        self.current_pwm = None
        # 当前读取到电流与电压值
        self.pwm_a = collections.OrderedDict()
        self.pwm_g = collections.OrderedDict()
        # 串口对象
        self.com_obj = None
        #
        self.com_list = []
        self.com_obj = None
        self.com_485_obj = None
        self.ts = time.time()

        self.x_a = []
        self.x_g = []
        self.z_a = []
        self.z_g = []
        # self.x = np.arange(1000, 2000, 1)
        # self.y = np.arange(1, 20, 0.01)
        # self.z = self.x * 0.015 - 10
        # self.X, self.Y = np.meshgrid(self.x, self.y)
        # self.z = np.sin(self.x)
        # self.R = np.sqrt(self.X ** 2 + self.Y ** 2)
        # self.Z = np.sin(self.R)
        self.current_x = 1000
        self.add_sample()

    def add_sample(self, x=1000):
        self.x_a.append(self.current_x)
        self.z_a.append(random.randint(0, 30))
        self.x_g.append(self.current_x)
        self.z_g.append(random.randint(0, 15))
        self.current_x += 5


if __name__ == '__main__':
    data_define_obj = DataDefine()
    print(data_define_obj.x.shape)
    print(data_define_obj.y.shape)
    print(data_define_obj.z.shape)
    LineFigure = Figure_Canvas()
    line_a = Line2D(data_define_obj.x, data_define_obj.z)
    LineFigure.ax.set_xlim(0, 2000)
    LineFigure.ax.set_ylim(0, 30)
    LineFigure.ax.add_line(line_a)
