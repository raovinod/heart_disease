
 
import numpy as np
import pickle
import streamlit  as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Admin/Downloads/trained_model.sav','rb'))

#creating a function for prediction

def heart_prdiction(input_data):
   
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The Person does not have a Heart Disease'
    else:
      return'The Person has Heart Disease'
      
      
      
def main():
    #giving a title
    st.title('Heart Disease prediction Web App')
    
    st.image("heart.jpg")
    
    #getting the input data from the user
    age=st.number_input('Enter the Age of the person')
    sex_list=['','0','1']
    sex =st.selectbox('select gender',sex_list)
    cp_list=['','0','1','2','3']
    cp=st.selectbox('Range of chest pain',cp_list)
    trestbps=st.number_input('Enter the Blood pressure')
    chol=st.number_input('Enter the cholestrol value')
    fbs_list=['','0','1']
    fbs=st.selectbox('Enter the Fbs value',fbs_list)
    restecg_list=['','0','1']
    restecg=st.selectbox('Enter the Restecg value',restecg_list)
    thalach=st.number_input('Enter the Thalach value')
    exang_list=['',0,1]
    exang=st.selectbox('Enter the Exang value',exang_list)
    oldpeak=st.number_input('Enter the Oldpeak value')
    slope_list=['','0','1','2']
    slope=st.selectbox('Enter the Slope value',slope_list)
    ca_list=['','0','1','2','3']
    ca=st.selectbox('Enter the ca value',ca_list)
    thal_list=['','1','2','3']
    thal=st.selectbox('Enter the Thal value',thal_list)
    
    
    #code for prediction
    predicter = ''
    
    #creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        predicter=heart_prdiction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(predicter)
    
    
if __name__ == '__main__':
    main()
        
        
    
    
    
    