# ------------------------------------
# -*- coding = utf-8 -*-
# @Time : 2021/6/14 18:30
# @Author ：chc_stars
# @File : visualization.py
# @Software : PyCharm 

# --------------------------------------
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon


import time
# from Train import get_time_dif
from datetime import timedelta
from Pred import CnnModel
import tensorflow as tf

tf.reset_default_graph()


def get_time_dif(start_time):
    """获取已使用时间"""
    end_time = time.time()
    time_dif = end_time - start_time
    return timedelta(seconds=int(round(time_dif)))
class Single_input:
    def __init__(self):
        # 从文件中加载ui定义
        # qfile = QFile("E:\CODE\python/新闻分类/News_Classification/New_Class.ui")
        qfile = QFile("New_Class.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从UI 定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也能成为窗口对象的属性
        self.ui = QUiLoader().load(qfile)
        self.ui.Button.clicked.connect(self.implement)

    def implement(self):
        start_time = time.time()
        info = self.ui.TextEdit.toPlainText()

        cnn_models = CnnModel()

        output = ''
        for line in info.splitlines():
            if not line.strip():
                continue

            output += cnn_models.predict(line)
            output += '\n'

        time_dif = get_time_dif(start_time)

        self.ui.textBrowser.append(output)
        self.ui.textBrowser.append(f'time_use:{time_dif}')


app = QApplication([])
# app.setWindowIcon(QIcon('hy.png'))
single = Single_input()
single.ui.show()

app.exec_() #循环，等待用户


