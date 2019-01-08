#testing something



from flask import Flask, request, redirect
import requests

app = Flask(__name__)




@app.route("/")
def hello():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:       #no reasonidk what that .-.
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR'])


    return "hi ho he"

if __name__ == "__main__":
    app.run()
