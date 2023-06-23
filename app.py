import numpy as np
from flask import Flask,request,jsonify,render_template #request is used for req for home pg, press button, navigate to file// render_template make basic template
import pickle

app=Flask(__name__)
model=pickle.load(open('F:/projects/dataset/model (1).pkl','rb'))



@app.route('/')#route to home page
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering Results in HTML GUI.
    '''
    features=[int(x) for x in request.form.values()]
    # airline=int(features[0])
    rating=int(features[0])
    cabin=int(features[1])
    seat_comfort=int(features[2])
    cabin_service=int(features[3])
    food_and_bev=int(features[4])
    entertainment=int(features[5])
    ground_service=int(features[6])
    value_for_money=int(features[7])
    recommended=int(features[8])
    satisfaction=int(features[9])

    final_features=[]

    # final_features.append(airline)
    final_features.append(rating)
    final_features.append(cabin)
    final_features.append(seat_comfort)
    final_features.append(cabin_service)
    final_features.append(food_and_bev)
    final_features.append(entertainment)
    final_features.append(ground_service)
    final_features.append(value_for_money)
    final_features.append(recommended)
    final_features.append(satisfaction)


    print(len(final_features))

    prediction=model.predict([final_features])
    airline_mapping = {
    0: "Air India",
    1: "Saudi Arabian Airlines",
    2: "Emirates",
    3: "Lufthansa",
    4: "FlyDubai",
    5: "Etihad Airways",
    6: "Qatar Airways",
    7: "AirAsia",
    8: "IndiGo",
    }
    result = airline_mapping[prediction[0]]
    # result=round(prediction[0],0)
    return render_template('index.html',prediction_text='airline recommended is {}'.format(result))

if __name__=="__main__":
    app.run(debug=True)
