import os

root_dir = os.path.dirname(os.path.abspath(__file__))

log_path = os.path.join(root_dir, 'log')
if not os.path.exists(log_path):
    os.mkdir(log_path)

baud_list = [1200, 2400, 4800, 9600, 19200, 38400, 115200]
