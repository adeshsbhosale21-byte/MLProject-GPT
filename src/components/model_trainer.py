import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from ..utils.file_utils import save_model
from ..logger import get_logger

logger = get_logger(__name__)

def train_and_select_model(X, y, preprocessor, config):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.get('test_size', 0.2), random_state=config.get('random_state', 42)
    )
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(random_state=config.get('random_state',42)),
        "XGBoost": XGBRegressor(),
        "CatBoost": CatBoostRegressor(verbose=False)
    }
    results = []
    for name, model in models.items():
        logger.info(f"Training {name}")
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('estimator', model)
        ])
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        logger.info(f"{name} -> R2: {r2:.4f}, RMSE: {mse**0.5:.4f}, MAE: {mae:.4f}")
        results.append({'name': name, 'r2': r2, 'pipeline': pipeline})
    # pick best
    best = max(results, key=lambda x: x['r2'])
    logger.info(f"Best model: {best['name']} with R2={best['r2']:.4f}")
    # save
    model_path = config.get('model_dir','artifacts/models')
    save_model(best['pipeline'], f"{model_path}/{best['name']}.joblib")
    return best