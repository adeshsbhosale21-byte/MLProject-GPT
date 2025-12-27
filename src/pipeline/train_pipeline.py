import yaml, os
from ..components.data_ingestion import read_raw
from ..components.data_validation import validate_schema
from ..components.data_transformation import build_preprocessor
from ..components.model_trainer import train_and_select_model
from ..logger import get_logger

logger = get_logger(__name__)

def load_config(path='config/config.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)['default']

def run_training(config_path='config/config.yaml'):
    config = load_config(config_path)
    df = read_raw(config['raw_data_path'])
    validate_schema(df, config['target_col'])
    X = df.drop(columns=[config['target_col']])
    y = df[config['target_col']]
    preprocessor = build_preprocessor(X)
    best = train_and_select_model(X, y, preprocessor, config)
    logger.info("Training completed. Best model saved.")
    return best

if __name__ == "__main__":
    run_training()