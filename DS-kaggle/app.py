# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

model = pickle.load(open('knn_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
       gender=(request.form['gender'])
       if gender=='M':
          gender=1
       else:
          gender=0
       ssc_p=float(request.form['ssc_p'])
       ssc_b=(request.form['ssc_b'])
       if ssc_b=='Central':
           ssc_b=0
       else:
           ssc_b=1
       hsc_p=float(request.form['hsc_p'])
       hsc_b=(request.form['ssc_b'])
       if hsc_b=='Central':
           hsc_b=0
       else:
           hsc_b=1
       hsc_s=(request.form['hsc_s'])
       if hsc_s=='Commerce':
           hsc_s=1
       elif(hsc_s=='Science'):
           hsc_s=2
       else:
           hsc_s=0
       degree_p=float(request.form['degree_p'])
       degree_t=(request.form['degree_t'])
       if degree_t=='Sci&Tech':
           degree_t=2
       elif(degree_t=='Comm&Mgmt'):
           degree_t=0
       else:
           degree_t=1
       workex=(request.form['workex'])
       if workex=='No':
           workex=0
       else:
           workex=1
       etest_p=float(request.form['etest_p'])
       specialisation=(request.form['specialisation'])
       if specialisation=='Mkt&HR':
           specialisation=1
       else:
           specialisation=0
       mba_p=float(request.form['mba_p'])
       
           
       prediction=model.predict([[gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p]])
       if prediction==0:
           return render_template('index.html',prediction_texts='Sorry, Not Placed')
       else:   
           return render_template('index.html',prediction_texts='Placed')
      
    else:
        return render_template('index.html')
       
        
if __name__=="__main__":
    app.run(debug=True)
        
        
            