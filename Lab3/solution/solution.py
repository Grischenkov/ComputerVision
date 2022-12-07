import cv2

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.applications.imagenet_utils import decode_predictions

class Solution():
    def __init__(self, w, h, model):
        self.__image_w = w
        self.__image_h = h
        self.__prediction = []
        self.__top1_acc = 0
        self.__top5_acc = 0
        try:
            tf.config.experimental.reset_memory_stats('GPU:0')
            self.__memory = tf.config.experimental.get_memory_info('GPU:0')['current'] / (1024 ** 3)
        except:
            self.__memory = 'No GPU available!'
        self.__model = model
        self.__x = []
        self.__y = []

    def load_source_files(self):
        df = pd.read_csv('data/data.csv', sep=';')
        images = []
        for i in range(len(df)):
            images.append(cv2.resize(cv2.imread(f"data/{df['class'][i]}/{df['image'][i]}"), (self.__image_w, self.__image_h)))
        self.__x = np.array(images)
        self.__y = np.array(df['class'].values)

    def process(self):
        self.__prediction = decode_predictions(self.__model.predict(self.__x))
        self.__top1_acc = self.__get_topK_acc(1)
        self.__top5_acc = self.__get_topK_acc(5)
        if self.__memory != 'No GPU available!':
            self.__memory = tf.config.experimental.get_memory_info('GPU:0')['peak'] / (1024 ** 3)
    
    def describe(self):
        return f"   Top-1 accuracy: {self.__top1_acc}\n   Top-5 accuracy: {self.__top5_acc}\n    Memory usage: {self.__memory} gb"

    def __get_topK_acc(self, k):
        acc = 0.0
        for i in range(len(self.__prediction)):
            if np.isin(self.__y[i], self.__prediction[i][:k]):
                acc += 1
        acc /= len(self.__prediction)
        return acc