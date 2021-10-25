import flask
import requests


app = flask.Flask(__name__)


def build_url(args):
    base = "https://rule34.xxx/index.php"

    index = 0
    for arg in args:
        value = args.get(arg)

        if index == 0:
            base += "?"
            index = 1
        else:
            base += "&"
        
        base += f"{arg}={value}"

    return base

def get_data(url):
    return requests.get(url).json()


@app.route("/api")
def api():
    data = get_data(build_url(flask.request.args))

    return flask.jsonify(data)


if __name__ == '__main__':
    app.run()