import streamlit as st
import pickle
import time

st.title('IMDB Sentiment Analysis')
model=pickle.load(open('C:/Users/JAMES/Documents/projects/streamlit\IMDB/model1.pkl','rb'))
review=st.text_input('Enter the review')
result=st.button('predict')
if result:
  start=time.time()
  prediction=model.predict([review])
  end=time.time()
  st.write(f'Time taken to predict: {end-start}')
  if prediction[0]==0:
    st.write('Negative')
  else:
    st.write('Positive')
