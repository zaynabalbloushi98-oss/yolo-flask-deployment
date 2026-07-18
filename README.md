# YOLO Object Detection Flask Deployment

## Project description
This project deploys a trained YOLO object-detection model through a Flask web
application. A user uploads an image, selects a confidence threshold, and
receives an annotated image plus a table of detected classes and confidence
scores.

## Project structure
```text
yolo_flask_deployment/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── models/
│   └── best.pt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── uploads/
    └── results/
```

## Add the trained model
Download the best YOLO weights from the training notebook, rename the file
`best.pt` if necessary, and place it inside `models/`.

## Run locally without Docker
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Run with Docker
```bash
docker build -t yolo-flask-app .
docker run --rm -p 5000:5000 yolo-flask-app
```
Open `http://localhost:5000`.

## Interface usage
1. Select a JPG, JPEG, PNG, or WEBP image.
2. Set the confidence threshold.
3. Click **Run Detection**.
4. Review the image and detection table.

## Known limitations
- The model detects only classes included in its training dataset.
- Accuracy depends on image quality and similarity to the training data.
- Large model files can exceed free hosting limits.
- CPU-only online hosting can make prediction slower.
