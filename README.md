# End-to-End Machine Learning Project

A simple end-to-end machine learning project that includes data ingestion, preprocessing, model training, artifact serialization, and a Flask web app for prediction.

---

## 🚀 Project Overview

This repository implements a complete ML workflow for predicting student exam performance. It includes:

- Data ingestion & splitting
- Data transformation (preprocessing pipeline)
- Model training and selection
- Saving trained artifacts (`model.pkl`, `preprocessor.pkl`)
- A Flask web app (`app.py`) to serve predictions via a web form

---

## 🧱 Repository Structure

```
.
├── app.py                  # Flask web application
├── main.py                 # Training entry point
├── artifacts/              # Generated training artifacts (model + preprocessor)
├── logs/                   # Logged run output
├── src/                    # Core pipeline code
│   ├── components/         # Ingestion, transformation, training components
│   ├── pipeline/           # Predict pipeline + data model
│   ├── utils.py            # Helper utilities (load/save objects)
│   ├── exception.py        # Custom exception wrapper
│   └── logger.py           # Logging configuration
├── templates/              # Flask HTML templates
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Setup (local)

1. **Create & activate a virtual environment** (recommended):

   ```sh
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Train the model** (produces `artifacts/model.pkl` and `artifacts/preprocessor.pkl`):

   ```sh
   python main.py
   ```

---

## 🧠 Run the Web App (Prediction)

1. Start the Flask server:

   ```sh
   python app.py
   ```

2. Open your browser and go to:

   - http://127.0.0.1:5000/ (home)
   - http://127.0.0.1:5000/predict-data (prediction form)

3. Fill the form and submit to get a prediction.

---

## 🗂️ Logs

Logs are stored under the `logs/` directory. Each run generates a new timestamped `.log` folder containing the generated `.log` file.

---

## 🧩 Notes / Troubleshooting

- If you see `ModuleNotFoundError: No module named 'numpy._core'` when serving, retrain the model inside the same environment used for the web app (e.g., rerun `python main.py` with the same interpreter).
- If the prediction form returns a 500 error, check the latest log file under `logs/` for the traceback.

---

## 📌 Next Improvements (optional)

- Add unit tests for each pipeline component
- Add Dockerfile / containerization for consistent deployment
- Add CI/CD pipeline to run tests + retrain + deploy
- Add input validation + error handling for the web form
