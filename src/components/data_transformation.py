import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from ..logger import get_logger

logger = get_logger(__name__)

def build_preprocessor(X):
    num_features = X.select_dtypes(exclude='object').columns.tolist()
    cat_features = X.select_dtypes(include='object').columns.tolist()
    logger.info(f"Numeric cols: {num_features}")
    logger.info(f"Categorical cols: {cat_features}")

    numeric_transformer = StandardScaler()
    oh_transformer = OneHotEncoder(handle_unknown='ignore',sparse_output=False)


    transformers = []
    if cat_features:
        transformers.append(('cat', oh_transformer, cat_features))
    if num_features:
        transformers.append(('num', numeric_transformer, num_features))

    preprocessor = ColumnTransformer(transformers, remainder='drop')
    return preprocessor