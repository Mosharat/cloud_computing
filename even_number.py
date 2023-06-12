# Python Program to Print Even Numbers from 1 to N

from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/")

maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        
        if __name__ == "__even_number__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
