##flask  --- pip install flask 

from flask import Flask, render_template, request,url_for
import pickle,joblib
import numpy as np 

model = joblib.load(open("spam_model.lb","rb"))
vectorizer = joblib.load(open("vectorizer.lb","rb"))


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method =="POST":
            message = request.form['message']
            transformed = vectorizer.transform([message])
            transformed_data = transformed.toarray()
            prediction = model.predict(transformed_data)
            output = prediction[0]
            return render_template('result.html',prediction=output)
    except Exception as e:
        return render_template('result.html',prediction = e)




if __name__ == '__main__':
    app.run(debug=True,host ="0.0.0.0",port=8080  )