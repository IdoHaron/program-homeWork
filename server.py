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
video = cv2.VideoCapture("MovieSPR.mp4")
isStreaming = False
#endregion


@app.route("/")
@app.route("/home")
def RenderIndex():
    return render_template("index.html")

@socketio.on("connected")
def connected():
    global isStreaming
    print("connected")
    ##emit("Ap-connection", {'msg': "succefuly connected"})
    if(isStreaming== True):
        return None
    isStreaming = True
    isFrame, frame = video.read()
    while isFrame:
        cv2.imwrite("Current_frame.png", frame)        
            ##emit("frame", {'frame': frame}, broadcast= True);
        cv2.waitKey(60)
        with open("Current_frame.png", "rb") as Cframe:
            emit("Frame", {'frame':(Cframe.read())}, broadcast=True)
        isFrame, frame = video.read()
    isStreaming = False

@socketio.on("Polygon")
def Send_Polygon(Poly):
    emit("draw_poly", {'Poly': Poly}, broadcast = True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

#region functions

#endregion