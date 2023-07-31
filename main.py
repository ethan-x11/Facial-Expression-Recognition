from flask import Flask, render_template, Response
import cv2
from FER import predictemotion, gen_frames
#Initialize the Flask app
app = Flask(__name__)

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fer')
def fer():
    return Response(predictemotion(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)