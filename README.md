# News_Classification

这是一个新闻分类的软件，使用的模型是textCNN。分类效果如下：

visualization.py 可以跳出界面框
![image](https://user-images.githubusercontent.com/76056473/224910640-c3673c43-d466-47fe-a6ab-3c8bfb16af18.png)


2021 软件杯-A7-新闻文本分类算法
Team：不知道取啥名

简介
环境
Tensorflow == 1.8.0

Keras == 2.1.6

python == 3.6.13

pyside2 == 5.15.2

文件说明
Data_exploration：用于探索性数据分析。
Data_Preprocessing：用于预训练语料的构建。
Cnn_model: TextCNN模型的搭建。
Train：用于新闻文本分类模型的训练。
Test：用于新闻文本分类模型的测试。
Pred：用于新闻文本分类模型的预测。
visualization: 用于可视化程序的制作。
data_class_handle：用于数据输入格式的转换。
其他
数据集下载地址：

链接：https://pan.baidu.com/s/18d4oQEZOCHl2eunIN-BMnQ 提取码：bh5p

项目介绍
实用价值
新闻发展越来越快，每天各种各样的新闻令人目不暇接，对新闻进行科学的分类既能方便不同的阅读群体根据需求快速的选取自身感兴趣的新闻，也能有效满足对海量的新闻素材提供科学的检索需求。

任务目标
1、输出分类的准确率不低于80%。

2、提供简单的可视化界面。能够输入单条新闻，输出新闻的分类，或者支持本地上传csv/xlsx文件，批量输入新闻，并输出新闻分类。

数据来源及数据示例
该项目使用的数据集大部分取至THUCNews，少量通过爬虫从网上爬取获得。

本次训练使用了十个类别的数据。数据分布如下所示：

img

image-20210622161846236

使用方法
注：除了Data_exploration.ipynb文件用jupyter打开之外，其他都在pycharm软件下运行。
数据转换
本软件的输入为类似上面标签-内容的txt文档。请使用前，将其用data_class_handle.py转换。

训练模型
设置好训练集、验证集、保存位置以及词典位置，点击run.Train，即可运行Train.py文件。

测试
1、设置好测试路径，点击run.Test，即可运行。

2、也可以使用Pred.py文件，测试少量新闻。只需将测试文本放入到test_demo列表。

可视化
visualization.py为可视化文件。点击run即可运行。

可执行文件
可执行文件可以输入单条新闻，也可输入多条新闻，若为多条新闻，则每条新闻需要以换行符分开。输入后点击确定即可出现结果。并打印执行时间。

1、输入单条新闻

image-20210711174652781

2、输入多条新闻

image-20210711174906085
