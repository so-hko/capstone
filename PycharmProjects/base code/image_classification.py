# -*- coding:utf-8 -*-

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from util import load_Fashion_MNIST, draw_result, visualization


class ModelMgr():
    def __init__(self, target_class=10, data_number = 100):
        self.target_class = target_class

        print('\n load dataset ...')
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = load_Fashion_MNIST(100)

    def train(self):
        print('\n train start ...')

        # model = self.get_my_model()  ## 모델 로드하는 부분입니다.
        model = self.get_sample_model()  ## 샘플 모델입니다.

        hp = self.get_hyperparameter()  ## 파라미터 로드하는 부분입니다.

        model.summary()  ## 모델 구조 출력하는 부분입니다.

        print('*****************')
        print('\tbatch size :', hp['batch_size'])
        print('\tepochs :', hp['epochs'])
        print('\toptimizer :', hp['optimizer'])
        print('\tlearning rate :', hp['learning_rate'])
        print('*****************')

        ## 모델의 손실 함수 및 최적화 알고리즘 설정하는 부분입니다.
        model.compile(optimizer=hp['optimizer'], loss='categorical_crossentropy', metrics=['accuracy'])

        if hp['epochs'] > 100:  ## epochs 최대 100으로 설정합니다.
            hp['epochs'] = 100

        history = model.fit(self.train_images, self.train_labels,
                            batch_size=hp['batch_size'], epochs=hp['epochs'], verbose=2,
                            validation_split=0.4)

        self.model = model
        self.history = history
        history.history['hypers'] = hp

    def get_hyperparameter(self):
        ########################
        # (1) 수정할 부분 입니다.   #
        # 파라미터 값들을 수정해 주세요.#
        #######################
        hyper = dict()
        hyper['batch_size'] = 32  ## 배치 사이즈 설정하는 부분 입니다.
        hyper['epochs'] = 20  ## 에폭을 설정하는 부분 입니다.
        hyper['learning_rate'] = 0.01  ## 학습률을 설정하는 부분입니다.
        hyper['optimizer'] = keras.optimizers.Adam(learning_rate=hyper['learning_rate'])  ## default: SGD
        return hyper

    def get_sample_model(self):
        ## 샘플 모델 입니다.
        ## 모델 구현시 참고하세요.
        model = tf.keras.models.Sequential()
        model.add(keras.layers.Dense(128, input_shape=(784,), name='dense_layer', activation='relu'))
        model.add(keras.layers.Dropout(0.3))
        model.add(keras.layers.Dense(128, name='dense_layer_2', activation='relu'))
        model.add(keras.layers.Dropout(0.3))
        model.add(keras.layers.Dense(self.target_class, name='dense_layer_3', activation='softmax'))
        return model

    def get_my_model(self):
        #######################
        # (2) 수정할 부분 입니다.   #
        #  모델 코드를 완성해 주세요. #
        #######################
        model = tf.keras.models.Sequential()
        '''
        주의사항
        1. 모델의 입력 데이터 크기는 (batch_size, 784) 
           출력 데이터 크기는 (batch_size, 10)
        2. out of memory 오류 시,
            메모리 부족에 의한 오류임.
            batch_size를 줄이거나, 모델 구조의 파라미터(ex. 유닛수)를 줄여야함
        3. BatchNormalization() 사용 금지

        기타 문의 : wodbs9522@gmail.com (수업조교)
        '''
        return model

    def test(self, model=None):
        print('\ntest model')
        if model is None:
            model = self.model
        test_loss, test_acc = self.model.evaluate(self.test_images, self.test_labels)
        train_loss, train_acc = self.model.evaluate(self.train_images, self.train_labels)
        print('test dataset result : ', test_acc)
        print('train dataset result : ', train_acc)

    def visualization_result(self, file_path='saves/result_visualization.png'):
        ## 이미지 데이터에 대해 예측값/정답을 함께 이미지로 저장해 주는 함수입니다.
        predictions = self.model.predict(self.test_images)
        visualization(predictions, self.test_images, self.test_labels, file_path=file_path)

    def draw_history_graph(self, file_path='saves/result.png'):
        ## 학습 데이터에 대한 정확도, 손실값을 그래프(이미지)로 저장해 주는 함수입니다.
        print('\nvisualize results : \"{}\"'.format(file_path))
        draw_result(self.history.history, file_path=file_path)

    def load_model(self, model_path='saves/model.h5'):
        print('\nload model : \"{}\"'.format(model_path))
        self.model = tf.keras.models.load_model(model_path)

    def save_model(self, model_path='saves/model.h5'):
        print('\nsave model : \"{}\"'.format(model_path))
        self.model.save(model_path)


if __name__ == '__main__':
    trained_model = None
    # trained_model = 'saves/model.h5'  ## 학습된 모델 테스트 시 사용해 주시면 됩니다.

    modelMgr = ModelMgr(data_number=100)
    if trained_model is None:
        modelMgr.train()  ## 모델 학습 시작
        modelMgr.save_model()  ## 학습 모델 저장 (saves/model.h5)
        modelMgr.test()  ## 학습 모델 테스트
        modelMgr.visualization_result()  ## 학습 결과 그래프 저장 (saves/result_visualization.png)
        modelMgr.draw_history_graph()  ## 학습 결과 그래프 저장 (saves/result.png)
    else:
        modelMgr.load_model(trained_model)
        modelMgr.test()
