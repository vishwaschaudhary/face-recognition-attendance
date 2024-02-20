from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)#this will access our camera

def generate_frames():
    while True:
        success,frame=camera.read() #success is a boolean variable telling if we are able to read the camera of not
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

    


@app.route("/")
def home_page():
    return render_template('home.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame') #this generate_frames will be taking frames from my webcam and pass it to the html page

if __name__=="__main__":
    app.run(debug=True)