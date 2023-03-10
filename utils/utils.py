import logging
import os
import time


def log_set(show_level=logging.DEBUG, save_level=logging.INFO):
    logger = logging.getLogger()  # 不加名称设置root logger
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 使用FileHandler输出到文件
    fh = logging.FileHandler('log.log')
    fh.setLevel(save_level)
    fh.setFormatter(formatter)

    # 使用StreamHandler输出到屏幕
    ch = logging.StreamHandler()
    ch.setLevel(show_level)
    ch.setFormatter(formatter)

    # 添加两个Handler
    logger.addHandler(ch)
    logger.addHandler(fh)


def clear_port(port=6006) -> int:
    export = os.popen("lsof -i :{} | grep {}".format(port, port)).read()
    if export != "":
        export = [word for word in export.split(" ") if word != '']
        os.system("kill -9 {}".format(export[1]))
        print("Successful kill port {}".format(port))
        time.sleep(2)
        return int(export[1])
