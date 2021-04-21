from flask import Flask, render_template, request
import utils

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/predict", methods = ['POST', 'GET'])    
def predict():

    print('antes')
    data = request.form.get('name[]')
    print('depois')
    print(data)
    data_tokenizer = utils.preprocess(data)
    print(data_tokenizer)
    model = utils.loadmodel()
    print(model)
    result = utils.predict(model, data_tokenizer)
    print(result)
    if result == 'Positive':
        resultBool = True
    else:
        resultBool = False
    
    print(resultBool)

    return render_template('index.html', prediction_text= result, modal = resultBool)

if __name__ == "__main__":
    app.run()















