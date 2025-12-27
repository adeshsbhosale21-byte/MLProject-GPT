# Refactored ML Project

Location: `/mnt/data/ml_project_refactor`

## How to run locally

1. Create virtualenv and install:
   ```
   pip install -r requirements.txt
   ```

2. Put your raw CSV at: `data/raw/students.csv`
   - It should contain the target column `math_score` (or adjust config/config.yaml)

3. Train:
   ```
   python -m src.pipeline.train_pipeline
   ```
   or
   ```
   python src/pipeline/train_pipeline.py
   ```

4. Run Flask app:
   ```
   python app.py
   ```

5. Predict:
   ```
   POST /predict
   Content-Type: application/json
   Body: { "gender": "female", "lunch":"standard", ... }
   ```

Notes:
- I converted your notebook logic into modular pipelines.
- The training will pick best model by R2 and save as joblib in `artifacts/models`.
- Data validation is basic; consider adding Great Expectations for stronger checks.