#region setup
#region imports
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit
import cv2
#endregion

app = Flask(__name__)
socketio = SocketIO(app)
#endregion


#region variables
video = cv2.VideoCapture("MovieSPR.mp4");
#endregion


@app.route("/")
@app.route("/home")
def RenderIndex():
    return render_template("index.html")

@socketio.on("connected")
def connected():
    print("connected")
    ##emit("Ap-connection", {'msg': "succefuly connected"})
    isFrame, frame = video.read()
    while isFrame:
        try:
            cv2.imwrite("Current_frame.png", frame)        
            ##emit("frame", {'frame': frame}, broadcast= True);
            cv2.waitKey(10)
            with open("Current_frame.png", "rb") as Cframe:
                emit("Frame", {'frame':(Cframe.read())}, broadcast=True)
        except:
            pass
        isFrame, frame = video.read()

if __name__ == '__main__':
    socketio.run(app, debug=True)

#region functions

#endregion