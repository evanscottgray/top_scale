import serial                                                                   
import top_scale as scl                                                         
from flask import Flask
from flask import jsonify
app = Flask(__name__)

scale_port = serial.Serial('/dev/ttyUSB0')
scale = scl.Scale(scale_port)

@app.route("/reading")
def get_reading():
    r = scale.reading()
    return jsonify({'reading': r}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
