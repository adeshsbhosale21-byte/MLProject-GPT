from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

def get_feature_info(df, target_col):
    X = df.drop(columns=[target_col])
    num_features = X.select_dtypes(exclude='object').columns.tolist()
    cat_features = X.select_dtypes(include='object').columns.tolist()
    return num_features, cat_features