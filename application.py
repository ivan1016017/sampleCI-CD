from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return "Hello World from Flask Hello Page.<b> v1.0"

@application.route("/help")
def helppage():
    return "Hello World from Flask Hello Page.<b> v1.0"

@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------
