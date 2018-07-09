from flask import  Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    return'<button type="submit">Home</button>'

if __name__ == '__main__':
    app.run()