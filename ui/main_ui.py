# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.com_485_combo_box = QtWidgets.QComboBox(self.groupBox_2)
        self.com_485_combo_box.setObjectName("com_485_combo_box")
        self.horizontalLayout.addWidget(self.com_485_combo_box)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.com_combo_box = QtWidgets.QComboBox(self.groupBox_2)
        self.com_combo_box.setObjectName("com_combo_box")
        self.horizontalLayout.addWidget(self.com_combo_box)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.baud_combo_box = QtWidgets.QComboBox(self.groupBox_2)
        self.baud_combo_box.setObjectName("baud_combo_box")
        self.horizontalLayout.addWidget(self.baud_combo_box)
        self.connect_com_push_button = QtWidgets.QPushButton(self.groupBox_2)
        self.connect_com_push_button.setCheckable(True)
        self.connect_com_push_button.setObjectName("connect_com_push_button")
        self.horizontalLayout.addWidget(self.connect_com_push_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.stop_pwm_spin_box = QtWidgets.QSpinBox(self.groupBox_9)
        self.stop_pwm_spin_box.setMinimum(1400)
        self.stop_pwm_spin_box.setMaximum(1600)
        self.stop_pwm_spin_box.setProperty("value", 1500)
        self.stop_pwm_spin_box.setObjectName("stop_pwm_spin_box")
        self.verticalLayout_4.addWidget(self.stop_pwm_spin_box)
        self.label_4 = QtWidgets.QLabel(self.groupBox_9)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.start_pwm_spin_box = QtWidgets.QSpinBox(self.groupBox_9)
        self.start_pwm_spin_box.setMinimum(1000)
        self.start_pwm_spin_box.setMaximum(2000)
        self.start_pwm_spin_box.setProperty("value", 1500)
        self.start_pwm_spin_box.setObjectName("start_pwm_spin_box")
        self.verticalLayout_4.addWidget(self.start_pwm_spin_box)
        self.label_5 = QtWidgets.QLabel(self.groupBox_9)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.end_pwm_spin_box = QtWidgets.QSpinBox(self.groupBox_9)
        self.end_pwm_spin_box.setMinimum(1000)
        self.end_pwm_spin_box.setMaximum(2000)
        self.end_pwm_spin_box.setProperty("value", 2000)
        self.end_pwm_spin_box.setObjectName("end_pwm_spin_box")
        self.verticalLayout_4.addWidget(self.end_pwm_spin_box)
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.step_pwm_spin_box = QtWidgets.QSpinBox(self.groupBox_9)
        self.step_pwm_spin_box.setMaximum(100)
        self.step_pwm_spin_box.setObjectName("step_pwm_spin_box")
        self.verticalLayout_4.addWidget(self.step_pwm_spin_box)
        self.label_7 = QtWidgets.QLabel(self.groupBox_9)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.step_time_spin_box = QtWidgets.QSpinBox(self.groupBox_9)
        self.step_time_spin_box.setObjectName("step_time_spin_box")
        self.verticalLayout_4.addWidget(self.step_time_spin_box)
        self.verticalLayout_2.addWidget(self.groupBox_9)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.save_data_push_button = QtWidgets.QPushButton(self.groupBox_6)
        self.save_data_push_button.setCheckable(True)
        self.save_data_push_button.setObjectName("save_data_push_button")
        self.verticalLayout_5.addWidget(self.save_data_push_button)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.pwm_a_check_box = QtWidgets.QCheckBox(self.groupBox_6)
        self.pwm_a_check_box.setObjectName("pwm_a_check_box")
        self.verticalLayout_5.addWidget(self.pwm_a_check_box)
        self.pwm_g_check_box = QtWidgets.QCheckBox(self.groupBox_6)
        self.pwm_g_check_box.setObjectName("pwm_g_check_box")
        self.verticalLayout_5.addWidget(self.pwm_g_check_box)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.start_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.start_pushButton.setCheckable(True)
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout_2.addWidget(self.start_pushButton)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.plot_grid_layout = QtWidgets.QGridLayout(self.groupBox_4)
        self.plot_grid_layout.setContentsMargins(-1, 0, 0, 0)
        self.plot_grid_layout.setSpacing(0)
        self.plot_grid_layout.setObjectName("plot_grid_layout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pwm_g_grid_layout = QtWidgets.QGridLayout(self.groupBox_5)
        self.pwm_g_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.pwm_g_grid_layout.setSpacing(0)
        self.pwm_g_grid_layout.setObjectName("pwm_g_grid_layout")
        self.plot_grid_layout.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName("groupBox_7")
        self.pwm_a_grid_layout = QtWidgets.QGridLayout(self.groupBox_7)
        self.pwm_a_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.pwm_a_grid_layout.setSpacing(0)
        self.pwm_a_grid_layout.setObjectName("pwm_a_grid_layout")
        self.plot_grid_layout.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "压力计485串口："))
        self.label.setText(_translate("MainWindow", "串口编号："))
        self.label_2.setText(_translate("MainWindow", "波特率："))
        self.connect_com_push_button.setText(_translate("MainWindow", "连接串口"))
        self.label_3.setText(_translate("MainWindow", "停止PWM"))
        self.label_4.setText(_translate("MainWindow", "起始pwm"))
        self.label_5.setText(_translate("MainWindow", "结束PWM"))
        self.label_6.setText(_translate("MainWindow", "步距"))
        self.label_7.setText(_translate("MainWindow", "步距持续时间"))
        self.save_data_push_button.setText(_translate("MainWindow", "保存数据"))
        self.label_9.setText(_translate("MainWindow", "显示模式："))
        self.pwm_a_check_box.setText(_translate("MainWindow", "pwm与电流"))
        self.pwm_g_check_box.setText(_translate("MainWindow", "pwm与压力"))
        self.start_pushButton.setText(_translate("MainWindow", "开始测试"))
        self.groupBox_4.setTitle(_translate("MainWindow", "图表显示"))
        self.groupBox_5.setTitle(_translate("MainWindow", "pwm与压力"))
        self.groupBox_7.setTitle(_translate("MainWindow", "pwm与电流"))