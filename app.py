# # from flask import Flask

# # ## WSGI application
# # app = Flask(__name__)

# # @app.route('/')
# # def welcome():
# #     return "Welcome to my first flask app. Thanks. Thank you so much for visiting."


# # @app.route('/members')
# # def members():
# #     return "Welcome to my first flask app. this is the member page."


# # if __name__ == "__main__":
# #     ## debug == True will update any updates saved on python code
# #     app.run(debug = True)




# ## 2nd lecture


# from flask import Flask, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome to my first flask app. Thanks. Thank you so much for visiting."

# @app.route('/success/<int:score>')
# def success(score):
#     return "The person has passed and the score is " + str(score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The person has passed and the score is " + str(score)

# ## result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result = ""
#     if marks < 50:
#         result = 'fail'
#     else:
#         result = 'success'
    
#     # return result
#     return redirect(url_for(result, score = marks))







# if __name__ == "__main__":
#     ## debug == True will update any updates saved on python code
#     app.run(debug = True)



## lec 08/ 09

from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
# camera=cv2.VideoCapture(0)

# def generate_frames():
#     while True:
            
#         ## read the camera frame
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#             ## encode and put to buffer
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()

#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

camera = cv2.VideoCapture(0)


def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index_video.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)