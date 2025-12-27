from ..logger import get_logger
logger = get_logger(__name__)

def validate_schema(df, target_col):
    # Basic checks: no duplicate column names, target exists, reasonable size
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not in dataframe")
    if df.shape[0] < 10:
        logger.warning("Very small dataset (<10 rows). Models may not generalize.")
    # check for NaNs
    missing = df.isnull().sum().sum()
    if missing > 0:
        logger.warning(f"Found {missing} missing values. Consider imputing.")
    return True