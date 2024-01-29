from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a la página de inicio by: Ivan Ertel Ramirez'
 
@app.route('/about')
def about():
    return 'Esta es la página acerca de nosotros :)'

if __name__ == '__main__':
    app.run(debug=True)