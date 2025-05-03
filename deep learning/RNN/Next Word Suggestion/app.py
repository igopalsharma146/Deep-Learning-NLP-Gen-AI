import streamlit as st
import numpy as np 
import pickle 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

##load model 
model = load_model('your_saved_model_name.h5')

##load tokenzier 
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

##function to predict next word 
def predict_next_word(model,tokenizer,text,max_seq):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_seq:
        token_list = token_list[-(max_seq-1):]
    token_list = pad_sequences([token_list],
                               maxlen = max_seq-1,
                               padding = "pre")
    predicted = model.predict(token_list,verbose=0)
    predicted_word_index = np.argmax(predicted,axis = 1)
    for word , index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

##streamlit app
st.title("project tiltle")
input_text = st.text_input("Input Text")
if st.button("Predict"):
    max_seq_len = model.input_shape[1] + 1
    next_word = predict_next_word(model,
                                  tokenizer,
                                  input_text,
                                  max_seq_len)
    st.write(next_word)