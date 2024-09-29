# Face Detection using Flask and OpenCV

This repository contains a Flask-based web application that performs face and eye detection using OpenCV's Haar Cascade classifiers. The application streams live video from the camera to a web interface hosted on `localhost`, where face and eye detection is performed in real-time.

## Features
- Real-time face detection using OpenCV.
- Eye detection integrated with face detection.
- Flask-based web server that streams live video feed.
- Utilizes Haar Cascade classifiers for face and eye detection.

## Technologies Used
- **Flask**: Lightweight web framework for hosting the application.
- **OpenCV**: For face and eye detection using Haar Cascade.
- **Haar Cascade Classifiers**: Pre-trained models for object detection provided by OpenCV.

## Getting Started

### Prerequisites
- Python 3.x
- OpenCV
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/face_detection_flask-opencv.git
   cd face_detection_flask-opencv

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt

### Running the Application
1. Run the Flask application:
   ```bash
   python app.py
2. Open your browser and go to http://127.0.0.1:5000/ to see the live video feed with face and eye detection.

### How it Works
- The application captures video feed from your device's camera.
- The live feed is processed using OpenCV to detect faces and eyes in real-time.
- The processed frames are then projected to the web interface, displaying the detected faces and eyes.

### Haar Cascade Files
The application uses the following Haar Cascade classifiers for detection:
- haarcascade_frontalface_default.xml: For face detection.
- haarcascade_eye.xml: For eye detection.
These files are provided by OpenCV and can be downloaded or referenced in the repository.

### License
This project is licensed under the MIT License.

### Acknowledgments
- OpenCV documentation: https://opencv.org/
- Flask documentation: https://flask.palletsprojects.com/
- Haar Cascade Classifiers: https://github.com/opencv/opencv/tree/master/data/haarcascades


