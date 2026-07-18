import os
import uuid
from pathlib import Path

from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
RESULT_FOLDER = BASE_DIR / "static" / "results"
MODEL_PATH = BASE_DIR / "models" / "best.pt"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "development-secret-key")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. "
        "Copy your trained YOLO model and rename it to models/best.pt."
    )

model = YOLO(str(MODEL_PATH))


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    detections = []

    if request.method == "POST":
        if "image" not in request.files:
            flash("Please select an image.")
            return render_template("index.html")

        file = request.files["image"]

        if not file or file.filename == "":
            flash("Please select an image.")
            return render_template("index.html")

        if not allowed_file(file.filename):
            flash("Allowed formats: PNG, JPG, JPEG, and WEBP.")
            return render_template("index.html")

        extension = secure_filename(file.filename).rsplit(".", 1)[1].lower()
        unique_name = f"{uuid.uuid4().hex}.{extension}"
        input_path = UPLOAD_FOLDER / unique_name
        file.save(input_path)

        confidence = float(request.form.get("confidence", 0.25))
        confidence = max(0.05, min(confidence, 0.95))

        results = model.predict(
            source=str(input_path),
            conf=confidence,
            save=False,
            verbose=False
        )

        result = results[0]
        plotted = result.plot()
        output_name = f"result_{unique_name.rsplit('.', 1)[0]}.jpg"
        output_path = RESULT_FOLDER / output_name

        import cv2
        cv2.imwrite(str(output_path), plotted)

        names = result.names
        if result.boxes is not None:
            for box in result.boxes:
                class_id = int(box.cls.item())
                score = float(box.conf.item())
                coordinates = [round(float(x), 1) for x in box.xyxy[0].tolist()]
                detections.append({
                    "class_name": names[class_id],
                    "confidence": round(score * 100, 2),
                    "coordinates": coordinates
                })

        result_image = f"results/{output_name}"

    return render_template(
        "index.html",
        result_image=result_image,
        detections=detections
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
