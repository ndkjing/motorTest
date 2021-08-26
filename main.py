# coding:utf-8
import sys
import os
import time
from ui import main_ui
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
from qt_material import apply_stylesheet
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import config
from driver import com_data
from data_manage import data_define
from data_manage import data_manage


class ComThread(QThread):
    """
    串口对象
    """

    def __init__(self, parent=None, run_func=None):
        """初始化方法"""
        super().__init__(parent)
        self.run_func = run_func

    def run(self):
        self.run_func()


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        plt.grid()
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.grid()

    def test(self):
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [2, 1, 3, 5, 6, 4, 3]
        self.ax.plot(x, y)


class MainDialog(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer1000 = QTimer()
        self.plot_timer = QTimer()
        # self.send_data = QTimer()
        self.data_define_obj = data_define.DataDefine()
        self.data_manage_obj = data_manage.DataManage(self.data_define_obj)
        self.com_thread = ComThread(run_func=self.data_manage_obj.get_com_data)
        self.com_485_thread = ComThread(run_func=self.data_manage_obj.get_485_data)
        self.com_485_thread.start()
        self.com_thread.start()
        self.start_test_time = None
        # self.data_manage_obj.init_thread()
        self.figure_dict = {}
        self.LineFigure = Figure_Canvas()
        self.LineFigure1 = Figure_Canvas()
        self.line_a = None
        self.line_g = None
        self.init_single_slot()
        self.init_timer()
        self.init_widget()

    def init_widget(self):
        for baud in config.baud_list:
            self.ui.baud_combo_box.addItem(str(baud))
        self.ui.baud_combo_box.setCurrentIndex(6)
        self.ui.step_pwm_spin_box.setValue(10)
        self.ui.step_time_spin_box.setValue(1)
        self.ui.pwm_a_check_box.setChecked(True)
        self.ui.pwm_g_check_box.setChecked(True)
        # 初始化绘图窗口
        line_figure_a = self.get_figure(date_type='a')
        line_figure_g = self.get_figure(date_type='g')
        self.figure_dict['pwm_a'] = line_figure_a
        self.figure_dict['pwm_g'] = line_figure_g
        self.ui.pwm_a_grid_layout.addWidget(line_figure_a)
        self.ui.pwm_g_grid_layout.addWidget(line_figure_g)

    def get_figure(self, date_type='a'):
        if date_type == 'a':
            LineFigure = Figure_Canvas()
            LineFigure.ax.set_xlim(1000, 2000)
            LineFigure.ax.set_ylim(0, 30)
            self.line_a = Line2D(self.data_define_obj.x_a, self.data_define_obj.z_a)
            LineFigure.ax.add_line(self.line_a)
        else:
            LineFigure = Figure_Canvas()
            LineFigure.ax.set_xlim(1000, 2000)
            LineFigure.ax.set_ylim(0, 15)
            self.line_g = Line2D(self.data_define_obj.x_g, self.data_define_obj.z_g)
            LineFigure.ax.add_line(self.line_g)
        return LineFigure

    def init_timer(self):
        """
        初始化定时器
        :return:
        """
        self.timer1000.timeout.connect(self.update_com_list)
        self.timer1000.start(1000)
        self.plot_timer.timeout.connect(self.update_plot)
        self.plot_timer.timeout.connect(self.send_com_data)

    def send_com_data(self):
        """
        发送串口数据
        :return:
        """
        if time.time() - self.start_test_time > self.data_define_obj.step_time:
            self.data_define_obj.current_pwm = self.data_define_obj.current_pwm + self.data_define_obj.step_pwm
            if self.data_define_obj.current_pwm > self.data_define_obj.end_pwm:
                self.data_define_obj.current_pwm = self.data_define_obj.stop_pwm
                # 到达最大值后设置开始测试为false
                self.ui.start_pushButton.setChecked(False)
                self.ui.start_pushButton.setText('开始测试')
                self.plot_timer.stop()
            self.start_test_time = time.time()
        print("pwm%dz" % self.data_define_obj.current_pwm)
        self.data_define_obj.com_obj.send_data("pwm%dz" % self.data_define_obj.current_pwm)

    def update_com_list(self):
        com_list = com_data.SerialData.print_used_com()
        com_list = list(set(com_list))

        def take_num(elem):
            return int(elem[3:])

        # 列表
        # 指定第二个元素排序
        com_list.sort(key=take_num)
        for com_name in com_list:
            if com_name not in self.data_define_obj.com_list:
                self.ui.com_combo_box.addItem(com_name)
                self.ui.com_485_combo_box.addItem(com_name)
                self.data_define_obj.com_list.append(com_name)

    # 绑定信号和槽
    def init_single_slot(self):
        self.ui.start_pushButton.clicked.connect(self.start_paint)
        self.ui.connect_com_push_button.clicked.connect(self.com_communication)
        # 动态显示图表失败 以后修改
        # self.ui.pwm_a_check_box.clicked.connect(self.update_plot_grid_layout)
        # self.ui.pwm_g_check_box.clicked.connect(self.update_plot_grid_layout)

    def com_communication(self):
        if self.ui.connect_com_push_button.isChecked():
            self.ui.connect_com_push_button.setText('断开串口')
            com_name = self.data_define_obj.com_list[self.ui.com_combo_box.currentIndex()]
            com_485_name = self.data_define_obj.com_list[self.ui.com_485_combo_box.currentIndex()]
            baud = config.baud_list[self.ui.baud_combo_box.currentIndex()]
            print('com_name', com_name, baud, 0.1)
            self.data_define_obj.com_obj = com_data.SerialData(com_name, baud, 0.1)
            self.data_define_obj.com_485_obj = com_data.SerialData(com_485_name, 38400, 0.1)
        else:
            self.ui.connect_com_push_button.setText('连接串口')
            self.data_define_obj.com_obj.close_Engine()
            self.data_define_obj.com_obj = None

    def update_plot_grid_layout(self):
        is_pwm_a = self.ui.pwm_a_check_box.isChecked()
        is_pwm_g = self.ui.pwm_g_check_box.isChecked()
        if self.sender() == self.ui.pwm_a_check_box:
            if is_pwm_a:
                if 'pwm_a' in self.figure_dict:
                    pass
                else:
                    print('add pwm_a')
                    line_figure = self.get_figure()
                    self.figure_dict['pwm_a'] = line_figure
                    self.ui.plot_grid_layout.addWidget(line_figure)
                    self.ui.plot_grid_layout.update()
            else:
                if 'pwm_a' in self.figure_dict:
                    self.ui.plot_grid_layout.removeWidget(self.figure_dict['pwm_a'])
                    self.ui.plot_grid_layout.update()
                    QApplication.processEvents()
                    del self.figure_dict['pwm_a']
                    print('delete pwm_a')
                    print(' self.figure_dict', self.figure_dict)

        if self.sender() == self.ui.pwm_g_check_box:
            if is_pwm_g:
                if 'pwm_g' in self.figure_dict:
                    pass
                else:
                    print('add pwm_g')
                    line_figure = self.get_figure()
                    self.figure_dict['pwm_g'] = line_figure
                    self.ui.plot_grid_layout.addWidget(line_figure)
            else:
                if 'pwm_g' in self.figure_dict:
                    self.ui.plot_grid_layout.removeWidget(self.figure_dict['pwm_g'])
                    self.ui.plot_grid_layout.update()
                    QApplication.processEvents()
                    del self.figure_dict['pwm_g']
                    print('delete pwm_g')

    def update_plot(self):
        is_test = False
        if is_test:
            self.data_define_obj.add_sample()
            if self.ui.pwm_a_check_box:
                self.line_a.set_xdata(self.data_define_obj.x_a)
                self.line_a.set_ydata(self.data_define_obj.z_a)
                self.figure_dict['pwm_a'].draw()
            if self.ui.pwm_g_check_box:
                self.line_g.set_xdata(self.data_define_obj.x_g)
                self.line_g.set_ydata(self.data_define_obj.z_g)
                self.figure_dict['pwm_g'].draw()
        else:
            if self.ui.pwm_a_check_box:
                if len(self.data_define_obj.pwm_a.keys()) == 0:
                    return
                x_a = list(self.data_define_obj.pwm_a.keys())
                y_a = []
                for i in x_a:
                    y_a.append(sum(self.data_define_obj.pwm_a[i]) / len(self.data_define_obj.pwm_a[i]))
                if len(y_a) > len(x_a):
                    y_a = y_a[0:len(x_a)]
                elif len(y_a) < len(x_a):
                    x_a = x_a[0:len(y_a)]
                self.line_a.set_xdata(x_a)
                self.line_a.set_ydata(y_a)
                self.figure_dict['pwm_a'].draw()
            if self.ui.pwm_g_check_box:
                if len(self.data_define_obj.pwm_g.keys()) == 0:
                    return
                x_g = list(self.data_define_obj.pwm_g.keys())
                y_g = []

                for i in x_g:
                    y_g.append(sum(self.data_define_obj.pwm_g[i]) / len(self.data_define_obj.pwm_g[i]))
                    print(len(self.data_define_obj.pwm_g[i]))
                print('g data', list(self.data_define_obj.pwm_a.keys()), y_g)
                if len(y_g) > len(x_g):
                    y_g = y_g[0:len(x_g)]
                elif len(y_g) < len(x_g):
                    x_g = x_g[0:len(y_g)]
                self.line_g.set_xdata(x_g)
                self.line_g.set_ydata(y_g)
                self.figure_dict['pwm_g'].draw()

    def start_paint(self):
        """
        开始绘图
        :return:
        """
        # 获取测试设置数据
        self.data_define_obj.stop_pwm = int(self.ui.stop_pwm_spin_box.value())
        self.data_define_obj.start_pwm = int(self.ui.start_pwm_spin_box.value())
        self.data_define_obj.end_pwm = int(self.ui.end_pwm_spin_box.value())
        self.data_define_obj.step_pwm = int(self.ui.step_pwm_spin_box.value())
        self.data_define_obj.step_time = int(self.ui.step_time_spin_box.value())
        self.data_define_obj.is_save_data = bool(self.ui.save_data_push_button.isChecked())
        self.data_define_obj.is_a = bool(self.ui.pwm_a_check_box.isChecked())
        self.data_define_obj.is_g = bool(self.ui.pwm_g_check_box.isChecked())
        # print( self.data_define_obj.stop_pwm, self.data_define_obj.start_pwm,self.data_define_obj.end_pwm,
        # self.data_define_obj.step_pwm, self.data_define_obj.step_time)
        if self.ui.start_pushButton.isChecked():
            # 开始测试前判断是否已经连接串口
            if self.data_define_obj.com_obj is None:
                QMessageBox.information(self, '提示', '还没有连接串口', QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)
                self.ui.start_pushButton.setChecked(False)
                return
            if self.ui.pwm_a_check_box.isChecked() or self.ui.pwm_g_check_box.isChecked():
                self.data_define_obj.com_obj.send_data("pwm%dz" % self.data_define_obj.stop_pwm)
                time.sleep(3)
                self.data_define_obj.current_pwm = self.data_define_obj.stop_pwm
                self.start_test_time = time.time()
                self.plot_timer.start(400)
            self.ui.start_pushButton.setText('结束测试')
        else:
            self.ui.start_pushButton.setText('开始测试')
            self.data_define_obj.com_obj.send_data("pwm%dz" % self.data_define_obj.stop_pwm)
            self.plot_timer.stop()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    main_windows = MainDialog()
    apply_stylesheet(myapp, theme='dark_teal.xml')
    main_windows.show()
    sys.exit(myapp.exec_())
