from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
from sklearn import preprocessing
app = Flask('__name__')
model=pickle.load(open('MERISkill.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')
def predict_api(feature):
    '''
    
    '''
    feature=[float(x) for x in request.form.values()]
    
    asarray=np.asarray(feature).reshape (1,-1)
    prediction=model.predict(asarray)
    # data = request.get_json(force=True)
    # prediction = model.predict([np.array(list(feature.values()))])
    
    return prediction[0]



@app.route('/predict',methods=["POST"])


def predict():
    if request.method == 'POST':
        feature= request.form.to_dict()
        feature=list(feature.values())
        feature=list(map(float, feature))
        predict=predict_api(feature)

        if  float (predict)==1:
            prediction ='positive'
            # print( 'RESULT: POSITIVE')
        else:
            # print(' RESULT: NEGATIVE')
            prediction = 'negative'
        return render_template('predict.html',prediction = prediction)  
  
    

    

if(__name__=='__main__'):
    app.run(debug=True)
