from flask import Flask
import bb8_utils
from datetime import datetime
from spherov2 import scanner

app = Flask(__name__)

bb8 = scanner.find_toy()

@app.route('/rgbtest')
def rgb_test():
    start = datetime.now()
    bb8_utils.rgb_test(bb8)
    end = datetime.now()
    runtime = end - start
    return "Took %s seconds" % runtime.seconds


@app.route('/drive')
def drive():
    start = datetime.now()
    bb8_utils.head_test(bb8)
    end = datetime.now()
    runtime = end - start
    return "Took %s seconds" % runtime.seconds

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)