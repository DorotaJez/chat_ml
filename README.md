# Chat ML
Simple Django chat app with Keras toxic messages detection

## About
The idea behind this application was to create a safe and simple environment for the users to exchange messages.
The architecture of the Keras ML model is specified in the "chat_ml/chat/ml_models/ml_model.py" file. For the sake of quick detection, this model has been saved 
to .h5 format.

The repository consists of two directories: "chat_proj", the main project directory, and "chat", the project's app where most of the functionalities are difeined.
Inside "chat_proj", apart from default Django files, there is a "config.py" file which stores the SECRET_KEY set to an empty string.

The application model is based on [Kaggle Custom Dataset for Jigsaw Rate Toxic Comments](https://www.kaggle.com/datasets/renokan/dataset-jigsaw-comments), more precisely the "predict_train_data.csv" dataset. In the project, the .csv file has been prepared with Pandas so that it only constains two columns: one with the comments, later tokenized and padded, and one with their respective binary labels (1 - toxic, 0 - not toxic). The accuracy of the model is around 95/96%.

The model is then loaded by the "test.py" script located in the "chat" folder. This script also opens a json file ("chat_ml/chat/ml_models/word_idx.json") which stores the 500 most common words appearing in the dataset with their respective numerical values; "test.py" contains a function which takes as argument a message, turns it into a sequence of integers using the word index and finally makes a prediction whether the message is toxic or not using the loaded model. This function is referenced in the "consumers.py" file, which is an ASGI equivalent of "views".

In order to work properly, the chat itself is built using Django Channels library, which enables WebSocket connection. The "routing.py" file in the "chat" folder creates connection to the "consumers.py" file.

Another file worth mentioning is the "lookups.py" script located in the same folder. The script contains the UserLookup class, which enables the users to dynamically type and search for users they wish to add to a new group. This functionality was implemented thanks to [ajax_select package](https://django-ajax-selects.readthedocs.io/en/latest/modules.html).


## Setup

In order to run this project on your machine all you need to do after downloading the repository and insalling the required libraries is to generate a Django Secret Key and add it to the "config.py" file as the SECRET_KEY.


## Further development
- Improve the security of accessing the groups
- Improve the layout and interface
