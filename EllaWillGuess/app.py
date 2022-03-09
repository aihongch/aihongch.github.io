from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
       age = request.form['age']
       weight = request.form['weight']
       return render_template('Index.html', result=age)

    return render_template('Index.html')


if __name__ == '__main__':
   app.run()