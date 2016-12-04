from flask import Flask
import file

app = Flask(__name__)


@app.route("/")
def index():
    return "<br/>".join(file.File.tail('alarm.log', 10))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
