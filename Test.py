# ------------------------------------
# -*- coding = utf-8 -*-
# @Time : 2021/6/14 14:06
# @Author ：chc_stars
# @File : Test.py
# @Software : PyCharm 

# --------------------------------------
from sklearn import metrics
import time
import tensorflow as tf
import os

from Data_Preprocessing import  process_file
from Train import feed_data,get_time_dif,word_to_id,cat_to_id,config,model,categories,evaluate
import numpy as np



# test_dir = os.path.join('E:\CODE\python\新闻分类\\News_Classification\\data\\test.txt')

# save_dir = 'E:\CODE\python/News_Classification\Saved_model/textcnn'
save_path = os.path.join('Saved_model/textcnn/best_validation')  # 最佳验证结果保存路径
def test():
    print("Loading Test Data...")
    start_time = time.time()
    x_test, y_test = process_file(test_dir, word_to_id, cat_to_id, config.seq_length)

    session = tf.Session()
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=save_path)  # 读取保存的模型

    print('Testing...')
    loss_test, acc_test = evaluate(session, x_test, y_test)
    msg = 'Test Loss: {0:>6.2}, Test Acc: {1:>7.2%}'
    print(msg.format(loss_test, acc_test))

    batch_size = 128
    data_len = len(x_test)
    num_batch = int((data_len - 1) / batch_size) + 1

    y_test_cls = np.argmax(y_test, 1)
    y_pred_cls = np.zeros(shape=len(x_test), dtype=np.int32)  # 保存预测结果
    for i in range(num_batch):  # 逐批次处理
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        feed_dict = {
            model.input_x: x_test[start_id:end_id],
            model.keep_prob: 1.0
        }
        y_pred_cls[start_id:end_id] = session.run(model.y_pred_cls, feed_dict=feed_dict)

    # 评估
    print("Precision, Recall and F1-Score...")
    print(metrics.classification_report(y_test_cls, y_pred_cls, target_names=categories))

    # 混淆矩阵
    print("Confusion Matrix...")
    CM = metrics.confusion_matrix(y_test_cls, y_pred_cls)
    print(CM)

    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

if __name__ =='__main__':
    test()