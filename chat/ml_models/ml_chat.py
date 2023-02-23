import tensorflow as tf
import pandas as pd
import numpy as np
import keras
import matplotlib.pyplot as plt
from keras.layers import Embedding, GlobalAveragePooling1D, Dense
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.utils import pad_sequences
from keras.models import Sequential
import json

# nltk.download('punkt')

raw_df = pd.read_csv('bad_words_archive/predict_train_data.csv')

# Getting rid of float64 columns (we only need binary values)
df = raw_df.drop(columns=['toxicity', 'severe_toxicity', 'obscene', 'threat','insult','identity_attack','id','index'])

# Creating a "rated" column containing ones (for the texts rated "one" in at least one of the label columns) and zeroes
labels = ['toxic','severe_toxic','-obscene-','-threat-','-insult-','identity_hate']

def rated(row):
    for label in labels:
        if row[label] > 0:
            return 1
    return 0

df['rated'] = df.apply(rated, axis=1)

# We will only work on the "rated" column so we can dismiss the other labels
df = df.drop(columns=labels)

# How many texts were rated insulting, toxic, obscene etc.
# rated_1 = len(df[df['rated']==1])
# rated_0 = len(df[df['rated']==0])
# print(rated_1, rated_0)

# Plotting the lengths of the texts in the df
# len_dict = {}
# for length in lengths:
#     if length not in len_dict.keys():
#         len_count = lengths.count(length)
#         len_dict[length] = len_count

# for length in range(5001):
#     if length not in len_dict.keys():
#         len_dict[length] = 0
# plt.bar(x=len_dict.keys(), height=len_dict.values())

# Dividing the dataframe into texts (X) and their binary labels (y)
X=df['text']
y=df['rated']

# Assuring that all texts in the df are strings
def stringify(x):
    try:
        return str(x)
    except:
        return('Cannot convert {} into string'.format(x))
    
X = X.map(stringify)

# Shuffling and splitting df into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5, shuffle=True)

# Converting "text" series to lists, "rated" series to numpy arrays
X_train=X_train.tolist()
X_test=X_test.tolist()
y_train = np.array(y_train)
y_test = np.array(y_test)

# Constants used in building the model
num_words = 50000
max_len = 500

# Creating tokenizer object and word index
tokenizer = Tokenizer(num_words=num_words, oov_token='<OOV>',)
tokenizer.fit_on_texts(X_train)
word_idx = tokenizer.word_index

# Saving the word index
# with open('chat\ml_models\word_idx.json', 'w') as file:
#     json.dump(word_idx, file)

# Tokenizing and padding the texts
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)
X_train_pad = pad_sequences(X_train, maxlen=max_len, truncating='post', padding='post')
X_test_pad = pad_sequences(X_test, maxlen=max_len, truncating='post', padding='post')

# Constructing the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(num_words,16,input_length=max_len),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')])


# Compiling the model 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fitting the model
hist = model.fit(X_train_pad, y_train, epochs=5, validation_data=(X_test_pad, y_test))

# Saving the model to be used in 'test.py' script
model.save('saved_model.h5')
