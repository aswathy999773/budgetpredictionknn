from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =61
batch_size = 50
epochs = 20
#------------------------------
import os, cv2, keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2


# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, LSTM
from sklearn.neighbors import KNeighborsClassifier

import os,cv2,keras

def read_dataset(path):
    data_list = []
    label_list = []
    i=-1
    my_list = os.listdir(r'C:\Users\Dell\PycharmProjects\Malayalam Sign Language\src\static\image_data')
    for pa in my_list:
        i=i+1
        print(pa,"==================")
        for root, dirs, files in os.walk(r'C:\Users\Dell\PycharmProjects\Malayalam Sign Language\src\static\image_data\\' + pa):

         for f in files:
            file_path = os.path.join(r'C:\Users\Dell\PycharmProjects\Malayalam Sign Language\src\static\image_data\\'+pa, f)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            data_list.append(res)

            label = i
            label_list.append(label)
            # label_list.remove("./training")
        # if i==6:
        #     break
    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))
def read_dataset1(path):
    data_list = []
    label_list = []

    file_p=ath = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

from sklearn.model_selection import train_test_split
# Define CNN model
x_dataset, y_dataset = read_dataset(r"")
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)

model = Sequential()

# 1st convolution layer
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))

# 2nd convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

# 3rd convolution layer
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

model.add(Flatten())

# fully connected neural networks
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))
# ------------------------------
# batch process

# Define KNN algorithm
knn = KNeighborsClassifier(n_neighbors=61)

# Define LSTM model
lstm_model = Sequential()
lstm_model.add(LSTM(128, input_shape=( 61,128), return_sequences=True))
lstm_model.add(LSTM(64))
lstm_model.add(Dense(61, activation='softmax'))
lstm_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# # load dataset
#
y_train1=[]
for i in y_train:
    emotion = keras.utils.to_categorical(i, 61)
    y_train1.append(emotion)

y_train=y_train1
x_train = np.array(X_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(X_test, 'float32')
y_test = np.array(y_test, 'float32')

x_train /= 255  # normalize inputs between [0, 1]
x_test /= 255

print("x_train.shape",x_train.shape)
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
x_train = x_train.astype('float32')
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
x_test = x_test.astype('float32')

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

print(x_train.shape)

gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

# ------------------------------

model.compile(loss='categorical_crossentropy'
              , optimizer=keras.optimizers.Adam()
              , metrics=['accuracy']
              )


if not os.path.exists("model_21.h5"):

    model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
    model.save("model_21.h5")  # train for randomly selected one
else:
    model = load_model("model_21.h5")  # load weights






# # Extract features from image data using CNN model
features = model.predict(x_train)

print(len(features),features[0],"======================")

# Train KNN algorithm on extracted features
knn.fit(features, y_train.argmax(axis=1))

# Use KNN to find similar images
similar_images = knn.kneighbors(features)
#
#
#
#
print(len(similar_images))
print(len(features))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(similar_images[0])
similar_images=np.asarray(similar_images)
# Use LSTM to analyze sequence of images, using KNN results for context
x_train_lstm = np.random.rand(9760, 61, 128)
print(len(similar_images))
print(len(y_train))
features1=[]
for i in features:
    features1.append([i])
features1=np.asarray(features1)
lstm_model.fit(x_train_lstm, similar_images[0],epochs=30)
# lstm_model.fit(features1, y_train,epochs=2)
# lstm_model.save("hybrid_model.h5")
def predict_hy(fn):
    lstm_model=load_model("hybrid_model.h5")
    dataset=read_dataset1(fn)

    (mnist_row, mnist_col, mnist_color) = 48, 48, 1

    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    dataset=dataset/255
    r=model.predict(dataset)

    r=[r[0]]
    r=np.asarray([r])
    print(r)
    try:
        rr=lstm_model.predict(r)
    except:
        pass
    print(r[0][0])
    a_list=list(r[0][0])
    max_value = max(a_list)
    max_index = a_list.index(max_value)
    print(max_value)
    print(max_index)
    return max_index

print(predict_hy(r"C:\Users\Dell\PycharmProjects\Malayalam Sign Language\src\static\image_data\Ya\3.jpg"))