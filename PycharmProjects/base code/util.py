import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf
import numpy as np

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def load_Fashion_MNIST(data_number=100):
    ## Fashion MNIST 데이터셋을 불러옵니다.
    fashion_mnist = keras.datasets.fashion_mnist
    ## 불러온 데이터에서 Train, Test 데이터셋을 각각 나눠줍니다.
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    train_images, train_labels = train_images[:data_number], train_labels[:data_number]
    #test_images, test_labels = test_images[:1000], test_labels[:1000]
    ## 데이터셋의 분석을 위한 시각화 부분입니다.
    ## 모델 학습을 하기 전에, 데이터셋이 어떻게 구성되어있는지 확인해보시길 바랍니다.
    '''
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()
    '''

    ## 모델에 넣기 위해 입력 데이터를 [28x28]에서 [784]로 변경
    ## 변경 전 : train_images = [60000, 28, 28], test_images = [10000, 28, 28]
    ## 변경 후 : train_images = [60000, 784], test_images = [10000, 784]
    train_images = train_images.reshape(len(train_images), 784)
    test_images = test_images.reshape(len(test_images), 784)
    train_images = train_images.astype('float32')
    test_images = test_images.astype('float32')
    train_images, test_images = train_images / 255.0, test_images / 255.0

    ## 데이터의 라벨들을 one-hot 벡터로 바꿔줍니다.
    ## 변경 전 : [3, 1, ...]
    ## 변경 후 : [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], ...]
    train_labels = tf.keras.utils.to_categorical(train_labels, 10)
    test_labels = tf.keras.utils.to_categorical(test_labels, 10)


    return (train_images, train_labels), (test_images, test_labels)

def draw_result(logs, file_path='./result.png'):
    test_label = 'Val'
    y_vloss = logs['val_loss']
    y_loss = logs['loss']
    y_vacc = logs['val_accuracy']
    y_acc = logs['accuracy']
    x_len = np.arange(len(y_loss))
    fig = plt.figure(figsize=(12, 5))
    title = 'Training Result Graph'
    if 'hypers' in logs:
        title = ''
        for k, v in logs['hypers'].items():
            if k == 'optimizer':
                title += k + ':' + str(v.__class__.__name__) + '   '
            else:
                title += k + ':' + str(v) + '   '
    fig.suptitle(title)
    plt.rcParams['figure.constrained_layout.use'] = True
    plt.subplot(121)
    plt.title('Train/' + test_label + ' Loss')
    plt.plot(x_len, y_vloss, marker='.', c='red', label=test_label + "-set Loss")
    plt.plot(x_len, y_loss, marker='.', c='blue', label="Train-set Loss")
    plt.xlim(left=-1)
    plt.xticks(x_len.tolist(), (x_len + 1).tolist())
    plt.ylim(bottom=0, top=1.5)
    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    idx = np.argmin(y_vloss)
    v = np.min(y_vloss)
    plt.annotate('min:' + str(v)[:5], xy=(idx, v), xytext=(idx, v + 0.15),
                 arrowprops=dict(arrowstyle="->", facecolor='black'), fontsize=10, )
    plt.subplot(122)
    plt.title('Train/' + test_label + ' Accuracy')
    plt.plot(x_len, y_vacc, marker='.', c='red', label=test_label + "-set Accuracy")
    plt.plot(x_len, y_acc, marker='.', c='blue', label="Train-set Accuracy")
    plt.xlim(left=-1)
    plt.xticks(x_len.tolist(), (x_len + 1).tolist())
    plt.ylim(bottom=0, top=1)
    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('Accuracy')
    idx = np.argmax(y_vacc)
    v = np.max(y_vacc)
    plt.annotate('max:' + str(v * 100)[:5] + '%', xy=(idx, v), xytext=(idx, v + 0.1),
                 arrowprops=dict(arrowstyle="->", facecolor='black'), fontsize=10, )
    plt.savefig(fname=file_path)
    plt.clf()

def visualization(predictions, test_images, test_labels, file_path='saves/result_visualization.png'):
    prediction_sample = tf.argmax(predictions[:10], 1)
    target = tf.argmax(test_labels[:10], 1)
    plt.figure(figsize=(10, 5))
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)
        plt.xlabel('{}/{}'.format(class_names[prediction_sample[i]], class_names[target[i]]))
    plt.savefig(fname=file_path)
    plt.clf()
