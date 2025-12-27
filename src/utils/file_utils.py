import os
import joblib

def save_model(obj, path):
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    joblib.dump(obj, path)

def load_model(path):
    return joblib.load(path)