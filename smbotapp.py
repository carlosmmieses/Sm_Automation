from flask import Flask, request, render_template

#Iniziacion del objeto app.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cm841164818'
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='167.172.134.145', port='8080', debug=True) 