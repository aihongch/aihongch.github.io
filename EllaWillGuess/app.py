from flask import Flask, render_template, request
import  model
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
       age = request.form['age']
       weight = request.form['weight']
       result  = model.load(int(age), int(weight))
       return render_template('Index.html', result=result)

    return render_template('Index.html')


if __name__ == '__main__':
   app.run()