from flask import Flask, render_template,escape,request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def home():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)