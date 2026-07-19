# Deployment of YOLO object detecting Flask. In this project we utilize a simple Flask web application for deploying a trained YOLOv8 object detection model. 

## The model was trained to identify two object classes:

- Lamp
- Window

Users upload an image, choose a confidence threshold, then get an annotated image of detected objects, class names, confidence scores, and bounding boxes.

## Live Application
Try the deployed app here:
(https://yolo-flask-deployment.onrender.com)

#### Application Preview

![YOLO Object Detection Application](screenshots/app_preview.png)

## How the Application Works
1. The user uploads an image through the web interface.  
2. Flask validates and stores the uploaded image.  
3. The image is evaluated via the trained YOLO model.  
4. YOLO returns detected classes, confidence scores, and bounding box coordinates.  
5. The application shows the annotated image and detection details.


## Technologies Used
- Python  
- Flask  
- YOLOv8  
- Ultralytics  
- OpenCV  
- Gunicorn  
- Docker  
- GitHub  
- Render  

## How to Use the Interface
1-Open the application.  
2-Select an image in JPG, JPEG, PNG, or WEBP format.  
3-Choose the confidence threshold.  
4-Click Run Detection.  
5-Review the annotated image and the detection table.  

## Run Locally Using Docker 
1. Clone the repository  
git clone https://github.com/zaynabalbloushi98-oss/yolo-flask-deployment.git  
2. Open the project folder
Use code blocks for Terminal commands-> cd yolo-flask-deployment  
3. Build the Docker image  
Use code blocks for Terminal commands-> docker build -t yolo-flask-app .  
4. Run the Docker container  
Use code blocks for Terminal commands-> docker run --rm -p 8000:5000 yolo-flask-app  
5. Open the application  
(Open this address in your browser):  
http://127.0.0.1:8000  


## Confidence Threshold 
-The confidence threshold controls the minimum confidence required for a detection to appear.  
-A lower threshold may show more detections, but may increase false positives.  
-A higher threshold shows fewer but more confident detections.  

## Known Limitations
-The model can only detect lamps and windows.  
-Detection accuracy depends on image quality, lighting, angle, and similarity to the training dataset.  
-The model may not detect objects that are very different from the training images.  
-Prediction can be slower on CPU-based hosting.  
-The free Render service may take time to start after a period of inactivity.  
-Uploaded images and generated results are stored temporarily by the application.  

## Future Improvements 
1-Add more training images.  
2-Improve dataset diversity.  
3-Add more object classes.  
4-Improve the user interface.  
5-Deploy the model using GPU-supported hosting.  

## Deployment 
-The project source code is hosted on GitHub.  
-The Dockerized application is deployed online using Render.

## Project structure
```text
yolo-flask-deployment/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── deployment_link.txt
├── slides_link.txt
├── models/
│   └── best.pt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── uploads/
│   └── results/
└── screenshots/
    └── app_preview.png