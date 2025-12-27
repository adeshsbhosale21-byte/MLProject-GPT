import yaml
from ..utils.file_utils import load_model
from ..logger import get_logger
import pandas as pd

logger = get_logger(__name__)

def load_config(path='config/config.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)['default']

def predict(input_df, model_path=None):
    config = load_config()
    if model_path is None:
        # pick latest model in model dir
        import os, glob
        model_files = glob.glob(config['model_dir']+'/*.joblib')
        if not model_files:
            raise FileNotFoundError("No model found. Train first.")
        model_files.sort(key=os.path.getmtime, reverse=True)
        model_path = model_files[0]
    logger.info(f"Loading model from {model_path}")
    model = load_model(model_path)
    preds = model.predict(input_df)
    return preds