import joblib
import streamlit as st


classifier = joblib.load('C:/Users/sesha/Downloads/CKD_Model.joblib')

@st.cache_data()

def prediction(age,bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, rbc_normal, pc_normal, pcc_present, ba_present, htn_yes, dm_yes, cad_yes, appet_poor, pe_ye, ane_yes):
  prediction = classifier(age,bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, rbc_normal, pc_normal. pcc_present, ba_present, htn_yes, dm_yes, cad_yes, appet_poor, pe_ye, ane_yes)
  return prediction

def main():
    html_temp = '''<div style = 'background-color:tomato;padding:10px'>
    <h2 style = 'color:white;text-align:center;'>Chronic Kidney Disease Prediction</h2>
    </div>'''
    st.title('Chronic Kidney Disease Prediction')
    start_new = True
    # while start_new == True:
      # ask_next_param = False     
    age = st.number_input('Enter age: ')
    bp = st.number_input('Enter blood pressure: ')
    sg = st.number_input('Enter specific gravity: ')
    al = st.number_input('Enter albumin level: ')
    su = st.number_input('Enter sugar level: ')
    bgr = st.number_input('Enter blood glucose random: ')
    bu = st.number_input('Enter blood urea: ')
    sc = st.number_input('Enter serum creatinine: ')
    sod = st.number_input('Enter sodium level: ')
    hemo = st.number_input('Enter hemoglobin level: ')
    pot = st.number_input('Enter potasium level: ')
    pcv = st.number_input('Enter packed cell volume: ')
    wc = st.number_input('Enter white blood cell count: ')
    rc = st.number_input('Enter red blood cell count: ')
    rbc = ['abnormal', 'normal'].index(st.radio('RBC', ['normal', 'abnormal']))
    pc = ['abnormal', 'normal'].index(st.radio('Pus Cell', ['normal', 'abnormal']))
    pcc = ['notpresent', 'present'].index(st.radio('Pus Cell CLumps', ['present', 'notpresent']))
    ba = ['notpresent', 'present'].index(st.radio('Bacteria', ['present', 'notpresent']))
    htn = ['no', 'yes'].index(st.radio('Hypertension', ['yes', 'no']))
    dm = ['no', 'yes'].index(st.radio('Diabetes Mellitus', ['yes', 'no']))
    cad = ['no', 'yes'].index(st.radio('Coronary Artery Disease', ['yes', 'no']))
    appet = ['good', 'poor'].index(st.radio('Appetitte', ['poor', 'good']))
    pe = ['no', 'yes'].index(st.radio('Pedal Edema', ['yes', 'no']))
    ane = ['no', 'yes'].index(st.radio('Anaemia', ['yes', 'no']))
      
    if st.button('Predict for Chronic Kidney Disease'):
        prediction = classifier.predict([[age,bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, rbc, pc, pcc, ba, htn, dm, cad, appet, pe, ane]])
        st.text(f'Prediction for CKD: {bool(prediction[0])}')
        start_new = False
          
    

if __name__=='__main__':
  main()


