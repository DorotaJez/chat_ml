import keras
import json

# Loading the saved model
model = keras.models.load_model('saved_model.h5')

# Opening the 500 most common words saved as a json object
with open('chat/ml_models/word_idx.json', 'r') as file:
  word_idx = json.load(file)

def get_prediction(message):
    '''Returns a value from 0 (not toxic at all) to 1 (very toxic)'''
    mess_list = message.split()
    tokenized_list = [0] * 500

    for x in range(len(mess_list)):
        if mess_list[x] in word_idx.keys():
            tokenized_list[x] = word_idx[mess_list[x]]
    
    return model.predict([tokenized_list])
