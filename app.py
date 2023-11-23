from flask import Flask
import bb8_utils


app = Flask(__name__)
bb8 = BB8_driver.Sphero() 

@app.route('/rgbtest')
def rgb_test(bb8):
    bb8_utils.rgb_test()
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)