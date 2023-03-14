# coding: utf-8
# ------------------------------------
# -*- coding = utf-8 -*-
# @Time : 2021/6/14 18:30
# @Author ：chc_stars
# @File : visualization.py
# @Software : PyCharm

# --------------------------------------
from __future__ import print_function

import os
import time

import tensorflow as tf
import tensorflow.contrib.keras as kr


from Train import get_time_dif

from Cnn_model import TCNNConfig, TextCNN
from Data_Preprocessing import read_category, read_vocab



# vocab_dir = os.path.join('E:\CODE\python/新闻分类/News_Classification\data/vocab.txt')
# vocab_dir = os.path.join('E:\\CODE\python\\PycharmProjects\\新闻分类\\News_Classification\\data/vocab.txt')
vocab_dir = os.path.join('data/vocab.txt')

# save_dir = 'Saved_model/textcnn'
save_path = os.path.join('Saved_model/textcnn/best_validation')  # 最佳验证结果保存路径


class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)  # 读取保存的模型

    def predict(self, message):

        content = message
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]

        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }

        y_pred_cls = self.session.run(self.model.y_pred_cls, feed_dict=feed_dict)
        return self.categories[y_pred_cls[0]]


if __name__ == '__main__':
    tf.reset_default_graph()
    start_time = time.time()
    cnn_model = CnnModel()
    test_demo = ['今年高考非常难',
                 '麻婆豆腐很好吃']
    for i in test_demo:
        print(cnn_model.predict(i))
    time_dif = get_time_dif(start_time)
    print(time_dif)
