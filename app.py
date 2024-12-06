from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Shruti Sachan, Roll No.: 2201330100256'

if __name__ == '__main__':
    app.run(port=5002)
