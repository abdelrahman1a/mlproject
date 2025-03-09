from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.Pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)  # Entry point
app = application

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Collect form data
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_DataFrame()
        print(pred_df)

        # Predict using pipeline
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.Predict(pred_df)

        if results[0] > 100:
            results[0] = 100

        # Return result as JSON for AJAX
        return jsonify({"prediction": results[0]})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
