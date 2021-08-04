import threading
import time
import binascii
from data_manage import data_define


class DataManage:
    def __init__(self, data_define_obj: data_define.DataDefine):
        self.data_define_obj = data_define_obj

    def init_thread(self):
        get_com_data_thread = threading.Thread(target=self.get_com_data)
        get_com_data_thread.setDaemon(True)
        get_com_data_thread.run()

    def get_com_data(self):
        while True:
            time.sleep(0.1)
            if self.data_define_obj.com_obj is None:
                print('pass')
                continue
            com_data_read = self.data_define_obj.com_obj.readline()
            a = 10
            g = 10
            # 解析串口发送过来的数据
            if com_data_read is None:
                continue
            try:
                com_data_list = com_data_read.split(',')
                if len(com_data_list) != 2:
                    print('发送参数长度不正确', com_data_read)
                    continue
                a = float(com_data_list[0][1:])
                g = float(com_data_list[1][:-5])
            except Exception as e:
                print('get_com_data error', e)
                continue
            print('com_data_read', com_data_read, a, g)
            # 更新电流与压力列表
            if self.data_define_obj.current_pwm is None:
                continue
            if self.data_define_obj.current_pwm in self.data_define_obj.pwm_a:
                self.data_define_obj.pwm_a.get(self.data_define_obj.current_pwm).append(a)
            else:
                self.data_define_obj.pwm_a[self.data_define_obj.current_pwm] = [a]
            # 板子485有问题改为用485转串口读取
            # if self.data_define_obj.current_pwm in self.data_define_obj.pwm_g:
            #     self.data_define_obj.pwm_g.get(self.data_define_obj.current_pwm).append(g)
            # else:
            #     self.data_define_obj.pwm_g[self.data_define_obj.current_pwm] = [g]

    def get_485_data(self):
        while True:
            time.sleep(0.2)
            if self.data_define_obj.com_485_obj is None:
                print('pass')
                continue
            data = '200300000002C2BA'
            self.data_define_obj.com_485_obj.send_data(data, is_hex=True)
            time.sleep(0.1)
            byte_data = self.data_define_obj.com_485_obj.readline(is_row=True)
            try:
                str_data = str(binascii.b2a_hex(byte_data))[2:-1]
                g = int(str_data[10:14] + str_data[6:10], 16) / 100.0
            except Exception as e:
                print('get_485_data error e', e)
                continue
            if self.data_define_obj.current_pwm is None:
                continue
            if g > 200 or g < 0.01:
                continue
            print('pwm_g', self.data_define_obj.pwm_g, self.data_define_obj.current_pwm in self.data_define_obj.pwm_g)
            if self.data_define_obj.current_pwm in self.data_define_obj.pwm_g:
                self.data_define_obj.pwm_g.get(self.data_define_obj.current_pwm).append(g)
            else:
                self.data_define_obj.pwm_g[self.data_define_obj.current_pwm] = [g]
