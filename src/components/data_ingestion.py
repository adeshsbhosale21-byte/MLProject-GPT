import pandas as pd
from ..logger import get_logger
logger = get_logger(__name__)

def read_raw(path):
    logger.info(f"Reading raw data from {path}")
    df = pd.read_csv(path)
    logger.info(f"Data shape: {df.shape}")
    return df