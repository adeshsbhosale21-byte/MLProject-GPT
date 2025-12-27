from flask import Flask, request, jsonify, render_template
import pandas as pd
from src.pipeline.predict_pipeline import predict
from src.logger import get_logger

logger = get_logger(__name__)

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = predict(df)
        return jsonify({
            "success": True,
            "prediction": round(float(prediction[0]), 2)
        })
    except Exception as e:
        logger.exception("Prediction failed")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
