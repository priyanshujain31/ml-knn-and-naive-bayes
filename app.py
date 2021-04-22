import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('Knearestneighborclassifier.pkl', 'rb'))
model_naive = pickle.load(open('naivebayesclassifier.pkl', 'rb'))
dataset= pd.read_csv('https://raw.githubusercontent.com/umangkejriwal1122/Machine-Learning/master/Data%20Sets/titanic.csv')
X=dataset[["Age","SibSp","Parch","Fare","Pclass"]]
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
def predict_note_authentication(Age,SibSp,Parch,Fare,Pclass):
 output= model.predict(sc.transform([[Age,SibSp,Parch,Fare,Pclass]]))
 print("Passenger will die =", output)
 if output==[1]:
   prediction="Passanger will survive"
 else:
   prediction="Passanger will die"
 print(prediction)
 return prediction

def predict_naive(Age,SibSp,Parch,Fare,Pclass):
 output= model_naive.predict(sc.transform([[Age,SibSp,Parch,Fare,Pclass]]))
 print("Passenger will die =", output)
 if output==[1]:
   prediction="Passanger will survive"
 else:
   prediction="Passanger will die"
 print(prediction)
 return prediction


def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Passenger Survived Prediction using K nearest neighbor And Naive Bayes")
   
    
    Age = st.number_input('Insert a Age',18,60)
    SibSp = st.number_input('Insert a SibSp',0,10)
    Parch = st.number_input('Insert a Parch',1,10)
    Pclass = st.number_input('Insert a Pclass',1,4)
   
    Fare = st.number_input("Insert Fare",1,15000)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(Age,SibSp,Parch,Fare,Pclass)
      st.success('Model has predicted {}'.format(result))
    if st.button("Naive Bayes Predict"):
      result=predict_naive(Age,SibSp,Parch,Fare,Pclass)
      st.success('Model has predicted {}'.format(result))
      
    if st.button("About"):
      st.subheader("Developed by Priyanshu Jain")
      st.subheader("Department of Computer Engineering")

if __name__=='__main__':
  main()
