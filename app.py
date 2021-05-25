from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Guys!"


@app.route("/webhook")
def webhook():
    return 'OK'
    
if __name__ == "__main__":
    app.run()