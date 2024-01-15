from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Mayssa Ayachi</p> <p>myFlaskapp</p> <p>version 0 </p> <p>127.0.0.1.5001/ </p> 22.12.2023'

if __name__ == '__main__':
    app.run(debug=True)